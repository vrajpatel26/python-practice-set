def calc_sum(a,b):
    sum = a+b
    print(sum)

calc_sum(2,5)
calc_sum(6,5)
calc_sum(8,5)




def odd_even(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")

odd_even(2)
odd_even(7)


s = 0
e = 10

for num in range(s , e):
    print(num)

print("----------------------")

list = [1,4,9,16,25,36,49,64,81,100,36]

for num in list:
    print(num)


x = 36
idx=0
for num in list:
    if(num == x):
        print(idx)
    idx += 1

print("----------------------")

# num = 5
# for i in range(1,11):
#     print(num*i)
    # i+=1


# n = 5
# i = 1

# while(i<=10):
#     print(n*i)
#     i+=1

print("-------------------")

# num = 0
# for i in range(1,11):
#     num = num + i
    
# print("sum is :",num)


num = 0
i = 1
while(i<11):
    num = num + i
    i += 1

print(num)

print("------------------------")

num = 4
fact = 1
for i in range(1,num+1):
    fact*=i

print(fact)

