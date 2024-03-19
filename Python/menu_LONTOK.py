def menu():
    print("<<-------------------------------------->>")
    print("Select your option from the menu >> ")
    print("1. Printing in Python")
    print("2. Variable Definition in Python")
    print("3. Operators in Python")
    print("4. Python Conditions and If statements in Python")
    print("5. Loop in Python")
    print("6. Functions in Python")
    print("7. Arrays in Python")
    print("8. Dictionary in Python")
    print("9. Exit Program")
    print("<<-------------------------------------->>")

    while True:
        choice = int(input("Select An Option >>>"))
        if choice == 1:
            choice1()
            continue

        elif choice == 2:
            choice2()
            continue

        elif choice == 3:
            choice3()
            continue

        elif choice == 4:
            choice4()
            continue

        elif choice == 5:
            choice5()
            continue
        elif choice == 6:
            choice6()
            continue
        elif choice == 7:
            choice7()
            continue
        elif choice == 8:
            choice8()
            continue

        elif choice == 9:
            print("Thank You For Using The Fundamentals Menu",name)
            break

        else:
            print("Invalid input!")


def menu1():
    print("<<-------------------------------------->>")
    print("Select your option from the menu >> ")
    print("1. Printing in Python")
    print("2. Variable Definition in Python")
    print("3. Operators in Python")
    print("4. Python Conditions and If statements in Python")
    print("5. Loop in Python")
    print("6. Functions in Python")
    print("7. Arrays in Python")
    print("8. Dictionary in Python")
    print("9. Exit Program")
    print("<<-------------------------------------->>")



def suggested1():
    print("Suggest Next Topic >>> ")
    print("1. Variable Definition")
    print("2. Operators in Python")
    print("3. Back To Main Menu")

    while True:
        choice = int(input("Suggested Options >>> "))
        if choice == 1:
            choice2()
        elif choice == 2:
            choice3()
        elif choice == 3:
            print("Welcome", name, "Back To The Main Menu")
            break
        else:
            print("Invalid Option")


def suggested2():
    print("Suggest Next Topic >>> ")
    print("1. Operators in Python")
    print("2. Conditional in Python")
    print("3. Back To Main Menu")

    while True:

        choice = int(input("Suggested Options >>> "))
        if choice == 1:
            choice3()
        elif choice == 2:
            choice4()
        elif choice == 3:
            print("Welcome", name, "Back To The Main Menu")
            break
        else:
            print("Invalid Option")


def suggested3():
    print("Suggest Next Topic >>> ")
    print("1. Conditional in Python")
    print("2. Loop in Python")
    print("3. Back To Main Menu")

    while True:

        choice = int(input("Suggested Options >>> "))
        if choice == 1:
            choice4()
        elif choice == 2:
            choice5()
        elif choice == 3:
            print("Welcome", name, "Back To The Main Menu")
            break
        else:
            print("Invalid Option")


def suggested4():
    print("Suggest Next Topic >>> ")
    print("1. Loop in Python")
    print("2. Functions in Python")
    print("3. Back To Main Menu")

    while True:

        choice = int(input("Suggested Options >>> "))
        if choice == 1:
            choice5()
        elif choice == 2:
            choice6()
        elif choice == 3:
            print("Welcome", name, "Back To The Main Menu")
            break
        else:
            print("Invalid Option")


def suggested5():
    print("Suggest Next Topic >>> ")
    print("1. Functions in Python")
    print("2. Arrays in Python")
    print("3. Back To Main Menu")

    while True:

        choice = int(input("Suggested Options >>> "))
        if choice == 1:
            choice6()
        elif choice == 2:
            choice7()
        elif choice == 3:
            print("Welcome", name, "Back To The Main Menu")
            break
        else:
            print("Invalid Option")


def suggested6():
    print("Suggest Next Topic >>> ")
    print("1. Arrays in Python")
    print("2. Dictionary in Python")
    print("3. Back To Main Menu")

    while True:

        choice = int(input("Suggested Options >>> "))
        if choice == 1:
            choice7()
        elif choice == 2:
            choice8()
        elif choice == 3:
            print("Welcome", name, "Back To The Main Menu")
            break
        else:
            print("Invalid Option")


def suggested7():
    print("Suggest Next Topic >>> ")
    print("1. Dictionary in Python")
    print("2. Printing in Python")
    print("3. Back To Main Menu")

    while True:

        choice = int(input("Suggested Options >>> "))
        if choice == 1:
            choice8()
        elif choice == 2:
            choice1()
        elif choice == 3:
            print("Welcome", name, "Back To The Main Menu")
            break
        else:
            print("Invalid Option")


