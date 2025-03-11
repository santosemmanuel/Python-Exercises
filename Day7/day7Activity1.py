import random

# First Name List
first_names = ["Adrian", "Bianca", "Carlo", "Denise", "Ethan", "Francesca", "Gabriel", "Hannah", "Ivan", "Jasmine"]

# Middle Name List
middle_names = ["Cruz", "Reyes", "Santos", "Dela Cruz", "Navarro", "Villanueva", "Mendoza", "Ramos", "Torres", "Gonzales"]

# Last Name List
last_names = ["Castillo", "Fernandez", "Gutierrez", "Hernandez", "Bautista", "Soriano", "Alvarado", "De Leon", "Pineda", "Velasco"]

generatedNameList = []

while(True):
    option = input("Do you want to generate a new name [y] yes or [n] no:")

    if option.lower() == 'n':
        if len(generatedNameList) != 0:
            for names in generatedNameList:
                print(names)
        else:
            print("no item(s) in the list")
        break
    elif option.lower() == 'y':
        generatedName = f"{first_names[random.randint(0,9)]} {middle_names[random.randint(0,9)]} {last_names[random.randint(0,9)]}"
        generatedNameList.append(generatedName)
        print(f"Congratulations! Your new name is {generatedName}")




