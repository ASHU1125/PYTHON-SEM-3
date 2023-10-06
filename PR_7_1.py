#01 create a tuple with different data types.
My_tuple=(1,'ASHISH',3.14,True,[1,2,3])
#02 Print tuple items.
print(My_tuple)
#03 convert tuple into a list. 
My_list=list(My_tuple)
print(My_list)
#04 remove data items from a list. 
items_to_remove = ['apple', True]
My_list = [item for item in My_list if item not in items_to_remove]   
print(My_list)
#05 convert list into a tuple.
my_tuple = tuple(My_list)
print(my_tuple)
#06 print tuple items.
print(my_tuple)

