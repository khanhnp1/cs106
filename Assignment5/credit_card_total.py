"""
File: credit_card_total.py
--------------------------
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""


INPUT_FILE = 'bill1.txt'


def main():
    """
    Add your code (remember to delete the "pass" below)
    """
    Bill = {}
    with open (INPUT_FILE) as bill_file:
        for line in bill_file:
            line = line.strip()
            line = line.replace("$", "")
            line = line.replace("]", "[")
            line = line.split("[")
            
            if Bill.get(line[1]) is None:
                Bill[line[1]] = int(line[2])
            else:
                Bill[line[1]] += int(line[2])

    print(Bill)

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
