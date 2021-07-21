 
class Employee:

    def __init__(self, id, name, doj, salary):
        self.id = id
        self.name = name
        self.doj = doj
        self.salary = salary

    def give_promotion(self):
        self.salary = self.salary * 0.30 + self.salary

Emp1 = Employee(1,"Hambira", '10-10-2018', 66000)
Emp2 = Employee(2,"Neelam", '17-07-2021', 27000)
Emp3 = Employee(3,"Puja", '01-03-2021', 20000)
Emp4 = Employee(4,"Anjali", '05-06-2019', 50000)
Emp5 = Employee(5,"jitrey", '01-07-2021', 5000)
Emp6 = Employee(6,"Akash", '01-07-2021', 5000)
Emp7 = Employee(7,"Manoj", '01-06-2021', 5000)
Emp8 = Employee(8,"Naveen", '05-07-2021', 18000)
Emp9 = Employee(9,"Shital", '09-08-2019', 40000)
Emp10 = Employee(10,"Neha", '01-11-2018', 17000)

print(Emp2.salary)
Emp2.give_promotion()
print(Emp2.salary)