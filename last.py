import random

# Quiz questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter"],
        "correct_answer": "Mars"
    }
    # Add more questions here
]

# Initialize user's score
user_score = 0

# Display Welcome Message and Rules
print("Welcome to the Quiz Game!")
print("You will be asked multiple-choice questions. Choose the correct answer.")

# Present Quiz Questions
random.shuffle(quiz_questions)  # Shuffle question order

for question_data in quiz_questions:
    print("\n" + question_data["question"])
    for idx, option in enumerate(question_data["options"], start=1):
        print(f"{idx}. {option}")

    user_answer = input("Your answer is : ")
    user_answer_idx = int(user_answer) - 1

    if question_data["options"][user_answer_idx] == question_data["correct_answer"]:
        print("Correct!")
        user_score += 1
    else:
        print(f"Incorrect. The correct answer is: {question_data['correct_answer']}")

# Display Final Results
print("\nQuiz completed!")
print(f"Your final score is: {user_score}/{len(quiz_questions)}")
if user_score == len(quiz_questions):
    print("Congratulations! You got all the questions right.")
else:
    print("You can improve your score. Keep practicing!")