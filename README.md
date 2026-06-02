# MITRE ATT&CK Mapper

> CLI tool that maps attack keywords and technique IDs to
> MITRE ATT&CK techniques — built from real incident response
> and vulnerability assessment experience.

## Problem

SOC analysts manually cross-reference MITRE ATT&CK during
triage. This tool automates technique lookup across 858
attack patterns in seconds.

## Features

- Keyword search across all ATT&CK techniques
- Direct lookup by technique ID (e.g. T1566)
- Tactic category returned with every result
- Export results to markdown report with --output flag

## Real-World Scenarios Covered

Built from actual Harness Projects security engagements:

| Scenario | Tactic | Technique |
|---|---|---|
| Phishing email delivering RAT | Initial Access | T1566 |
| Insider data exfiltration via SFTP | Exfiltration | T1048 |
| Lateral movement across file servers | Lateral Movement | T1021 |
| Privilege escalation via admin credentials | Privilege Escalation | T1078 |
| DDoS botnet attack | Impact | T1498 |
| Ransomware via RDP | Initial Access | T1133 |

## Setup

```bash
git clone https://github.com/eclipsefendurat3-D2Veyclipse/mitre-attack-mapper.git
cd mitre-attack-mapper
pip3 install -r requirements.txt
curl -o data/attack.json https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json
```

## Usage

```bash
# Search by keyword
python3 mapper.py "phishing"

# Search by technique ID
python3 mapper.py "T1566"

# Export to markdown report
python3 mapper.py "lateral movement" --output report.md
```

## Sample Output
