prevsum = 0
currentsum = 0
count = 0

with open('input.txt') as f:
    lines = f.readlines()
    # print(len(lines))
    for i in range(len(lines)-2):
        currentsum = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        if currentsum > prevsum:
            count += 1
        prevsum = currentsum
print(count-1)