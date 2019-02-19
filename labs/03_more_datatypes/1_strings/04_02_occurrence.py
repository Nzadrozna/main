'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input:
Result: 4
w
'''
print("how many times does the letter appear in your sentence")
prompt = input("Please enter a sentence")
letter = input("please enter a random letter.")
print(prompt.count(letter))
