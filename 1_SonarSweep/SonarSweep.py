prev = 0
count = 0

with open('input.txt') as f:
    lines = f.readlines()
    for num in lines:
        if int(num) > prev:
            count += 1
        prev = int(num)
print(count-1)