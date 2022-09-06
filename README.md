# pre-commit-hooks

Some pre-commit hooks for SI-Analytics repositories.

## Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/SIAnalytics/pre-commit-hooks
    rev: v0.1.0  # Use the ref you want to point at
    hooks:
    -   id: check-copyright
        args: ["dir_to_check"]  # replace the dir_to_check with your expected directory to check
```

## Hooks available

### say-hello

A template to show how to implement a pre-commit hook

### check-copyright

Check whether the code contains copyright

- `includes` - directory to add copyright.
- `--excludes` - exclude directory.
- `--suffixes` - copyright will be added to files with suffix.

## Acknowledgement

This repository is inspired by [open-mmlab/pre-commit-hooks](https://github.com/open-mmlab/pre-commit-hooks).
