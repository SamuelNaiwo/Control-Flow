print("How old are you")
age = int(input(range))

if age not in range(1, 117):
    print("Please enter a valid age between 1 and 117 ")
elif age <= 11:
    print("U and PG films are available")
elif age <= 14:
    print("U, PG, and 12 films are available")
elif age <= 17:
    print("U, PG, 12 and 15 films are available")
else:
    print("All films are available")