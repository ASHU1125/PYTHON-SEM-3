#01create two different set with data
My_set={1,'ASHISH',3.14,'ASUR'}
My_set2={2,'JAYSWAL',3.14,'ASUR'}
#02 print set items 
print(My_set)
print(My_set2)
#03 add and remove item from set 
My_set.add('ASUR')
print(My_set)
My_set2.discard('ASUR')
print(My_set2)
#04
My_set1={1,'ASHISH',3.14,'ASUR'}
My_set3={2,'JAYSWAL',3.14,'ASUR'}
#union
print(My_set1|My_set3)
#intersection
print(My_set1&My_set3)
#difference
print(My_set1 - My_set3)
#symmetric difference
symmetric_difference=My_set1.symmetric_difference(My_set3)
print(symmetric_difference)
#Chek subset of another set 
subset=My_set3<My_set1
print(subset)
