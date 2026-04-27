
import re

#beg and end match
'''
txt = input('Enter a text : ') #India is my country
bpat = input('Enter beginning pattern : ') #India
epat = input('Enter ending pattern : ') #country
bpat = '^' + bpat #^India
epat = epat + '$' #try$

if re.search(pattern = bpat, string = txt):
    print('Beginning Pattern Available')
else:
    print('Beginning Pattern not available')

if re.search(pattern = epat, string = txt):
    print('Ending Pattern Available')
else:
    print('Ending Pattern not available')
'''

#digit
'''
mobno = input('Enter a text : ')
pat = r"[0-9]"     
if re.fullmatch(pattern =pat, string = mobno):    #re.search(pattern =pat, string = mobno):
    print('Only Digits')
else:
    print('Other characters available')
'''

#username
'''
un = input('Enter username : ')
pat = r"^[a-z_]{8,}$"       #writing characters in lowercase exactly 8 times

if re.match(pattern = pat, string = un):   #check for first 8 chr match with the pattern
    print('Valid')
else:
    print('Invalid')
'''

#email
'''
emailadd = input('Enter the Email : ')
pat = r"^[a-zA-Z0-9_]+@+[a-z]+\.+[a-z]+$"
if re.match(pattern = pat, string = emailadd):
    print('Valid')
else:
    print('Invalid')
'''

#pwd
'''
pwdtxt = input('Enter password : ')
pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@_-]).{8,}$"
if re.match(pattern = pat, string = pwdtxt):
    print('Valid')
else:
    print('Invalid')
'''

txt = input('Enter the text  : ')
pat = r"\s+"

# print(re.sub(pattern = pat, string = txt, repl = '*'))

print(re.split(pattern = pat, string = txt))