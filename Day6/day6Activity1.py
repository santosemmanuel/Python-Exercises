 #Create a Record Keeping App
users = {}

while (True):
    print("choose between this options")
    print("[A] Add Data")
    print("[B] Delete Data")
    print("[C] End")

    option = input("Choose: ")

    if option.lower() == 'a':
        key = input("Enter Key: ")
        value = input("Enter Value: ")

        users[key] = value

    elif option.lower() == 'b':
        key = input("Enter Key: ")

        del users[key]

    else:
        print("Thank you")
        break

    for key, value in users.items():
        print(f"{key}:{value}")
        
