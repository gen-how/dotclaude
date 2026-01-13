---
allowed-tools: Bash(git --no-pager diff:*), Bash(git --no-pager log:*)
argument-hint: [user-comment]
description: Create a git commit that requires user confirmation.
---

# Git Commit Creation Guide

## Role and Purpose

You are a professional software engineer. When you receive a git diff, you will refer to the recent commits and user comment to decide what commit message to create.

Commits should follow the Conventional Commits specification unless the repo already has an existing format.

When git diff in [Provided Context](#provided-context) contains numerous changes:

- Prioritize the most significant changes in descriptions
- Group similar changes in body (e.g., "update 15 component imports" not listing each)
- Focus on WHAT changed and WHY, not exhaustive file-by-file details

When recent commits in [Provided Context](#provided-context) show a specific style or pattern:

- Follow the established patterns and styles in recent commits

When User comment are provided in [Provided Context](#provided-context):

- Consider it carefully when generating the commit message
- Incorporate relevant information into the commit body as appropriate
- The context may clarify what changed, explain why, explain the scope, the type or provide any other relevant information
- Can break formatting rules if user comment asks for it
- Still base the description of WHAT changed primarily on the diff itself

### The Conventional Commits Specification

1. Commits MUST be prefixed with a type, which consists of a noun, `feat`, `fix`, etc., followed by the OPTIONAL scope, OPTIONAL "!", and REQUIRED terminal colon and space.
2. The type `feat` MUST be used when a commit adds a new feature to your application or library.
3. The type `fix` MUST be used when a commit represents a bug fix for your application.
4. A scope MAY be provided after a type. A scope MUST consist of a noun describing a section of the codebase surrounded by parenthesis, e.g., `fix(parser):`.
5. A description MUST immediately follow the colon and space after the type/scope prefix. The description is a short summary of the code changes, e.g., *fix: array parsing issue when multiple spaces were contained in string*.
6. A longer commit body MAY be provided after the short description, providing additional contextual information about the code changes. The body MUST begin one blank line after the description.
7. A commit body is free-form and MAY consist of any number of newline separated paragraphs.
8. One or more footers MAY be provided one blank line after the body. Each footer MUST consist of a word token, followed by either a `:<space>` or `<space>#` separator, followed by a string value (this is inspired by the git trailer convention).
9. A footer’s token MUST use `-` in place of whitespace characters, e.g., `Acked-by` (this helps differentiate the footer section from a multi-paragraph body). An exception is made for `BREAKING CHANGE`, which MAY also be used as a token.
10. A footer’s value MAY contain spaces and newlines, and parsing MUST terminate when the next valid footer token/separator pair is observed.
11. Breaking changes MUST be indicated in the type/scope prefix of a commit, or as an entry in the footer.
12. If included as a footer, a breaking change MUST consist of the uppercase text BREAKING CHANGE, followed by a colon, space, and description, e.g. BREAKING CHANGE: environment variables now take precedence over config files.
13. If included in the type/scope prefix, breaking changes MUST be indicated by a "!" immediately before the ":". If "!" is used, BREAKING CHANGE: MAY be omitted from the footer section, and the commit description SHALL be used to describe the breaking change.
14. Types other than `feat` and `fix` MAY be used in your commit messages, e.g., docs: update ref docs.
15. The units of information that make up Conventional Commits MUST NOT be treated as case sensitive by implementors, with the exception of BREAKING CHANGE which MUST be uppercase.
16. BREAKING-CHANGE MUST be synonymous with BREAKING CHANGE, when used as a token in a footer.
17. For Commits that include dependency updates, the body MUST include a list of all updated DIRECT dependencies with the versions they were updated from and the versions to which they were updated to. When a diff includes both package manifest files (package.json, Cargo.toml, pyproject.toml, etc.) and lockfiles (pnpm-lock.yaml, package-lock.json, yarn.lock, Cargo.lock, poetry.lock, uv.lock, etc.), ONLY the direct dependencies explicitly changed in the manifest file MUST be listed. Transitive dependency changes visible only in lockfiles MUST NOT be included, as they are automatic consequences of direct dependency updates.

#### Commit Message Format

```
<type>[optional (<scope>)]: <description>
<BLANK LINE>
[optional <body>]
<BLANK LINE>
[optional <footer(s)>]
```

**Subject Line:**

- Must be in English
- Maximum of 50 characters including any spaces or special characters
- Imperative mood
- No capitalization
- No period at the end

**When to include scope:**

- The change affects a specific, identifiable component, module, or area (e.g., `auth`, `api`, `database`, `infra`, `terraform`)
- Including scope adds clarity about what part of the codebase changed
- The scope has been given as part of the "User comment" from [Provided Context](#provided-context)
- The scope is clear from the file paths or nature of changes

**When to omit scope:**

- Adding scope exceeds the 50 characters limit
- The change affects the entire project or multiple unrelated areas
- No single scope accurately describes all changes
- The type and description are sufficient to understand the change

**Body:**

- Must be in English
- Maximum of 72 characters per line including any spaces or special characters
- Bullet points with "-"
- Bullet points that exceed the 72 characters per line count should use line breaks without adding extra bullet points
- Explain what and why, using ONLY factual, verifiable information from the diff
- Be objective and precise - describe EXACTLY what changed without subjective interpretations
- AVOID vague qualifiers like "for clarity", "for consistency", "improve readability" unless the diff explicitly shows formatting/style changes
- ONLY include reasoning (the "why") when:
  - It is provided in "User comment" from [Provided Context](#provided-context)
  - It is clearly evident from the code context or commit scope
  - It is objectively verifiable from the diff itself
- Omit the body entirely if the subject line is self-explanatory and no "User comment" from [Provided Context](#provided-context) is provided

**Footer:**

This section is optional. If it is necessary to add it, the format is as follows:

```
<token>: <value>
```

For example:

```
BREAKING CHANGE: The API endpoint `/users` has been removed and replaced with `/members`.
```

#### Footer Reference

| Token           | Description                                                                                               |
| --------------- | --------------------------------------------------------------------------------------------------------- |
| BREAKING CHANGE | Indicates significant changes that are not backward compatible                                            |
| Fixes           | Used when the commit addresses a bug                                                                      |
| Closes          | Used to indicate that the commit resolves a specific issue or ticket                                      |
| Related to      | Used to link the commit to related commits, issues or tickets                                             |
| References      | Similar to "Related to"                                                                                   |
| Reviewed-by     | To acknowledge reviewers of the commit                                                                    |
| Signed-off-by   | To indicate that the commit complies with the project's contribution guidelines                           |

Some examples of footer usage:

```
Fixes #123
Closes #456
Resolves #789
Related to #101
References #202
Reviewed-by: John Smith <john.smith@example.com>
Signed-off-by: Alice Johnson <alice.johnson@example.com>
```


#### Type Reference

| Type     | Description                                                                                            | Example Scopes (non-exaustive)                                |
| -------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| build    | Changes that affect the build system or external dependencies                                          | gulp, broccoli, npm                                           |
| chore    | Other changes that don't modify src or test files                                                      | scripts, config                                               |
| ci       | Changes to our CI configuration files and scripts                                                      | Travis, Circle, BrowserStack, SauceLabs,github actions, husky |
| docs     | Documentation only changes                                                                             | README, API                                                   |
| feat     | A new feature                                                                                          | user, payment, gallery                                        |
| fix      | A bug fix                                                                                              | auth, data                                                    |
| perf     | A code change that improves performance                                                                | query, cache                                                  |
| refactor | A code change that neither fixes a bug nor adds a feature                                              | utils, helpers                                                |
| revert   | Reverts a previous commit                                                                              | query, utils,                                                 |
| style    | Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc) | formatting                                                    |
| test     | Adding missing tests or correcting existing tests                                                      | unit, e2e                                                     |
| i18n     | Changes related to internationalization                                                                | locale, translation                                           |

##### build

Used when a commit affects the build system or external dependencies. It includes changes to build scripts, build configurations, or build tools used in the project.

##### chore

Typically used for routine or miscellaneous tasks related to the project, such as code reformatting, updating dependencies, or making general project maintenance.

##### ci

CI stands for continuous integration. This type is used for changes to the project's continuous integration or deployment configurations, scripts, or infrastructure.

##### docs

Documentation plays a vital role in software projects. The docs type is used for commits that update or add documentation, including readme files, API documentation, user guides or code comments that act as documentation.

##### feat

Used for commits that introduce new features or functionalities to the project.

##### fix

Commits typed as fix address bug fixes or resolve issues in the codebase. They indicate corrections to existing features or functionality.

##### perf

Short for performance, this type is used when a commit improves the performance of the code or optimizes certain functionalities.

##### refactor

Commits typed as refactor involve making changes to the codebase that neither fix a bug nor add a new feature. Refactoring aims to improve code structure, organization, or efficiency without changing external behavior.

##### revert

Commits typed as revert are used to undo previous commits. They are typically used to reverse changes made in previous commits.

##### style

The style type is used for commits that focus on code style changes, such as formatting, indentation, or whitespace modifications. These commits do not affect the functionality of the code but improve its readability and maintainability.

##### test

Used for changes that add or modify test cases, test frameworks, or other related testing infrastructure.

##### i18n

This type is used for commits that involve changes related to internationalization or localization. It includes changes to localization files, translations, or internationalization-related configurations.

## Provided Context

### Current git diff

!`git --no-pager diff --cached`

### Recent Commits

!`git --no-pager log --oneline -10`

### User Comment

$ARGUMENTS

## Your Task

- ONLY generate commit message for a single commit.
- DO NOT use any other tools or do anything else.
- NO additional explanations or commentary, JUST the commit message.
- NO questions or comments.
- NO formatting instructions or metadata.