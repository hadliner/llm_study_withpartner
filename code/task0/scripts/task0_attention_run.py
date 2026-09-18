"""Run the frozen official CPU reference and original tests for Task0.
Official code: Datawhale llm-algo-leetcode, Apache-2.0.
This runner records a fresh run; it never uses notebook stored outputs.
"""
import contextlib
from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys
import traceback

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / 'sources' / '04_Attention_MHA_GQA.ipynb'

class Tee:
    def __init__(self, *streams):
        self.streams = streams
    def write(self, text):
        for stream in self.streams:
            stream.write(text)
            stream.flush()
        return len(text)
    def flush(self):
        for stream in self.streams:
            stream.flush()

def main():
    run_id = datetime.now().astimezone().strftime('%Y%m%d_%H%M%S_%f')
    evidence = ROOT / 'evidence'
    evidence.mkdir(exist_ok=True)
    report = {'run_id': run_id, 'task': '202609 Task0',
              'python': sys.version, 'executable': sys.executable,
              'notebook_sha256': hashlib.sha256(NOTEBOOK.read_bytes()).hexdigest(),
              'source_commit': (ROOT/'sources'/'commit.txt').read_text(encoding='utf-8-sig').strip(),
              'mode': 'official reference cells 6 -> 11 -> original tests 8; CPU',
              'gpu_benchmark': False, 'passed': False}
    status = 0
    log_path = evidence / f'run_{run_id}.log'
    with log_path.open('w', encoding='utf-8') as log:
        with contextlib.redirect_stdout(Tee(sys.stdout, log)), contextlib.redirect_stderr(Tee(sys.stderr, log)):
            print('202609 Task0 | Attention / MHA / GQA / KV Cache')
            print('Official Part02 04 reference implementation + original CPU tests')
            print('Run:', run_id)
            print('Python:', sys.executable)
            try:
                import torch
                torch.set_num_threads(1)
                torch.set_default_device('cpu')
                torch.manual_seed(42)
                report['torch'] = torch.__version__
                report['device'] = 'cpu'
                print('Torch:', torch.__version__, '| device: CPU | threads: 1')
                notebook = json.loads(NOTEBOOK.read_text(encoding='utf-8'))
                namespace = {'__name__': '__official_cpu__'}
                for index in (6, 11, 8):
                    cell = notebook['cells'][index]
                    assert cell['cell_type'] == 'code'
                    code = ''.join(cell['source'])
                    if index == 11:
                        assert 'class GroupedQueryAttention' in code and 'def repeat_kv' in code
                    if index == 8:
                        assert 'def test_mha_mqa_gqa' in code
                    exec(compile(code, f'{NOTEBOOK.name}:cell{index}', 'exec'), namespace)
                report['passed'] = True
                print('Coverage: MHA / GQA output shapes and finite values')
                print('Coverage: KV Cache incremental consistency / invalid head configurations')
                print('OFFICIAL_TASK0_CPU_TESTS_PASS')
                print('Note: official reference implementation; CPU checks only; MLA is conceptual.')
            except Exception:
                status = 1
                traceback.print_exc()
            print('EXIT_STATUS:', status)
            print('Evidence:', log_path.name)
    report['log_file'] = log_path.name
    (evidence/f'run_{run_id}.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    (evidence/'latest_run.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    return status

if __name__ == '__main__':
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(errors='backslashreplace')
    raise SystemExit(main())
