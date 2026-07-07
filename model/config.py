import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
load_dotenv()



llm=ChatOpenAI(
    model="openai/gpt-5-nano",
    base_url="https://api.aicredits.in/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=60
)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    base_url="https://api.aicredits.in/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=60,
)
