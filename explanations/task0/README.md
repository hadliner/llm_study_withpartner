# Task 0：Attention、MHA/GQA/MLA

学习目标见 [Task 0 要求](https://github.com/datawhalechina/llm-algo-leetcode/issues/146)；[本地文稿](../../learning-docs/task0/打卡正文.md)解释了 Attention 与 Transformer 的关系，以及 MHA、GQA、MLA 的缓存思路。

## 代码与复现

[运行入口](../../code/task0/scripts/task0_attention_run.py)使用[第 04 节官方 Notebook](../../code/task0/sources/04_Attention_MHA_GQA.ipynb)，固定上游提交 `4fa62623ae7f2f207871b43c3f254a765765bf2e`。在安装 PyTorch 的 Python 环境中，从仓库根目录执行：

```powershell
python code/task0/scripts/task0_attention_run.py
```

脚本按导入单元 6 → 参考实现单元 11 → 原测试单元 8 运行。本地 PyCharm/Conda CPU 验证过 MHA/GQA 输出、KV Cache 增量一致性与非法参数，测试通过且退出码 0。此结果来自官方参考实现，并非独立完成 Notebook 中的练习 TODO；MLA 本轮仅做概念学习。原始截图与日志未放入公开仓库，重新运行会在 `code/task0/evidence/` 生成本机记录。

当前是本地交付版，没有在课程 Issue 或群内完成打卡。
