from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    check = True
    left = True
    while True:
        if (check):
            put_beeper()
        if front_is_blocked(): 
            if (left_is_clear() and left == True):
                turn_left()
                move()
                turn_left()
            elif (right_is_clear() and left == False):
                turn_right()
                move()
                turn_right()
            else:
                break
            left = not left
        else:
            move()
        check = not check


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
