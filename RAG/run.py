
from .chunking import build_vector_database
from .retriver import retrive_documents

build_vector_database()


query = input("Ask a question: ")

docs = retrive_documents(query)

print("\nRetrieved Documents:\n")

for i, doc in enumerate(docs, start=1):
    print(f"------ Document {i} ------")
    print(doc.page_content)
    print()