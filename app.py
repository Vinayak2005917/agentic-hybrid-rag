import os
import mysql.connector
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.messages import HumanMessage,AIMessage
from tools.tools import file_reader,pdf_loader,mysql_tool

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

model=ChatOpenAI(
    model="openai/gpt-5-nano",
    base_url="https://api.aicredits.in/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=60
)

tools=[
    file_reader,
    pdf_loader,
    mysql_tool
    ]

agent=create_agent(
    model=model,
    tools=tools
)

while True:
    user_input=input("meee:")
    if user_input.lower()=="exit":
        print("boyee boyeee")
        break 

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        }
    )

    print(response["messages"][-1].content)