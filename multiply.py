#!/usr/bin/env python3

import random

def get_color(text, color):
    colors = {
        'green': '\033[92m',
        'red': '\033[91m',
        'reset': '\033[0m'
    }
    return f"{colors[color]}{text}{colors['reset']}"

def multiplication_quiz():
    while True:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 * num2
        
        while True:
            try:
                user_answer = int(input(f"\nWhat is {num1} × {num2}? "))
                
                if user_answer == correct_answer:
                    print(get_color("OK", 'green'))
                    break
                else:
                    print(get_color("Error", 'red'))
            except ValueError:
                print(get_color("Error", 'red'))
                print("Please enter a valid number.")
        
    #    again = input("\nAnother question? (y/n): ").lower()
    #    if again != 'y':
    #        break

if __name__ == "__main__":
    multiplication_quiz()