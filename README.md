<div align="center">

# 🌯 Git & GitHub Bowl Builder

**A hands-on starter repo for practicing the real GitHub team workflow — themed like a Chipotle bowl order.**

[![CI Check](https://github.com/Steven-Baez/ssd-git-playground/actions/workflows/ci.yml/badge.svg)](https://github.com/Steven-Baez/ssd-git-playground/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

</div>

---

## 📖 About

This is the starter project for the **Git & GitHub Hands-on Team Workflow Workshop**.

The repo is intentionally simple **and intentionally broken**. The goal isn't to build a real app — it's to practice the full GitHub workflow:

<div align="center">

**Issue → Branch → Commit → Push → Pull Request → Review → CI Check → Merge Decision**

</div>

---

## 📁 Project contents

```text
git-workshop-starter-repo/
├── src/
│   ├── workshop.py
│   └── title.py
├── test/
│   └── test_workshop.py
└── .github/
    ├── workflows/ci.yml
    └── pull_request_template.md
```

---

## 🚦 Current state

> [!NOTE]
> The CI check is **supposed to fail** at first. That's intentional!

Your job during the workshop is to:

1. ✅ Read the issue assigned to you.
2. 🌿 Create a branch for the issue.
3. 🛠️ Fix the bowl status bug.
4. 🌶️ Add your own item to the menu (e.g. *Danny's Oreo Ice Cream*).
5. 🧪 Run the test locally.
6. 📝 Commit with a clear message.
7. ⬆️ Push your branch.
8. 🔀 Open a pull request.
9. 👀 Request a review.
10. 🟢 Check whether GitHub Actions turns green.

---

## ▶️ Running the tests

This project has **no outside dependencies** — just Python 3.

```bash
python test/test_workshop.py
```

At first, the test should fail with a message like:

```text
FAIL: Bowl status should be ready
Expected: ready
Received: not ready
```

After the correct one-line fix, the test should pass:

```text
All checks passed.
```

---

## 🐞 Main workshop issue

The main bug is in:

```text
src/workshop.py
```

The function `get_bowl_status()` currently returns the wrong status.

> [!WARNING]
> Do not fix it directly on `main`. Create a branch first!

---

## 🌮 Add your own menu item

`src/workshop.py` also has a `MENU` dict with `base`, `protein`, and `toppings` lists. While you're on your branch, add one item of your own to `MENU["toppings"]` — make it yours, like:

```python
"toppings": ["salsa", "cheese", "guac", "sour cream", "Danny's Oreo Ice Cream"],
```

Your PR should include **both** the bug fix and your new menu item.

---

## 🌿 Branch naming examples

Use the pattern:

```text
type/short-description
```

| Example | Use case |
|---|---|
| `fix/bowl-status` | Bug fixes |
| `docs/readme-setup` | Documentation changes |
| `feat/update-title` | New features |
| `chore/repo-cleanup` | Maintenance tasks |

---

## 📝 Commit message examples

<table>
<tr>
<td valign="top">

**❌ Bad**

```text
fix
stuff
changes
final
```

</td>
<td valign="top">

**✅ Better**

```text
fix: correct bowl status check
feat: add Danny's Oreo Ice Cream topping
docs: add setup instructions
chore: clean unused files
```

</td>
</tr>
</table>

---

## 🔀 Pull request rules

A PR should include:

- [x] What changed
- [x] Why it changed
- [x] How you tested it
- [x] Linked issue using `Closes #X`
- [x] Passing GitHub Actions check

> [!IMPORTANT]
> Do not merge until another person reviews it.

---

<div align="center">

Made with ❤️ for the workshop.

</div>
