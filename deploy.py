#!/usr/bin/env python3
"""
Deploy skills from this repo into Claude CoWork.

Usage:
    python deploy.py                  # deploy all skills in skills/
    python deploy.py my-skill         # deploy one skill by name
    python deploy.py --list           # show what's installed and what's here
    python deploy.py --dry-run        # show what would change without doing it
"""

import json
import re
import shutil
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent
SKILLS_SRC = REPO_ROOT / "skills"
COWORK_BASE = Path.home() / "Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin"


# --------------------------------------------------------------------------- #
# Finding the active CoWork install                                            #
# --------------------------------------------------------------------------- #

def find_active_manifest() -> Path:
    """Return the manifest.json with the highest lastUpdated timestamp."""
    candidates = list(COWORK_BASE.rglob("manifest.json"))
    if not candidates:
        sys.exit("❌  No CoWork manifests found. Is Claude CoWork installed?")

    def last_updated(p: Path) -> int:
        try:
            return json.loads(p.read_text()).get("lastUpdated", 0)
        except Exception:
            return 0

    return max(candidates, key=last_updated)


# --------------------------------------------------------------------------- #
# Parsing SKILL.md frontmatter                                                 #
# --------------------------------------------------------------------------- #

def parse_frontmatter(skill_dir: Path) -> dict:
    """Extract name and description from SKILL.md YAML frontmatter."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        sys.exit(f"❌  No SKILL.md found in {skill_dir}")

    text = skill_md.read_text()
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        sys.exit(f"❌  No YAML frontmatter found in {skill_md}")

    frontmatter = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            frontmatter[key.strip()] = value.strip().strip('"')

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not name:
        sys.exit(f"❌  SKILL.md in {skill_dir} is missing 'name' in frontmatter")
    if not description:
        print(f"  ⚠️  No description in frontmatter for {name} — manifest entry will have empty description")

    return {"name": name, "description": description or ""}


# --------------------------------------------------------------------------- #
# Deploy one skill                                                             #
# --------------------------------------------------------------------------- #

def deploy_skill(skill_dir: Path, manifest_path: Path, manifest: dict, dry_run: bool) -> str:
    """Copy skill directory and update manifest. Returns skill name."""
    meta = parse_frontmatter(skill_dir)
    name = meta["name"]
    description = meta["description"]

    target_skills_dir = manifest_path.parent / "skills"
    target_dir = target_skills_dir / skill_dir.name

    # Find existing manifest entry (match by name or directory name)
    existing = next(
        (s for s in manifest["skills"] if s.get("name") == name or s.get("name") == skill_dir.name),
        None
    )

    skill_id = existing["skillId"] if existing else f"skill_{uuid.uuid4().hex[:24]}"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    new_entry = {
        "skillId": skill_id,
        "name": name,
        "description": description,
        "creatorType": "user",
        "updatedAt": now,
        "enabled": True,
    }

    action = "update" if existing else "add"
    print(f"  {'[dry-run] ' if dry_run else ''}{action}: {name}  →  {target_dir}")

    if not dry_run:
        # Copy skill directory (overwrite)
        if target_dir.exists():
            shutil.rmtree(target_dir)
        shutil.copytree(skill_dir, target_dir)

        # Update manifest
        if existing:
            idx = manifest["skills"].index(existing)
            manifest["skills"][idx] = new_entry
        else:
            manifest["skills"].insert(0, new_entry)

    return name


# --------------------------------------------------------------------------- #
# Main                                                                         #
# --------------------------------------------------------------------------- #

def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    list_only = "--list" in args
    targets = [a for a in args if not a.startswith("--")]

    manifest_path = find_active_manifest()
    manifest = json.loads(manifest_path.read_text())

    if list_only:
        installed = {s["name"] for s in manifest["skills"] if s.get("creatorType") == "user"}
        local = {d.name for d in SKILLS_SRC.iterdir() if d.is_dir()} if SKILLS_SRC.exists() else set()
        print(f"\nCoWork manifest: {manifest_path}\n")
        print("Local skills (in repo):")
        for s in sorted(local):
            status = "✅ deployed" if s in installed else "⬜ not yet deployed"
            print(f"  {s}  —  {status}")
        print("\nUser skills in CoWork (not in repo):")
        for s in sorted(installed - local):
            print(f"  {s}")
        return

    if not SKILLS_SRC.exists() or not any(SKILLS_SRC.iterdir()):
        print("No skills found in skills/ — add a skill directory there first.")
        return

    # Collect skill directories to deploy
    if targets:
        skill_dirs = []
        for t in targets:
            d = SKILLS_SRC / t
            if not d.is_dir():
                sys.exit(f"❌  No skill directory found at skills/{t}")
            skill_dirs.append(d)
    else:
        skill_dirs = [d for d in sorted(SKILLS_SRC.iterdir()) if d.is_dir()]

    print(f"\nDeploying to: {manifest_path.parent}\n")

    deployed = []
    for skill_dir in skill_dirs:
        name = deploy_skill(skill_dir, manifest_path, manifest, dry_run)
        deployed.append(name)

    if not dry_run:
        manifest["lastUpdated"] = int(datetime.now(timezone.utc).timestamp() * 1000)
        manifest_path.write_text(json.dumps(manifest, indent=2))
        print(f"\n✅  Deployed {len(deployed)} skill(s): {', '.join(deployed)}")
        print("   Reload CoWork to pick up changes.")
    else:
        print(f"\n[dry-run] Would deploy {len(deployed)} skill(s). Run without --dry-run to apply.")


if __name__ == "__main__":
    main()
