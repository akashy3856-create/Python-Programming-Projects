#arithmetic operators
a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) #power

#relational operators
a = 50
b = 20 

print(a == b) #False
print(a != b) #True
print(a > b) #True
print(a < b) #False
print(a >= b) #True
print(a <= b) #False

#assignment operators
num = 10
num /= 10
print("num :", num)

#logical operators 
a = 50 
b = 30
print(not False) 
print(not (a > b))

val1 = True
val2 = False 
print("AND operator:", val1 and val2)

print("OR operator:", (a == b) or (a > b))

#type conversion
a = int("2") 
b = 4.25

print(type(a))
print(a + b)

a = 3.14 
a = str(a)

print(type(a))

name = input("enter your name:")
print("Welcome", name)

val = input("enter some value: ")
print (type(val), val) # "25", "99.99"


int("5")
val = float(input("enter some value: "))
print(type(val), val)

namename = input("enter name: ")
age = input("enter age: ")
marks = input("enter marks: ")

print("welcome", name)
print("age =", age)
print("marks =", marks)


first = int(input("enter first : " ))
second = int(input("enter second : "))

print("sum =", first + second)


side = float(input("enter square side : "))

print("area =", side * side)


a = float(input("enter first : "))
b = float(input("enter second : "))

print("avg =", (a + b)/2)