"""
Day-1
Date: 22/4/26
"""
#appearance of "a" in a string using enumerate

string = input('Enter a string: ')
count = 0
for i, ch in enumerate(string):
    if ch == 'a':
        count += 1
print('appearance of a in the string: ',count)

