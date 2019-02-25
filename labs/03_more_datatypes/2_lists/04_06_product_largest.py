'''
Take in 10 numbers from the user. Place the numbers in a list.
Calculate the product of all of the numbers in the list.
Also, find the largest number in the list.

Print the results.

'''

num = [int(n, 10) for n in input("insert 10 numbers with spaces inbetween the numbers: ").split()]
list1 = list(num)
def multiply(num):
    total = 1
    for x in num:
        total *= x
    return total

print (multiply(list1))
print(max(list1))