import os
import streamlit as st
from dotenv import load_dotenv
from llama_index.core import (
    SimpleDirectoryReader, 
    VectorStoreIndex, 
    StorageContext,
    load_index_from_storage,
    Settings
)
from llama_index.llms.openai import OpenAI
from llama_index.llms.anthropic import Anthropic
from llama_index.embeddings.openai import OpenAIEmbedding

# Load environment variables
load_dotenv()

class RAGSystem:
    """Complete RAG system implementation with multi-provider support"""
    
    def __init__(self, data_path, index_name="document_index"):
        self.data_path = data_path
        self.index_name = index_name
        self.index = None
        self.query_engine = None
        
    def load_documents(self):
        """Load documents from data directory"""
        try:
            documents = SimpleDirectoryReader(
                input_dir=self.data_path,
                required_exts=[".pdf", ".txt", ".docx", ".md"]
            ).load_data()
            return documents
        except ValueError as e:
            st.error(f"❌ No documents found in {self.data_path}")
            st.info("📁 Please add documents to the data directory and try again.")
            return []
        except Exception as e:
            st.error(f"❌ Error loading documents: {str(e)}")
            return []
    
    def create_or_load_index(self):
        """Create new index or load existing one"""
        try:
            if os.path.exists(self.index_name):
                # Load existing index
                with st.spinner("📂 Loading existing document index..."):
                    storage_context = StorageContext.from_defaults(persist_dir=self.index_name)
                    self.index = load_index_from_storage(storage_context)
                st.success("✅ Loaded existing document index")
                return True
            else:
                # Create new index
                documents = self.load_documents()
                if not documents:
                    return False
                    
                with st.spinner(f"🔄 Building document index from {len(documents)} documents... This may take a few minutes."):
                    # Show progress
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    status_text.text("Processing documents...")
                    progress_bar.progress(25)
                    
                    self.index = VectorStoreIndex.from_documents(
                        documents, 
                        show_progress=False  # We'll handle progress ourselves
                    )
                    
                    progress_bar.progress(75)
                    status_text.text("Saving index...")
                    
                    self.index.storage_context.persist(persist_dir=self.index_name)
                    
                    progress_bar.progress(100)
                    status_text.text("Complete!")
                    
                st.success(f"✅ Created new document index with {len(documents)} documents")
                return True
                
        except Exception as e:
            st.error(f"❌ Error creating/loading index: {str(e)}")
            return False
    
    def setup_query_engine(self, provider="openai", model=None):
        """Setup query engine with specified provider"""
        if not self.index:
            st.error("❌ No index available. Please initialize the system first.")
            return False
            
        try:
            if provider.lower() == "openai":
                api_key = os.getenv("OPENAI_API_KEY")
                if not api_key:
                    st.error("❌ OpenAI API key not found. Please set OPENAI_API_KEY in your .env file.")
                    return False
                    
                llm = OpenAI(
                    model=model or "gpt-4",
                    temperature=0.1,
                    api_key=api_key
                )
                
                # Set embedding model for OpenAI
                Settings.embed_model = OpenAIEmbedding(
                    model="text-embedding-ada-002",
                    api_key=api_key
                )
                
            elif provider.lower() == "anthropic":
                api_key = os.getenv("ANTHROPIC_API_KEY")
                if not api_key:
                    st.error("❌ Anthropic API key not found. Please set ANTHROPIC_API_KEY in your .env file.")
                    return False
                    
                llm = Anthropic(
                    model=model or "claude-3-sonnet-20240229",
                    api_key=api_key,
                    temperature=0.1
                )
                
                # For Anthropic, we still use OpenAI embeddings (most common setup)
                openai_key = os.getenv("OPENAI_API_KEY")
                if openai_key:
                    Settings.embed_model = OpenAIEmbedding(
                        model="text-embedding-ada-002",
                        api_key=openai_key
                    )
                
            else:
                st.error("❌ Unsupported provider. Please choose 'openai' or 'anthropic'.")
                return False
                
            self.query_engine = self.index.as_query_engine(llm=llm)
            return True
            
        except Exception as e:
            st.error(f"❌ Error setting up query engine: {str(e)}")
            return False
    
    def query(self, question):
        """Query the RAG system"""
        if not self.query_engine:
            return "❌ Query engine not initialized. Please setup the system first."
        
        try:
            with st.spinner("🤔 Searching documents and generating response..."):
                response = self.query_engine.query(question)
                return str(response)
        except Exception as e:
            return f"❌ Error processing query: {str(e)}"

def initialize_session_state():
    """Initialize Streamlit session state variables"""
    if "rag_system" not in st.session_state:
        st.session_state.rag_system = None
    if "initialized" not in st.session_state:
        st.session_state.initialized = False
    if "messages" not in st.session_state:
        st.session_state.messages = []

