userinput = int(input("enter value: "))

# printing shapes in python

# no-1
for i in range(userinput):
    for j in range(i+1):
        print("*",end=" ")
    print(" ")

# no-2
for i in range(userinput):
    for j in range(userinput-i):
        print("*",end=" ")
    print(" ")

# no-3
k = (userinput*2)-2
for i in range(userinput):
    for j in range(k):
        print(end=" ")

    k=k-2
    for a in range(i+1):
        print("*", end=" ")
    print("\r")