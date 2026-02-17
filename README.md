# Agentic AI Starter

Multi-agent AI system with RAG integration - Production-ready starter kit.

Built by **Marcus Pollard** - U.S. Navy Veteran (SDVOSB)

![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen)
![CSNA](https://img.shields.io/badge/CSNA_2.0-Integrated-blue)
![DeFi](https://img.shields.io/badge/DeFi_Agent-New-orange)

## What This Does

This is a functional multi-agent AI system demonstrating:

- **Research Agent**: Uses RAG (Retrieval Augmented Generation) to search documents
- **Writing Agent**: Formats research into professional reports
- **Orchestrator**: Coordinates agent workflow
- **DeFi Agent** *(NEW)*: Autonomous profit-maximizing engine for decentralized finance — yield farming, cross-chain arbitrage, and strategic liquidity provision

## Architecture

```
agentic-ai-starter/
├── main.py                          # Core multi-agent system (Research + Writing + Orchestrator)
├── agents/
│   ├── __init__.py                  # Agent package exports
│   └── defi_agent.py               # DeFi profit-maximizing agent — CSNA 2.0 Logic Engine
├── prompts/
│   └── defi_agent_prompt.md         # Full system prompt & CSNA 2.0 mapping documentation
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## DeFi Agent — CSNA 2.0 Logic Engine

The DeFi Agent implements the full CSNA 2.0 four-part AI reasoning architecture:

| Module | Function | Purpose |
|--------|----------|---------|
| **RAG** | `rag_scan_market()` | Retrieves verified market intelligence from protocol APIs, price oracles, and on-chain analytics |
| **CAD** | `cad_decompose_strategy()` | Decomposes market state into independent sub-tasks: yield rebalancing, arbitrage execution, risk assessment |
| **ToT** | `tot_evaluate_branches()` | Explores multiple decision branches per sub-task, applies adversarial validation, selects optimal path |
| **RSIP** | `rsip_refine()` | Feeds performance metrics back into strategy parameters — recursive self-improvement |

### Strategies

- **DeFi Yield Farming Optimization** — Leveraged farming, yield compression/decompression, cross-protocol risk arbitrage
- **High-Frequency Cross-Exchange & Cross-Chain Arbitrage** — 10+ CEX/DEX monitoring, 0.15%+ net profit threshold, millisecond execution
- **Strategic Liquidity Provision** — Active impermanent loss management, market-making algorithms, liquidity bootstrapping

### Risk Management

- Portfolio risk score maintained below 6/10 at all times
- Only audited protocols with security score >= 8.5/10
- Gas optimization with L1/L2 threshold deferral
- Emergency pause with asset isolation on anomaly detection
- Ethical boundaries enforced — no market manipulation

## Quick Start

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
```

### Run the Research Agent

```bash
python main.py
```

### Run the DeFi Agent

```bash
python -m agents.defi_agent
```

## Connected Platforms

This project is part of the **Celestial Quantum Ascendancy** ecosystem.

| Platform | Link | Description |
|----------|------|-------------|
| **CQA Portfolio** | [celestialqa-bx9tvcdx.manus.space](https://celestialqa-bx9tvcdx.manus.space/) | Sovereign infrastructure showcase & service architecture |
| **CQA Repository** | [csna-web8-core](https://github.com/mkpollard101/csna-web8-core-or-celestial-quantum-ascendancy) | Zero-trust enterprise repo — CSNA 2.0 Logic Engine & Web8 Core |
| **Contra** | [contra.com](https://contra.com/) | Commission-free freelance network — hire or engage services |
| **Taskade** | [Taskade Flow](https://www.taskade.com/flows/01KHM9246XMWGJ3JABATK9A8PG) | AI-powered workflow & project management |

---
*Built by [Marcus Pollard](https://github.com/mkpollard101) — Procedural Architect of Modular Systems*
