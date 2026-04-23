
'''
#functions
def add(n1 , n2):
    #sum = n1 + n2
    #return sum
    return n1 + n2


def sub(n1 , n2):
    return n1 - n2


def mul(n1 , n2):
    return n1 * n2


def div(n1 , n2):
    return n1 // n2

def pow():
    pass

#driver
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

result = add(num1 , num2)       #positional arguments
print('Add : ', result)
result = sub(num1 , num2)
print('Add : ', result)
result = mul(num1 , num2)
print('Add : ', result)
result = div(num1 , num2)
print('Add : ', result)
'''


'''
#ARBITARY 1

def add(nums):
    sum = 0
    for n in nums:
        sum += n
    return sum

numbers = list()
count = int(input('enter how many: '))

for _ in range(1, count+1):
    numbers.append(int(input('NO. : ')))
print(add(numbers))
'''

'''
#ARBITARY 2
def add(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum


print(add( 2,3,4))
'''


'''
#lambda
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

add = lambda n1, n2 : n1 + n2
print(add(num1,num2))
'''

'''
numbers = [1,2,3,4,5]

sq = lambda nums : [num * num   for num in nums]
print(sq(numbers))
print(tuple(sq(numbers)))

sq = lambda nums : [num * num   for num in nums if num%2 == 0]
print(sq(numbers))
'''