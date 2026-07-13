from .generator import generate_answer

while True:
    question=input("ASK:")
    if question.lower=="exit":
        break
    answer=generate_answer(question)
    print("\n_+_+_+_+_+__+_+_+e")
    print(answer)

