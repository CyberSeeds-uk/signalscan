# SignalScan Report – {{ client_name }}

*Assessment Date:* {{ assessment_date }}  
*Confidential: Do not distribute without permission*

## Scope

{{ scope_description }}

## Executive Judgement

{{ executive_summary }}

## Business Objective

{{ business_objective }}

## Method

{{ method_overview }}

## Legal & Ethical Boundary

{{ boundaries_statement }}

## Surface Map

{{ surface_map_description }}

{{ surface_map_markdown }}

## Critical Observations

{{ critical_observations_markdown }}

## Findings

{% for stage, findings in grouped_findings.items() %}
### {{ stage }} Findings

{% for finding in findings %}
#### {{ finding.finding_id }} – {{ finding.title }} ({{ finding.status }})

- **Observation:** {{ finding.observation }}
- **Affected asset:** {{ finding.affected_asset }}
- **Trust/Security impact:** {{ finding.trust_or_security_impact }}
- **Commercial impact:** {{ finding.commercial_impact }}
- **Urgency:** {{ finding.urgency }}
- **Ease of repair:** {{ finding.ease_of_repair }}
- **Confidence:** {{ finding.confidence }}
- **Interpretation:** {{ finding.interpretation }}
- **Recommendation:** {{ finding.recommendation }}
- **Owner:** {{ finding.owner }}  
  **Target date:** {{ finding.target_date }}
- **Retest method:** {{ finding.retest_method }}
- **Limitation:** {{ finding.limitation }}
- **Evidence Timestamp:** {{ finding.evidence_timestamp }}
- **Evidence:**  
  {% for ev in finding.evidence %}
  - {{ ev }}
  {% endfor %}
{% if finding.sensitive %}
> **Sensitive:** {{ finding.disclosure_handling }}
{% endif %}

{% endfor %}
{% endfor %}

## Priority Matrix

{{ priority_matrix_markdown }}

## 24‑Hour Actions

{% for action in actions_24h %}
- {{ action }}
{% endfor %}

## 30‑Day Roadmap

{% for action in actions_30d %}
- {{ action }}
{% endfor %}

## Optional Prototype

{{ prototype_recommendation }}

## Retest Criteria

{{ retest_criteria }}

## Limitations

{{ limitations }}

© {{ year }} Jxnesyy Signal Lab – Confidential