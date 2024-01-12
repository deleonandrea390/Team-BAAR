import re

string = input('Enter String: ')

#letters
letters = "".join(re.split("[^a-zA-Z]*", string))

#numbers
numbers = "".join(re.split("[^0-9]*", string))

#uppercase letters
uppercase = "".join(re.split("[^A-Z]*", string))

#even numbers
even = "".join(re.split("[^2,4,6,8,0]*", string))

#answer
print("Letter String: ", str(letters))
print("Number String: ", str(numbers))

#printing uppercase letter
print("Upper Case Letters: ", str(uppercase))

#converting uppercase letters to ascii 
converted = list(uppercase.encode('ascii'))
print("ASCII Code: ", converted)

#printing even numbers
print("Even Numbers: ", str(even))

#converting even numbers to ascii
converted = list(even.encode('ascii'))
print("ASCII Code: ", converted)


