from oopconcepts.agecalc import AgeCalculation
from oopconcepts.myexception import AgeException

age = int(input('Enter your Age : '))

aobj = AgeCalculation()
'''
try:
    if aobj.voting_age_check(age):
        print('Eligible to Vote. Contact next step....')
except AgeException as ae:
    print(ae)

'''
try:
    aobj.voting_age_check(age)
    aobj.pension_age_check(age)
except AgeException as ae:
    print(ae)
else:
    print('Eligible to Vote. Contact next step.....')