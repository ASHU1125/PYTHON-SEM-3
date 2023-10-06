#01
L1 = [1, 2, 3, 4, 5]
print("List created:", L1)
#02
L1 = [1, 2, 3, 4, 5]
L1.append(6)
L1.remove(3)
print( "Num Appended and removed list:" , L1)
#03
num_elements = len(L1)
print("Number of elements in the list:", num_elements)
#04
index = 3
element = L1[index]
print(f"Element at index {index}: {element}")
#05
L1.sort()
print("Sorted list in ascending order:", L1)
#06
L1.reverse()
print("Reversed list:",L1)