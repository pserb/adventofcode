for line in open('input.txt'):
    inital = line.split(",")
    numinit = [int(x) for x in inital]

def solve(init, days):
    for i in range(days):
        for j in range(len(init)):
            if init[j] == 0:
                init[j] = 6
                init.append(8)
            else:
                init[j] -= 1
    return len(init)

# print(solve(numinit, 80))
# print(solve(numinit, 256))
print(len(numinit))