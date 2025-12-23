<p align="center">
  <a href="README.md">English</a> | 
  <a href="README_zh.md">中文</a>
</p>

# Agentic RAG 系统

[English README](README.md)

## 🎯 项目概述

这是一个用于学习和实现以下能力的项目：
- **向量化检索**：使用 Qdrant 实现 Dense + Sparse 混合检索
- **Agent 编排**：基于 LangGraph 的查询处理工作流
- **RAG 流程**：文档导入、分块、索引和检索

## ✏️ 我做了什么

- 基于 LangGraph 官方文档和示例，从零搭建 Agentic RAG 系统，并针对中文长文档做适配
- 落地 LangGraph 状态管理与图编排，构建主图（对话管理、结果聚合）与子图（深度检索）
- 实现层次化索引（Parent-Child）以平衡检索精度与上下文
- 集成混合检索（Dense + Sparse）提升召回率
- 设计对话记忆，支持多轮对话；添加查询重写与 Human-in-the-loop 机制
- 实现多 Agent Map-Reduce 处理复杂查询

## 🚀 核心功能

- **混合检索**：结合 Dense Embedding (BGE-zh) 和 Sparse Embedding (BM25) 提升搜索准确性
- **LangGraph 工作流**：将对话记忆、查询改写、文档检索实现为图节点
- **中文优化**：针对中文文档定制，使用 BGE-zh 嵌入模型
- **分层分块**：父子分块策略，兼顾精确度和上下文
- **Gradio 界面**：交互式文档管理和问答界面

## 🛠️ 技术栈

- **框架**：LangGraph, LangChain
- **向量数据库**：Qdrant (本地文件存储)
- **嵌入模型**：
  - 密集向量：BAAI/bge-base-zh-v1.5
  - 稀疏向量：Qdrant/bm25
- **大语言模型**：通义千问 (DashScope API)
- **界面**：Gradio

## 📚 学习收获

1. **LangGraph 概念**：
   - 使用 Pydantic 模型进行状态管理
   - 节点函数和条件边
   - 图编译和检查点

2. **RAG 架构**：
   - 父子分块策略
   - 混合检索（密集 + 稀疏）
   - 查询改写和澄清

3. **向量数据库**：
   - Qdrant 配置和集合管理
   - 带阈值控制的相似度搜索
   - 稀疏向量支持

4. **Agent 工作流**：
   - 查询分析和改写
   - 工具调用（搜索、检索）
   - 响应聚合

## 🏗️ 项目结构

```
├── core/                    # 核心 RAG 组件
│   ├── rag_system.py       # RAG 系统初始化
│   ├── chat_interface.py   # 聊天接口处理
│   └── document_manager.py # 文档导入和管理
├── db/                      # 数据库管理
│   ├── vector_db_manager.py    # Qdrant 向量数据库操作
│   └── parent_store_manager.py # 父块存储 (JSON)
├── rag_agent/              # LangGraph Agent 实现
│   ├── graph.py            # 图构建和编译
│   ├── nodes.py            # 节点函数（总结、改写、代理）
│   ├── edges.py            # 条件路由逻辑
│   ├── graph_state.py      # 状态定义
│   ├── prompts.py          # LLM 系统提示词
│   ├── tools.py            # 检索工具（搜索、检索）
│   └── schemas.py          # Pydantic 数据模型
├── ui/                      # 用户界面
│   ├── gradio_app.py       # Gradio UI 组件
│   └── css.py              # 自定义样式
├── config.py                # 配置（模型、分块大小）
├── document_chunker.py      # 文档分块策略
├── util.py                  # PDF 转 Markdown 转换
└── app.py                   # 应用入口
```

## 🚦 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API 密钥

在项目根目录创建 `config_secrets.json`：

```json
{
  "DASHSCOPE_API_KEY": "你的-dashscope-api-key"
}
```

或设置环境变量：
```bash
export DASHSCOPE_API_KEY="你的-api-key"
```

### 3. 运行应用

```bash
python app.py
```

Gradio 界面将在 `http://127.0.0.1:7860` 启动

## 📖 工作原理

1. **文档导入**：
   - 通过 UI 上传 PDF/Markdown 文件
   - 转换为 Markdown 格式
   - 分割为父块和子块

2. **索引构建**：
   - 子块：小且精确的块（500 tokens）用于初始检索
   - 父块：更大的上下文块（2000-10000 tokens）单独存储
   - 两者都进行嵌入并存储在 Qdrant 中

3. **查询处理**：
   - 对话摘要以获取上下文
   - 查询分析和改写
   - 混合检索（密集 + 稀疏）
   - 检索父块以获取完整上下文
   - 生成带来源引用的响应

## 🔧 定制化

系统设计为模块化：

- **LLM 提供商**：在 `config.py` 中切换 DashScope、OpenAI、Ollama
- **嵌入模型**：在 `config.py` 中更改密集/稀疏模型
- **分块策略**：在 `config.py` 中调整大小
- **Agent 工作流**：在 `rag_agent/` 中修改节点和边

## 📝 说明
- 专注于 RAG + Agent 架构实践，提供可运行的 Demo（Gradio UI + Qdrant 本地存储）
- 默认使用云端 API，可按需切换本地模型（如 Ollama）
- 针对中文文档处理进行了定制

## 🔗 参考资料

- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
- [Qdrant 文档](https://qdrant.tech/documentation/)
- [LangChain 文档](https://python.langchain.com/)

## 📄 许可证
本项目基于 MIT 许可证发布。