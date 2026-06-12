# Matrix Repair Prompt

You violated or failed part of the Matrix Blueprint validation.

Fix only the listed violations. Do not redesign the app. Do not change the architecture. Do not add dependencies. Do not modify Matrix control files.

## Violations

{{ violations }}

## Allowed files for repair

{{ allowed_files }}

## Required fixes

{{ required_fixes }}

## Validation commands

{{ validation_commands }}

## Output format

Return only the minimal patch needed to satisfy validation.
