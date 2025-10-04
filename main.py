"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michaela Tóthová
email: misatothova7@seznam.cz
"""

import random
from typing import Tuple, List


import random

def generate_secret() -> str:
    digits = random.sample("0123456789", 4)   
    if digits[0] == "0":                      
        digits[0], digits[1] = digits[1], digits[0]  
    return "".join(digits)


def validate_guess(guess: str) -> Tuple[bool, List[str]]:
   
    errors: List[str] = []
    if len(guess) != 4:
        errors.append("The number must have exactly 4 digits.")
    if not guess.isdigit():
        errors.append("The guess must contain only digits (0–9).")
    else:
        if guess[0] == "0":
            errors.append("The number cannot start with zero.")
        if len(set(guess)) != 4:
            errors.append("All digits must be unique.")
    return (len(errors) == 0, errors)


def count_bulls_cows(secret: str, guess: str) -> Tuple[int, int]:
    
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = len(set(secret) & set(guess)) - bulls
    return bulls, cows


def format_count(n: int, singular: str, plural: str) -> str:
    return f"{n} {singular if n == 1 else plural}"


def get_valid_guess() -> str:
    
    while True:
        guess = input(">>> ").strip()
        valid, errors = validate_guess(guess)
        if valid:
            return guess
        print("Invalid guess:")
        for e in errors:
            print(f" - {e}")
        print("-----------------------------------------------")
        print("Enter a number:")
        print("-----------------------------------------------")


def play_game(secret: str) -> None:
   
    attempts = 0
    while True:
        guess = get_valid_guess()
        attempts += 1
        bulls, cows = count_bulls_cows(secret, guess)
        if bulls == 4:
            print("Correct, you've guessed the right number")
            print(f"in {attempts} guesses!")
            print("-----------------------------------------------")
            print("That's amazing!")
            break
        else:
            print(f"{format_count(bulls, 'bull', 'bulls')}, "
                  f"{format_count(cows, 'cow', 'cows')}")
            print("-----------------------------------------------")
            print("Enter a number:")
            print("-----------------------------------------------")


def main() -> None:
   
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    print("Enter a number:")
    print("-----------------------------------------------")

    secret = generate_secret()
    play_game(secret)


if __name__ == "__main__":
    main()
