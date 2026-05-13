# Schemas

## intake.json

Save to `<client-folder>/intake.json`.

```json
{
  "schema_version": "1.1",
  "client_name": "string",
  "intake_date": "YYYY-MM-DD",
  "intake_completed_by": "Jim Henley",

  "engagement_scope": {
    "scope_type": "whole_company | function_or_team | use_case_bundle",
    "scope_description": "string (e.g., 'leadership and knowledge workers')",
    "scope_seat_count": 0
  },

  "company_profile": {
    "industry": "string",
    "total_employee_count": 0,
    "nonprofit_status": "for_profit | 501c3 | 501c6_amc | other_nonprofit | government",
    "regulatory_posture": "none | standard | hipaa | financial | government | other",
    "regulatory_notes": "string"
  },

  "current_stack": {
    "productivity_suite": "m365_deep | m365_light | google_deep | google_light | mixed | other",
    "m365_tenant_maturity": "mature | mixed | immature | unknown | n/a",
    "identity_provider": "string",
    "sso_required": "yes | no | nice_to_have",
    "scim_required": "yes | no | n/a",
    "existing_ai_tools": "string"
  },

  "use_cases": {
    "ranked": ["string", "string", "string"],
    "image_gen_required": "required | preferred | marginal | n/a",
    "excel_critical_features": ["pivot_tables", "power_query", "vba_macros", "named_ranges", "financial_connectors", "none"],
    "connectors_needed": ["string"]
  },

  "security": {
    "data_residency": "us | eu | none | other",
    "training_opt_out": "must | preferred | no_preference",
    "dlp_admin_controls": "must | nice | none",
    "baa_required": "yes | no | n/a",
    "air_gap_required": "yes | no"
  },

  "budget": {
    "per_seat_ceiling_usd": 0,
    "per_seat_ceiling_none": false,
    "budget_basis": "all_in | add_on | show_both",
    "total_annual_ceiling_usd": 0,
    "total_annual_ceiling_none": false,
    "procurement_notes": "string"
  },

  "team_change": {
    "ai_maturity": "novice | mixed | intermediate | advanced",
    "change_tolerance": "low | medium | high",
    "exec_sponsorship": "strong | moderate | weak"
  },

  "strategic": {
    "success_in_6_months": "string",
    "risk_if_wrong": "string",
    "vendor_stability_concern": "yes | no | client_raised",
    "preconceptions": "string"
  }
}
```

## filter_result (in-memory, not saved separately)

```json
{
  "surviving": [
    {"vendor": "claude", "tier": "enterprise"}
  ],
  "eliminated": [
    {"vendor": "chatgpt", "tier": "business", "rule": "Rule 3", "reason": "No BAA on Business tier"}
  ]
}
```

## Schema version history

- **1.0** — Initial schema (May 2026)
- **1.1** — Added engagement_scope section; added nonprofit_status, m365_tenant_maturity, scim_required, image_gen_required, excel_critical_features, budget_basis, vendor_stability_concern fields (May 12, 2026)
