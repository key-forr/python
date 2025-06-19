while True:
    try:
        score: int = int(input("What's your grade? "))

        if type(score) == int:
            break
    except ValueError:
        print("Enter again!")

if score > 100 or score < 0:
    print("Great is not defined")
elif 90 <= score <= 100:
    print("Great 10.")
elif 80 <= score < 90:
    print("Great 9.")
elif 70 <= score < 80:
    print("Great 8.")
elif 60 <= score < 70:
    print("Great 7.")
elif 50 <= score < 60:
    print("Great 6.")
else:
    print("Great is less than 6")


if score >= 90:
    print("Great 10.")
elif score >= 80:
    print("Great 9.")
elif score >= 70:
    print("Great 8.")
elif score >= 60:
    print("Great 7.")
elif score >= 50:
    print("Great 6.")
else:
    print("Great is less than 6")