# Standards update process

The updater is designed to behave like antivirus definitions, but with human review for risky changes.

```text
trusted source registry
→ digest check
→ candidate findings
→ candidate standards pack
→ canary generation
→ pull request
→ review
→ signed release
```

## Safety model

- Tier 1 official sources can generate candidate proposals.
- No internet-sourced change activates automatically.
- Template behavior changes require human review.
- Critical changes require Ruslan Magana approval.
- Failed canary tests quarantine the candidate pack.
