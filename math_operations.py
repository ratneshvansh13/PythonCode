def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

def is_square(num):
    return num **2

#Test the functions
num = int(input("Enter any integer: "))

if is_even(num):
    print(f"{num} is even. ")
else:
    print(f"{num} is odd. ")

print(f"The sqaure of {num} is {is_square(num)}.") 