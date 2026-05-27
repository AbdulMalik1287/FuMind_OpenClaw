# Reflection

## What worked well?
The skill-based architecture made adding each data source very easy.
Writing a separate Python class for ERP, MES, and SCADA meant each skill had one 
job which isolated and made it so that each skill is independent and not coupled.
The reverse lookup dictionary in the reconciler was simple to implement, mapping 
source IDs to canonical IDs in one dictionary made resolve() fast and easy to reason about.
Getting OpenClaw to recognise our custom skills via SKILL.md files was tricky but also straightforward 
once I found the correct directory.

## What was the hardest part?
The trickiest part was figuring out where OpenClaw actually looks for custom skills. 
The prompted options doesn't make this easy and I put the skill files in 
the wrong folder. Once that was solved, making sure every record from every source 
system got a canonical_machine_id before the join step was critical. Without that, 
the cross-silo merge would produce wrong or incomplete results.

## One thing I would change in production
Instead of the hardcoded Python dictionary, moving the machine registry to a 
versioned database or a YAML config file tracked in Git could be done to maintain consistency.
When an unknown machine ID appears, instead of just sending a warning, the system should trigger
an alert to the data engineering team with the unknown ID, the source system, and a timestamp. 
This prevents data loss while keeping the pipeline running.