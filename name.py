number = int(input("Give me a number:"))

if number < 0:
    print(f"{number} is negative")
elif number > 0:
    print(f"{number} is positive")
else:
    print(f"{number} is not a number")