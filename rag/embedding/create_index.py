import os

from llama_index.core import (SimpleDirectoryReader, StorageContext,
                              VectorStoreIndex, load_index_from_storage)
"""
    1. SimpleDirectoryReader: Reads the documents from the data directory
"""

# Get the data path from the data directory, current_path/../../data
data_path = os.path.join(os.path.dirname(__file__), "..", "..", "data")


def get_index(documents, index_name):
    index = None
    if not os.path.exists(index_name):  # If the index does not exist, create it
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(documents=documents, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:  # If the index exists, load it from storage context
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index


if __name__ == "__main__":
    # For testing, use both PDF and TXT files
    # For importing in other modules, try PDF files first, then TXT files
    try:
        data = SimpleDirectoryReader(data_path, required_exts=[".pdf"]).load_data()
        # Create the index for the DeepSeek-OCR paper
        deepseek_ocr_engine = get_index(data, "deepseek_ocr_index").as_query_engine()
    except ValueError:
        # Fallback to text files if no PDF files found
        try:
            data = SimpleDirectoryReader(data_path, required_exts=[".txt"]).load_data()
            deepseek_ocr_engine = get_index(data, "deepseek_ocr_index").as_query_engine()
        except ValueError:
            print("Warning: No PDF or TXT files found in data directory")
            deepseek_ocr_engine = None    
    
    # Test queries specifically about DeepSeek-OCR paper
    print("\n=== Testing RAG system with DeepSeek-OCR Paper ===")
    
    # Check if engine was created successfully
    if deepseek_ocr_engine is None:
        print("Cannot run queries: No documents found or engine creation failed")
        exit(1)
    
    # Question 1: Core concept
    response1 = deepseek_ocr_engine.query("What is DeepSeek-OCR and what problem does it solve?")
    print(f"Q: What is DeepSeek-OCR and what problem does it solve?")
    print(f"A: {response1}\n")
    
    # Question 2: Technical architecture
    response2 = deepseek_ocr_engine.query("What are the main components of DeepSeek-OCR architecture?")
    print(f"Q: What are the main components of DeepSeek-OCR architecture?")
    print(f"A: {response2}\n")

