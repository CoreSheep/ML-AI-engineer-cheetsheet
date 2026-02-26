# ML/AI Engineering Cheat Sheet

A practical cheat sheet for **ML/AI engineering interviews** covering algorithms, ML fundamentals, Python skills, data analysis, and production AI systems.

---

## What's Inside

This repository contains **5 core modules** to help you prepare for technical interviews:

### 1. 🧠 **Machine Learning Fundamentals**
`ml-basic/`

- 100+ page comprehensive guide covering ML concepts, algorithms, and deep learning
- Topics: Loss functions, regularization, decision trees, neural networks, CNN, RNN, Transformers
- Available in both English and Chinese
- 18 visualization diagrams

**Files**: `ml_fundamentals.md`, `ml_basics.md` (Chinese), `README.md` (quick reference)

---

### 2. 💻 **Coding & Algorithms**
Root directory: `LeetCode_blind75_list.md`, `summary_notes/`

- **LeetCode Blind 75** (75/75 complete) with detailed solutions
- **Dynamic Programming** mastery guide with 5-step framework
- Algorithm patterns: Two Pointers, Sliding Window, Trees, Graphs, DP, Backtracking

**Files**: `LeetCode_blind75_list.md`, `summary_notes/dp_mastery_guide.md`

---

### 3. 🐍 **Python Skills**
`python/`

- Modern Python patterns: Decorators, dataclasses, type hints
- Unit testing with pytest
- 26 Python-focused LeetCode solutions

**Files**: `decorator_*.py`, `dataclass_demo.py`, `pytest_demo.py`

---

### 4. 📊 **Pandas & Data Analysis**
`pandas/`

- Interactive Jupyter notebook with pandas examples
- DataFrame operations, data cleaning, time series
- Quick reference for data manipulation

**Files**: `pandas_cheatsheet.ipynb`

---

### 5. 🤖 **Production RAG System**
`rag/`

- Full RAG (Retrieval-Augmented Generation) implementation
- Multi-provider LLM support (OpenAI GPT-4, Anthropic Claude)
- Vector indexing with LlamaIndex
- Streamlit web interface

**Files**: `app.py`, `agent.py`, `embedding/create_index.py`

---

### 6. 💬 **Behavioral Interview Prep** *(Bonus)*
`BQ/`

- STAR method framework with examples
- 91 categorized interview questions (General, Data Engineering, ML Engineering, AI Engineering)

**Files**: `behavioral_interview_guide.md`

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/CoreSheep/ML-AI-engineer-cheetsheet.git
cd ML-AI-engineer-cheetsheet

# Explore ML fundamentals
cat ml-basic/ml_fundamentals.md

# Practice coding
cat LeetCode_blind75_list.md

# Run RAG system (optional)
cd rag
pip install -r requirements.txt
cp .env.example .env  # Add your API keys
streamlit run app.py
```

---

## Repository Structure

```
├── ml-basic/                      # ML Fundamentals (100+ pages)
├── BQ/                            # Behavioral Interviews (91 questions)
├── python/                        # Python Skills & LeetCode
├── pandas/                        # Data Analysis
├── rag/                           # Production RAG System
├── summary_notes/                 # DP Framework
├── LeetCode_blind75_list.md       # Blind 75 (75/75)
└── TODO.md                        # Roadmap
```

---

## How to Use This Cheat Sheet

**For interview prep**:
1. Start with `ml-basic/` for ML theory
2. Practice coding with `LeetCode_blind75_list.md`
3. Prepare behavioral stories using `BQ/behavioral_interview_guide.md`

**For hands-on learning**:
1. Explore Python examples in `python/`
2. Run the RAG system in `rag/`
3. Try pandas notebook in `pandas/`

**For specific roles**:
- **Data Engineering**: Focus on `pandas/` and `rag/` system architecture
- **ML Engineering**: Deep dive into `ml-basic/` and `rag/` implementation
- **AI Engineering**: Study RAG system, LLM sections, and AI behavioral questions

---

## Progress

```
ML Fundamentals:     ████████████████████ 100%
LeetCode Blind 75:   ████████████████████ 75/75
Python Proficiency:  ████████████████████ 100%
RAG System:          ████████████████████ llamaindex
Behavioral Guide:    ████████████████████ 91 questions
```

---

## License

Personal educational use. External resources maintain their original licenses.

---

**Last Updated**: February 2026
