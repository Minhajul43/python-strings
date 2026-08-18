# Conditional Statements in Python

# if statement
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))

if a>b:
    print(a,"is greater than",b)
else:
    print(b,"is greater than",a)

# elif statement 

if a>b:
    print(a,"is greater than",b)
elif a<b:
    print(b,"is greater than",a)
else:
    print("Both numbers are equal")

# problem solve
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")