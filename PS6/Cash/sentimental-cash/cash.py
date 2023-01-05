from cs50 import get_float

change = 0
count = 0

while change <= 0:
    change = get_float("Change owed: ")

cents = round(change * 100)

while cents > 0:
    if cents >= 25:
        cents -= 25
        count += 1
    elif cents >= 10:
        cents -= 10
        count += 1
    elif cents >=5:
        cents -= 5
        count += 1
    elif cents >=1:
        cents -= 1
        count += 1

print(count)
