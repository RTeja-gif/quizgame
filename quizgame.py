import json

# Sample quiz data
quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["1. Paris", "2. London", "3. Berlin", "4. Madrid"],
        "answer": "1"
    },
    {
        "question": "What is 2 + 2?",
        "choices": ["1. 3", "2. 4", "3. 5", "4. 6"],
        "answer": "2"
    },
    {
        "question": "What is the capital of Japan?",
        "choices": ["1. Tokyo", "2. Kyoto", "3. Osaka", "4. Nagoya"],
        "answer": "1"
    }
]

def run_quiz():
    score = 0
    total_questions = len(quiz_data)

    for question_data in quiz_data:
        print(question_data["question"])
        for choice in question_data["choices"]:
            print(choice)
        
        answer = input("Enter the number of your answer: ")
        
        if answer == question_data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            correct_choice = question_data["choices"][int(question_data["answer"]) - 1]
            print(f"Incorrect! The correct answer is: {correct_choice}\n")
    
    print(f"Quiz completed! Your score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Your percentage: {percentage:.2f}%")

if __name__ == "__main__":
    run_quiz()


print("Teja Jain University")