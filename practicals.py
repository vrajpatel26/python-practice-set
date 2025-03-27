
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


# 2.2 Write a Python program to print Fibonacci series up to n terms. 
"""
num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
"""

#3.3 WAP to find the reverse of given numbers (Example2564-4652).
"""
num = 2564
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(reverse)

"""
# 3.4 WAP to check whether entered number is prime or not. 

"""
num = int(input("Enter a number: "))


if num <= 1:
    print(f"{num} is not a prime number.")
elif num == 2:
    print(f"{num} is a prime number.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")

"""

#3.5 WAP to print all eve numbers between 1 to n except the numbers Divisible by 6. 
"""
num = int(input("Enter number : "))

for i in range(1,num+1):
    if(i % 6 == 0):
        continue
    print(i)

  """  


#6.6 Write a python program to check whether given number is Armstrong or not. 
"""
num = int(input("Enter a number: "))

num_digits = len(str(num))

sum_of_digits = sum(int(digit) ** num_digits for digit in str(num))

if sum_of_digits == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

"""

#3.7 Write a python program to check whether given number is Palindrome or not. 
"""
num = int(input("Enter a number: "))

# Convert the number to a string and reverse it
reverse_num = str(num)[::-1]

if str(num) == reverse_num:
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is not a Palindrome number.")

"""


#3.8 

# 1
# 12
# 123
# 1234
# 12345


"""# Number of rows
n = 5

# Loop to print the pattern
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()  # Move to the next line
"""


# *****
# ****
# ***
# **
# *


n = 5

# Loop to print the pattern
for i in range(n, 0, -1):  #Outer loop starts from n and decreases to 1.
    for j in range(i):
        print("*", end="")
    print()  # Move to the next line