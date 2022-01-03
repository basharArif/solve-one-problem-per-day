userinput = int(input("enter value: "))

# printing shapes in python

# no-1

for i in range (userinput):
    for j in range(userinput):
        print("1 ",end="")

    print("")

# no-2

for i in range(userinput):
    for j in range(i+1):
        print("*",end=" ")
    print(" ")

# no-3

for i in range(userinput):
    for j in range(userinput-i):
        print("*",end=" ")
    print(" ")

# no-4

k = (userinput*2)-2
for i in range(userinput):
    for j in range(k):
        print(end=" ")

    k=k-2
    for a in range(i+1):
        print("*", end=" ")
    print("\r")

# no-5

for i in range(1,5):
    for j in range(userinput):
        print(i,end=" ")
    print("")

# no-6

for i in range(1,5):
    for j in range(userinput):
        print(userinput-i,end=" ")
    print("")

# no-7

for i in range(1,5):
    for j in range(1,userinput):
        print(j,end=" ")
    print("")