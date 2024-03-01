#OVER_RIDING--
class Employee:
    def setnumberofworkinghours(self):
        self.setnumberofworkinghours = 40
    def dispaythenumberofworkinghours(self):
        print(self.setnumberofworkinghours)
emp = Employee()
emp.setnumberofworkinghours()
print("NO. of working hours of emp's :", end=" ")
emp.dispaythenumberofworkinghours()

#A CLASS INSIDE A CLASS--
class Employee:
    def setnumberofworkinghours(self):
        self.setnumberofworkinghours = 40
    def dispaythenumberofworkinghours(self):
        print(self.setnumberofworkinghours)
class Trainee(Employee):
    def setnumberofworkinghours(self):
        self.setnumberofworkinghours = 45
emp = Employee()
emp.setnumberofworkinghours()
print("NO. of working hours of emp's :", end = " ")
emp.dispaythenumberofworkinghours()

Train = Trainee()
Train.setnumberofworkinghours()
print("NO. of working hours of Trainee :", end = " ")
Train.dispaythenumberofworkinghours()

#SUPER-- Go back to original value.
class Employee:
    def setnumberofworkinghours(self):
        self.setnumberofworkinghours = 40
    def dispaythenumberofworkinghours(self):
        print(self.setnumberofworkinghours)
class Trainee(Employee):
    def setnumberofworkinghours(self):
        self.setnumberofworkinghours = 45
    def resetthenumberofworkinghours(self):
        super().setnumberofworkinghours()
emp = Employee()
emp.setnumberofworkinghours()
print("NO. of working hours of emp's :", end = " ")
emp.dispaythenumberofworkinghours()

Train = Trainee()
Train.setnumberofworkinghours()
print("NO. of working hours of Trainee :", end = " ")
Train.dispaythenumberofworkinghours()
Train.resetthenumberofworkinghours()
print("NO. of working hours  has been reset :", end = " ")
Train.dispaythenumberofworkinghours()

#
