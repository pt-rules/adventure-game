number = 0
total = 0
while number < 1001:
    number += 1
    if number%3 == 0:
        total += number
number = 0
while number < 1000:
    number += 1
    if number%5 == 0:
        if number%3 == 0:
            print(number)
            total += number
        else:
            total += number
print(total)