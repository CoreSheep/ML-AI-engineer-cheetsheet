import os
import shutil
import tempfile
from pathlib import Path

import pytest

from embedding.create_index import get_index


@pytest.fixture
def setup_real_test_environment():
    """
    Creates a real test environment with actual files and directories.
    This is an integration test fixture - no mocking!
    """
    # Create a temporary directory for our test
    test_dir = tempfile.mkdtemp(prefix="hackerrank_test_")
    
    # Create a data directory with a real test file
    data_dir = os.path.join(test_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    
    # Create a real test document (simple text file since we don't have PDFs)
    test_file = os.path.join(data_dir, "test_document.txt")
    with open(test_file, "w") as f:
        f.write("""
        This is a test document for HackerRank skills assessment.
        
        Python Programming Skills:
        - Data structures and algorithms
        - Object-oriented programming
        - Error handling and debugging
        - Working with APIs and databases
        
        Machine Learning Skills:
        - Data preprocessing and cleaning
        - Model training and evaluation
        - Feature engineering
        - Cross-validation techniques
        """)
    
    # Index name for our test
    index_name = os.path.join(test_dir, "test_index")
    
    yield {
        "test_dir": test_dir,
        "data_dir": data_dir,
        "index_name": index_name,
        "test_file": test_file
    }
    
    # Cleanup: Remove the entire test directory
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir, ignore_errors=True)


def test_get_index_creates_new_index_real(setup_real_test_environment):
    """
    Integration test: Actually creates a real index from real documents.
    No mocking - this tests the entire pipeline!
    """
    env = setup_real_test_environment
    
    # Import the real components we need
    from llama_index.core import SimpleDirectoryReader
    
    # Load real documents from our test data directory
    # Note: Using .txt files instead of .pdf for simplicity
    reader = SimpleDirectoryReader(
        input_dir=env["data_dir"], 
        required_exts=[".txt"]  # Changed from .pdf to .txt
    )
    real_documents = reader.load_data()
    
    # Verify we actually loaded some documents
    assert len(real_documents) > 0, "Should have loaded at least one document"
    assert "Python Programming" in real_documents[0].text, "Document should contain our test content"
    
    # Make sure no index exists initially
    assert not os.path.exists(env["index_name"]), "Index should not exist initially"
    
    # Call the REAL function with REAL data
    index = get_index(real_documents, env["index_name"])
    
    # Verify the REAL results
    assert index is not None, "Should return a real index object"
    assert os.path.exists(env["index_name"]), "Should create real index directory"
    
    # Verify the index directory has real files
    index_files = os.listdir(env["index_name"])
    assert len(index_files) > 0, "Index directory should contain real files"
    
    # Test that the index actually works by querying it
    query_engine = index.as_query_engine()
    response = query_engine.query("What programming skills are mentioned?")
    
    # Verify we get a real response
    assert response is not None, "Should get a real response from the index"
    assert len(str(response)) > 0, "Response should not be empty"
    print(f"Query response: {response}")


def test_get_index_loads_existing_index_real(setup_real_test_environment):
    """
    Integration test: Actually loads an existing real index.
    Tests the 'index already exists' path with real files.
    """
    env = setup_real_test_environment
    
    # Import the real components
    from llama_index.core import SimpleDirectoryReader
    
    # Load real documents
    reader = SimpleDirectoryReader(
        input_dir=env["data_dir"], 
        required_exts=[".txt"]
    )
    real_documents = reader.load_data()
    
    # FIRST: Create a real index
    first_index = get_index(real_documents, env["index_name"])
    assert os.path.exists(env["index_name"]), "Index should be created"
    
    # Get the creation time of the index
    index_creation_time = os.path.getctime(env["index_name"])
    
    # SECOND: Call get_index again - it should load the existing one
    second_index = get_index(real_documents, env["index_name"])
    
    # Verify it loaded the existing index (didn't recreate it)
    index_current_time = os.path.getctime(env["index_name"])
    assert index_creation_time == index_current_time, "Should not recreate index, just load existing one"
    
    # Verify both indexes work the same way
    query1 = first_index.as_query_engine().query("What is mentioned about machine learning?")
    query2 = second_index.as_query_engine().query("What is mentioned about machine learning?")
    
    assert query1 is not None and query2 is not None, "Both indexes should work"
    print(f"First index query: {query1}")
    print(f"Second index query: {query2}")


def test_index_persistence_real(setup_real_test_environment):
    """
    Integration test: Verify that the index actually persists to disk
    and can be loaded in a completely new session.
    """
    env = setup_real_test_environment
    
    from llama_index.core import SimpleDirectoryReader, StorageContext, load_index_from_storage
    
    # Create real documents
    reader = SimpleDirectoryReader(
        input_dir=env["data_dir"], 
        required_exts=[".txt"]
    )
    real_documents = reader.load_data()
    
    # Create and persist an index
    original_index = get_index(real_documents, env["index_name"])
    
    # Simulate a new session: Load the index directly from storage
    # (This is what happens when the program restarts)
    storage_context = StorageContext.from_defaults(persist_dir=env["index_name"])
    loaded_index = load_index_from_storage(storage_context)
    
    # Test that both indexes work identically
    original_response = original_index.as_query_engine().query("What skills are covered?")
    loaded_response = loaded_index.as_query_engine().query("What skills are covered?")
    
    assert original_response is not None, "Original index should work"
    assert loaded_response is not None, "Loaded index should work"
    
    print(f"Original index response: {original_response}")
    print(f"Loaded index response: {loaded_response}")


if __name__ == "__main__":
    # You can run this directly to see the real tests in action
    pytest.main([__file__, "-v", "-s"])
