class Employee:
    Company_name="TechCorp Solutions"
    total_employees=0
    pf_percentage=12.0
    MIN_SALARY=15000
    MAX_SALARY=500000
    def __init__(self,emp_id,name,department,salary,pan_number):
        self.name=name
        self._emp_id=emp_id
        self._department=department
        self.salary=salary
        self.__pan_number=pan_number
        Employee.total_employees+=1
    @property
    def pan_number(self):
        return self.__pan_number
    @property
    def emp_id(self):
        return self._emp_id
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if value>self.MAX_SALARY or value<self.MIN_SALARY:
            raise ValueError(f"Salary must be between {self.MIN_SALARY} and {self.MAX_SALARY}")
        elif value<=Employee.MAX_SALARY and value>=Employee.MIN_SALARY:
            self._salary=value
        else:
            raise TypeError("Salary must be a number")
    def apply_hike(self,percent):
        if percent<0 or percent>50:
            raise ValueError("Hike Percentage Must be between 0 to 50")
        else:
            self._salary+=(self.salary*percent/100)
        print(f"The Salary Hike of {self.name} is {self._salary}")
    def calculate_pf(self):
        pf=self._salary*(self.pf_percentage/100)
        print(f"The Calculated pf of {self.name} is {pf}")
    def transfer_department(self,newdept):
        old_dept=self._department
        self._department=newdept
        print(f"{old_dept} is changed to {self._department}")
    @classmethod
    def get_total_employees(cls):
        return Employee.total_employees
    @staticmethod
    def is_valid_salary(amount):
        if amount>=Employee.MIN_SALARY and amount<=Employee.MAX_SALARY:
            return True
        else:
            return False
    def __str__(self):
        return f"In the company {Employee.Company_name} There are {Employee.total_employees} employees"
    
    