# Python Test

Small smoke repo for testing Bumpkin on Python package changes.

Current support floor: Python 3.11+

## Package

The package lives under `src/python_test`.

## Release workflow

This repo includes the standard Bumpkin preview/publish workflow at:

- `.github/workflows/bumpkin.yml`

Required secrets:

- `BUMPKIN_MODEL`
- `BUMPKIN_FALLBACK_MODEL` (optional)
- `BUMPKIN_MODELS_ENDPOINT`
- `MODELS_TOKEN`
