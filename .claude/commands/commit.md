---
allowed-tools: Bash(git --no-pager diff:*), Bash(git --no-pager log:*)
description: Create a git commit that requires user confirmation.
argument-hint: [user-comment]
context: fork
agent: commit-hook
---

## Context

### Current git diff

!`git --no-pager diff --cached`

### Recent Commits

!`git --no-pager log --oneline -10`

### User Comment:

> $ARGUMENTS

## Your Task

Based on the Context provided above, generate commit message for a single git commit.