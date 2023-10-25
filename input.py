age = int(input("Enter your age: "))

print(age)

if age < 3:
    print("You are still a toddler.")
elif age >= 3 and age < 13:
    print("You are a child.")
elif age >= 13 and age <= 19:
    print("You are a teenager.")
elif age >= 40:
    print("You are an adult.")
else:
    print("invalid input")