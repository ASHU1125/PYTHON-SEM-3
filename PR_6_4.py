L1 = [1, 2, 3, 4, 5, 6, 1, 4]
L2 = []

for item in L1:
    if item not in L2:
        L2.append(item)

print("Original list:", L1)
print("List without duplicates:", L2)
  