from oopconcepts.employeedetails import EmployeeDetails

#driver
eno = int(input('Enter Emp no : '))
name = input('Enter Emp name : ')
bp = float(input('Enter basic pay : '))

employee = EmployeeDetails(empno = eno , ename = name, basic_pay = bp)

# print('Emp no : ', employee.get_empno())
print('Emp no : ', employee.empno)
print('Emp name : ', employee.ename)
print('Basic Pay : ', employee.basic_pay)
print('Salary : ', employee.calculate_netsal())