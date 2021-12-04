bit = []
gamma = []
newlines = []
cplines = []


with open('input.txt') as f:
    lines = f.readlines()
    part = lines[0].split()
    print(lines)
    part = lines[0].split()
    

    cplines = lines
    
    for i in range(len(part[0])):
        print(i)
        for line in cplines:
            bit.append(int(line[i]))
        print(bit)
        # for oxygen gen, maxnum = max, minnum = min
        # for co2 scrubber, maxnum = min, minnum = max
        maxnum = max(set(bit), key = bit.count)
        minnum = min(set(bit), key = bit.count)
        # print(maxnum, minnum)

        newlines.clear()
        # print(cplines)
        for line in cplines:
            if (maxnum == minnum):
                # for oxygen gen, == 1
                # for co2 scrubber, == 0
                if (int(line[i]) == 1):
                    newlines.append(line)
                    pass
            elif (int(line[i]) == maxnum):
                newlines.append(line)
        
        bit.clear()

        cplines = newlines.copy()
        if (len(newlines) == 1):
            break
    # as set up this returns binary val of co2 scrubber    
    print(newlines)