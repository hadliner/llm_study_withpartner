# 代码

每个 Task 目录包含自编 `scripts/` 运行入口与固定版本的官方 `sources/` Notebook。运行脚本会在对应 Task 下生成 `evidence/` 日志；这些可能含本机路径，已被 `.gitignore` 排除。

本地已验证的环境是 Python 3.13.9、PyTorch 2.14.0+cpu；Task 1 环境还有 NumPy 2.3.5。脚本使用自身位置寻找 `sources/`，但跨平台环境配置未在本仓库重新验证。具体单元顺序和验证边界见各任务的[讲解文档](../explanations/)。

`sources/` 的 Notebook 来自 [Datawhale llm-algo-leetcode](https://github.com/datawhalechina/llm-algo-leetcode)。文字与代码分别适用每个 `sources/` 中的 `LICENSE`、`LICENSE-CODE`，不得当作本仓库原创。
