from Employee import Employee
def main():
    print("Company Name:",Employee.Company_name)
    print("Total Employees:",Employee.total_employees)
    e1=Employee(109,"Hansitha","testing",100000,12345)
    e2=Employee(151,"Kavya","Operating",50000,67890)
    print("Company Name:",Employee.Company_name)
    print("Total Employees:",Employee.total_employees)
    e1.calculate_pf()
    e1.apply_hike(10)
    e2.transfer_department("Development")
    print(Employee.is_valid_salary(e1.salary))
    e1.salary=10
    # e1.emp_id=110
    # print(e1.emp_id)
    #print(e1.pan_number)
    # print(e1._department)
    """In Python the attributes cannot be encapsulated through private,protected access specifiers
    the main use of underscores is to make the developer understand What needs to be protected and encapsulated.
    """

if __name__=="__main__":
    main()