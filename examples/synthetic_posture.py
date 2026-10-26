"""Standalone synthetic scoring example. No collection or external effects."""
import json
from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    PARTIAL = "PARTIAL"
    UNAVAILABLE = "UNAVAILABLE"
    NOT_RUN = "NOT_RUN"


@dataclass(frozen=True)
class Control:
    control_id: str
    status: Status
    safeguard: bool = True


def summarize(controls: list[Control]) -> dict[str, float | int | None]:
    """Reject malformed/duplicate inputs; distinguish evidence from inventory."""
    seen: set[str] = set()
    for control in controls:
        if not isinstance(control.control_id, str) or not control.control_id.strip():
            raise ValueError("A nonempty control ID is required")
        if control.control_id in seen:
            raise ValueError("Duplicate control ID")
        if not isinstance(control.status, Status) or type(control.safeguard) is not bool:
            raise ValueError("Invalid control result")
        seen.add(control.control_id)
    applicable = [control for control in controls if control.safeguard]
    evaluated = [c for c in applicable if c.status in (Status.PASS, Status.FAIL)]
    passed = sum(c.status == Status.PASS for c in evaluated)
    return {
        "posture": round(100 * passed / len(evaluated), 2) if evaluated else None,
        "coverage": round(100 * len(evaluated) / len(applicable), 2) if applicable else None,
        "requested_safeguards": len(applicable),
        "evaluated_safeguards": len(evaluated),
    }


if __name__ == "__main__":
    synthetic = [
        Control("synthetic_pass", Status.PASS),
        Control("synthetic_fail", Status.FAIL),
        Control("synthetic_unavailable", Status.UNAVAILABLE),
        Control("synthetic_inventory", Status.PASS, safeguard=False),
    ]
    print(json.dumps({"mode": "synthetic", **summarize(synthetic)}, indent=2))
