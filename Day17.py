# Day 17 - for loops - full video code

print ("--- 1. simple for loop range(5 ---)") 
# ye 0 se 4 tak chalegha (5 baar) 
for i in range(5): 
    print(i)

print("\n--- 2. range(start , stop) ---") 
#  1 se 9 tak 
for i in range(1 , 10):
    print(i) 

print("\n--- 3. range (start , stop , step) ---") 
# 1 se 10tak , 2-2 step se
for i in range(1 , 12 , 2): 
    print(i)

print("\n--- 4. String par loop ---")
name = "Akshat"
for char in name:
    print(char)

print("\n--- 5. list par loop(sabse zyada kaam ka ) ---") 
friends = ["Aman" , "Rahul" , " GORAKHPUR Wala dost"]
for dost in friends:
    print(dost) 
    # andar ek aur loop
    for letter in dost:
        print(letter) 

print("\n --- else ke saath for loop ---") 
# ye harry ne last me important bataya tha 
for i in range(3):
    print(i)
else:
    print(" loop pura khatam hogaya ab else chalega") 