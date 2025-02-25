# How to Swap two numbers without using the third variable ?
a = int(input("Enter the first number : "))

b = int(input("Enter the second number : "))

a = a + b

b = a - b

a = a - b

print("After swapping : ")

print(f"First number is {a} and Second number is {b}")