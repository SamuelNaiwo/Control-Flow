# Control Flow Task 4

### Print 10 - 100

Initialising the variable
```commandline
x = 10
```

If the number is lower than 301 it will be true and loop around.

```commandline
while x < 301:
```

This will add 10 to x every time it loops around.

```commandline
print(x)
    x += 10
```

### Average Value

Initialising the variables.

```commandline
sum = 0
count = 0
```

This allows the user to enter a number 10 times.

```commandline
while count < 10:
    num = float(input('Enter a number: '))
```

This adds the numbers the user is entering together.

```commandline
sum += num
```

This counts how many times the user has entered a number.
```commandline
count += 1
```

Created a variable to take the sum of the numbers and divide by 10 to get the average.
```commandline
average = sum / 10

print(f'The average of these numbers is: {average}')
```