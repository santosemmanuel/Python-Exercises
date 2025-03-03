
wordBank = []

while(True):
    word = input("Enter a word: ")
    wordBank.append(word)

    option = input("Do you want to try again? Y/y if yes N/n if no: ")

    if option.lower() == "y": 
        continue
    elif option.lower() == "n":
        for value in wordBank:
            print(value)

        print(f"Total Number of words: {len(wordBank)}")
        break