def display_sidebar():
    """Display the configuration sidebar"""
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # API Key Status
        st.subheader("🔑 API Key Status")
        openai_key = os.getenv("OPENAI_API_KEY")
        anthropic_key = os.getenv("ANTHROPIC_API_KEY")
        
        if openai_key:
            st.success("✅ OpenAI API Key Found")
        else:
            st.error("❌ OpenAI API Key Missing")
            
        if anthropic_key:
            st.success("✅ Anthropic API Key Found")
        else:
            st.warning("⚠️ Anthropic API Key Missing")
        
        st.divider()
        
        # Provider selection
        st.subheader("🤖 AI Provider")
        provider = st.selectbox(
            "Choose LLM Provider",
            ["OpenAI", "Anthropic"],
            help="Select which AI provider to use for generating responses"
        )
        
        # Model selection
        if provider == "OpenAI":
            model = st.selectbox(
                "Model", 
                ["gpt-4", "gpt-3.5-turbo", "gpt-4-turbo-preview"],
                help="Choose the OpenAI model to use"
            )
        else:
            model = st.selectbox(
                "Model", 
                ["claude-3-sonnet-20240229", "claude-3-haiku-20240307", "claude-3-opus-20240229"],
                help="Choose the Anthropic model to use"
            )
        
        st.divider()
        
        # Data path configuration
        st.subheader("📁 Document Settings")
        data_path = st.text_input(
            "Data Directory", 
            value="data",
            help="Path to the directory containing your documents"
        )
        
        # Document info
        if os.path.exists(data_path):
            try:
                files = [f for f in os.listdir(data_path) 
                        if f.endswith(('.pdf', '.txt', '.docx', '.md'))]
                st.info(f"📄 Found {len(files)} documents")
                if files:
                    with st.expander("View Documents"):
                        for file in files:
                            st.text(f"• {file}")
            except:
                st.warning("⚠️ Cannot read data directory")
        else:
            st.warning("⚠️ Data directory not found")
        
        st.divider()
        
        # Initialize system button
        if st.button("🚀 Initialize RAG System", type="primary"):
            initialize_rag_system(data_path, provider.lower(), model)
        
        # Reset button
        if st.session_state.initialized:
            if st.button("🔄 Reset System", type="secondary"):
                reset_system()
        
        st.divider()
        
        # System status
        st.subheader("📊 System Status")
        if st.session_state.initialized:
            st.success("✅ System Ready")
            st.info(f"🤖 Using: {provider} {model}")
        else:
            st.warning("⚠️ System Not Initialized")

def initialize_rag_system(data_path, provider, model):
    """Initialize the RAG system"""
    try:
        with st.spinner("🔄 Initializing RAG system..."):
            rag = RAGSystem(data_path)
            
            # Create or load index
            if rag.create_or_load_index():
                # Setup query engine
                if rag.setup_query_engine(provider, model):
                    st.session_state.rag_system = rag
                    st.session_state.initialized = True
                    st.session_state.current_provider = provider
                    st.session_state.current_model = model
                    
                    # Add welcome message
                    if not st.session_state.messages:
                        welcome_msg = f"Hello! I'm your AI assistant powered by {provider.title()} {model}. I'm ready to answer questions about your documents. What would you like to know?"
                        st.session_state.messages = [
                            {"role": "assistant", "content": welcome_msg}
                        ]
                    
                    st.success(f"✅ RAG system initialized successfully!")
                    st.balloons()
                else:
                    st.error("❌ Failed to setup query engine")
            else:
                st.error("❌ Failed to create/load document index")
                
    except Exception as e:
        st.error(f"❌ Initialization failed: {str(e)}")

def reset_system():
    """Reset the RAG system"""
    st.session_state.rag_system = None
    st.session_state.initialized = False
    st.session_state.messages = []
    if 'current_provider' in st.session_state:
        del st.session_state.current_provider
    if 'current_model' in st.session_state:
        del st.session_state.current_model
    st.success("✅ System reset successfully!")
    st.rerun()

def display_chat_interface():
    """Display the main chat interface"""
    if not st.session_state.initialized:
        st.info("👈 Please initialize the RAG system using the sidebar configuration panel.")
        
        # Show sample questions
        st.subheader("💡 Sample Questions You Can Ask")
        sample_questions = [
            "What is DeepSeek-OCR and what problem does it solve?",
            "What are the main components of DeepSeek-OCR architecture?",
            "What compression ratios does DeepSeek-OCR achieve?",
            "How does DeepEncoder work and what makes it efficient?",
            "How does DeepSeek-OCR compare to other OCR models?",
            "What are the practical applications of DeepSeek-OCR?",
            "What datasets were used to train DeepSeek-OCR?",
            "What are the key contributions of this research?"
        ]
        
        for question in sample_questions:
            st.text(f"• {question}")
        
        return
    
    # Display current configuration
    if hasattr(st.session_state, 'current_provider'):
        st.caption(f"🤖 Using {st.session_state.current_provider.title()} {st.session_state.current_model}")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask a question about your documents...", key="chat_input"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            response = st.session_state.rag_system.query(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

