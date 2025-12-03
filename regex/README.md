# Regular expressions (regex)

Regular expressions (regex) are patterns used to find, match or validate text.
This document gives a compact reference and a few Python examples so the notes render nicely on GitHub.

## Quick reference

Basic metacharacters:

- `.`    — any character except a newline
- `*`    — 0 or more repetitions (greedy)
- `+`    — 1 or more repetitions (greedy)
- `?`    — 0 or 1 repetition (also used for non-greedy `*?`, `+?`)
- `{m}`  — exactly `m` repetitions
- `{m,n}`— between `m` and `n` repetitions (inclusive)

Anchors and sets:

- `^`    — start of the string (or start of line in multiline mode)
- `$`    — end of the string (or just before final newline; in multiline mode it can match end-of-line)
- `[]`   — character set, for example `[abc]`
- `[^]`  — negated set, for example `[^@]` means any character except `@`

Predefined classes:

- `\d` — decimal digit (equivalent to `[0-9]`)
- `\D` — not a decimal digit
- `\s` — whitespace (space, tab, newline)
- `\S` — not a whitespace character
- `\w` — word character (letters, digits, underscore)
- `\W` — not a word character

Grouping and alternatives:

- `(...)`   — capture group and group for quantifiers
- `(?:...)` — non-capturing group
- `A|B`     — either `A` or `B`

## Examples (Python)

```python
import re

pattern = r"^.+@.+\.com$"   # simple anchored pattern that requires the whole string to end with .com

print(bool(re.search(pattern, "user@example.com")))   # True
print(bool(re.search(pattern, "prefix user@example.com suffix")))  # False because of anchors

# Use fullmatch to require the whole string to match (equivalent to ^...$)
print(bool(re.fullmatch(r"[^@]+@[^@]+\.com", "user@example.com")))

# Find all words in a string
print(re.findall(r"\w+", "Hello, world! 123"))  # ['Hello', 'world', '123']
```

## Anchors: what `^` and `$` mean

Both `^` and `$` are zero-width anchors — they match a position, not a character.
- `^` asserts the position is at the start of the string (or start of a line in multiline mode).
- `$` asserts the position is at the end of the string, or just before the final newline. If you need to require the absolute end (no trailing newline allowed) use `\Z`.

So `r"\.com$"` means the literal `".com"` must appear immediately before the end of the string.

## Common pitfalls

- Unanchored patterns (no `^`/`$`) will match anywhere in the string. Use `re.search` for substring matches, `re.fullmatch` to require the entire string.
- `.` does not match newline by default. Use `re.DOTALL` (or `re.S`) if you want `.` to include newlines.
- Email validation is tricky. A simple pattern like `r"^.+@.+\.com$"` will allow multiple `@` signs and other invalid formats. Prefer a stricter pattern such as `r"^[^@]+@[^@]+\.com$"` for the `.com` case, or use a well-tested library for full RFC-compliant validation.

## Tips

- Prefer `re.fullmatch` when you want the pattern to cover the whole string — it's clearer than `^...$`.
- Use raw strings for patterns in Python (prefix with `r`), e.g. `r"\d+"`, to avoid double escaping.
- When building patterns dynamically, `re.escape()` helps if you need to match literal user input.

---

If you want, I can add a short table of examples (emails, URLs, phone numbers) or convert a few of the patterns in this repo into runnable tests/snippets.
Regular expressions are nothing but patterns.
They are used to recognize or validate some type of patterns in your code.


.       --> any character except a new line
*       --> 0 or more repetitions
+       --> 1 or more repetitions
?       --> 0 or 1 repetition
{m}     --> m repetitions
{m,n}   --> m-n repetitions
^       --> matches the start of the string
$       --> matches the end of the string or just before the newline at the end of the string
[]      --> set of characters
[^]     --> Complementing the set (not present in the set)

\d      --> Decimal digit
\D      --> not a decimal digit
\s      --> whitespace characters
\S      --> Not a whitespace character
\w      --> word character as well as numbers and the underscore
\W      --> Not a word character

(...)   --> For grouping together
A|B     --> Either A or B
(?: ...) --> Non capturing version