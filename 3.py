# Find the second largest element in the list ?
l = [12,13,44,21,54,23,76,15,65,26,62,75,13,76]

l.sort()

l2 = []

for i in l:
    if i not in l2:
        l2.append(i)

print(l2[-2])