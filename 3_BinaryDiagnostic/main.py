bit = []
gamma = []
ans = ""

with open('input.txt') as f:
    lines = f.readlines()
    part = lines[0].split()
    print(part)
    for i in range(len(part[0])):
        for line in lines:
            bit.append(int(line[i]))
            
        gamma.append(max(set(bit), key = bit.count))
        bit.clear()

for g in gamma:
    ans += str(g)
print(ans)
print(int(ans,2))
