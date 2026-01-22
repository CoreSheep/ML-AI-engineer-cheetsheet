import os
import shutil
from unittest.mock import MagicMock, patch

import pytest

from rag.embedding.hackerank import get_index


@pytest.fixture
def setup_data():
    index_name = "test_index"
    data = ["Sample data"]

    yield index_name, data

    if os.path.exists(index_name):
        shutil.rmtree(index_name, ignore_errors=True)


@patch("rag.embedding.hackerank.VectorStoreIndex.from_documents")
@patch("rag.embedding.hackerank.StorageContext.from_defaults")
@patch("rag.embedding.hackerank.load_index_from_storage")
@patch("rag.embedding.hackerank.SimpleDirectoryReader")
def test_get_index_creates_new_index(
    mock_simple_directory_reader,
    mock_load_index,
    mock_storage_context,
    mock_from_documents,
    setup_data,
):
    index_name, data = setup_data

    mock_reader = MagicMock()
    mock_reader.load_data.return_value = data
    mock_simple_directory_reader.return_value = mock_reader

    mock_index = MagicMock()
    mock_from_documents.return_value = mock_index
    mock_storage_context.return_value = MagicMock()

    if os.path.exists(index_name):
        shutil.rmtree(index_name)

    index = get_index(data, index_name)

    mock_from_documents.assert_called_once_with(documents=data, show_progress=True)
    mock_index.storage_context.persist.assert_called_once_with(persist_dir=index_name)
    assert index == mock_index, "The index should be created and returned"


@patch("rag.embedding.hackerank.VectorStoreIndex.from_documents")
@patch("rag.embedding.hackerank.StorageContext.from_defaults")
@patch("rag.embedding.hackerank.load_index_from_storage")
@patch("rag.embedding.hackerank.SimpleDirectoryReader")
def test_get_index_loads_existing_index(
    mock_simple_directory_reader,
    mock_load_index,
    mock_storage_context,
    mock_from_documents,
    setup_data,
):
    index_name, data = setup_data
    
    # Create a fake index directory to simulate existing index
    os.makedirs(index_name, exist_ok=True)
    
    # Mock the loaded index
    mock_index = MagicMock()
    mock_load_index.return_value = mock_index
    mock_storage = MagicMock()
    mock_storage_context.return_value = mock_storage
    
    # Call the function
    index = get_index(data, index_name)
    
    # Verify it loaded existing index instead of creating new one
    mock_from_documents.assert_not_called()
    mock_storage_context.assert_called_once_with(persist_dir=index_name)
    mock_load_index.assert_called_once_with(mock_storage)
    assert index == mock_index