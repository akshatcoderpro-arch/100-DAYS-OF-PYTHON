# Day 15 - Exercise 2: good morning sir
# harry bhai ka exercise time ke hisab se great karna hai

import time # time module import kiya , isse current time lagega

timestamp = time.strftime('%H: %M: %S:')
# YE LINE CURRENT TIME KO HOUR MINUTE SECOND FORMAT ME DEGI
# jaise 14:30:00 matlab dopahar ke 2:30 baj rahe hai

hour = int(time.strftime('%H')) # sirf hour nikal liya or int me convert kasr diya
# %H ka matlab 24 hour format me hour(0 se 23 tak)

print(f"abhi hour ho raha hai: {hour} baje")
# ye check karne ke liye likha hai ki abhi kitna baj raha hai

# ab if-else-elif ka khel shuru - yahi main logic hai

if(hour >= 5 and hour < 12):
    # agar time subah 5 se 212 ke beech hai
    print(" Good morning sir!")

elif(hour >= 12 and hour <17):
    # agar time dopahar 12 se 5(17 baje) tak hai
    ("Good afternoon sir!")

elif(hour >= 17 and hour < 21):
    #  agar time shaam 5 se 9 (21 baje ) tak hai
    print("Good evening sir!")

else:
    # bacha hua time raat 9 se subah 5 baje tak
    # 21,22 , 23 , 0, 1 , 2 , 3 , 4 
    print("Good night sir!")

# ---Extra knowledge ---
# time.strftime('%M) SE MINUTE milega
# tme.strftime ('%S) se seconed milega
#  time.strftime(' %H , %M , %S)  se pura time milega
# 
print(" code complete! Exercise done.")
