
#  pallindrome

userinput = input("enter value: ")

w = ""
for i in userinput:
    w = i + w

if (userinput == w):
    print("true")
else:
    print("false")