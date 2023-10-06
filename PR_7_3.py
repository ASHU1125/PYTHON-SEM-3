# Create a dictionary
my_dict = {
    'NAME': 'Ashish',
    'AGE': 19,
    'CITY': 'Vadodara'
}
# Print dictionary items
print("Dictionary:", my_dict)
# Add item from dictionary 
my_dict['SURNAME']='JAYSWAL'
print("Dictionary:", my_dict)
#Remove item from dictionary
del my_dict ['AGE']
print("Dictionary:", my_dict)
#Chek whether a key exist in a dictionary 
key=input("enter key:")
if key in my_dict:
    print("key is exists")
else:
    print("key is not exists")