#LAMBDA FUNCTION-
Add = lambda x: x + 45
result = Add(20)
print(result)

#EX-2
Add = lambda x,y: x + y
result = Add(20,10)
print(result)

#EX-3
def classroom(n):

    square = lambda x: x + n
    return square

demo = classroom(20)
print(demo(30))

#EX-4
def multilier(n):
    multiply_by = lambda x: x * n
    return multiply_by
multilier_by_5 = multilier(5)
print(multilier_by_5(10))
print(multilier_by_5(7))

#



