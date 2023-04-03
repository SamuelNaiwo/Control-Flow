# Movie Ratings

### User Input
This first line ask the user of their age.
```
print("How old are you")
```

This then follows by allowing the user to enter their age.
```commandline
age = int(input())
```

### If, Elif and Else Statements

If the user inputs an age not between 1 and 117, it will ask them to try again.
```commandline
if age not in range(1, 117):
    print("Please enter a valid age between 1 and 117 ")
```

If the users age is 11 or under, they are only allowed to watch U and PG rated films.
```commandline
elif age <= 11:
    print("U and PG films are available")
```

If the users age is between 12 and 14, they are only allowed to watch U, PG and 12 rated films.
```commandline
elif age <= 14:
    print("U, PG, and 12 films are available")
```

If the users age is between 15 and 17, they are only allowed to watch U, PG, 12 and 15 rated films.
```commandline
elif age <= 17:
    print("U, PG, 12 and 15 films are available")
```

If the users age is 18 or over, they are allowed to watch all films available.
```commandline
else:
    print("All films are available")
```
