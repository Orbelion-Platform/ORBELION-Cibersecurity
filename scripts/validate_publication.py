"""Validate the entire candidate public tree; never print suspected credentials."""
from pathlib import Path
import re
import hashlib

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = set(["README.md","PUBLICATION_SCOPE.md","SECURITY.md","docs/MAINTENANCE.md","docs/VERIFIED_CAPABILITIES.md","docs/FAILURE_MODEL.md",".gitignore","examples/synthetic_posture.py","tests/test_synthetic_posture.py",".github/workflows/validate.yml","scripts/validate_publication.py"])
ASSET = 'docs/assets/cybersecurity-defense-in-depth.png'
ASSET_SHA256 = '9a639dc189fae52ce75b6be42a6f06eef80002193fa0896fe0e28e482ad35f51'
ALLOWED.add(ASSET)
SKIP = {".git", "__pycache__", ".venv", ".pytest_cache"}
PATTERNS = [
    r"-----BEGIN " + r"(?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    r"gh[pousr]_[A-Za-z0-9]{30,}",
    r"github_pat_[A-Za-z0-9_]{30,}",
    r"sk-[A-Za-z0-9]{24,}",
]
seen = set()
for path in ROOT.rglob("*"):
    relative = path.relative_to(ROOT)
    if ".git" in relative.parts:
        continue
    if path.is_symlink():
        raise SystemExit(f"Symlink prohibited: {relative.as_posix()}")
    if any(part in SKIP for part in relative.parts) or not path.is_file():
        continue
    name = relative.as_posix()
    if name not in ALLOWED:
        raise SystemExit(f"Unapproved file: {name}")
    if name == ASSET:
        data = path.read_bytes()
        if not data.startswith(b"\x89PNG\r\n\x1a\n") or hashlib.sha256(data).hexdigest() != ASSET_SHA256:
            raise SystemExit("Approved image integrity check failed")
        seen.add(name)
        continue
    content = path.read_text(encoding="utf-8")
    if any(re.search(pattern, content) for pattern in PATTERNS):
        raise SystemExit(f"Potential credential in: {name}")
    if path.suffix == ".md":
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if "://" not in target and not target.startswith("#"):
                resolved = (path.parent / target.split("#")[0]).resolve()
                if not resolved.is_relative_to(ROOT) or not resolved.is_file():
                    raise SystemExit(f"Invalid local link in: {name}")
    seen.add(name)
if ALLOWED - seen:
    raise SystemExit(f"Missing approved files: {sorted(ALLOWED - seen)}")
print(f"PASS: {len(seen)} approved files (including the original image)")
