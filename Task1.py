"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def getDistinctNumbers(a_list):
    """
    Returns a list of distinct phone numbers.
    """
    distinct_numbers = []
    for row in a_list:
        if row[0] not in distinct_numbers:
            distinct_numbers.append(row[0])
        if row[1] not in distinct_numbers:
            distinct_numbers.append(row[1])
    return distinct_numbers

numbers = getDistinctNumbers(texts) + getDistinctNumbers(calls)
numbers = set(numbers)
print("There are {} different telephone numbers in the records.".format(len(numbers)))
 