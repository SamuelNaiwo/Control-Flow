# ## Even and Odd Number
#
# print("Please pick a number: ")
# number = int(input())
#
# if (number % 2) == 0:  # MODULO - Number divided by 2 has a remainder of 0
#     print("The Number is even")
# else:
#     print("The number is odd")
#
# ## Number Guess
#
# import random
#
# random_number = random.randint(1, 20)
# user_guess = int(input("Guess a number between 1 and 20: "))
#
# while True:
#     if user_guess < random_number:
#         print("Guess is too low, try again")
#         user_guess = int(input("Guess a number between 1 and 20: "))
#     elif user_guess > random_number:
#         print("Guess is too high, try again")
#         user_guess = int(input("Guess a number between 1 and 20: "))
#     else:
#         print("You guessed right, well done!")
#         break

# Fizz Buzz

for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz: " + str(number))
    elif number % 3 == 0:
        print("Fizz: " + str(number))
    elif number % 5 == 0:
        print("Buzz: " + str(number))
    else:
        print(number)