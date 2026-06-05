# PTAC Call Review Daily Focus Agent

This repository is a structured knowledge base for an AI agent that generates accurate daily WhatsApp training posts for Precision Tune Auto Care call performance improvement.

The campaign is built from monthly call review data and focuses on:

- Required phone greeting compliance
- Professional first impressions
- Affirmative and confident language
- Active listening and clarifying questions
- Tone, warmth, clarity, and conciseness
- Strong call closure and appointment confirmation
- Automotive Hospitality standards

## Required Answering Procedure

Every customer phone call must be answered exactly like this:

> Thank you for choosing Precision Tune Auto Care, my name is [employee’s name], who do I have the pleasure of speaking with?

This greeting is strict, trained, and expected. It is not optional.

## Agent Usage

Attach this repository as source context to the AI agent that produces daily WhatsApp posts. The agent should read:

1. `prompts/daily-focus-agent-prompt.md`
2. `data/call-review-monthly-2026-06.json`
3. `data/weekly-focus-plan.json`
4. `content/whatsapp-posts-3-week-campaign.md`
5. `schemas/daily-post-output.schema.json`

## Expected Agent Behavior

The agent should generate one daily WhatsApp post Monday through Friday for 3 weeks, aligned to the current week/day focus.

Each post should include:

- Short bold title
- Direct coaching message
- One behavior to practice that day
- “Today’s challenge” statement
- Encouragement connected to Automotive Hospitality

## Campaign Title

**Own the First 10 Seconds. Control the Last 30 Seconds.**

## Leadership Principle

Customers should feel welcomed, heard, guided, and confident before their vehicle ever enters the bay.
