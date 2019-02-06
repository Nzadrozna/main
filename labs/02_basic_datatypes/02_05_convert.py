'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

a =1
a = float(a)
print(a)

b =2.0
b = int(b)
print(b)

c = b/a
print(c)

d = input("please pick any number")
e = input("please pick any number")
d=int(d)
e=int(e)
f = d * e
print(f)
