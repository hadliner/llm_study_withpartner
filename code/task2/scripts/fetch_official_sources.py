"""Fetch a frozen copy of the Task2 source notebooks via GitHub's contents API.

Requires an authenticated gh CLI. This is source acquisition, not execution.
"""

import base64
import hashlib
import json
import subprocess
from pathlib import Path


COMMIT = "518cc451c51a1e86d6e17f304147135d2a8cb379"
REPO = "datawhalechina/llm-algo-leetcode"
FILES = [
    "01_Hardware_Math_and_Systems/11_KV_Cache_and_Memory_Growth.ipynb",
    "02_PyTorch_Algorithms/21_Decoding_Strategies.ipynb",
    "02_PyTorch_Algorithms/23_Speculative_Decoding.ipynb",
    "02_PyTorch_Algorithms/35_Multi_Token_Decoding.ipynb",
    "02_PyTorch_Algorithms/68_Speculative_Decoding_Benchmark.ipynb",
    "LICENSE",
    "LICENSE-CODE",
]
ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = {"repo": REPO, "commit": COMMIT, "files": {}}
    for path in FILES:
        response = subprocess.run(
            ["gh", "api", f"repos/{REPO}/contents/{path}?ref={COMMIT}"],
            check=True, capture_output=True, text=True, encoding="utf-8"
        )
        record = json.loads(response.stdout)
        if record["encoding"] != "base64":
            raise ValueError(f"Unexpected encoding: {path}")
        data = base64.b64decode(record["content"], validate=False)
        target = ROOT / "sources" / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        manifest["files"][path] = {
            "git_blob_sha": record["sha"],
            "sha256": hashlib.sha256(data).hexdigest(),
            "bytes": len(data),
        }
        print(f"{path}: {len(data)} bytes")
    (ROOT / "sources" / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
