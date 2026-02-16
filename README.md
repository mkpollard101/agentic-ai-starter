# Agentic AI Starter

Multi-agent AI system with RAG integration - Production-ready starter kit.

Built by **Marcus Pollard** - U.S. Navy Veteran (SDVOSB)

## 🎯 What This Does

This is a functional multi-agent AI system demonstrating:

- **Research Agent**: Uses RAG (Retrieval Augmented Generation) to search documents
- **Writing Agent**: Formats research into professional reports
- **Orchestrator**: Coordinates agent workflow

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- OpenAI API key

### Installation

```bash
# Clone the repository
git clone https://github.com/mkpollard101/agentic-ai-starter.git
cd agentic-ai-starter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "OPENAI_API_KEY=your_key_here" > .env
