def student(name, math, english, science):
    average = (math + english + science) / 3
    print(f"{name}'s grade (Math={math}, Science={science}, English={english}) and the average is {average:.2f}")

student("Emmanuel", 80, 90, 79)