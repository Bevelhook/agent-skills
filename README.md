# Agent Skills

name: AI Push

on:
  repository_dispatch:
    types: jobs:
  push:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          token: ${{ secrets.AI_TOKEN }}

      - name: Apply changes
        run: |
          echo "Changes would be applied here" basic framework for skills and functionality automation.

## Structure
- `skills/`: Contains individual skill modules.
- `activation/`: Contains scripts to activate and utilize skills.

## How to Run
1. Clone the Repository:
   ```bash
   git clone https://github.com/Bevelhook/agent-skills.git
   cd agent-skills
   ```

2. Run the activation script:
   ```bash
   python activation/activate_skills.py
   ```

3. View the output:
   ```
   Activating skills...
   Executing Hello Skill:
   Hello!
   Executing Greet Skill:
   Welcome, Bevelhook!
   ```

## Automation
This project automatically tests and runs scripts using GitHub Actions.
