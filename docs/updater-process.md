# Updater Process

The updater is intentionally conservative.

```text
fetch trusted sources → detect changes → propose candidate pack → run canary tests → open PR → human review → signed release
```

The updater must not silently activate production rules that change generated code or validation behavior.
