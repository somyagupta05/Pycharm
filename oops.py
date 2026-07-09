# class Employee:
#     salary=89
#     name="rohan"
#     def getSalary(self):
#         return self.salary
#
# rohan=Employee()
# print(rohan.salary)
# print(rohan.name)

# constructor
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def getSalary(self):
        print(self.salary)
rohan=Employee("rohan",5000)
# print(rohan.salary)
# print(rohan.name)
rohan.getSalary()

somya=Employee("somya",90000)
print(somya.salary)
print(somya.name)

