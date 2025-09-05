# Simple Quiz Application in Python
import time
def run_quiz(questions):
    score = 0
    for question, answer in questions.items():
        print("\n" + question)
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == answer.lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {answer}")
    print(f"\n🎯 You got {score}/{len(questions)} correct!")

# Quiz Questions (can be expanded easily)
quiz_questions = {
    "What is the capital of France?": "Paris",
    "Which programming language is known as the 'snake language'?": "Python",
    "What is 5 + 7?": "12",
    "Who developed the theory of relativity?": "Einstein",
}

# Run the quiz
print("===== Welcome to the Quiz Game =====")
run_quiz(quiz_questions)
print("===== Thanks for playing! =====")