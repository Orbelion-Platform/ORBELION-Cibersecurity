# Publication scope

Only the exact text files listed in scripts/validate_publication.py are approved.

Included: original explanatory documentation, an independently written synthetic scoring example, unit tests and public validation CI.

Excluded: private engine source and history, manifests, client data, account identifiers, credentials, operational reports, logs, local state, databases, screenshots, deployment settings and production endpoints.

This public checkout has a single public origin. The private checkout retains its existing private origin. There is no submodule, automatic sync or runtime dependency between them.

The validator checks an exact file allowlist, symbolic links, Markdown local links and common credential patterns. It is defense in depth and cannot detect every kind of sensitive information. Review every public diff.

Private source paths, private commit identifiers and detailed implementation inventories are also excluded. Claims in the capability table must refer only to public files.
