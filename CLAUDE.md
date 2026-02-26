# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a personal learning repository combining ML/AI engineering resources:
- **LeetCode Blind 75 solutions** (75/75 complete) with pattern recognition
- **RAG system** using LlamaIndex with multi-provider LLM support
- **Python best practices** (decorators, dataclasses, pytest)
- **Pandas cheatsheet** and data manipulation examples

**Important**: Directory naming quirk - `ML-AI-engineer-cheetsheet` contains a typo. Do not rename it as it would break existing paths and imports.

## Development Commands

### RAG System

The RAG system is the primary application in this repository. All commands should be run from the `ML-AI-engineer-cheetsheet/rag/` directory.

```bash
# Setup environment
cd ML-AI-engineer-cheetsheet/rag
pip install -r requirements.txt

# Configure API keys (required before running)
cp .env.example .env
# Edit .env with OPENAI_API_KEY and ANTHROPIC_API_KEY

# Run Streamlit app
streamlit run app.py

# Run agent tests
python test_agents.py

# Create vector index
cd embedding
python create_index.py

# Run integration tests
python test_index_integration.py
```

### Python Examples

```bash
# Run decorator examples
python ML-AI-engineer-cheetsheet/python/decorator_args_kwargs.py
python ML-AI-engineer-cheetsheet/python/decorator_nnmau.py

# Run dataclass demo
python ML-AI-engineer-cheetsheet/python/dataclass_demo.py

# Run pytest examples
cd ML-AI-engineer-cheetsheet/python
pytest pytest_demo.py -v
```

### Pandas Exploration

```bash
# Open Jupyter notebook
cd ML-AI-engineer-cheetsheet/pandas
jupyter notebook pandas_cheatsheet.ipynb
```

### ML Fundamentals Study

```bash
# Read comprehensive ML guide
cat ML-AI-engineer-cheetsheet/ml-basic/ml_fundamentals.md

# Quick reference and study approach
cat ML-AI-engineer-cheetsheet/ml-basic/README.md
```

### Behavioral Interview Prep

```bash
# Review STAR framework and question bank
cat ML-AI-engineer-cheetsheet/BQ/behavioral_interview_guide.md
```

## High-Level Architecture

### RAG System Design

The RAG system (`rag/`) uses a modular architecture with two main implementations:

**Primary Implementation (LlamaIndex + ReAct Agent)**:
```
app.py (Streamlit UI)
  ↓
RAGSystem class
  ↓
agent.py (ReAct Agent)
  ↓
get_llm() → OpenAI or Anthropic
  ↓
get_query_engine() → Vector index
  ↓
embedding/create_index.py → Persistent storage
```

**Alternative Implementation (LangChain)**:
- `langchain/rag_pipeline.py`: Standard RAG pipeline
- `langchain/invoice_generator.py`: Document generation example

**Key architectural decisions**:
1. **Multi-provider LLM support**: Both OpenAI and Anthropic are first-class citizens. The `get_llm()` function in `agent.py` switches between providers.
2. **Persistent vector indexes**: Created in `embedding/deepseek_ocr_index/` directory to avoid re-embedding on every run.
3. **Dual framework approach**: Both LlamaIndex (primary) and LangChain (examples) are maintained for comparison.

### LLM Model Configuration

Current model versions (as of Feb 2024):
- **OpenAI**: `gpt-4`, `gpt-3.5-turbo`
- **Anthropic**: `claude-3-5-sonnet-20241022`, `claude-3-5-haiku-20241022`
- **Embeddings**: `text-embedding-ada-002` (OpenAI)

Model configuration is centralized in:
- `rag/agent.py:get_llm()` - ReAct agent LLM initialization
- `rag/app.py:RAGSystem` - Streamlit app LLM configuration

### Directory Structure Patterns

```
ML-AI-engineer-cheetsheet/
├── ml-basic/        # Machine Learning Fundamentals
│   ├── ml_fundamentals.md  # Comprehensive ML guide (English, 100+ pages)
│   ├── ml_basics.md        # Original guide (Chinese, 1600+ lines)
│   ├── README.md           # Study guide and quick reference
│   └── img/                # 18 diagrams (MSE/MAE, CNN, RNN, etc.)
├── BQ/              # Behavioral Interview Preparation
│   └── behavioral_interview_guide.md  # STAR method, 65+ questions
├── python/          # Standalone Python examples (no dependencies)
├── pandas/          # Data manipulation (requires pandas, jupyter)
├── rag/             # RAG system (requires llama-index, streamlit)
│   ├── agent.py     # ReAct agent initialization
│   ├── app.py       # Streamlit UI (RAGSystem class)
│   ├── prompts.py   # System prompts
│   ├── embedding/   # Vector indexing utilities
│   └── langchain/   # Alternative LangChain examples
├── summary_notes/   # Algorithm pattern guides (DP mastery)
└── oa/              # Online assessment notes (company-specific)
```

### Data Flow: RAG Query Processing

1. **Document Ingestion**: `SimpleDirectoryReader` loads PDF/TXT/DOCX/MD files from `data/`
2. **Chunking**: Documents split into chunks for embedding
3. **Embedding**: OpenAI `text-embedding-ada-002` creates vector representations
4. **Index Storage**: Vectors persisted to `embedding/deepseek_ocr_index/` or `document_index/`
5. **Query Time**:
   - User query embedded with same model
   - Semantic search retrieves relevant chunks
   - Chunks + query sent to LLM (OpenAI or Anthropic)
   - LLM generates grounded response

## Important Patterns and Conventions

### Environment Variables

API keys are **never** hardcoded. Always use `.env` file:
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

Template is in `rag/.env.example` with placeholders.

### Import Patterns

