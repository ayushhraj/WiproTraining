Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1 = 'hello'
s1
'hello'
type(s1)
<class 'str'>
s1.capitalize()
'Hello'
s1.upper()
'HELLO'
s1.lower()
'hello'
s1='hELLO;
SyntaxError: unterminated string literal (detected at line 1)
s1='hELLO'
s1.casefold(
    )
'hello'
s1='HeLLo'
s1.casefold()
'hello'
s1.count()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s1.count()
TypeError: count expected at least 1 argument, got 0
s1.count('l')
0
s1.count('L')
2
s1.count('H')
1
s1.endswith('o')
True
s1.endswith('0')
False
s1.find('L')
2
s1.find('0')
-1
s1.index('o')
4
s1.index('m')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s1.index('m')
ValueError: substring not found
s1.isalpha()
True
s1.isalnum()
True
s1.join(' there')
' HeLLotHeLLohHeLLoeHeLLorHeLLoe'
s1.replace('L','l')
'Hello'
s1
'HeLLo'
s1 = 'Hello there how are you'
s1
'Hello there how are you'
s1.split(' ')
['Hello', 'there', 'how', 'are', 'you']
s1 = 'Hello there - how are you'
s1
'Hello there - how are you'
s1.split(' ')
['Hello', 'there', '-', 'how', 'are', 'you']
s1.split('')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s1.split('')
ValueError: empty separator
s1.split('-')
['Hello there ', ' how are you']
s1.swapcase()
'hELLO THERE - HOW ARE YOU'
s1 = 'hello there !!!'
len(s1)
15
s1[1]
'e'
>>> s1[-3]
'!'
>>> s1[-4]
' '
>>> s1[-15]
'h'
>>> s1[-16]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s1[-16]
IndexError: string index out of range
>>> s1[15]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s1[15]
IndexError: string index out of range
>>> s1
'hello there !!!'
>>> s1[0:5]
'hello'
>>> s1[0:10]
'hello ther'
>>> s1[0:]
'hello there !!!'
>>> s1[2:12:2]
'lotee'
>>> s1[::2]
'hlotee!!'
>>> s1[-15:-10]
'hello'
>>> s1[-10:-15]
''
>>> s1[::-2]
'!!eetolh'
