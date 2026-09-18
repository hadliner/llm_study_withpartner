# LLM 学习与实践

这个仓库统一保存 [Datawhale llm-algo-leetcode](https://github.com/datawhalechina/llm-algo-leetcode) 推理优化路线 Task 0–2 的代码、学习文档和讲解文档。这里记录的是本地学习交付，不代表已在课程 Issue 或微信群完成打卡。

| 目录 | 内容 |
| --- | --- |
| [`code/`](code/) | 可运行的示例、练习和项目代码 |
| [`learning-docs/`](learning-docs/) | 学习笔记、知识点与参考资料 |
| [`explanations/`](explanations/) | 对应代码的思路、运行方式和逐步讲解 |

| 任务 | 学习文档 | 代码 | 讲解文档 | 状态 |
| --- | --- | --- | --- | --- |
| Task 0：Attention、MHA/GQA/MLA | [阅读](learning-docs/task0/打卡正文.md) | [查看](code/task0/) | [复现与边界](explanations/task0/README.md) | 本地 CPU 验证通过；未对外打卡 |
| Task 1：Prefill、FlashAttention | [阅读](learning-docs/task1/打卡正文.md) | [查看](code/task1/) | [复现与边界](explanations/task1/README.md) | 本地 CPU 验证通过；未对外打卡 |
| Task 2：Decode、KV Cache、生成策略 | [阅读](learning-docs/task2/打卡正文.md) | [查看](code/task2/) | [复现与边界](explanations/task2/README.md) | 4.1 草稿、本地 CPU 验证通过；未对外打卡 |

`code/task*/sources/` 中的官方 Notebook 是上游固定版本的快照，不是本仓库原创。其教程文字按 CC BY 4.0、代码单元按 Apache-2.0 授权；每个快照目录保留了上游许可说明。自编 runner 的作用是按明确的单元顺序运行参考实现和原测试；通过结果只说明 CPU 教学样例的机制检查通过，不是 GPU 性能或真实模型效果证明。

原始 IDE 截图和包含本机绝对路径的运行日志留在本地交付目录，未放进这个公开仓库。复现方式及来源提交见各任务讲解文档。当前没有已构建、可安装的 `study_agent` 技能包。