def display_header():
    """Display the main header"""
    st.title("🤖 RAG Document Q&A System")
    st.markdown("""
    **Ask questions about your documents using AI-powered search and generation.**
    
    This system uses Retrieval-Augmented Generation (RAG) to provide accurate answers based on your document collection.
    """)
    
    # Add tabs for different views
    tab1, tab2, tab3 = st.tabs(["💬 Chat", "📚 Documents", "ℹ️ About"])
    
    with tab1:
        display_chat_interface()
    
    with tab2:
        display_document_info()
    
    with tab3:
        display_about_info()

def display_document_info():
    """Display information about loaded documents"""
    st.subheader("📚 Document Information")
    
    if st.session_state.initialized and st.session_state.rag_system:
        data_path = st.session_state.rag_system.data_path
        
        if os.path.exists(data_path):
            files = [f for f in os.listdir(data_path) 
                    if f.endswith(('.pdf', '.txt', '.docx', '.md'))]
            
            if files:
                st.success(f"✅ Successfully loaded {len(files)} documents")
                
                # Display file details
                for file in files:
                    file_path = os.path.join(data_path, file)
                    file_size = os.path.getsize(file_path)
                    file_size_kb = file_size / 1024
                    
                    with st.expander(f"📄 {file}"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.text(f"Size: {file_size_kb:.1f} KB")
                        with col2:
                            st.text(f"Type: {file.split('.')[-1].upper()}")
                        
                        # Show first few lines for text files
                        if file.endswith('.txt'):
                            try:
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    preview = f.read(500)
                                st.text_area("Preview:", preview, height=100, disabled=True)
                            except:
                                st.text("Preview not available")
            else:
                st.warning("⚠️ No supported documents found in the data directory")
        else:
            st.error("❌ Data directory not found")
    else:
        st.info("ℹ️ Initialize the system to view document information")

def display_about_info():
    """Display information about the RAG system"""
    st.subheader("ℹ️ About RAG Document Q&A")
    
    st.markdown("""
    ### What is RAG?
    
    **Retrieval-Augmented Generation (RAG)** is an AI technique that combines:
    - **Document Retrieval**: Finding relevant information from your documents
    - **AI Generation**: Using that information to generate accurate, contextual answers
    
    ### How It Works
    
    1. **📄 Document Processing**: Your documents are processed and split into searchable chunks
    2. **🔍 Embedding Creation**: Text is converted to numerical vectors for semantic search
    3. **💾 Index Storage**: Vectors are stored for fast retrieval
    4. **❓ Query Processing**: Your questions are matched against document content
    5. **🤖 Answer Generation**: AI generates responses based on retrieved context
    
    ### Supported Features
    
    - ✅ **Multiple AI Providers**: OpenAI and Anthropic
    - ✅ **Various Document Types**: PDF, TXT, DOCX, MD
    - ✅ **Smart Caching**: Indexes are saved for faster subsequent use
    - ✅ **Real-time Chat**: Interactive conversation interface
    - ✅ **Configurable Models**: Choose from different AI models
    
    ### Supported File Types
    
    - **PDF**: Portable Document Format files
    - **TXT**: Plain text files
    - **DOCX**: Microsoft Word documents
    - **MD**: Markdown files
    
    ### Current Document Collection
    
    This system currently includes research papers on:
    - **DeepSeek-OCR**: Vision-text compression and optical character recognition
    - **Context Compression**: Techniques for handling long sequences in LLMs
    - **Vision-Language Models**: Multi-modal AI architectures
    - **Document Understanding**: End-to-end OCR and parsing systems
    
    ### Tips for Best Results
    
    - 📝 **Clear Questions**: Ask specific, well-formed questions about the research
    - 📚 **Technical Depth**: Feel free to ask about architectures, methodologies, and results
    - 🎯 **Focused Queries**: Break complex research questions into smaller parts
    - 🔄 **Iterate**: Build on previous answers to explore topics deeper
    - 🔬 **Research Context**: Ask about comparisons, limitations, and future work
    """)

def main():
    """Main application function"""
    # Page configuration
    st.set_page_config(
        page_title="RAG Document Q&A",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # Display sidebar
    display_sidebar()
    
    # Display main content
    display_header()

if __name__ == "__main__":
    main()
