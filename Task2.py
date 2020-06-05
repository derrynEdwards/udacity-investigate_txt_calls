"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
phone_call_duration = {}
longest_duration = 0
phone_number = ""

for call in calls:
    if call[0] in phone_call_duration:
        phone_call_duration[call[0]] += int(call[3])
    else:
        phone_call_duration[call[0]] = int(call[3])
    if call[1] in phone_call_duration:
        phone_call_duration[call[1]] += int(call[3])
    else:
        phone_call_duration[call[1]] = int(call[3])

for k in phone_call_duration:
    if phone_call_duration[k] > longest_duration:
        longest_duration = phone_call_duration[k]
        phone_number = k

print("{} spent the longest time, {} seconds, on " \
      "the phone during September 2016.".format(phone_number, longest_duration))
