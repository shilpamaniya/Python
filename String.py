import numpy as np

#display new line
print('c:\hello\name')

#\n not allowed an new line 
print(r'c:\hello\name')

print('py''thon')

a="hello python"
#print value
print(a)

#print last character
print(a[-1])

#print second last character
print(a[-2])
# display all values
print(a[:])
#display 0 to 2 value
print(a[0:2])

print(a[:2]+a[2:])
print(a[:4]+a[1:])
print(a[-5]+a[-2])
#string array
print(a[1])
#lentth of string
print(len(a))
# uppercase string
print(a.upper())
#Remove Whitespace
b=" hello python "
print(b.strip())

#replace value
c="hello,world"
print(c.replace("h","j"))
print(c.split(",")) # returns ['hello', ' world'] 

p="hello"
q="everyone!"
q=p+q
print(q)

q=p +" "+ q
print(q)
# string format
name="shilpa"
txt="my name is " + name
print(txt)