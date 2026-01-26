import logging
from typing import Any, Dict, List

import fitz
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class InvoiceProcessor:
    def __init__(self, model_name: str = "gpt-4o"):  # do not change the model name
        """
        Initialize the Invoice Processor with the specified model.

        Args:
            model_name: The name of the OpenAI model to use
        """
        self.model_name = model_name
        self.llm = ChatOpenAI(model=model_name, temperature=0)
        self.embeddings = OpenAIEmbeddings()
        self.index = None

    def read_and_chunk_file(self, pdf_path: str) -> List[Document]:
        """
        Read a PDF file and chunk it into smaller documents using fitz (PyMuPDF).

        Args:
            pdf_path: Path to the PDF file.

        Returns:
            List of document chunks.
        """
        # 1. Extract text from PDF using fitz
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()

        # 2. Split text into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = splitter.split_text(text)

        # 3. Return chunks as Document objects
        return [Document(page_content=chunk) for chunk in chunks]

    def create_index(self, chunks: List[Document]) -> FAISS:
        """
        Create a vector index from document chunks.

        Args:
            chunks: List of document chunks

        Returns:
            FAISS index
        """
        # 1. Create vector embeddings for chunks
        # 2. Store in FAISS index
        # 3. Return the index
        self.index = FAISS.from_documents(chunks, self.embeddings)
        return self.index

    def retrieve_top_chunks(self, query: str, k: int = 3) -> List[Document]:
        """
        Retrieve the top k relevant document chunks for a given query.

        Args:
            query: The query to search for
            k: Number of chunks to retrieve

        Returns:
            List of relevant document chunks

        Raises:
            ValueError: If the index does not exist.
        """
        # 1. Check if index exists
        if self.index is None:
            raise ValueError("Index does not exist.")

        # 2-4. Find similar vectors and return corresponding documents
        return self.index.similarity_search(query, k=k)

    def generate_answer(self, query: str) -> Dict[str, Any]:
        """
        Generate an answer to a query using the RAG system.

        Args:
            query: The query to answer.

        Returns:
            Dictionary containing:
            - "answer": The generated answer.
            - "source_chunks": The relevant document chunks.

        Raises:
            ValueError: If the index does not exist.
        """
        # 1. Check if an index exists
        if self.index is None:
            raise ValueError("Index does not exist.")

        # 2. Create prompt template
        prompt_template = PromptTemplate(
            input_variables=["context", "question"],
            template="""Use the following context to answer the question.
Extract the exact value from the context. Be concise and only return the value.

Context: {context}

Question: {question}

Answer:"""
        )

        # 3. Set up retrieval chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.index.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True,
            chain_type_kwargs={"prompt": prompt_template}
        )

        # 4. Generate answer
        result = qa_chain.invoke({"query": query})

        # 5. Return answer and source chunks
        return {
            "answer": result["result"],
            "source_chunks": result["source_documents"]
        }

    def process_invoice(self, pdf_path: str) -> bool:
        """
        Process an invoice PDF and prepare for querying.

        Args:
            pdf_path: Path to the PDF file
        """
        # 1. Read and chunk the PDF
        chunks = self.read_and_chunk_file(pdf_path)

        # 2. Create the index
        self.create_index(chunks)
        return True

    def answer_invoice_query(self, query: str) -> Dict[str, Any]:
        """
        Answer a query about the processed invoice.

        Args:
            query: The query to answer

        Returns:
            Dictionary containing the answer and source chunks
        """
        # 1. Call generate_answer
        # 2. Return the result
        return self.generate_answer(query)


if __name__ == "__main__":
    from invoice_generator import generate_multiple_invoices

    invoice_files = generate_multiple_invoices(1)
    pdf_path = invoice_files[0]

    processor = InvoiceProcessor()
    processor.process_invoice(pdf_path)

    sample_queries = [
        "What is the invoice number?",
        "What is the payment term?",
        "What is the shipper line?",
        "What is shipment term?",
    ]

    for query in sample_queries:
        result = processor.answer_invoice_query(query)
        print(f"\nQuery: {query}")
        print(f"Answer: {result['answer']}")