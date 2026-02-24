# RAG Document Q&A System

A production-ready Retrieval-Augmented Generation system built with LlamaIndex, supporting multiple LLM providers.

## Features

- Multi-provider LLM support (OpenAI, Anthropic)
- Document indexing and semantic search
- Interactive Streamlit web interface
- Persistent vector storage
- Support for PDF, TXT, DOCX, and MD files

## Architecture

```
User Query
    │
    ▼
Streamlit UI (app.py)
    │
    ▼
RAG System
    ├─► Document Loader
    ├─► Vector Indexing (LlamaIndex)
    ├─► Semantic Search
    └─► LLM Generation
        ├─► OpenAI (GPT-4)
        └─► Anthropic (Claude)
```

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

### 3. Add Documents

Place your documents in the `data/` directory (create if it doesn't exist):
```bash
mkdir -p ../../data
cp your_document.pdf ../../data/
```

### 4. Run the Application

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser.

## Components

### app.py
Complete RAG system with Streamlit UI:
- Document loading and indexing
- Multi-provider configuration
- Chat interface with history
- Document preview

### agent.py
ReAct agent implementation:
- Provider-agnostic LLM setup
- Query engine configuration
- Tool creation for RAG

### prompts.py
System prompts and context:
- Agent instructions
- Tool descriptions
- Custom context

### embedding/create_index.py
Vector index management:
- Document chunking
- Embedding generation
- Index persistence

## Usage Examples

### Basic Query
```python
from agent import get_agent

agent = get_agent(provider="openai", model="gpt-4")
response = agent.run("What is the main topic of the document?")
print(response)
```

### Custom RAG System
```python
from app import RAGSystem

rag = RAGSystem(data_path="../../data")
rag.create_or_load_index()
rag.setup_query_engine(provider="anthropic", model="claude-3-5-sonnet-20241022")
response = rag.query("Explain the methodology")
```

## Configuration

### Supported Models

**OpenAI**:
- gpt-4
- gpt-3.5-turbo
- gpt-4-turbo-preview

**Anthropic**:
- claude-3-5-sonnet-20241022
- claude-3-5-haiku-20241022
- claude-3-opus-20240229

### Embeddings
- Default: OpenAI text-embedding-ada-002
- Customizable in `Settings.embed_model`

## File Structure

```
rag/
├── app.py                  # Main Streamlit application
├── agent.py                # Agent initialization
├── prompts.py              # System prompts
├── requirements.txt        # Dependencies
├── .env.example            # API key template
├── README.md               # This file
│
├── langchain/              # LangChain examples
│   ├── rag_pipeline.py     # Alternative RAG implementation
│   └── invoice_generator.py
│
├── embedding/              # Vector indexing utilities
│   ├── create_index.py     # Index creation
│   ├── test_hackerank.py   # Integration tests
│   └── test_index_integration.py
│
└── document_index/         # Persisted vector indexes
    ├── default__vector_store.json
    ├── docstore.json
    └── ...
```

## Troubleshooting

### API Key Issues
- Ensure `.env` file exists in the `rag/` directory
- Verify API keys are valid
- Check that `python-dotenv` is installed

### Document Loading Errors
- Verify documents exist in the data directory
- Check file extensions match supported types
- Ensure files are not corrupted

### Index Creation Fails
- Check available disk space
- Verify OpenAI API key for embeddings
- Review error messages in console

## Development

### Running Tests
```bash
cd embedding
pytest test_*.py -v
```

### Adding New Providers
1. Install provider SDK
2. Add provider case in `get_llm()` function
3. Update model selection in UI
4. Test with sample queries

## Performance Tips

- Use GPT-3.5-turbo for faster, cheaper queries
- Index documents once, then load from storage
- Chunk large documents appropriately
- Use Haiku models for simple queries

## References

- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API](https://platform.openai.com/docs/api-reference)
- [Anthropic API](https://docs.anthropic.com/)
