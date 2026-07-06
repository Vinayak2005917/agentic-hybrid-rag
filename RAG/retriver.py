import os
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
load_dotenv()
print(os.getenv("OPENAI_API_KEY")[:10])

model=OpenAIEmbeddings(
    model="openai/gpt-5-nano",
    base_url="https://api.aicredits.in/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=60
)


def build_vector_database():
    documents = []

    # Load text file
    documents.extend(
        TextLoader("../data/sample_data.txt").load()
    )

    # Load PDF
    documents.extend(
        PyPDFLoader("../data/sample.pdf").load()
    )

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    chunks = splitter.split_documents(documents)

    # Embedding model
    embeddings = OpenAIEmbeddings()

    # Store in Chroma
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db",
    )

    print(f"Stored {len(chunks)} chunks successfully!")