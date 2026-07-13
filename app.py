import os
import mysql.connector
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.messages import HumanMessage,AIMessage
from tools.tools import file_reader,pdf_loader,mysql_tool,rag_tool
from model.config import llm

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)


tools=[
    file_reader,
    pdf_loader,
    mysql_tool,
    rag_tool
    ]

agent=create_agent(
    model=llm,
    tools=tools
)

while True:
    question=input("meee:")
    if question.lower()=="exit":
        print("boyee boyeee")
        break 

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    print(response["messages"][-1].content)