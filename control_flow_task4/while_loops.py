# Print 10 - 100
x = 10

while x < 301:
    print(x)
    x += 10

# Average Value
sum = 0
count = 0

while count < 10:
    num = float(input('Enter a number: '))
    sum += num
    count += 1

average = sum / 10

print(f'The average of these numbers is: {average}')