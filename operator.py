# all kind of operators are used in python programming language.

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

# Addition
Sum=a+b
print("Sum:", Sum)

# Subtraction
Sub=a-b
print("Subtraction:", Sub)

#Multiplication
Mul=a*b
print("Multiplication:", Mul)

# Division
Div=a/b
print("Division:", Div)

# Modulus
Mod=a%b
print("Modulus:", Mod)

# Exponentiation
Exp=a**b
print("Exponentiation:", Exp)

# Floor Division
FloorDiv=a//b
print("Floor Division:", FloorDiv)

# Comparison Operators
print("a==b:", a==b)
print("a!=b:", a!=b)
print("a>b:", a>b)
print("a<b:", a<b)
print("a>=b:", a>=b)
print("a<=b:", a<=b)

# Logical Operators

print("a>0 and b>0:", a>0 and b>0)
print("a>0 or b>0:", a>0 or b>0)
print("not(a>0):", not(a>0))

# Bitwise Operators
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)

# Shift Operators
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

# Assignment Operators
a += b
print("a += b:", a)

a -= b
print("a -= b:", a)


a*= b
print("a *= b:", a)

a/= b

print("a /= b:", a)

# Modulus Assignment
a %= b
print("a %= b:", a)

# Exponentiation Assignment
a **= b
print("a **= b:", a)

# Floor Division Assignment
a //= b
print("a //= b:", a)

# Identity Operators
print("a is b:", a is b)
print("a is not b:", a is not b)

# Membership Operators
list1 = [1, 2, 3, 4, 5]

print("3 in list1:", 3 in list1)
print("6 not in list1:", 6 not in list1)
print("2 in list1:", 2 in list1)