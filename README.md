# agent-habitat-demo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![CI](https://github.com/Nueramarcos/agent-habitat-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/Nueramarcos/agent-habitat-demo/actions/workflows/ci.yml)

Minimal demo repo for **Agent Habitat OS**. Three intentional bugs — boot the stack, run tests, let an agent fix them.

## Bugs (by design)

1. `sum_range(1, 5)` returns 14 instead of 15 (off-by-one)
2. `is_palindrome` is case-sensitive (`"Racecar"` fails)
3. `clamp` does not handle inverted bounds

## Try it

```bash
python3 -m pytest          # fails
grok -p "Fix habitat/calc.py"
python3 -m pytest          # passes
```

## Autonomous lane

1. Push this repo to GitHub as `your-user/agent-habitat-demo`
2. Add label `agent-triage`
3. Open issues from [`issues/`](issues/) or use GitHub issue templates
4. `issue-agent fix --repo your-user/agent-habitat-demo --issue 1`

## CI

GitHub Actions runs `pytest` on push — same gate the agent must pass.