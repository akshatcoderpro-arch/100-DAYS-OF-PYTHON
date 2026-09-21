# Day 13 - String methods in python

# 1 . upper() or lower() - bada karna / chota karna
a = "Harry"
print(a.upper()) #HARRY sab kar dega
print(a.lower()) # harry sab chota kar dega

# 2 . strip() or rstrip() - space hatana
b = "  hello world!!!"
print(b.strip()) # aage peeche ka space hata dega
c = "hello!!!   "
print(c.rstrip("!)")) # sirfpeeche ka ! hata dega ~hello 

# 3 . replace() - badalna
str1 = " Silence is golden"
print(str1.replace("Silence" , "Money")) # Money is golden

# 4. split() - todna
str2 = "apple , banana cherry"  
print(str2.split(" ,")) # list bana dega [apple , banana , cherry]

# 5 . capitalize() - pehla akshar bada
str3 = "hello python"
print(str3.capitalize()) # Hello python

# 6 . center() - beech me laana
str4 = "Welcome"
print(str4.center(20, "-")) # ------Welcome----------

# 7 . count() - ginti karna
str5 = "abrakadabra"
print(str5.count("a")) # kitni baar "a" aaya - 5

# 8 .endswith() - check karna last me kya
str6 = "Hello world."
print(str6.endswith(".")) # true

# 9 . find()or index() - dhoondna
str7 = " He is dancing"
print(str7.find("is")) # 3 - mil gaya to position dega
print(str7.find("xyz")) # -1 - nahi mila to -1 dega
# print(str7.index("xyz")) # ye eror de dega agar nhi mila

# 10 .isalnum(), isalpha(), islower() etc.
str8 = "Welcometopython" 
print(str8.isalnum()) # true sirf A-Z , A-Z, 0-9 HAI?
print(str8.isalpha()) # true - sirf A-Z, a-z hai?
print("hello".islower()) # true sab chota hai kya?
print("HELLO".isupper()) # true - sab bada hai kya?

# 11 . isspace() or istitle()
print("   ".isspace()) # true- sirf space hai kya?
print("HELLO".isupper()) # true - har woed ka pehla bada hai kya?

# 12 . startswith()
print("python is fun".startswith("Python")) # TRUE 
