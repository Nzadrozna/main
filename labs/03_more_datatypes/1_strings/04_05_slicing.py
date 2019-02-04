'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

name= input("Enter a name")
firstletter= name[0]
new_name= name + firstletter + "ay"
new1_name= new_name[1:]
print(new1_name)


# print(name) mving the firt letter to the back na dadding