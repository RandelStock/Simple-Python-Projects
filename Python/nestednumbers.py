num = eval(input("Enter An Number : "))

if num % 2 == 0:
    print("That is an even number")
    if num ** 2:
        num1 = num ** 2
        print(num, "has a square of", num1)
    else:
        print(num, "has no square")
else:
    print("That Is an ODD Number")
    if num % 3 == 0:
        print(num, "is divisible by 3")
        if num ** 1.3:
            num2 = num ** 3
            print(num, "has a cube of", num2)
    else:
        print(num, "is not divisible by 3")


