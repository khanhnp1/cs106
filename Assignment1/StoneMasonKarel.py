from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()


def fix_one_col():
    turn_left()
    while True:
        if no_beepers_present():
            put_beeper()
        if front_is_blocked():
            break
        move()
    # Back to the first
    turn_around()
    while front_is_clear():
        move()
    turn_left()

def move_to_next_col():
    for i in range(4):
        move()
    
def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while True:    
        fix_one_col()
        if front_is_clear():
            move_to_next_col()
        else:
            break


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
