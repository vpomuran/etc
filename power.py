#!/usr/bin/env python3
import random

def power_quiz():
    """Interactive quiz to test power calculations."""
    
    question_count = 0
    
    while True:
        base = random.randint(1, 20)
        power = random.randint(0, 5)
        correct_answer = base ** power
        
        while True:
            question_count += 1
            try:
                user_answer = int(input(f"\nQuestion {question_count}: What is {base}^{power}? "))
                
                if user_answer == correct_answer:
                    print("\033[92m✓ Correct!\033[0m")  # Green
                    break
                else:
                    print("\033[91m✗ Incorrect. Try again.\033[0m")  # Red
            except ValueError:
                print("\033[91m✗ Please enter a valid number.\033[0m")  # Red
        
        #try:
        #    cont = input("\nContinue? (y/n): ").lower()
        #    if cont != 'y':
        #        print(f"\nQuiz ended. Total questions: {question_count}")
        #        break
        #except KeyboardInterrupt:
         #   print(f"\n\nQuiz ended. Total questions: {question_count}")
         #   break

if __name__ == "__main__":
    power_quiz()