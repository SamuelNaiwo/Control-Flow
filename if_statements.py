# if, elif and else

# if
age = 18
if age >= 18:
    print("You are allowed to buy a ticket for this movie")
# elif
elif age < 18:
    print("Sorry, you're not old enough")

film_rating = "universal"

if film_rating.lower() == "universal":
    print("All ages can watch this movie")
elif film_rating.lower() == "pg":
    print("Parental guidance recommended")
elif film_rating.lower() == "12":
    print("Must be at least 12 years old")
elif film_rating.lower() == "15":
    print("Must be at least 15 years old")
elif film_rating.lower() == "18":
    print("Must be at least 18 years old")
else:
    print("This is not a correct rating, please us universal, pg, 12, 15 or 18")

