def stringManipulation(word):
    print(f"INPUT: {word}")
    print(f"OUTPUT: {word[::-1].upper()} ({len(word)} characters)")

word = input("Input a word: ")
stringManipulation(word)