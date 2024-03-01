#DIAMOND INHERITANCE--
class A:
    def method(self):
        print("Method of class A")
class B(A):
    def method(self):
        print("Method of class B")
class C(A):
    def method(self):
        print("Method of class C")
class D(B,C):
    pass
d = D()
d.method()

#
