# Git Workshop Starter

This is the starter project for the **Git & GitHub Hands-on Team Workflow Workshop**.

The repo is intentionally simple and intentionally broken. The goal is not to build a real app. The goal is to practice the GitHub workflow:

**Issue → Branch → Commit → Push → Pull Request → Review → CI Check → Merge Decision**

## Project contents

```text
git-workshop-starter-repo/
  src/
    workshop.js
    title.js
  test/
    workshop.test.js
  .github/
    workflows/ci.yml
    pull_request_template.md
```

## Current state

The CI check is supposed to fail at first.

That is intentional.

Your job during the workshop is to:

1. Read the issue assigned to you.
2. Create a branch for the issue.
3. Make a small fix.
4. Run the test locally.
5. Commit with a clear message.
6. Push your branch.
7. Open a pull request.
8. Request a review.
9. Check whether GitHub Actions turns green.

## Running the test

This project has no outside dependencies.

Run:

```bash
npm test
```

At first, the test should fail with a message like:

```text
FAIL: Workshop status should be ready
Expected: ready
Received: not ready
```

After the correct one-line fix, the test should pass.

## Main workshop issue

The main bug is in:

```text
src/workshop.js
```

The function `getWorkshopStatus()` currently returns the wrong status.

Do not fix it directly on `main`. Create a branch first.

## Branch naming examples

Use the pattern:

```text
type/short-description
```

Examples:

```text
fix/workshop-status
docs/readme-setup
feat/update-title
chore/repo-cleanup
```

## Commit message examples

Bad:

```text
fix
stuff
changes
final
```

Better:

```text
fix: correct workshop status check
docs: add setup instructions
feat: update workshop title
chore: clean unused files
```

## Pull request rules

A PR should include:

- what changed
- why it changed
- how you tested it
- linked issue using `Closes #X`
- passing GitHub Actions check

Do not merge until another person reviews it.
