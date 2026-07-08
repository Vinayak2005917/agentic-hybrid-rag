import os
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

from model.config import embeddings
load_dotenv()

print(os.getenv("OPENAI_API_KEY")[:10])


embeddings=embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    base_url="https://api.aicredits.in/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=60,
)


def build_vector_database():
    documents = []

    # Load text file
    documents.extend(
        TextLoader("../data/sample_data.txt").load()
    )

    documents.extend(
        PyPDFLoader("../data/sample.pdf").load()
    )


    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=50,
    )

    chunks = splitter.split_documents(documents)

    # Store in Chroma
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db",
    )

    print(f"Stored {len(chunks)} chunks successfully!")