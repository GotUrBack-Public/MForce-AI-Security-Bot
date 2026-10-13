#!/usr/bin/env python3
"""Conservative fixer: replace top-level GitHub Actions write-all permissions.

Only touches an exact unindented 'permissions: write-all' line in workflow YAML.
Does not modify job-level permissions or guess required write scopes.
"""
from pathlib import Path
import sys

def main() -> int:
    root = Path(".github/workflows")
    changed = []
    if not root.exists():
        return 0
    for path in sorted(root.glob("*")):
        if path.suffix not in {".yml", ".yaml"} or not path.is_file():
            continue
        original = path.read_text(encoding="utf-8")
        lines = original.splitlines(keepends=True)
        replacement = []
        for line in lines:
            if line.rstrip("\r\n") == "permissions: write-all":
                replacement.append("permissions: read-all" + ("\r\n" if line.endswith("\r\n") else "\n"))
            else:
                replacement.append(line)
        updated = "".join(replacement)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(str(path))
    for name in changed:
        print(f"Reduced broad token permissions: {name}")
    if not changed:
        print("No exact top-level write-all permissions found; no changes needed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
