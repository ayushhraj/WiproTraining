class EmployeeDetails:
    def __init__(self, empno, ename, basic_pay):
        self.__empno = empno
        self.__ename = ename
        self.__basic_pay = basic_pay
        self.da = 20.0
        self.hra = 10.0
        self.pf = 5.5

    @property
    def empno(self):
        return self.__empno

    @property
    def ename(self):
        return self.__ename

    @property
    def basic_pay(self):
        return self.__basic_pay

    ''' 
    @empno.setter
    def empno(self,eno):
        self.__empno = eno

    @ename.setter
    def ename(self, name):
            self.__empno = name

    @basic_pay.setter
    def basic_pay(self, bp):
                self.__empno = bp
    '''

    # def get_empno(self):
    #     return self.__empno
    # def set_empno(self,eno):
    #     self.__empno=eno

    def calculate_allowance(self):
        allowance = (self.basic_pay * self.da / 100) +  (self.basic_pay * self.hra / 100)
        return allowance

    def calculate_deduction(self):
        deduction = (self.basic_pay * self.pf / 100)
        return deduction

    def calculate_netsal(self):
        netsal = (self.basic_pay + self.calculate_allowance() - self.calculate_deduction())
        return netsal