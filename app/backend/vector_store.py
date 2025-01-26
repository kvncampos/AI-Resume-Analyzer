from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

# Load environment variables from .env file
load_dotenv()

# More Models can be found https://huggingface.co/models?library=sentence-transformers
EMBEDDING_MODEL = os.environ.get(
    "HUGGINGFACE_EMBEDDING_MODEL", default="sentence-transformers/all-mpnet-base-v2"
)

# Initialize the Hugging Face embedding model
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


def create_vector_store(chunks):
    # Store embeddings into the vector store
    vector_store = FAISS.from_documents(
        documents=chunks,  # Input chunks to the vector store
        embedding=embeddings,  # Use the initialized embeddings model
    )
    return vector_store
