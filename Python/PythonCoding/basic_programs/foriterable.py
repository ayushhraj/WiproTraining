"""
day 2
date: 23/4/26
"""

#for list
numbers = [11,22,98,54,63,45,20,45]

for number in numbers:
    print(number%10, end ='\t')
print('\n')


#for tuple
numbers = (11,22,98,54,63,45,20,45)

for number in numbers:
    print(number%10, end ='\t')
print('\n')


#for set
numbers = {11,22,98,54,63,45,20,45}

for number in numbers:
    print(number%10, end ='\t')
print('\n')


#for dict
stud = {'rno':'101' , 'name':'AAA' , 'city':'MUM'}

for stu in stud:
    print(stu , end = '\t')
print('\n')
for k,v in stud.items():
    print(k, '--' , v)
print('\n')