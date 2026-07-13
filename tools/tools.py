from langchain.tools import tool
from langchain_community.document_loaders import PyPDFLoader
from RAG.generator import generate_answer
from pathlib import Path
import mysql.connector

@tool(description="Read the content from txt file")
def file_reader(file_name:str)->str:
    try:
        file_path=Path("data")/file_name
        with open(file_path,"r") as file:
            return file.read()
    except Exception as e:
        return f"Error:{e}"
    
@tool(description="Read the content from the pdf")
def pdf_loader(file_name:str)->str:
    try:
        file_path=Path("data")/file_name
        loader=PyPDFLoader(file_path)
        document=loader.load()
        text=""
        for page in document:
            text+=page.page_content+"\n"
        return text
    except Exception as e:
        return f"Error:{e}"

@tool(description="Execute a SQL query on the database")
def mysql_tool(query:str)->str:
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sana$More!LikeOcean",
            database="company"
        )        
        cursor=connection.cursor()
        cursor.execute(query)
        row=cursor.fetchall()
        connection.close()

        return str(row)
    except Exception as e:
        return f"Error:{e}"
    

@tool
def rag_tool(question: str) -> str:
    """
    use this tool whenever the user asked something inside ths
    text file and pdf exapmle:
    what is the leave,wfh policy 
    and first read the documents if content not available there 
    if u can not find the content then give ur own answer 
    
    """
    print("====rag tool used+++")
    return generate_answer(question)
    
