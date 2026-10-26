# Failure considerations

## Demonstrated in the public example

| Condition | Behavior |
| --- | --- |
| Inventory result supplied | Excluded from safeguard scoring |
| PARTIAL, UNAVAILABLE or NOT_RUN safeguard | Excluded from posture; reduces coverage |
| No evaluated safeguards | Posture is null |
| No requested safeguards | Posture and coverage are null |
| Duplicate control ID | Input rejected |
| Malformed status or safeguard flag | Input rejected |

The caller supplies the status and classification. This example cannot validate the truth of evidence.

## General production considerations

A production assessment system should distinguish collection errors from vulnerabilities, expose incomplete pagination, enforce authorization before collection, and reconcile uncertain external outcomes before retrying. Identity isolation, durable storage, retention and recovery need independent verification.

These are design considerations, not functionality implemented in this repository.
