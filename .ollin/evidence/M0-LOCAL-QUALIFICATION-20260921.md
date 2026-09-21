# M0 Local Qualification Evidence — 2026-09-21

## Repository

`ollin-corp/ollin-fruit-fly-lab`

Local path reported by owner:

`D:\Dev\ollin-fruit-fly-lab`

## Baseline identity

Expected and observed HEAD:

`a99aefcaa4f667d47fd4a9a3ac2e750824139974`

Accepted tree:

`8f48f2d3cfd0b4ee54c1b48c5cbe88c0c897b02d`

Remote:

`https://github.com/ollin-corp/ollin-fruit-fly-lab.git`

## Worktree observation

`git status --porcelain` returned no entries.

## Qualification command

```powershell
python tools\qualification\m0_qualify.py
```

## Reported qualification output

```text
M0 universal spine                 PASS
M0 project identity                PASS
M0 dataset registry                PASS
M0 no vendored bulk connectome     PASS
M0 unit verification               PASS
OLLIN FRUIT FLY LAB M0 QUALIFICATION: PASS
```

## PowerShell note

During clone/verification, two standalone `else` clauses produced interactive PowerShell parser errors because the preceding `if` blocks had already executed. Those parser errors occurred outside the Git and qualification operations. The repository cloned successfully, HEAD matched, the worktree status was empty, and the M0 qualification harness completed with PASS.

## Result

`M0_LOCAL_REQUALIFICATION = PASS`
