questions = [
    {"question": "How many colours does rainbow have?", "answer": "7"},
    {"question": "Who is Tamil Nadu Cheif Minister?", "answer": "Thiru C. Joseph Vijay"},
    {"question": "How many days are in a week?", "answer": "7"}
]

score = 0

for q in questions:
    answer = input(q["question"] + " ").lower()

    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Answer:", q["answer"])

print("Final score:", score, "/", len(questions))
