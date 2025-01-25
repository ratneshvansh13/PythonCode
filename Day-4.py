#a = int(input("Enter a name: "))
#print("Name is: ", a)

#if else condition:
"""
age = int(input("Enter your age"))
if age >= 18:
    print("User is adult")
else:
    print("user is not adult")
    """
#nested if-else:
"""
x = 14
y = 5

if x > 10:
    print(x, "is greater than ", y)
    if x > 15:
        print(x, "is greater than 15")
    else:
        print(x, "is not greater than 15")
else:
    print(x, "is not greater than ", y)
"""
#LOOPS --------------------------
""" For -------------
fruit = ['apple', 'banana', 'cheery', 'pineapple']
for x in fruit:
    print(x)
    """
#While Loop
"""
count = 0
while count < 5:
    print(count)
    count +=1
"""
"""
for i in range(5):
    print(i)
else:
    print("Loop is completed without a break")
"""
#Using a for loop to print numbers from 1 to user-input number
user_input = int(input("Enter an interger: "))
print("Numbers from 1 to: ", user_input)
for i in range(1, user_input + 1):
    print(i)