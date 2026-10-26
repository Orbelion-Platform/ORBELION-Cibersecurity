# Public example capabilities

All evidence below refers exclusively to files included in this public repository.

| Demonstrated behavior | Public evidence | Limit |
| --- | --- | --- |
| Separate posture and coverage | examples/synthetic_posture.py | Uses invented input, not collected evidence |
| Inventory excluded from scoring | tests/test_synthetic_posture.py | Classification is supplied by the caller |
| Missing evidence reduces coverage | tests/test_synthetic_posture.py | Does not diagnose why evidence is missing |
| No evaluated safeguards produces null posture | tests/test_synthetic_posture.py | Null is not a passing result |
| Duplicate IDs and malformed results rejected | tests/test_synthetic_posture.py | Small educational input contract |
| Curated publication file set | scripts/validate_publication.py | Automated scanning cannot replace manual review |

Provider integration, authentication, storage, tenant isolation and external actions are outside this example. Discussion of those topics documents design considerations only.
