Generate commit messages that are fully compatible with `redjue.git-commit-plugin`.

Use this format:
`<emoji> <type>(<scope>): <subject>`

Optional sections:
- body after one blank line
- footer after one blank line

Type must be one of:
- `feat` `fix` `docs` `style` `refactor` `perf` `test` `chore`

Emoji mapping:
- `feat` -> `✨`
- `fix` -> `🐞`
- `docs` -> `📃`
- `style` -> `🌈`
- `refactor` -> `🦄`
- `perf` -> `🎈`
- `test` -> `🧪`
- `chore` -> `🐳`

Rules:
- Scope is required; use `*` when multiple scopes are affected.
- Subject uses imperative present tense, starts lowercase, has no trailing `.`, and stays within 20 words.
- Body explains motivation and contrasts with previous behavior.
- Footer is only for `BREAKING CHANGE:` and/or issue references like `Closes #123`.
- Output only the final commit message text, with no markdown fences or extra commentary.
