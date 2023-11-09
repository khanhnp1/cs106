"""
File: rating_stats.py
----------------------
This file defines a program that allows a user to calculate
baseline summary statistics about a datafile of professor review
data. 
"""


def calculate_rating_stats(filename):
    """
    This function analyzes the professor review data in the given
    file to calculate the percentage of reviews for both men and
    women that fall in the "high rating" bucket, which is a numerical
    rating that is greater than 3.5.

    The resulting information is printed to the console.
    """
    # You fill this in.  Don't forget to remove the 'pass' statement above.
    rating_m = 0
    rating_high_m = 0
    rating_w = 0
    rating_high_w = 0
    with open(filename) as fp:
        next(fp)
        for line in fp:
            line = line.strip()
            line = line.split(",")
            if line[1] == "M":
                rating_m +=1
                if float(line[0]) > 3.5:
                    rating_high_m +=1
            else:
                rating_w +=1
                if float(line[0]) > 3.5:
                    rating_high_w +=1

    m_percent = (rating_high_m * 100 / rating_m)
    w_percent = (rating_high_w * 100 / rating_w)
    print(round(w_percent), "% of reviews for women in the dataset are high.", sep="")
    print(round(m_percent), "% of reviews for men in the dataset are high.", sep="")     

def main():
    # Ask the user to input the name of a file
    filename = input("Which data file would you like to load? ")

    # Calculate review distribution statistics by gender for
    # that file. This function should print out the results of
    # the analysis to the console.
    calculate_rating_stats(filename)


if __name__ == '__main__':
    main()