def suggested8():
    print("Suggest Next Topic >>> ")
    print("1. Printing in Python")
    print("2. Variable Definition")
    print("3. Back To Main Menu")

    while True:

        choice = int(input("Suggested Options >>> "))
        if choice == 1:
            choice1()
        elif choice == 2:
            choice2()
        elif choice == 3:
            print("Welcome", name, "Back To The Main Menu")
            break
        else:
            print("Invalid Option")


def choice1():
    print("Welcome", name, "TO The Printing in Python...")
    print("----------------------------")
    print("The print() function prints the specified message to the screen, or other standard output device. ")
    print("The message can be a string, or any other object, the object will be converted into a string before "
          "written to the screen.")
    print("----------------------------")
    print("For Example: print('Hello, World!')")
    print("Try The Example")

    while True:
        hello = input()
        hello1 = "print('Hello, World!')"
        if hello != hello1:
            print("Please Try Again >>")
        elif hello == hello1:
            print("Hello, World!")
            print("Good Job!")
            suggested1()
            break
        else:
            print("INVALID")


def choice2():
    print("Welcome", name, "TO The Variable Definition in Python...")
    print("----------------------------")
    print("A Python variable is a symbolic name that is a reference or pointer to an object. ")
    print("----------------------------")
    print("Example: x = variable")
    print("variable")
    print("Try The Example")
    while True:
        variable = input()
        variable1 = "x = Variable"
        variable2 = input()
        variable3 = "print(x)"

        if variable != variable1 and variable2 != variable3:
            print("Please Try Again >> ")
        elif variable == variable1 or variable2 == variable3:
            print("variable")
            print("Good Job!")
            suggested2()
            break
        else:
            print("Invalid")


def choice3():
    print("Welcome", name, "TO The Operators in Python...")
    print("----------------------------")
    print("Operators are used to perform operations on variables and values.")
    print("There are different type's of operators")
    print(">Arithmetic operators<", "\n>Assignment operators<", "\n>Comparison operators<", "\n>Logical operators<")
    print("----------------------------")
    print(
        "Python Arithmetic Operators\n+ = Addition,\n- = Subtraction\n* = Multiplication\n/ = Division\n% = Modulus\n** = ""Exponentiation\n// = Floor Division ")
    print("----------------------------")
    print("Python Assignment Operators\n(=) For Example >>> x =5 : is Same as >>> x =5"
          "\n(+=) For Example >>> x +=3 : is Same as >>> x = x + 3"
          "\n(-=) For Example >>> x -=3 : is Same as >>> x = x - 3")
    print("----------------------------")
    print("Python Comparison Operators\nOperator >>> (==) : Name >>> Equal : Example >>> x == y"
          "\nOperator >>> (!=) : Name >>> Not Equal : Example >>> x != y"
          "\nOperator >>> (>) : Name >>> Greater Than  : Example >>> x > y")
    print("Operator >>> (<) : Name >>> Less Than : Example >>> x < y"
          "\nOperator >>> (>=) : Name >>> Greater Than Or Equal To  : Example >>> x >= y"
          "\nOperator >>> (<=) : Name >>> Less Than Or Equal To : Example >>> x <= y")
    print("----------------------------")
    print("Python Logical Operators\nOperator >>> (and) : Description >>> "
          "Returns True if both statements are true : Example >>> x < 5 and  x < 10"
          "\nOperator >>> (or) : Description >>> Returns True if one of the statements is true : Example >>> x < 5 or x < 4"
          "\nOperator >>> (not) : Description >>> Reverse the result, returns False if the result is true : Example >>> not(x < 5 and x < 10)")
    print("----------------------------")
    while True:
        next = input("Type Yes To Continue >>> ")
        yes = "Yes"
        if next != yes:
            print("Thank You For Using The Program", name)

        elif next == yes:
            print("Thank You For Continuing The Program", name)
            suggested3()
            break
        else:
            print("Invalid Option")


