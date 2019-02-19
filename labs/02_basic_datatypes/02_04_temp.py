'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"
w

'''
temp = input("Input the  temperature in Fahrenheit to convert it to Celsius? : ")
temp = float(temp)
result = float((temp - 32) * 5 / 9)
print(str(result)+ " celsius")

