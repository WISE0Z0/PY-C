###SET----
G = {4,5,6,7,3}
print(G)
G.add(2)
print(G)

#SET OPERATIONS---
set1={1,2,3,4,5,}
set2={4,5,6,7,8}
#UNION-
union_set = set2.union(set1)
print(union_set)
#INTERSECTION-
intersection_set = set1.intersection(set2)
print(intersection_set)
#Differnce-
difference_set = set2.difference(set1)
print(difference_set)
difference_set = set1.difference(set2)
print(difference_set)
#TRUE/FALSE-
print(1 in set1)
print(5 in set2)
print(1 in set2)
#
original = {1,2,3,4,5}
print("original_set:{}".format( original))
##covert set to list ,reverse the list and convert it back to
##set
