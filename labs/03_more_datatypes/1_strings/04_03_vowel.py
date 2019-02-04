'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''
 #DONT UNDERSTAND WHY IT WONT WORK

sentence = input("Enter ur string")
count = 0
vowels = set("aeiou")
for letter in sentence:
    if letter in vowels:
        count += 1
print 'Number of vowels:', count




