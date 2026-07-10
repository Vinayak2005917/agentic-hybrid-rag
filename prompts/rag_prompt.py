from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_template(
"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not found in the context, reply:

"I couldn't find that information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""
)