# Rectangle Pattern
height = int(input("Enter the height : "))

width = int(input("Enter the width : "))

for i in range(1, height + 1):
    print("*"*width)

# Hollow Rectangle Pattern
height = int(input("Enter the height : "))

width = int(input("Enter the width : "))

print()

for i in range(1, height + 1):
    if i == 1 or i == height:
        print("*"*width)
    else:
        print("*"+ " "*(width - 2)+"*")


# Pyramid Pattern

n = int(input("Enter the size of the Pyramid :"))

for i in range(1, n+1):
    print(" "*(n-i) + " *"*i)

# Right Angled Triangle Pattern
n = int(input("Enter the size of the Right Angled Triangle : "))

for i in range(1, n+1):
    print("*"*i)


# Inverted Pyramid Pattern
n = int(input("Enter the size : "))
for i in range(n, 0, -1):
    print(" "*(n-i) + " *"*i)


# Diamond Pattern

n = int(input("Enter the size of the Diamond : "))

for i in range(1, n+1, 2):
    print(" "*(n-i)+" *"*i)
    
for j in range(n, 0, -2):
    print(" "*(n-j)+" *"*j)