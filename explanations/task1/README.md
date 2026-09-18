# Task 1：Prefill 与 FlashAttention

[本地文稿](../../learning-docs/task1/打卡正文.md)围绕 Prefill 的访存问题、tiling 与 online softmax；任务要求见 [Task 1 Issue](https://github.com/datawhalechina/llm-algo-leetcode/issues/147)。

## 代码与复现

[运行入口](../../code/task1/scripts/task1_flashattention_run.py)使用[第 20 节官方 Notebook](../../code/task1/sources/20_FlashAttention_Sim.ipynb)，同目录还保留 GPU 架构和访存模型两份学习材料。上游固定提交为 `4fa62623ae7f2f207871b43c3f254a765765bf2e`。在安装 PyTorch 的 Python 环境中，从仓库根目录执行：

```powershell
python code/task1/scripts/task1_flashattention_run.py
```

脚本按导入单元 6 → 参考实现单元 11 → 原测试单元 8 运行。本地 PyCharm/Conda CPU 验证过数值一致性、非整除分块、因果遮罩等，退出码 0。这里只证明分块与 online softmax 教学实现的逻辑；没有运行 GPU benchmark，也没有完成 FlashAttention 1–4 比较的全部增项。原始截图与日志未放入公开仓库，重新运行会在 `code/task1/evidence/` 生成本机记录。

这份 Task 1 材料曾被误当成 Task 0 交付，现已按正确任务归档；尚未在课程 Issue 或群内发布。
