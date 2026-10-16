str1 = "This is a string. \twe are creating it in python."
print(str1)

str1 = "apna"
str2 = "college"
print(str1+str2)

str1 = "apna"
len1 = len(str1)
print(len1)

str2 = "college"
len2 = len(str2)
print(len2)

final_str = str1 + " " + str2
print(final_str)
print(len(final_str))


str = "apna college"
ch = str[0]
print(ch)

str = "apna college" 
ch = str[1]
print(ch)

str = "apna college"
ch = str[3]
print(ch)

str = "apna college"
str = print(str[1:4])

str = "apna college"
print(str [0:4])

str ="apna college"
print(str[:4]) #[0:4]
print(str[5:]) #[5:len(str)]

str = "apple"
print(str[-5:-2])

str = "I am studying python from ApnaCollege"
print(str.endswith("ege"))

str = "I am studing python from ApnaCollege"
print(str.endswith("app"))


str = "i am studing python from ApnaCollege"
print(str.capitalize())

str = "i am studing python from ApnaCollege"
print(str.capitalize())
print(str)

str = "i am studing python from ApnaCollege"
str = str.capitalize()
print(str)


str = "i am studying python from ApnaCollege"
print(str.replace("o", "a")) 

str = "i am studying python from ApnaCollege"
print(str.replace("python", "javascript"))


str = "i am studying python from ApnaCollege"
print(str.find("o"))

str = "i am from studying python from ApnaCollege"
print(str.find("from"))


str = "i am from studying python from ApnaCollege"
print(str.count("from"))

str = "i am from studying python from ApnaCollege"
print(str.count("o"))


name = input("enter your name :")
print("length of your name is", len(name)) 


str = "Hi, $ I am the $ symbol $ 99.99"
print(str.count("$"))


age = 21

if(age>=18): #True
   print("can vote & apply for license")

age = 24

if(True):
   print("can vote")
   print ("can drive")


light = "green"
if(light == "red"):
   print("stop")
elif(light == "green"):   
    print("go")
elif(light == "yellow"):  
    print("look")

    print("end of code") 


num = 5 
if(num > 2):
   print("greater than 2")
if(num > 3):
   print("greater than 3")

num = 5
if(num > 2):
   print("greater than 2")   
elif(num > 3):
   print("greater than 3")

light = "pink"

if(light == "red"):
   print("stop")
elif(light == "green"):   
   print("go")
elif(light == "yellow"):
   print("look")
else:
   print("light is broken") #indentaion

   print("end of code")


age = 24

if(age >= 18):
   print("can vote")
else:
   print("CANNOT vote")

age = 14

if(age >= 18):
   print("can vote")
else:
   print("CANNOT vote")


marks = 74

if(marks >= 90):
   grade = "A"
elif(marks >= 80 and marks < 90):
   grade = "B"
elif(marks >= 70 and marks < 80):
   grade = "C"
else:
   grade = "D"

print("grade of the student ->", grade)


age = 95

#nesting
if(age >= 80):
   if(age >= 80):
      print("cannot drive")
   else:
      print("can drive")
else:
   print("cann0t drive") 



num = int(input("enter number:"))

rem = num % 2

if(rem == 0): 
   print("EVEN")
else:
   print("ODD")

num = int(input("enter number:"))

if(num % 2 == 0):
   print("EVEN")
else:
   print("ODD") 



a = int(input("enter first number"))     
b = int(input("enter second number"))
c = int(input("enter third number"))

if(a >= b and a >= c):
   print("first number is largest", a)
elif(b >= c):
   print("second number is largest", b)
else:
   print("third number is largest", c)


x = int(input("enter number :"))

if(x % 7 == 0):
   print("multiple of 7")
else:
   print("not a multiple")

x = int(input("enter number :"))

if(x % 7 == 0):
   print("multiple of 7")
else:
   print("not a multiple")   