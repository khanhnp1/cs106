"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    n = int(input("Enter a number: "))
    cnt = 0
    while(n != 1):
        cnt = cnt + 1
        if (n % 2) == 0:
            print(n, "is even, so I take half", n // 2)
            n = n // 2
        else:
            print(n, "is odd, so I make 3n + 1", n * 3 + 1)
            n = n * 3 + 1
    print ("The process took", cnt ,"steps to reach 1")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
