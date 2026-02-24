# ML/AI Engineering Interview Preparation

A comprehensive resource for Data Engineering, Machine Learning Engineering, and AI Engineering interview preparation. This repository provides structured content covering technical fundamentals, coding problems, behavioral interviews, and production system implementation.

## Quick Navigation

- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Study Guides](#study-guides)
- [How to Use This Repository](#how-to-use-this-repository)
- [Progress Tracking](#progress-tracking)

## Getting Started

### For ML/AI Engineering Interviews

**Week 1-2: Fundamentals**
```bash
# Study core ML concepts
cat ml-basic/ml_fundamentals.md

# Quick reference
cat ml-basic/README.md
```

**Week 3-4: Behavioral Prep**
```bash
# Prepare STAR stories
cat BQ/behavioral_interview_guide.md
```

**Week 5-8: Coding Practice**
```bash
# LeetCode problems
cat LeetCode_blind75_list.md

# DP framework
cat summary_notes/dp_mastery_guide.md
```

### For Data Engineering Interviews

**Focus Areas**:
1. Data pipeline design (see `rag/` for production examples)
2. SQL and data processing (see `pandas/`)
3. Python proficiency (see `python/`)
4. Behavioral questions (see `BQ/behavioral_interview_guide.md` - Data Engineering section)

## Repository Structure

```
ML-AI-engineer-cheetsheet/
│
├── ml-basic/                          # Machine Learning Fundamentals
│   ├── ml_fundamentals.md             # 100+ page comprehensive guide (English)
│   ├── ml_basics.md                   # Original guide (Chinese, 1600+ lines)
│   ├── README.md                      # Study guide with quick reference
│   └── img/                           # 18 visualization diagrams
│
├── BQ/                                # Behavioral Interview Preparation
│   └── behavioral_interview_guide.md  # Complete STAR framework guide
│                                      # 91 questions for Data/ML/AI roles
│
├── python/                            # Python Programming
│   ├── LeetCode_AC_list.md            # 26 Python problems with solutions
│   ├── decorator_args_kwargs.py       # Advanced decorator patterns
│   ├── decorator_nnmau.py             # nnmau pattern examples
│   ├── dataclass_demo.py              # Modern Python dataclasses
│   └── pytest_demo.py                 # Unit testing with pytest
│
├── pandas/                            # Data Processing
│   ├── pandas_cheatsheet.ipynb        # Interactive Jupyter guide
│   ├── LeetCode_AC_list.md            # Pandas-based solutions
│   └── img/strftime.png               # Date formatting reference
│
├── rag/                               # Production RAG System
│   ├── app.py                         # Streamlit Q&A interface
│   ├── agent.py                       # ReAct agent implementation
│   ├── prompts.py                     # System prompts
│   ├── requirements.txt               # Python dependencies
│   ├── .env.example                   # API key template
│   ├── embedding/create_index.py      # Vector indexing
│   └── langchain/                     # Alternative implementations
│
├── summary_notes/                     # Algorithm Guides
│   └── dp_mastery_guide.md            # Dynamic programming patterns
│
├── LeetCode_blind75_list.md           # Blind 75 (75/75 complete)
│
└── oa/                                # Online Assessment Notes
    └── [company-specific prep]
```

## Study Guides

### 1. Machine Learning Fundamentals

**Location**: `ml-basic/`

**Coverage**:
- Core Concepts: Loss functions, evaluation metrics, bias-variance tradeoff, regularization
- Classic ML: Linear/Logistic Regression, SVM, Naive Bayes, Decision Trees, Random Forest, GBDT/XGBoost, K-Means
- Deep Learning: DNN, CNN, RNN/LSTM, Transformers, attention mechanism
- Feature Engineering: Numerical, categorical, text, and sequence data

**Files**:
- `ml_fundamentals.md` - Primary resource (English, well-structured)
- `ml_basics.md` - Comprehensive original (Chinese)
- `README.md` - Study approach and quick reference tables

**Study Time**: 4-6 weeks for comprehensive coverage

**How to Study**:
1. Read `README.md` first for overview and study strategy
2. Study `ml_fundamentals.md` section by section
3. Review diagrams in `img/` for visual understanding
4. Use README quick reference tables during interview prep

### 2. Behavioral Interviews

**Location**: `BQ/behavioral_interview_guide.md`

**Coverage**:
- STAR method framework with examples
- 15 general tips for behavioral interviews
- 91 categorized questions:
  - General behavioral (10)
  - Data Engineering (13)
  - ML Engineering (32)
  - AI Engineering (36)
- 3 complete STAR story examples
- Preparation checklist and practice grid

**Study Time**: 1-2 weeks

**How to Prepare**:
1. Read the guide completely first
2. Identify 10-15 stories from your experience
3. Write full STAR answers for each story
4. Practice out loud (2-3 minutes per story)
5. Map each story to multiple question types

### 3. Coding & Algorithms

**Location**: `LeetCode_blind75_list.md`, `summary_notes/dp_mastery_guide.md`

**Coverage**:
- LeetCode Blind 75 (75/75 complete)
- Dynamic programming 5-step framework
- Algorithm patterns:
  - Arrays & Hashing
  - Two Pointers
  - Sliding Window
  - Binary Search
  - Trees & Graphs
  - Backtracking

**Study Time**: 8-12 weeks

**How to Practice**:
1. Start with `summary_notes/dp_mastery_guide.md` for DP strategy
2. Work through Blind 75 by pattern, not sequentially
3. Understand the pattern, not just the solution
4. Practice explaining your approach out loud

### 4. Python Proficiency

**Location**: `python/`

**Coverage**:
- Decorator patterns (timing, logging, memoization)
- Modern Python (dataclasses, type hints)
- Unit testing with pytest
- 26 LeetCode problems focused on Python techniques

**Study Time**: 1-2 weeks

**How to Study**:
1. Run each Python file to see examples in action
2. Modify examples to understand behavior
3. Read `LeetCode_AC_list.md` for problem-solving patterns
4. Practice writing tests with pytest

### 5. Data Processing

**Location**: `pandas/`

**Coverage**:
- DataFrame operations
- Data cleaning techniques
- Time series handling
- Visualization basics

**Study Time**: 1 week

**How to Study**:
1. Open `pandas_cheatsheet.ipynb` in Jupyter
2. Run cells and experiment with examples
3. Reference `img/strftime.png` for date formatting
4. Practice with `LeetCode_AC_list.md` problems

### 6. Production AI Systems

**Location**: `rag/`

**What It Is**: A production-ready RAG (Retrieval-Augmented Generation) system demonstrating:
- Multi-provider LLM support (OpenAI, Anthropic)
- Vector indexing with LlamaIndex
- Persistent embedding storage
- Web interface with Streamlit

**Study Time**: 2-3 weeks

**How to Use**:
1. Study the architecture first:
   ```
   Documents → Load & Split → Embed → Vector Store → Query → LLM → Response
   ```

2. Set up and run:
   ```bash
   cd rag
   pip install -r requirements.txt
   cp .env.example .env
   # Add your API keys to .env
   streamlit run app.py
   ```

3. Study the code:
   - `app.py`: Web interface and RAGSystem class
   - `agent.py`: ReAct agent with tool integration
   - `embedding/create_index.py`: Vector indexing logic
   - `langchain/`: Alternative implementations

## How to Use This Repository

### For Complete Interview Prep (8 weeks)

**Weeks 1-2: ML Fundamentals**
- Read `ml-basic/ml_fundamentals.md` sections 1.1-1.15
- Understand loss functions, metrics, overfitting/underfitting
- Practice explaining bias-variance tradeoff

**Weeks 3-4: Classic ML + Deep Learning**
- Study sections 2-3 of `ml_fundamentals.md`
- Focus on when to use which algorithm
- Understand CNN, RNN, Transformers

**Weeks 5-6: Coding Practice**
- Complete 40+ Blind 75 problems
- Master DP using 5-step framework
- Practice 2-3 problems daily

**Week 7: Behavioral Prep**
- Read `BQ/behavioral_interview_guide.md`
- Write 10-15 STAR stories
- Practice answering out loud

**Week 8: Review & Mock Interviews**
- Review weak areas in ML
- Complete remaining problems
- Mock interviews with peers

### For Targeted Preparation

**Data Engineering Focus**:
1. Data pipeline design: Study `rag/` implementation
2. Data processing: Master `pandas/` content
3. Python: Complete `python/` examples
4. Behavioral: Focus on DE questions in `BQ/`

**ML Engineering Focus**:
1. ML fundamentals: Deep dive `ml-basic/`
2. Production ML: Study `rag/` system
3. Algorithms: Complete Blind 75
4. Behavioral: Focus on ML questions in `BQ/`

**AI Engineering Focus**:
1. LLM systems: Study `rag/` architecture
2. ML fundamentals: Transformers section in `ml-basic/`
3. Coding: Focus on graph/tree problems
4. Behavioral: Focus on AI questions in `BQ/`

### For Quick Reference

**Before Technical Interview**:
1. Review `ml-basic/README.md` quick reference tables
2. Review key algorithms in `ml_fundamentals.md`
3. Glance at common patterns in `summary_notes/dp_mastery_guide.md`

**Before Behavioral Interview**:
1. Review your prepared STAR stories
2. Glance at question categories in `BQ/behavioral_interview_guide.md`
3. Practice 2-3 stories out loud

## Progress Tracking

### Current Repository Status

```
ML Fundamentals:      [====================] Complete (100+ pages)
Behavioral Guide:     [====================] Complete (91 questions)
LeetCode Blind 75:    [====================] 75/75 (100%)
Python Proficiency:   [====================] Complete (26 problems)
Pandas Guide:         [====================] Complete
RAG System:           [====================] Production-ready
```

### Recommended Learning Path Checklist

**Fundamentals**
- [ ] Read ML fundamentals overview
- [ ] Understand all loss functions
- [ ] Master evaluation metrics
- [ ] Understand bias-variance tradeoff
- [ ] Know when to use each algorithm

**Coding**
- [ ] Complete 40+ Blind 75 problems
- [ ] Master DP 5-step framework
- [ ] Understand all major patterns
- [ ] Can explain solutions clearly

**Behavioral**
- [ ] Prepared 10-15 STAR stories
- [ ] Stories cover all categories
- [ ] Can answer in 2-3 minutes
- [ ] Practiced out loud

**Systems**
- [ ] Understand RAG architecture
- [ ] Can explain vector indexing
- [ ] Know LLM selection criteria
- [ ] Can discuss production ML

## Tips for Success

### Studying ML Fundamentals
1. Don't memorize - understand the "why"
2. Draw diagrams to visualize concepts
3. Practice explaining to others
4. Connect concepts to real projects

### Solving Coding Problems
1. Identify the pattern first
2. Think out loud during practice
3. Write clean, readable code
4. Test with edge cases
5. Analyze time/space complexity

### Behavioral Interviews
1. Use specific examples with metrics
2. Focus on YOUR actions, not the team's
3. Show impact with numbers
4. Balance technical depth with clarity
5. Prepare questions for the interviewer

### Production Systems
1. Understand the full pipeline
2. Know the trade-offs made
3. Can explain architectural decisions
4. Understand monitoring and debugging

## Languages

- English: Primary language for `ml_fundamentals.md`, `behavioral_interview_guide.md`
- Chinese: Available for `ml_basics.md`

## Contributing

This is a personal learning repository. Suggestions for improvements are welcome through issues or pull requests.

## License

Personal educational use. Referenced external resources maintain their original licenses.

---

**Last Updated**: February 2026

**Status**: Active development

**Coverage**: Data Engineering, ML Engineering, AI Engineering interview preparation
