
#---------------------------------Set 1------------------------------------------------


# 1.2 Write a Python program to swap two variables using third variable.

"""
a = 2
b = 4

print("value of a before swap is : ",a)
print("value of b before swap is : ",b)

c = a
a = b
b = c

print("value of a After swap is : ",a)
print("value of b After swap is : ",b)

"""



# 1.3 Write a Python program to swap two variables without third variable. 
"""
a = 2
b = 4

print("value of a before swap is : ",a)
print("value of b before swap is : ",b)

(a,b) = (b,a)

print("value of a After swap is : ",a)
print("value of b After swap is : ",b)"

"""



#1.6 Write a Python program to find sum of n natural numbers without loop.
"""
n = 10

sum = n*(n+1)/2 #remember this euqation

print("The sum of n number is : ",sum)
"""

#---------------------------------Set 2------------------------------------------------

#2.1 WAP to check whether entered number Is even or odd.

"""
num = int(input("Enter Number : "))

if(num % 2 == 0):
    print("Number is Even")
else:
    print("Number is odd")
"""


# 2.2 WAP to find whether entered number is positive,negative or zero.

"""num = int(input("Enter Number : "))

if(num>0):
    print("Number is positive")
elif (num<0):
    print("Number is negative")
else:
    print("Number is Zero")"""



# 2.4 WAP to check whether entered character is vowel or consonant.
"""
vowel = ["a","e","i","o","u"]
char = (input("Enter Character : ")).lower()

if(char in vowel):
    print("Character Is Vowel")
else:
    print("Charactrer is consonant")
"""

    

# 2.5 WAP to find maximum of three numbers(nested if-else). 
"""
num1 = int(input("Enter Number a : "))
num2 = int(input("Enter Number b : "))
num3 = int(input("Enter Number c : "))

if(num1>num2):
    if(num1>num3):
        print("The maximum number is : ",num1)
    else:
        print("The maximum number is : ",num3)
else:
    if(num2>num3):
        print("The maximum number is : ",num2)
    else:
        print("The maximum number is : ",num3)
"""


# 5.6 WAP to calculate the salary of an employee based on following conditions
#     (nested if-else):
#       1. If degree=B.E.and experience<5years,salary=30000
#       2. If degree=B.E.and experience>=5years,salary=40000
#       3. If degree=M.E.and experience<5years,salary=50000
#       4. If degree=M.E.and experience>=5years,salary=60000

"""
degree = input("Enter your Degree(BE or ME) : " ).upper()
exprience = int(input("Enter exprience in years : "))

if(degree == "BE"):
    if(exprience<5):
        print("salary is 30000")
    else:
        print("salary is 40000")
elif(degree == "ME"):
    if(exprience<5):
        print("salary is 50000")
    else:
        print("salary is 60000")
else:
    print("Invalide degree")
"""




# 2.7 WAP to check whether entered input is character,digit or special symbol Using ladder if-else. 
"""
inpData = (input("Enter Input : "))

if(inpData.isalpha()):
    print("entered input is character")
elif(inpData.isdigit()):
    print("entered input is digit")
else:
    print("entered input is special symbol")

"""




#-------------------------------------------- set 3------------------------------------------------------

# 3.1 WAP to find sum of N scanned numbers. 
"""
n = int(input("Enter number : "))
sum = 0

for i in range(n):
    sum += i 

print(f"sum of {n} is :",sum)

#output : 
# Enter number : 10
# sum of 10 is : 45

"""
# lll
# lslslsl


