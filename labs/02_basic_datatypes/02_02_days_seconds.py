'''

Write a script that takes in a number in days from the user between 1 and 1,000,000,000 and convert it to seconds.

NOTE: We will use the input() funtion to collect users input. An example is demonstrated below.
w
'''

# the input of the user will be saved in the variable days. (sentence)
# because the input() function collects the input as a string, we have to convert it to an int
# The string passed to the input() function is what the user is prompted with


days = input("Please enter a number in days between 1 and 1,000,000,000: ")
days = int(days)
c = days * 86400
# 24*60*60 = 86400
print(c)