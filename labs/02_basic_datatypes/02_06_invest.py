'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
print("To find yoour future value of your investment please answer the three questions below.")
q_1 = input("Please put your investment amount")
q_2 = input("please put your investment rate in a percentage")
q_3 = input("please put the numbers of years you plan to invest")
q_1 = int(q_1)
q_2 = int(q_2)
q_4 = q_2 / 100
q_3= int(q_3)
#cfigure out what is wrong with my math its the percent that im confused on!!!
print(q_1 * (1+q_2)** q_3)
#formula is initial investment(1 + investment rate) **squared to the ampunt of years invested