def choice4():
    print("Welcome", name, "Python Conditions and If statements in Python...")
    print("----------------------------")
    print("Python supports the usual logical conditions from mathematics:")
    print("----------------------------")
    print("Equals: a == b"
          "\nNot Equals: a != b"
          "\nLess than: a < b"
          "\nLess than or equal to: a <= b"
          "\nGreater than: a > b"
          "\nGreater than or equal to: a >= b")
    print("These conditions can be used in several ways, most commonly in 'if statements'' and loops."
          "\n----------------------------"
          "\nAn 'if statement' is written by using the if keyword.")
    print("For Example >>>\nIf statement:")
    print("a = 33\nb = 200\nif b > a:\n\tprint('b is greater than a')\nb is greater than a")
    print("----------------------------")
    print("Elif\nThe elif keyword is Python's way of saying "
          "'if the previous conditions were not true, then try this condition'.")
    print("For Example >>>"
          "\na = 33\nb = 33\nif b > a:\n\tprint('b is greater than a')\nelif a == b:\n\tprint('a and b are equal')"
          "\na and b are equal")
    print("----------------------------")
    print("Else\nThe else keyword catches anything which isn't caught by the preceding conditions.")
    print("For Example >>>\na = 200\nb = 33"
          "\nif b > a:\n\tprint('b is greater than a')"
          "\nelif a == b:\n\tprint('a and b are equal'')"
          "\nelse:\n\tprint('a is greater than b')"
          "a is greater than b")
    print("----------------------------")
    print("Nested If\nYou can have if statements inside if statements, this is called nested if statements.")
    print("For Example >>>\nx = 41"
          "\nif x > 10:"
          "\n\tprint('Above ten,')"
          "\n\tif x > 20:"
          "\n\t\tprint('and also above 20!')"
          "\n\telse:"
          "\n\t\tprint('but not above 20.')")
    print("Above ten"
          "\nand also above 20!")
    print("----------------------------")
    while True:
        next = input("Type Yes To Continue >>> ")
        yes = "Yes"
        if next != yes:
            print("Thank You For Using The Program", name)

        elif next == yes:
            print("Thank You For Continuing The Program", name)
            suggested4()
            break
        else:
            print("Invalid Option")


def choice5():
    print("Welcome", name, "Loop in Python...")
    print("----------------------------")
    print("A for loop is used for iterating over a sequence "
          "(that is either a list, a tuple, a dictionary, a set, or a string).")
    print("This is less like the for keyword in other programming languages, "
          "\nand works more like an iterator method as found in other object-orientated programming languages.")
    print("With the for loop we can execute a set of statements,\nonce for each item in a list, tuple, set etc.")
    print("----------------------------")
    print("For Example >>> ")
    print("fruits = ['apple' , 'banana' , 'grapes']")
    print("for x in fruits:\nprint(x)\napple\nbanana\ngrapes")
    print("----------------------------")
    print("Looping Through a String\nEven strings are iterable objects, they contain a sequence of characters:")
    print("For Example >>>\nLoop through the letters in the word 'banana':\nfor x in 'banana'"
          "\nprint(x)\nb\na\nn\na\nn\na")
    print("----------------------------")
    print("The Break Statement"
          "\nWith the break statement we can stop the loop before it has looped through all the items:")
    print("fruits = ['apple' , 'banana' , 'grapes']")
    print("for x in fruits:\n\tprint(x)\n\tif x == 'banana':\n\t\tbreak\napple\nbanana")
    print("Exit the loop when x is 'banana'', but this time the break comes before the print:")
    print("fruits = ['apple' , 'banana' , 'grapes']")
    print("for x in fruits:\n\tif x == 'banana':\n\t\tbreak\n\tprint(x)\napple")
    print("----------------------------")
    print("The continue Statement"
          "With the continue statement we can stop the current iteration of the loop, \nand continue with the next:")
    print("For Example >>>\nDo not print banana:")
    print("fruits = ['apple' , 'banana' , 'grapes']")
    print("for x in fruits:\n\tif x == 'banana':\n\t\tcontinue\n\tprint(x)\napple\ngrapes")
    print("----------------------------")
    print("The range() Function"
          "\nTo loop through a set of code a specified number of times, we can use the range() function,"
          "\nThe range() function returns a sequence of numbers, "
          "starting from 0 by default, \nand increments by 1 (by default), and ends at a specified number.")
    print("For Example >>>\nUsing the range() function:")
    print("for x in range(6):\n\tprint(x)\n0\n1\n2\n3\n4\n5")
    print("#Note that range(6) is not the values of 0 to 6, but the values 0 to 5.")
    print("----------------------------")
    print("Else in For Loop"
          "\nThe else keyword in a for loop specifies a block of code to be executed when the loop is finished:")
    print("For Example >>>\nPrint all numbers from 0 to 5, and print a message when the loop has ended:")
    print("for x in range(6):\n\tprint(x)\nelse:\n\tprint('Finally Finished!')\n0\n1\n2\n3\n4\n5\nFinally Finished!")
    print("----------------------------")
    print("Nested Loops\nA nested loop is a loop inside a loop."
          "\nThe 'inner loop' will be executed one time for each iteration of the 'outer loop':")
    print("For Example >>>\nPrint each adjective for every fruit:")
    print("adj = ['red', 'big', 'tasty']\nfruits = ['apple' , 'banana' , 'grapes']"
          "\nfor x in adj:\n\tfor y in fruits:\n\t\tprint(x,y)")
    print("red apple\nred banana\nred grapes\nbig apple"
          "\nbig banana\nbig grapes\ntasty apple\ntasty banana\ntasty grapes")
    print("----------------------------")
    while True:
        next = input("Type Yes To Continue >>> ")
        yes = "Yes"
        if next != yes:
            print("Thank You For Using The Program", name)

        elif next == yes:
            print("Thank You For Continuing The Program", name)
            suggested5()
            break
        else:
            print("Invalid Option")


