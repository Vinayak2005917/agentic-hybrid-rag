import os
from dotenv import load_dotenv
from  langchain_chroma import Chroma
from model.config import embeddings
from .store_db import get_vector
vectorstore=get_vector()

retriver=vectorstore.as_retriever(search_kwags={"k":3})
def retrive_documents(query:str):
    return retriver.invoke(query)

