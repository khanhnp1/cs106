"""
File: moon_weight.py
--------------------
Add your comments here.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    MOON_PER_EARTH = float(16.5 / 100)
    earth_weight = input("Enter your weight: ")
    earth_weight = float(earth_weight)
    if(earth_weight > 0):
        moon_weight = MOON_PER_EARTH * earth_weight
        print("Your weight on the moon is ", moon_weight)
    else:
        print("Sorry, you can't have a negative weight.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
