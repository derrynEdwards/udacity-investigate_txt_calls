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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
outgoing_call = []
incoming_call = []
outgoing_text = []
incoming_text = []
telemarketers = []

for call in calls:
    if call[0][:3] != '140':
        outgoing_call.append(call[0])
        incoming_call.append(call[1])

for text in texts:
    outgoing_text.append(text[0])
    incoming_text.append(text[1])

for num in outgoing_call:
    if ((num not in incoming_call) and
        (num not in outgoing_text) and
        (num not in incoming_text)):
        telemarketers.append(num)

distinct_telemarketers = list(dict.fromkeys(telemarketers))
print("These numbers could be telemarketers:")
for num in sorted(distinct_telemarketers):
    print(num)
