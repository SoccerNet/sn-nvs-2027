"""Run Triangle Splatting metrics.py on prepared scene model directories.

Each model needs test/<method>/{renders,gt}/*.png and the upstream CUDA
environment. This is not yet the official CodaBench ranking adapter.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--triangle-repo", type=Path, required=True)
    parser.add_argument("--model-path", type=Path, action="append", required=True)
    args = parser.parse_args()
    script = (args.triangle_repo / "metrics.py").resolve()
    if not script.is_file():
        parser.error("Triangle Splatting metrics.py not found")
    model_paths = [path.resolve() for path in args.model_path]
    for path in model_paths:
        if not (path / "test").is_dir():
            parser.error(f"Missing {path / 'test'}")
        (path / "results.json").unlink(missing_ok=True)
    result = subprocess.run(
        [sys.executable, str(script), "-m", *map(str, model_paths)],
        cwd=args.triangle_repo.resolve(), check=False,
    )
    if result.returncode:
        return result.returncode
    for path in model_paths:
        output = path / "results.json"
        if not output.is_file():
            print(f"Triangle Splatting produced no results for {path}", file=sys.stderr)
            return 1
        metrics = json.loads(output.read_text(encoding="utf-8"))
        if not metrics or not all("PSNR" in item for item in metrics.values()):
            print(f"No PSNR in {output}", file=sys.stderr)
            return 1
        print(f"{path}: {metrics}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
