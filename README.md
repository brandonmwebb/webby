# Scheduled Learning Agent

An always-on agent that runs on a schedule to research and learn about topics of interest, delivering insights automatically.

## Purpose

This agent continuously explores and gathers information on:
- Earning money and income opportunities
- Stocks and investing strategies
- User-generated content trends
- Family travel destinations and tips
- Other evolving interests

## Architecture

**Current**: Single agent that runs scheduled tasks via cron, executing tasks defined in the `tasks/` folder.

**Future**: May delegate to specialized sub-agents for deeper domain expertise.

## How It Works

1. **Cron Schedule**: Multiple scheduled jobs run at different intervals
2. **Task Execution**: Reads all `.txt` files in `tasks/enabled/` folder and executes them with kiro-cli
3. **Knowledge Base**: Uses kiro's built-in knowledge management to persist state
4. **Self-Improvement**: `improve.md` analyzes and optimizes tasks every 2 hours
5. **Governance**: `governance.md` validates task objectives every 6 hours

## File Structure

- `tasks/enabled/*.txt` - Active task definitions (plain text instructions for kiro)
- `tasks/disabled/` - Tasks that failed governance validation
- `tasks/learnings.log` - Log of task optimizations made over time
- `profile.json` - User configuration (email, name, etc.)
- `improve/improve.md` - Instructions for self-optimization (runs every 2 hours)
- `governance/governance.md` - Task validation rules (runs every 6 hours)
- `governance/governance.log` - Log of governance actions
- `agent.log` - Execution log from cron runs

## Cron Schedule

- **Every hour**: Run all enabled tasks
- **Every 2 hours**: Self-improvement analysis
- **Every 6 hours**: Governance validation

## Current Tasks

- **calculating_pi**: Calculates next digit of pi, saves to knowledge base, emails result

## Setup

1. Configure `profile.json` with your email
2. Add task files to `tasks/enabled/` folder
3. Crontab runs automatically every hour
4. View logs: `tail -f agent.log`

## Adding New Tasks

Create a new `.txt` file in `tasks/enabled/` with plain text instructions for what kiro should do. Make sure to include a clear objective line (e.g., "Objective: Calculate and email the next digit of pi"). The agent will automatically pick it up on the next run.

## Output

The agent delivers research findings, insights, and actionable information via email and the kiro knowledge base at scheduled intervals.
