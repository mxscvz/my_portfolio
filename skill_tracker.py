
skill = input("What skill are you currently learning? ")
level = int(input("On a scale of 1-10, what is your level? "))
if level <= 3:
    print("Keep practicing! You'll get there.")
elif level <= 7:
    print("Great job! You're making progress.")
elif level <= 10:
    print("Awesome! You're mastering this skill.")
