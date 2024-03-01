# LOOPS-- FOR LOOP:
favfruits = ["APPLE", "MANGO", "BERRY", "ORANGE"]
print(favfruits)
##syntax for "for" loop:
for demo in favfruits:
    print(demo)


# range()
for number in range(1, 10):
    print(number)


# WHILE LOOP : takes range whether it is true or false.
temp = 77
while temp >= 68 and temp <= 77:
    print("room temp is  maintained at {} deg F".format(temp))
    temp = temp - 1

#
#while True:
 #   print("THIS LOOP RUNS FOREVER")




#WHILE LOOP WITH 2 VARIABLE CONDITIONS
temp = 77
while temp >= 68 and temp <= 77:
    print("room temp is  maintained at {} deg F".format(temp))
    temp = temp -1


# MARIX 3X3
number = 1
for row in range(1, 4):
    for column in range(1, 4):
        print(number, end=' ')
        number = number + 1
    print()




# BREAK:
for number in range(1, 11):
    if number == 5:
        break
    else:
        print(number)


#CONTINUE:
for number in range(1,11):
    if number == 5:
        continue
    else:
        print(number)



