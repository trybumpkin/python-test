# Python Test

Small smoke repo for testing Bumpkin on Python package changes.

## Package

The package lives under `src/python_test`.

Current behavior:

- `greet(" Alice ")` returns `Hello, Alice!`
- empty or whitespace-only names fall back to `Hello, friend!`

Public exports include:

- `greet`
- `greet_many`
- `greet_pair`
- `greet_formally`
- `farewell`

## Release workflow

This repo includes the standard Bumpkin preview/publish workflow at:

- `.github/workflows/bumpkin.yml`

Required secrets:

- `BUMPKIN_MODEL`
- `BUMPKIN_FALLBACK_MODEL` (optional)
- `BUMPKIN_MODELS_ENDPOINT`
- `MODELS_TOKEN`
