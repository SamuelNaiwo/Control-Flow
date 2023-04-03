# Even and Odd Number

### Select Number

The user selects any number they want

```
print("Please pick a number: ")
number = int(input())
```

### If and Else Statement

After the user inputs their number of choice, it will tell them if the number is even or odd.

```commandline
if (number % 2) == 0:
    print("The Number is even")
else:
    print("The number is odd")
```

# Number Guess

### Random Number

This selects a random number between 1 and 20 for the user to guess.

```commandline
import random

random_number = random.randint(1, 20)
```

### User Input

This allows the user to input their number

```commandline
user_guess = int(input("Guess a number between 1 and 20: "))
```

### While True

The while true allows it to loop forever until the number is guessed correctly.

```commandline
while True:
```

### If, Elif and Else

These will tell the user if the guess is too low, too high or if they have guessed correctly.

```commandline
    if user_guess < random_number:
        print("Guess is too low, try again")
        user_guess = int(input("Guess a number between 1 and 20: "))
    elif user_guess > random_number:
        print("Guess is too high, try again")
        user_guess = int(input("Guess a number between 1 and 20: "))
    else:
        print("You guessed right, well done!")
        break
```

# Fizz Buzz

### Number Range

This statement gives a list of numbers between 1 and 100.

```commandline
for number in range(1, 100):
```

### Multiples of 3 and 5

If the number is a multiple of 3 and 5, it will have the word "FizzBuzz" next to it.

```commandline
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz: " + str(number))
```

### Multiples of 3

If the number is a multiple of 3, it will have the word "Fizz" next to it.

```commandline
    elif number % 3 == 0:
        print("Fizz: " + str(number))
```

### Multiples of 5

If the number is a multiple of 5, it will have the word "Buzz" next to it.

```commandline
    elif number % 5 == 0:
        print("Buzz: " + str(number))
```

### Other Numbers

If the number is not a multiple of 3 or 5, it will just show the number.

```commandline
    else:
        print(number)
```