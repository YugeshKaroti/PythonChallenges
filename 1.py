# Find the closest number to zero in the given list ?
list_1 = [10,20,30,11,26,22,15,7,4,65,21,0,0,44]

list_2 = [i for i in set(list_1)]

if min(list_2) == 0:
    list_2.sort()
    print(list_2[1])
    
else:
    print(min(list_2))