Local imports use relative paths from the working directory:
```python
# In rag/agent.py
from prompts import CONTEXT, TOOL_DESCRIPTION  # Local module
from embedding.create_index import get_index   # Submodule
```

### Testing Philosophy

Tests are minimal and integration-focused:
- `test_agents.py`: End-to-end agent behavior
- `test_index_integration.py`: Vector index creation and querying
- `pytest_demo.py`: Python pattern examples

No unit test framework is set up beyond pytest for Python examples.

### LeetCode Problem Format

Problems in `LeetCode_blind75_list.md` and `python/LeetCode_AC_list.md` follow this structure:
- Problem link
- Solution code with explanation
- Time/space complexity analysis
- Pattern category (e.g., "Two Pointers", "DP")

Solutions reference the **5-step DP framework** in `summary_notes/dp_mastery_guide.md`.

### ML Fundamentals Content

The `ml-basic/` directory contains comprehensive machine learning documentation:

**Structure**:
- `ml_fundamentals.md` (English): 100+ page refactored guide with improved organization
- `ml_basics.md` (Chinese): Original 1600+ line comprehensive guide
- `README.md`: Study approach, quick reference tables, interview question guide
- `img/`: 18 visualization diagrams

**Coverage**:
1. **Core Concepts** (15 topics): ML workflow, loss functions, evaluation metrics, overfitting/underfitting, bias-variance tradeoff, regularization techniques
2. **Classic ML Algorithms** (50+ topics): Feature engineering, linear/logistic regression, SVM, Naive Bayes, decision trees, random forest, GBDT/XGBoost, K-means clustering
3. **Deep Learning** (20+ topics): DNN architecture, CNN, RNN/LSTM, Transformers, attention mechanism, dropout, batch normalization

**Language Note**: Both English and Chinese versions are maintained. The English version (`ml_fundamentals.md`) is restructured for international accessibility with better formatting and clearer explanations.

### Behavioral Interview Preparation

The `BQ/` directory contains interview preparation materials:

**Content** (`behavioral_interview_guide.md`):
- 15 general tips for behavioral interviews
- STAR framework (Situation, Task, Action, Result) with examples
- 65+ categorized questions covering:
  - General behavioral (self-intro, motivation, failure, conflict)
  - Data Engineering specific (pipelines, data quality, APIs)
  - ML Engineering specific (model deployment, collaboration)
  - Platform/Infrastructure (tooling, stakeholder management)
- Practice grid template for preparing core stories
- Tips for different interview rounds (first round, deep dive, executive)

**Note**: All personal information has been removed. This is a general framework applicable to any technical interview.

## Working with This Repository

### Adding New RAG Documents

1. Place files in `ML-AI-engineer-cheetsheet/data/` directory
2. Supported formats: PDF, TXT, DOCX, MD
3. Index will auto-create on first query or run `embedding/create_index.py`
4. Index persists in `embedding/deepseek_ocr_index/` or `document_index/`

### Switching LLM Providers

Edit the Streamlit sidebar in `app.py` or pass `provider` parameter to `get_agent()`:
```python
# In agent.py
agent = get_agent(provider="anthropic", model="claude-3-5-sonnet-20241022")
# or
agent = get_agent(provider="openai", model="gpt-4")
```

### Extending Python Examples

Python examples in `python/` are self-contained and don't depend on the RAG system:
- Add new decorator patterns to `decorator_*.py` files
- Add pytest examples to `pytest_demo.py`
- No external dependencies required (except pytest for testing)

## Known Issues and Quirks

1. **Nested git repository**: `ML-AI-engineer-cheetsheet/.git` exists inside the main repo. Git operations should be run from the root directory unless specifically working on the submodule.

2. **Data directory not in version control**: `data/` is gitignored. You'll need to add your own documents for RAG testing.

3. **Index directories**: Multiple index directories exist (`document_index/`, `embedding/deepseek_ocr_index/`). This is intentional for testing different indexing strategies.

4. **Model version updates**: When Anthropic/OpenAI release new models, update version strings in both `agent.py` and `app.py`.

## Dependencies

### Core RAG System
- `llama-index>=0.10.0` - Primary RAG framework
- `streamlit>=1.28.0` - Web interface
- `openai>=1.0.0` - OpenAI API client
- `anthropic>=0.7.0` - Anthropic API client
- `python-dotenv>=1.0.0` - Environment variable management

### Python Examples
- No dependencies for decorator/dataclass examples
- `pytest>=7.0.0` for running tests

### Data Analysis
- `pandas` for data manipulation examples
- `jupyter` for notebook exploration

## Study & Interview Preparation Workflow

### For ML/AI Interviews

**Week 1-2: ML Fundamentals**
1. Read `ml-basic/ml_fundamentals.md` sections 1-1.15 (Core Concepts)
2. Practice explaining bias-variance tradeoff, overfitting solutions
3. Memorize evaluation metrics formulas and use cases

**Week 3-4: Classic ML Algorithms**
1. Study `ml-basic/ml_fundamentals.md` section 2 (Classic ML)
2. Understand decision trees → random forest → GBDT progression
3. Practice explaining when to use which algorithm

**Week 5-6: Deep Learning**
1. Study `ml-basic/ml_fundamentals.md` section 3 (Deep Learning)
2. Understand CNN for images, RNN for sequences, Transformers
3. Practice explaining backpropagation and attention mechanism

**Week 7: Behavioral Prep**
1. Read `BQ/behavioral_interview_guide.md`
2. Prepare 10-15 core stories using STAR framework
3. Practice out loud for 2-3 minutes per story

**Week 8: Algorithm Practice**
1. Work through `LeetCode_blind75_list.md`
2. Focus on DP problems using the 5-step framework
3. Practice explaining thought process clearly

### For Coding Interviews

Follow the algorithm-focused workflow in `summary_notes/dp_mastery_guide.md`
