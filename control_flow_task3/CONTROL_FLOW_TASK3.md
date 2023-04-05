# Task 3

### Loop Hello 10 Times

This statement prints hello 10 times.

```commandline
for num in range(10):
    print("hello")
```

Output
```commandline
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
```

### Names and List_Names

Create an empty list.

```commandline
list_names = []
```

This allows 3 different users to enter their name.

```commandline
for x in range(3):
    user_names = input("What is your name? ")
```

This if statement only allows user to enter characters. It also adds the name to the empty list created above.

```commandline
    if user_names.isalpha():
        list_names.append(user_names)
```

This else statement prints a sentence to let the user know what they entered is invalid.

```commandline
    else:
        print("This is invalid")
```

### New List and Lowercase

Created a new list.

```commandline
list_names_lower = []
```

### List of Numbers (Even)

Created a list of 8 numbers

```commandline
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
```

Iterating each number in the list created.
```
for num in list_of_numbers:
```

This checks to see the condition and prints out all the even numbers.
 ```
 if num % 2 == 0:
    print(f"This number is even: {num}")
 ```
