from langchain_chroma import Chroma
from embedding import embeddings

def get_vector():
    return Chroma(
    persist_directory="Chroma_db",
    embedding_function=embeddings,
)