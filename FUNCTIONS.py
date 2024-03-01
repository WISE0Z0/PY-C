#FUNCTIONS-
#1.USER DEFINED FUNCTION-
#def functionname():
#         block of code

#EX1-
def helloworld():
    print("welcome to the session")
helloworld()

#EX2-
def greet(name):
    print("HELLO,"+ name +"!")
greet("SAI")

#EX3-
def calculate(length,width):
    area = length * width
    print(area)
calculate(25,35)

#EX4-RETURN
def calculate(length,width):
    area = length * width
    return area
rectangle_length =5
rectangle_width = 3
area_result = calculate(rectangle_length,rectangle_width)
print(f"THE AREA OF THE RECTANGLE IS: {area_result}")


