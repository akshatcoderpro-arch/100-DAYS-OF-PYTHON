# DAY 11 - STRINGS IN PYTHON - HAR HAR MAHADEV

print("day 11 strings")

# 1 . strings kya hai? - double ye single quote me
name = "AKSHAT"
city = "kanpur nagar"
print (name)
print (city)

# 2 . quote ke andar quote kaise likhe
# trick - bahar single yo aznder double , bahar double to ander single
print('he said " i want to eat an apple".')
print('he said " i am from kanpur nagar".')

# 3 . multiline string - triple quote se
about = """har har mahadev,
mera name akshat hai,
 main 100 days of python kar raha hu,"""
print (about)

# 3 . string ek array hai - indexing 0 se start hoti hai
# A K S H A T
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# 5 . for loop se har letter alag print karna
print("for loop se name print:")
for charecter in name:
    print(charecter)

    # 6 . favourite god wala example
    god = "Mahakal"
    print(f"enter your favourite god name : {god}")
    print("har har mahadev")
    print("akshat lage raho paaji")