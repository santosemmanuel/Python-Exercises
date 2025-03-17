while(True):
    try:
        print("Choose Operations [1] (+)Addition, [2] (-)Subtraction, [3] (*)Multiply, [4] (/)Divide")
        operations = int(input("Select From Options: "))
        
        number1 = int(input("Input first number: "))
        number2 = int(input("Input second number: "))
        
        if operations == 1:
            print(f"The result: {number1 + number2}")
        elif operations == 2:
             print(f"The result: {number1 - number2}")
        elif operations == 3:
             print(f"The result: {number1 * number2}")
        elif operations == 4:
             print(f"The result: {number1 / number2}")
        else:
            print("Not in the option please select from the option above")

        tryAgain = input("Do you want to try again [y] yes pr [n] no: ")

        if tryAgain.lower() == "n":
            break

    except ZeroDivisionError:
        print("Cannot Divide By Zero")    