---
title: Agentic Rag Portfolio
emoji: 📉
colorFrom: green
colorTo: blue
sdk: gradio
sdk_version: 6.2.0
app_file: app.py
pinned: false
license: mit
---

<p align="center">
  <a href="README.md">English</a> | 
  <a href="README_zh.md">中文</a>
</p>

# Agentic RAG System

[中文版 README](README_zh.md)

## 🎯 Project Overview

This project is built to explore and implement:
- **Vector Embeddings**: Dense + Sparse hybrid retrieval using Qdrant
- **Agent Orchestration**: LangGraph-based workflow for query processing
- **RAG Pipeline**: Document ingestion, chunking, indexing, and retrieval

## ✏️ What I Built

- Built an Agentic RAG system from scratch with LangGraph, adapted for Chinese long documents
- Implemented LangGraph state management and graph orchestration: main graph for dialogue + aggregation, subgraph for deep retrieval
- Added hierarchical indexing (Parent-Child) to balance precision and context
- Integrated hybrid retrieval (Dense + Sparse) to improve recall
- Designed conversation memory for multi-turn dialogue; added query rewriting and human-in-the-loop controls
- Implemented multi-agent Map-Reduce to handle complex queries

## 🚀 Key Features

- **Hybrid Retrieval**: Combines dense embeddings (BGE-zh) and sparse embeddings (BM25) for better search accuracy
- **LangGraph Workflow**: Implements conversation memory, query rewriting, and document retrieval as graph nodes
- **Chinese Optimization**: Customized for Chinese documents with BGE-zh embedding model
- **Hierarchical Chunking**: Parent-child chunking strategy for precision + context
- **Gradio UI**: Interactive interface for document management and Q&A

## 🛠️ Tech Stack

- **Framework**: LangGraph, LangChain
- **Vector DB**: Qdrant (local file-based)
- **Embeddings**: 
  - Dense: BAAI/bge-base-zh-v1.5
  - Sparse: Qdrant/bm25
- **LLM**: Qwen-max via DashScope API
- **UI**: Gradio

## 📚 What I Learned

1. **LangGraph Concepts**: 
   - State management with Pydantic models
   - Node functions and conditional edges
   - Graph compilation and checkpointing

2. **RAG Architecture**: 
   - Parent-child chunking strategy
   - Hybrid retrieval (dense + sparse)
   - Query rewriting and clarification

3. **Vector Databases**: 
   - Qdrant setup and collection management
   - Similarity search with score thresholds
   - Sparse vector support

4. **Agent Workflows**: 
   - Query analysis and rewriting
   - Tool calling (search, retrieve)
   - Response aggregation

## 🏗️ Project Structure

```
├── core/                    # Core RAG components
│   ├── rag_system.py       # Main RAG system initialization
│   ├── chat_interface.py   # Chat interface handler
│   └── document_manager.py # Document ingestion and management
├── db/                      # Database management
│   ├── vector_db_manager.py    # Qdrant vector DB operations
│   └── parent_store_manager.py # Parent chunk storage (JSON)
├── rag_agent/              # LangGraph agent implementation
│   ├── graph.py            # Graph construction and compilation
│   ├── nodes.py            # Node functions (summarize, rewrite, agent)
│   ├── edges.py            # Conditional routing logic
│   ├── graph_state.py      # State definitions
│   ├── prompts.py          # System prompts for LLM
│   ├── tools.py            # Retrieval tools (search, retrieve)
│   └── schemas.py          # Pydantic data models
├── ui/                      # User interface
│   ├── gradio_app.py       # Gradio UI components
│   └── css.py              # Custom styling
├── config.py                # Configuration (models, chunk sizes)
├── document_chunker.py      # Document chunking strategy
├── util.py                  # PDF to Markdown conversion
└── app.py                   # Application entry point
```

## 🚦 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

Create `config_secrets.json` in the project root:

```json
{
  "DASHSCOPE_API_KEY": "your-dashscope-api-key"
}
```

Or set environment variable:
```bash
export DASHSCOPE_API_KEY="your-api-key"
```

### 3. Run the Application

```bash
python app.py
```

The Gradio interface will launch at `http://127.0.0.1:7860`

## 📖 How It Works

1. **Document Ingestion**: 
   - Upload PDF/Markdown files through the UI
   - Convert to Markdown format
   - Split into parent and child chunks

2. **Indexing**:
   - Child chunks: Small, precise chunks (500 tokens) for initial retrieval
   - Parent chunks: Larger context chunks (2000-10000 tokens) stored separately
   - Both embedded and stored in Qdrant

3. **Query Processing**:
   - Conversation summarization for context
   - Query analysis and rewriting
   - Hybrid retrieval (dense + sparse)
   - Parent chunk retrieval for full context
   - Response generation with source citations

## 🔧 Customization

The system is designed to be modular:

- **LLM Provider**: Switch between DashScope, OpenAI, Ollama in `config.py`
- **Embedding Models**: Change dense/sparse models in `config.py`
- **Chunking Strategy**: Adjust sizes in `config.py`
- **Agent Workflow**: Modify nodes and edges in `rag_agent/`

## 📝 Notes
- Focused on RAG + Agent architecture practice; provides a runnable demo (Gradio UI + Qdrant local storage)
- Uses cloud APIs by default; local models (e.g., Ollama) are optional
- Customized for Chinese document processing

## 🔗 References

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Qdrant Documentation](https://qdrant.tech/documentation/)
- [LangChain Documentation](https://python.langchain.com/)

## 📄 License
MIT License.
