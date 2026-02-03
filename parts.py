#!/usr/bin/env python3
import random
from fractions import Fraction

def get_color(text, color):
    colors = {
        'green': '\033[92m',
        'red': '\033[91m',
        'reset': '\033[0m'
    }
    return f"{colors[color]}{text}{colors['reset']}"

def format_fraction(frac):
    """Convert fraction to mixed number format if improper."""
    if frac.numerator < 0:
        # Handle negative fractions
        frac = abs(frac)
        sign = "-"
    else:
        sign = ""
    
    whole = frac.numerator // frac.denominator
    remainder = frac.numerator % frac.denominator
    
    if whole == 0:
        return f"{sign}{frac}"
    elif remainder == 0:
        return f"{sign}{whole}"
    else:
        return f"{sign}{whole} {remainder}/{frac.denominator}"

def parse_mixed_number(user_input):
    """Parse mixed number or fraction input from user."""
    user_input = user_input.strip()
    
    # Try to parse as mixed number (e.g., "1 2/3")
    if ' ' in user_input:
        parts = user_input.split()
        if len(parts) == 2:
            try:
                whole = int(parts[0])
                frac = Fraction(parts[1])
                return Fraction(whole * frac.denominator + frac.numerator, frac.denominator)
            except:
                pass
    
    # Try to parse as regular fraction or whole number
    return Fraction(user_input)

def generate_fraction_quiz(num_questions=5):
    """Generate a quiz with random fraction operations."""
    operations = ['+', '-', '*', '/', '/','/']
 #   operations = ['+', '-', '/']
    score = 0
    
    while True:
        # Generate random fractions
        while True:
            num1 = random.randint(1, 10)
            den1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            den2 = random.randint(1, 10)
            
            # Check if fractions divide evenly (are whole numbers), if so, regenerate
            if num1 % den1 != 0 and num2 % den2 != 0:
                break
        frac1 = Fraction(num1, den1)
        frac2 = Fraction(num2, den2)
        
        # Random operation
        operation = random.choice(operations)
        
        # Calculate correct answer
        if operation == '+':
            answer = frac1 + frac2
        elif operation == '-':
            answer = frac1 - frac2
        elif operation == '*':
            answer = frac1 * frac2
        elif operation == '/':
            answer = frac1 / frac2
        
        # Ask user
        question_str = f"{format_fraction(frac1)} {operation} {format_fraction(frac2)}"
        print(f"\nQuestion : {question_str}")
        
        while True:
            user_answer = input("Enter your answer (as numerator/denominator or whole remainder/denominator): ")
            
            try:
                user_frac = parse_mixed_number(user_answer)
                if user_frac == answer: 
                    print(get_color("✓ Correct!", 'green'))
                    score += 1
                    break
                else:
                    print(get_color("✗ Wrong!", 'red'))
            except ValueError:
                print(get_color("✗ Wrong!", 'red'))
    
    print(f"\n\nFinal Score: {score}/{num_questions}")

if __name__ == "__main__":
    generate_fraction_quiz(5)