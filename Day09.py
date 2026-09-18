# Day 9 typecasting in python

#  1 EXPLICT typecasting - hum khud karte hai

a = 10
b = 20.5
print(int(a) + int(b)) # 15+ 10 = 25
# int() se string number ban gaya

#  IMPLICIT typecasting - python khud kar deta hai
C = 10    #int
D = 2.5    #float
print(C + D) #python khud c float me convert kar deta hai
print(type(C + D)) # type dekho float ayega

#3 . check karne ke liye
x = "harry"
y = 40
print(type(x))
print(type(y))

print(int("34")+6) # 40