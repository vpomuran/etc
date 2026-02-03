#!/usr/bin/env python3
import random
from fractions import Fraction

# ANSI color codes (used instead of colorama)
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def parse_mixed_number(user_input):
    """Parse input that may be a mixed number (e.g. '1 2/3'), a fraction '5/3', or an integer '2'.
    Returns a Fraction or raises ValueError on invalid input.
    """
    s = user_input.strip()
    if not s:
        raise ValueError("empty input")

    # Only positive numbers are allowed
    if s[0] == '-':
        raise ValueError("negative numbers not allowed")

    # Mixed number like '1 2/3'
    if ' ' in s:
        parts = s.split()
        if len(parts) == 2:
            try:
                whole = int(parts[0])
                if whole < 0:
                    raise ValueError("negative numbers not allowed")
                frac = Fraction(parts[1])
                if frac < 0:
                    raise ValueError("negative numbers not allowed")
                return Fraction(whole) + frac
            except Exception:
                raise ValueError("invalid mixed number")

    # Fraction like '5/3' or integer like '4'
    try:
        if '/' in s:
            val = Fraction(s)
            if val < 0:
                raise ValueError("negative numbers not allowed")
            return val
        else:
            val = int(s)
            if val < 0:
                raise ValueError("negative numbers not allowed")
            return Fraction(val, 1)
    except Exception:
        raise ValueError("invalid number")

def generate_quiz():
    # Generate left operand by multiplying two random numbers (2-999)
    num1 = random.randint(2, 999)
    num2 = random.randint(2, 999)
    dividend = num1 * num2
    
    # Generate divisor (2-999, but less than dividend)
    divisor = random.randint(2, min(999, dividend - 1))
    
    # Calculate correct answer as a Fraction so it can be compared to parsed input
    correct_answer = Fraction(dividend, divisor)
    
    # Ask user and keep asking until correct
    while True:
        print(f"\nDivide {dividend} by {divisor}:")
        try:
            user_input = input("Your answer: ")
            try:
                user_frac = parse_mixed_number(user_input)
            except ValueError:
                print(f"{RED}Invalid input{RESET}")
                continue

            if user_frac == correct_answer:
                print(f"{GREEN}Correct!{RESET}")
                break
            else:
                print(f"{RED}Incorrect, try again{RESET}")
        except ValueError:
            print(f"{RED}Invalid input{RESET}")
    

def main():
    while True:
        generate_quiz()
   #     print("AFTER CORRECT!")
   #     again = input("\nTry another? (y/n): ").lower()
   #     if again != 'y':
   #         break

if __name__ == "__main__":
    main()