def choice6():
    print("Welcome", name, "Functions in Python...")
    print("----------------------------")
    print("A function is a block of code which only runs when it is called."
          "\nYou can pass data, known as parameters, into a function."
          "\nA function can return data as a result.")
    print("----------------------------")
    print("Creating a Function"
          "\nIn Python a function is defined using the def keyword:")
    print("For Example >>>"
          "\ndef my_function():"
          "\n\tprint('Hello from a function'')"
          "\nmy_function()"
          "\nHello from a function")
    print("----------------------------")
    while True:
        next = input("Type Yes To Continue >>> ")
        yes = "Yes"
        if next != yes:
            print("Thank You For Using The Program", name)

        elif next == yes:
            print("Thank You For Continuing The Program", name)
            suggested6()
            break
        else:
            print("Invalid Option")


def choice7():
    print("Welcome", name, "Arrays in Python...")
    print("----------------------------")
    print("Arrays\nArrays are used to store multiple values in one single variable:")
    print("For Example >>>"
          "\nCreate an array containing car names:"
          "\ncars = ['Ford', 'Volvo', 'BMW']")
    print("What is an Array?"
          "\nAn array is a special variable, which can hold more than one value at a time."
          "\nIf you have a list of items (a list of car names, for example), "
          "storing the cars in single variables could look like this:")
    print("car1 = 'Ford'"
          "\ncar2 = 'Volvo'"
          "\ncar3 = 'BMW'")
    print("However, what if you want to loop through the cars and find a specific one? "
          "And what if you had not 3 cars, but 300?")
    print("The solution is an array!"
          "An array can hold many values under a single name, "
          "and you can access the values by referring to an index number.")
    print("----------------------------")
    while True:
        next = input("Type Yes To Continue >>> ")
        yes = "Yes"
        if next != yes:
            print("Thank You For Using The Program", name)

        elif next == yes:
            print("Thank You For Continuing The Program", name)
            suggested7()
            break
        else:
            print("Invalid Option")


def choice8():
    print("Welcome", name, "Dictionary in Python...")
    print("----------------------------")
    print("Python Dictionaries\nDictionaries are used to store data values in key:value pairs."
          "\nA dictionary is a collection which is ordered*, changeable and do not allow duplicates."
          "\nDictionaries are written with curly brackets, and have keys and values:")
    print("----------------------------")
    print("For Example >>>\nCreate and print a dictionary:"
          "\nthis_dict = {"
          "\n\t'brand': 'Ford',"
          "\n\t'model': 'Mustang',"
          "\n\t'year': 1964"
          "\n}"
          "\nprint(this_dict)"
          "\n{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}")
    print("----------------------------")
    while True:
        next = input("Type Yes To Continue >>> ")
        yes = "Yes"
        if next != yes:
            print("Thank You For Using The Program", name)

        elif next == yes:
            print("Thank You For Continuing The Program", name)
            suggested8()
            break
        else:
            print("Invalid Option")


name1 = input("Enter Your Name :>>> ")
name = name1.upper()
print("Welcome ", name, "To The FUNDAMENTALS OF PYTHON")

while True:

    menu1()
    choice = int(input("Select An Option >>>"))
    if choice == 1:
        choice1()
        continue

    elif choice == 2:
        choice2()
        continue

    elif choice == 3:
        choice3()
        continue

    elif choice == 4:
        choice4()
        continue

    elif choice == 5:
        choice5()
        continue
    elif choice == 6:
        choice6()
        continue
    elif choice == 7:
        choice7()
        continue
    elif choice == 8:
        choice8()
        continue

    elif choice == 9:
        print("Thank You For Using The Fundamentals Menu",name)
        break
    else:
        print("Invalid input!")