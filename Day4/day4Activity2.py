while(True):
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

    print(f"The sum of {num1} and {num2} is {num1 + num2}")

    option = input("Do you want to try again? Y/y if yes N/n if no: ")

    if option.lower() == "y":
        continue
    elif option.lower() == "n":
        print("Thank you!")
        break