from model.config import llm
from .retriver import retrive_documents
from prompts.rag_prompt import rag_prompt

def generate_answer(question:str):
    documents=retrive_documents(question)
    content="\n\n".join(
        doc.page_content for doc in documents
    )

    prompt=rag_prompt.invoke({ 
        "context":content,
        "question":question
    })
    response=llm.invoke(prompt)
    return response.content


