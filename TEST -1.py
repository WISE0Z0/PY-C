#1--LIST--
DD = [1,2,3,4,5]
DD.append(6)
DD.remove(3)
DD.sort()
DD.reverse()
print(DD)

#List Comprehension---
AA = [x**2 for x in range(1,11)]
print(AA)

#MERGE LISTS---
A = [1,2,3,4,5]
B = [6,7,8,9]
C = A + B
print(C)

#2Dictionaries:--
BB = {"1" : 1, "2" : 4,"3": 9,"4": 16,"5": 25 }
print(BB.keys())
print(BB.values())
NN = BB.copy()
print(NN)
del NN["3"]
print(NN.clear())

#Dictionary Merging---
def Merge(CC,EE):
	return(CC.update(EE))
CC = {"a":100,"b":200}
EE = {"c":300,"d":400}
print(Merge(CC, EE))
print(CC)

#Dictionary Comprehension---
GG = {x:x**2 for x in range(1,6)}
print(GG)

#Tuple Operations---concatanating tuples
HH = (1,2,3,4,5)
II = (6,7)
JJ = HH + II
print(JJ)

#Tuple Unpacking---SUM--
HH = (1,2,3,4,5)
KK = [x for x in HH]
print(sum(KK))

#






















