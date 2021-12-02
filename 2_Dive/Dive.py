forward = 0
depth = 0

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        parts = line.split(" ")
        if (parts[0] == "forward"):
            forward += int(parts[1])
        elif (parts[0] == "down"):
            depth += int(parts[1])
        elif (parts[0] == "up"):
            depth -= int(parts[1])

print(forward*depth)