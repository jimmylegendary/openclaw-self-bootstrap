# Workflow: LaTeX Paper Writing

## Purpose

Support conversational paper writing with repeatable compile / preview loops.

## When to use

- academic writing
- technical reports that need LaTeX structure
- iterative section drafting with compilation checks

## Inputs

- target template
- section drafts
- bibliography entries

## Outputs

- LaTeX source
- compiled PDF when environment is available
- resolved compile issues

## Procedure

1. Choose a template before drafting.
2. Generate or edit sections incrementally.
3. Compile after major changes.
4. Fix compile errors before continuing.
5. Keep bibliography inputs versioned with the source.

## Verification

- the document compiles
- section structure is explicit
- bibliography and references resolve correctly

## Risks / gotchas

- local TeX environments can be heavy and brittle
- do not treat this as a default workflow unless academic writing is common

## Related files

- `templates/latex-paper-template.md`
