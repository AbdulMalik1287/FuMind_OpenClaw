## What this does
Resolves inconsistent machine IDs across three factory systems (ERP, MES, SCADA)
into a single canonical Fusion ID, then answers a cross-silo query that no single
source could answer alone.

## Project Structure
| File | Description |
|---|---|
| `erp_skill.py` | OpenClaw skill — reads ERP orders data |
| `mes_skill.py` | OpenClaw skill — reads MES batch data |
| `scada_skill.py` | OpenClaw skill — reads SCADA telemetry data |
| `skill_registry.py` | Registers all three skills with the agent |
| `reconciler.py` | Maps source machine IDs to canonical Fusion IDs |
| `run_query.py` | Runs the cross-silo query and prints the result table |
| `query_output.csv` | Output of the cross-silo query |
| `REFLECTION.md` | reflection on the assignment |

## Setup Instructions

1. Make sure Python 3.10+ is installed
2. Install OpenClaw globally: npm install -g openclaw@latest
3. Clone this repo and navigate into it: 
    git clone https://github.com/AbdulMalik1287/fusion-agent.git
    cd fusion-agent
4. Create and activate a virtual environment:
    python -m venv venv
    venv\Scripts\activate
5. Install dependencies:
    pip install -r requirements.txt
6. Register skills with OpenClaw by copying skill folders to:
    %USERPROFILE%.openclaw\skills\

## How to Run

python run_query.py

## Output
![Query Output](<Screenshot 2026-05-27 133941.png>)
