a=int(input("enter a number "))
match a:
    case 1:
        print("case is 1")
    case 2:
        print("case is 2")
    case 13:
        print("case is 13")
    case 22:
        print("case is 22")
    case _:
        print("df")

# quick quiz: write a python program to print table of number while lies between 1 to 10
num = int(input("Enter a number (1-10): "))

match num:
    case n if 1 <= n <= 10:
        print(f"{n} x 1 = {n*1}")
        print(f"{n} x 2 = {n*2}")
        print(f"{n} x 3 = {n*3}")
        print(f"{n} x 4 = {n*4}")
        print(f"{n} x 5 = {n*5}")
        print(f"{n} x 6 = {n*6}")
        print(f"{n} x 7 = {n*7}")
        print(f"{n} x 8 = {n*8}")
        print(f"{n} x 9 = {n*9}")
        print(f"{n} x 10 = {n*10}")

    case _:
        print("Invalid number")