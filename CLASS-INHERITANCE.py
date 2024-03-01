#IMPORTING CLASS FROM ANOTHER FILE--
from Class import Calculator
class childimp1(Calculator):
    num2 = 200
    def __init__(self):
        Calculator.__init__(self,2,10)
    def getcompletedata(self):
        return self.num2 + self.num + self.summation()
obj = childimp1()
print(obj.getcompletedata())

#input ()
print("hello world")
print("what is your name?")
myname = input()
print("it's good to meet you" + myname)
print("the length of your name is : " )
print(len(myname))
print("what is your age?")
myage = input()
print("you will be "+ str(int(myage)+1)+" in a year")

#

