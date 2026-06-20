# Python Test

Small smoke repo for testing Bumpkin on Python package changes.

## Package

The package lives under `src/python_test`.

Public exports include:

- `greet`
- `greet_many`
- `farewell`

## Release workflow

This repo includes the standard Bumpkin preview/publish workflow at:

- `.github/workflows/bumpkin.yml`

Required secrets:

- `BUMPKIN_MODEL`
- `BUMPKIN_FALLBACK_MODEL` (optional)
- `BUMPKIN_MODELS_ENDPOINT`
- `MODELS_TOKEN`
