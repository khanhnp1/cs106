"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    MIN_RANDOM = 0
    MAX_RANDOM = 100
    correct_answer = 0

    while (correct_answer < 3):
        num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        print ("What is", num1,"+", num2)
        answer = int(input("Your Answer: "))
        if (answer == num1 + num2):
            correct_answer = correct_answer + 1
            print("Correct! You've gotten", correct_answer,"correct in a row")
        else:
            correct_answer = correct_answer - 1
            print("Incorrect. The expected answer is", num1 + num2)
    
    print("Congratulations! You mastered addition")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
