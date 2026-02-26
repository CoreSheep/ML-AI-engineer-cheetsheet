# ML/AI Engineering Cheatsheet - Project Structure

## Visual Organization

```
ml-ai-engineering/
│
├── 📄 README.md                           # Project overview and guide
├── 📝 CHANGELOG.md                        # Change history
├── 📋 PROJECT_STRUCTURE.md                # This file
├── 🚫 .gitignore                          # Git ignore rules
│
└── 📁 ML-AI-engineer-cheetsheet/
    │
    ├── 📄 README.md                       # Module overview
    ├── 📝 TODO.md                         # Development roadmap
    │
    ├── 📊 LeetCode_blind75_list.md        # Blind 75 solutions (75/75)
    │
    ├── 🐍 python/                         # Python Patterns
    │   ├── 📄 README.md                   # Python patterns guide
    │   ├── 📊 LeetCode_AC_list.md         # 26 solved problems
    │   ├── 🔧 decorator_args_kwargs.py    # Advanced decorators
    │   ├── 🔧 decorator_nnmau.py          # nnmau pattern
    │   ├── 📦 dataclass_demo.py           # Modern Python dataclasses
    │   └── 🧪 pytest_demo.py              # Testing examples
    │
    ├── 🐼 pandas/                         # Data Processing
    │   ├── 📄 README.md                   # Pandas quick reference
    │   ├── 📊 LeetCode_AC_list.md         # Pandas solutions
    │   ├── 📓 pandas_cheatsheet.ipynb     # Interactive guide
    │   ├── 🐍 code_test.py                # Code examples
    │   └── 🖼️ img/
    │       └── strftime.png               # Date format reference
    │
    ├── 🤖 rag/                            # RAG System
    │   ├── 📄 README.md                   # Complete documentation
    │   ├── 🌐 app.py                      # Streamlit interface
    │   ├── 🤖 agent.py                    # ReAct agent
    │   ├── 💬 prompts.py                  # System prompts
    │   ├── 📦 requirements.txt            # Dependencies
    │   ├── 🔑 .env.example                # API key template
    │   ├── 🧪 test_agents.py              # Agent tests
    │   │
    │   ├── 🔗 langchain/                  # LangChain Examples
    │   │   ├── 🔄 rag_pipeline.py         # Alternative RAG
    │   │   └── 📝 invoice_generator.py    # Document generation
    │   │
    │   ├── 🔢 embedding/                  # Vector Indexing
    │   │   ├── 🏗️ create_index.py        # Index creation
    │   │   ├── 🧪 test_hackerank.py       # Integration tests
    │   │   ├── 🧪 test_index_integration.py
    │   │   └── 📁 deepseek_ocr_index/     # Persisted indexes
    │   │
    │   └── 💾 document_index/             # Vector stores
    │       ├── default__vector_store.json
    │       ├── docstore.json
    │       └── ...
    │
    ├── 📚 summary_notes/                  # Algorithm Guides
    │   ├── 📄 README.md                   # Algorithm overview
    │   └── 🎯 dp_mastery_guide.md         # DP patterns & framework
    │
    ├── 💼 oa/                             # Interview Prep
    │   ├── futu.md                        # Company-specific notes
    │   └── roland_berger.md
    │
    └── 📊 data/                           # Sample Data
        └── sample_skills_report.txt
```

## Content Categories

### 1. Algorithm Mastery
**Files**: `LeetCode_blind75_list.md`, `summary_notes/dp_mastery_guide.md`

- Blind 75 problems with solutions (75/75 complete)
- Dynamic Programming 5-step framework
- Pattern recognition guides
- Time/space complexity analysis

### 2. Python Engineering
**Directory**: `python/`

- Decorator patterns (timing, logging, memoization)
- Modern Python features (dataclasses, type hints)
- Testing with pytest
- 26 LeetCode solutions

### 3. Data Processing
**Directory**: `pandas/`

- Interactive Jupyter cheatsheet
- DataFrame operations
- Data cleaning techniques
- Time series handling

### 4. RAG & AI Systems
**Directory**: `rag/`

- Production-ready RAG implementation
- Multi-provider support (OpenAI, Anthropic)
- Streamlit web interface
- Vector indexing with LlamaIndex

### 5. Interview Preparation
**Files**: `oa/`, `TODO.md`

- Company-specific notes
- Online assessment preparation
- Development roadmap

## File Type Legend

```
📄 Documentation (README, markdown guides)
📝 Notes and lists (TODO, changelog)
📊 Data files (CSV, JSON, datasets)
🐍 Python source files
📓 Jupyter notebooks
🔧 Utility scripts
🧪 Test files
🤖 AI/ML components
🌐 Web applications
🔗 Integration code
🔢 Data processing
💾 Storage/indexes
🖼️ Images/assets
📦 Package files
🔑 Configuration templates
💬 Prompts/templates
🎯 Focused guides
💼 Professional content
```

## Key Features by Directory

### python/
- **Purpose**: Python best practices and coding patterns
- **Key Files**: decorator patterns, dataclass examples, pytest demos
- **Use Case**: Interview prep, production code patterns

### pandas/
- **Purpose**: Data manipulation reference
- **Key Files**: Interactive notebook, quick reference guide
- **Use Case**: Data analysis, ETL operations

### rag/
- **Purpose**: Production RAG system
- **Key Files**: app.py (UI), agent.py (logic), create_index.py (indexing)
- **Use Case**: Document Q&A, knowledge base systems

### summary_notes/
- **Purpose**: Algorithm pattern mastery
- **Key Files**: DP mastery guide with 5-step framework
- **Use Case**: Technical interview preparation

## Quick Navigation

### For Interview Prep
1. Start with `LeetCode_blind75_list.md`
2. Study patterns in `summary_notes/dp_mastery_guide.md`
3. Review `python/LeetCode_AC_list.md` for Python-specific solutions

### For Building RAG Systems
1. Read `rag/README.md` for setup
2. Configure `.env` from `.env.example`
3. Run `streamlit run rag/app.py`

### For Data Analysis
1. Open `pandas/pandas_cheatsheet.ipynb`
2. Reference `pandas/README.md` for quick lookups
3. Check `pandas/img/strftime.png` for date formatting

## Progress Tracking

```
Algorithm Mastery:
├── Blind 75: ████████████████████ 75/75 (100%)
├── DP Patterns: ████████████████████ Complete
└── Python Solutions: ████████████░░░░░░░░ 26 problems

Documentation:
├── READMEs: ████████████████████ 6/6 modules
├── Code Comments: ██████████████░░░░░░ ~70%
└── Examples: ████████████████░░░░ Good coverage

Production Code:
├── RAG System: ████████████████████ Production-ready
├── Test Coverage: ████████░░░░░░░░░░░░ Moderate
└── CI/CD: ░░░░░░░░░░░░░░░░░░░░ Not implemented
```

## Maintenance Notes

### Regular Updates Needed
- LeetCode progress tracking
- Model version updates (OpenAI, Anthropic)
- Dependency version bumps
- Documentation accuracy

### Known Technical Debt
- Directory typo: "cheetsheet" vs "cheatsheet"
- Nested git repository structure
- Limited test coverage in RAG system
- No CI/CD pipeline

### Future Enhancements
- Add more DP pattern examples
- Complete remaining 18 Blind 75 problems
- Implement comprehensive testing
- Add performance benchmarks
- Create video walkthroughs

---

**Last Updated**: February 24, 2026
**Maintained By**: jiufeng
