# Day 12 - string slicing & operations and string
# Video 12 - code with harry

# 1 . Lenght nikalna - len() function
fruit = "Mango"
len1 = len(fruit)
print("Mango is a" , len1 , "letter word.")

# 2 .String ko array ki tarh samjhana
pie = "applepie"
# Index: A p p l e P i e
# pos: 0 1 2 3 4 5 6 7
# neg: -8 -7 -6 -5 -4 -3 -2 -1

print(pie[:5]) # slicing from start ~ APPLE
print(pie[5:]) # slicing till end~ piew
print(pie[2:6]) # slicing in between
print(pie[-8:]) # slicing with negative index ~ apple pie
print(pie[-3:]) # last 3 letters ~ pie

print(pie[6]) # single charecter at index ~ pir

# 3 . loop through string
alphabets = "ABCDE"
for i in alphabets:
    print(i)