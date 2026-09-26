# 16 - match case - harry bhai wala

x = int(input("Ek number daal 1 , 2 , tya 3 me se: "))

match x:
    case 1:
        print("tune ek dabaya , tu jeet gaya!")
    case 2:
        print(" tune  do dabaya, seconed position!")
    case 3:
        print(" tune teen dabaya , try again bro!")
    case _:
        print(" arey ye to list me hi nahi hai , 1-3 hi dal")

print(" ac 16 pe chale to lagti hai thandva jindigi jhandwa phir bhi hai ghamanddba")