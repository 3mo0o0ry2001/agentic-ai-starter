<div align="center">

# 🤖 Agentic AI Starter Kit

### A modular, production-ready framework for building AI Agents using `aisuite` and Tool Calling patterns.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![AISuite](https://img.shields.io/badge/AI%20Suite-Enabled-orange?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenRouter-Compatible-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

[Report Bug](https://github.com/3mo0o0ry2001/agentic-ai-starter/issues) · [Request Feature](https://github.com/3mo0o0ry2001/agentic-ai-starter/issues)

</div>

---

## 📖 Overview

This project implements a robust **Agentic Workflow** where an LLM (Large Language Model) acts as an intelligent orchestrator. Instead of just generating text, the agent analyzes user requests, selects the appropriate tools from a custom toolkit, executes them, and synthesizes the results.

It serves as a foundational template for building autonomous agents capable of interacting with external APIs, file systems, and more.

## ✨ Key Features

* **🧠 Intelligent Orchestration:** The agent autonomously decides *which* tool to use and *when* based on context.
* **🛠️ Modular Tool System:** Tools are decoupled from the core logic (`tools.py`), making it easy to add new capabilities (e.g., Web Search, Database Querying).
* **🔌 Provider Agnostic:** Built with `aisuite`, allowing seamless switching between OpenAI, Anthropic, Mistral, or OpenRouter models.
* **🔄 Multi-Step Reasoning:** Handles complex queries that require chaining multiple tools (e.g., "Check weather -> Write report -> Save file").

## 📂 Project Structure

```text
agentic-ai-starter/
├── main.py             # 🧠 The Agent's Brain (Orchestration Logic)
├── tools.py            # 🛠️ The Toolkit (Python Functions)
├── .env                # 🔐 Environment Variables (API Keys)
├── requirements.txt    # 📦 Dependencies
└── README.md           # 📄 Documentation