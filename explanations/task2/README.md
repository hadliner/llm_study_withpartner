# Task 2：单请求 Decode 与生成策略

[本地文稿](../../learning-docs/task2/打卡正文.md)是 [Task 2 Issue #165](https://github.com/datawhalechina/llm-algo-leetcode/issues/165) 的 4.1 最小档草稿，讨论 KV Cache、Greedy/Temperature/Top-k/Top-p 与投机解码。未向 Issue 或群提交。

## 代码与复现

[运行入口](../../code/task2/scripts/task2_official_cpu_run.py)读取 `sources/manifest.json`，校验 SHA256，再执行上游固定提交 `518cc451c51a1e86d6e17f304147135d2a8cb379` 下的三个 Notebook：

1. 第 11 节 KV Cache：代码单元 4、8、11。
2. 第 21 节 Decoding Strategies：导入 6、参考实现 11、原测试 8。
3. 第 23 节 Speculative Decoding：导入 3、参考实现 8、原测试 5。

在安装 PyTorch 的 Python 环境中，从仓库根目录执行：

```powershell
python code/task2/scripts/task2_official_cpu_run.py
```

本地 PyCharm/Conda CPU 环境的机制检查通过，退出码 0。Notebook 的练习 TODO 不是由本轮独立完成。`sources/` 中第 35 节和第 68 节仅作为参考材料下载，未执行，因此不能称为已完成 4.2/4.3。KV Cache 数字是理论账本，脚本没有测真实模型显存、生成质量或 GPU 加速。原始截图与日志未放入公开仓库，重新运行会在 `code/task2/evidence/` 生成本机记录。
