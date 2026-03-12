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

1. **Cron Schedule**: Runs every 5 minutes (configurable via crontab)
2. **Task Execution**: Reads all `.txt` files in `tasks/` folder and executes them with kiro-cli
3. **Knowledge Base**: Uses kiro's built-in knowledge management to persist state
4. **Self-Improvement**: `improve.md` contains instructions for the agent to analyze and optimize its own tasks

## File Structure

- `tasks/*.txt` - Task definitions (plain text instructions for kiro)
- `tasks/learnings.log` - Log of task optimizations made over time
- `profile.json` - User configuration (email, name, etc.)
- `improve.md` - Instructions for self-optimization
- `agent.log` - Execution log from cron runs

## Current Tasks

- **calculating_pi**: Calculates next digit of pi, saves to knowledge base, emails result

## Setup

1. Configure `profile.json` with your email
2. Add task files to `tasks/` folder
3. Crontab runs automatically every 5 minutes
4. View logs: `tail -f agent.log`

## Adding New Tasks

Create a new `.txt` file in `tasks/` with plain text instructions for what kiro should do. The agent will automatically pick it up on the next run.

## Output

The agent delivers research findings, insights, and actionable information via email and the kiro knowledge base at scheduled intervals.
