favfruits = ["APPLE","MANGO","BERRY","ORANGE"]
print(favfruits)
print(favfruits[1])
#UPDATE
favfruits[1] = "ORANGE"
print(favfruits)
#APPEND-TO ADD A NEW OBJECT TO THE LAST OF THE LIST
favfruits.append("KIWI")
print(favfruits)
#INSERT IS TO ADD IN THE MIDDLE OR ANYWHERE BUT IT DOES NOT REPLACE BUT ADJUSTS THE INDEX OF THE REMAINING OBJECTS.
favfruits.insert(1,"GAO")
print(favfruits)
#REMOVE
favfruits.remove("APPLE")
print(favfruits)

#SORT-
#favfruits.sort()

#REVERSE - REVERSES THE ENTIRE LIST AS LAST TO  FIRST.
favfruits.reverse()
print(favfruits)
#POP - IT REMOVES THE MENTIONED INDEX VALUE AND ITS DEFAULT REMOVES THE LAST OBJECT.
favfruits.pop(2)
print(favfruits)

#TUPLE - A tuple holds many objects under a single name  unlike list  it is inmutable.(INDEXING  PREMITS)
KING = ("ROYAL","MAJESTIC","FAME")
print(KING)

#DICTIONERY -
DK = {"KEY":600,"LOCK":700}
print(DK)
print(DK.keys())
print(DK.values())
#COPY-
NEWDK = DK.copy()
print(NEWDK)
#DELETE-
del DK["KEY"]
print(DK)
#CLEAR- TO REMOVE ALL THE KEYS AND VALUES IN A DICTIOARY.
DK.clear()
print(DK)












