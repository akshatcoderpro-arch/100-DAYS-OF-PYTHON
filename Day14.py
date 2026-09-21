# Day 14 - if else condition

# Example 1 : simple if-else
age = 18
print("Example 1 - voting check") 
print("tumhari age hai" , age) 

if age >= 18:
    print("tu vote de sakta hai")
else:
    print("tu vote nahi de sakta hai")

#  print() #khali line ke liye

# example 2: elif: bahut sari condition
marks = 85
print("example 2 result check")
print("tumhare marks hai:" , marks) 

if marks >= 90:
    print("Grade A - topper hai tu!")
elif marks>= 80:
    print("Grade B - bahut badhiya")    
elif marks >= 60:
    print("Grade C - pass hai")
else:
    print("fail hai bhai padh le")  
print()

# example 3 : user se input lena - real wala code
print("example 3 input wala")
num = int(input("ek number daal:"))

if num > 0:
    print(" ye positive number hai")
elif num < 0:
    print("ye negative number hai")
else:
    print("ye zero hai")

print()

# 4 .  nested if - if ke andar if
print("example 4 - nested if")
age2 = 25
has_licence = True

if age2>= 18:
    print("18 se zayda hai")
    if has_licence == True:
       print(" aur licence bhi hai, gaadi chala sakta hai ")
    else:
        print("licence nahi hai nahi chala sakta")
else:
    print("abhi chota hai tu")

