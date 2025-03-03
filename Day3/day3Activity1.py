name = input("Name: ")
math = int(input("Math: "))
science = int(input("Science: "))
english = int(input("English: "))

average = float((math + science + english) / 3)

print(f"Average: {round(average, 2)}")

subject = ""

if math < 75 :
    subject = "But you need to re-enroll Math subject"
elif science < 75:
    subject = "But you need to re-enroll Science subject"
elif english < 75:
    subject = "But you need to re-enroll English subject"

if average >= 75:
    print("Congratulations! You passed the semester. " + subject)
else:
    print("Sorry, You Failed the semester")