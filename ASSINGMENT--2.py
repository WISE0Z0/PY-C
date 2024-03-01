#A YEAR TO BE CHECKED TO SEE LEAP YEAR OR NOT!---
year = int(input("Enter the year: "))
if (year%4 == 0 and year%100!= 0 or year%400 == 0):
    print("this ia a leap-year")
else:
    print("this is not a leap year")

#GREATEST NUMBER BETWEEN THE THREE NUKMBERS---
First = int(input("Enter the first number: " ))
second = int(input("Entefr the second number: "))
third = int(input("Enter thr third number: "))
print("The greatest number between the three numbers is: ", end="")
print(max(First,second,third))

#SUM OF THE DIGITS IN A GIVEN NUMBER-(METHOD : Using String Character Extraction)---
num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)


