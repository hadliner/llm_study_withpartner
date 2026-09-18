"""Run frozen Task2 official reference cells and their original checks on CPU.

The fetched notebooks are never edited. Exercise TODO cells are intentionally
not executed: reference functions precede the notebook's own test cell.
"""

import contextlib
import hashlib
import io
import json
import platform
import sys
import traceback
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "sources"
EVIDENCE = ROOT / "evidence"
PLAN = (
    ("kv_cache", "01_Hardware_Math_and_Systems/11_KV_Cache_and_Memory_Growth.ipynb", (4, 8, 11)),
    ("decoding", "02_PyTorch_Algorithms/21_Decoding_Strategies.ipynb", (6, 11, 8)),
    ("speculative", "02_PyTorch_Algorithms/23_Speculative_Decoding.ipynb", (3, 8, 5)),
)


def execute():
    import torch

    manifest = json.loads((SOURCE_ROOT / "manifest.json").read_text(encoding="utf-8"))
    assert torch.cuda.is_available() is False, "This evidence is specifically a CPU run"
    report = {
        "run_id": datetime.now().strftime("%Y%m%d_%H%M%S_%f"),
        "status": "running",
        "source_commit": manifest["commit"],
        "executable": sys.executable,
        "python": platform.python_version(),
        "torch": torch.__version__,
        "device": "cpu",
        "notebooks": [],
    }
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            print("TASK2 OFFICIAL CPU RUN", report["run_id"])
            print("SOURCE COMMIT", manifest["commit"])
            print("PYTHON", sys.executable, "TORCH", torch.__version__, "DEVICE cpu")
            for label, relpath, cell_ids in PLAN:
                path = SOURCE_ROOT / relpath
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                assert digest == manifest["files"][relpath]["sha256"], f"Source changed: {relpath}"
                notebook = json.loads(path.read_text(encoding="utf-8"))
                scope = {"__name__": f"task2_{label}"}
                print(f"\n--- {label}: {relpath} cells {cell_ids} ---")
                for cell_id in cell_ids:
                    cell = notebook["cells"][cell_id]
                    assert cell["cell_type"] == "code"
                    source = "".join(cell["source"])
                    exec(compile(source, f"{relpath}#cell-{cell_id}", "exec"), scope)
                report["notebooks"].append({
                    "label": label, "path": relpath, "cells": list(cell_ids),
                    "sha256": digest, "status": "pass"
                })
            print("\nALL THREE MINIMUM-SCOPE NOTEBOOK CHECKS PASSED")
        report["status"] = "pass"
    except Exception:
        report["status"] = "fail"
        output.write(traceback.format_exc())
    log = EVIDENCE / f"run_{report['run_id']}.log"
    result = EVIDENCE / f"run_{report['run_id']}.json"
    log.write_text(output.getvalue(), encoding="utf-8")
    result.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (EVIDENCE / "latest_run.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(output.getvalue(), end="")
    print("EVIDENCE", log, result)
    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="backslashreplace")
    execute()
