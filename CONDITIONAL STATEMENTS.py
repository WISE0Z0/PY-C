#IF- condition
totalmarks = 97
if totalmarks >= 90:
    print("CONGRATS you have secured grade 'A'")
elif totalmarks >= 40:
    print("you have PASSED the exam")
else:
    print("you have FAILED")

#NESTEDIF-condition
totalmarks = 100
if totalmarks >= 90:
    print("congrats, you have got grade 'A'")
    if totalmarks == 100:
        print("congrats, you have got grade 'S'")

# WITH 2 variables  & using AND GATE
totalmarks = 95
attendance = 90
if totalmarks >= 90 and attendance >= 90:
    print("you are a DISCIPLINED student")


#OR is used here
fruit = "APPLE"
if fruit is "MANGO" or fruit is "APPLE":
    print("I like that fruit")







