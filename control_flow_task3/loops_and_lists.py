# Loop says hello 10 times.

for num in range(10):
    print("hello")

# Names and list_names.

list_names = []

for x in range(3):
    user_names = input("What is your name? ")
    if user_names.isalpha():
        list_names.append(user_names)
    else:
        print("This is invalid")

# Turn names into lowercase and make a new list.

list_names_lower = []

for name in list_names:
    list_names_lower.append(name.lower())

# List of numbers and find if they're even.

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for num in list_of_numbers:
    if num % 2 == 0:
        print(f"This number is even: {num}")