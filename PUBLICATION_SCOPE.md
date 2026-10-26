# Publication scope

Only the exact files listed in scripts/validate_publication.py are approved.

Included: original explanatory documentation, an independently written synthetic scoring example, unit tests and public validation CI.

Excluded: private engine source and history, manifests, client data, account identifiers, credentials, operational reports, logs, local state, databases, operational screenshots, deployment settings and production endpoints.

This public checkout has a single public origin. The private checkout retains its existing private origin. There is no submodule, automatic sync or runtime dependency between them.

The validator checks an exact file allowlist, symbolic links, Markdown local links and common credential patterns. It is defense in depth and cannot detect every kind of sensitive information. Review every public diff.

Private source paths, private commit identifiers and detailed implementation inventories are also excluded. Claims in the capability table must refer only to public files.

Approved visual exception: docs/assets/cybersecurity-defense-in-depth.png is the original conceptual image explicitly supplied for publication by the user. It contains a general defense-in-depth illustration. The validator verifies its exact SHA-256 and PNG signature; it does not scan image pixels for secrets.
