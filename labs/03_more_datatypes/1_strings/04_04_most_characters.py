'''
Write a script that takes three strings from the user and prints the one with the most characters.
w
'''
print("PLease think about three words and write each word down in the correct areas, Thank you")
s1 = input("write one word please.")
s2 = input("Write one more word please.")
s3 = input("write your last word please.")
# count s1,s2,s3
#pick biggest charrcher of 3 print
l1 = len(s1)
l2 = len(s2)
l3 = len(s3)
print(l1)
print(l2)
print(l3)

if l1 > l2:
    if l1 > l3:

        print(s1)

elif l3 > l2:
    print(s3)

else:
    if l2 > l3:
         print(s2)

    if l3 > l1:
        print(s3)




# print the ons with the most characters.
# print(output).count????
