import numpy as np

Lx1,Lx2,Ly1,Ly2 = [],[],[],[]

x1,y1,x2,y2 = 0,0,0,0
spx1,spx2,spy1,spy2 = 0,0,0,0

with open('test.txt') as f:
    lines = f.readlines()
    for line in lines:
        lsplit = line.split()
        Lx1.append(int(lsplit[0].split(",")[0]))
        Ly1.append(int(lsplit[0].split(",")[-1]))
        Lx2.append(int(lsplit[-1].split(",")[0]))
        Ly2.append(int(lsplit[-1].split(",")[-1]))

    if max(Lx1) > max(Lx2):
        xMax = max(Lx1)
    else:
        xMax = max(Lx2)

    if max(Ly1) > max(Ly2):
        yMax = max(Ly1)
    else:
        yMax = max(Ly2)

    points = np.zeros((xMax+1, yMax+1), dtype=int)

    for line in lines:
        splitl = line.split()
        x1 = int(splitl[0].split(",")[0])
        y1 = int(splitl[0].split(",")[-1])
        x2 = int(splitl[-1].split(",")[0])
        y2 = int(splitl[-1].split(",")[-1])

        if (x1 == x2):
            spy1 = y1
            spy2 = y2

            if (y1 > y2):
                spy2 = y1
                spy1 = y2
            if (y1 == y2):
                spy2 = y2 + 1
                spy1 = y1
        
            for i in range(spy1,spy2+1):
                points[i][x1] += 1

        elif (y1 == y2):
            spx1 = x1
            spx2 = x2

            if (x1 > x2):
                spx2 = x1
                spx1 = x2
            if (x1 == x2):
                spx2 = x2 + 1
                spx1 = x1

            for i in range(spx1,spx2+1):
                points[y1][i] += 1

        else:
            print(line)
            if (x1 > x2):
                spx2 = x1
                spx1 = x2
            if (x1 == x2):
                spx2 = x2 + 1
                spx1 = x1
            # if (x1 == y1) and (x2 == y2):
            j = y2
            for i in range(spx1, spx2+1):
                print(i,j)
                points[i][j] += 1
                j -= 1
            # elif (x1 == y2) and (y1 == x2):
            #     j = y1
            #     for i in range(x1, x2+1):
            #         print(i,j)
            #         points[i][j] += 1
            #         j -= 1

        
    # print(points)

    count = 0
    for line in points:
        for p in line:
            if p >= 2:
                count += 1
    print(count)
    print(points)

    # j = 9 # (y2)
    # x1, x2
    # for i in range(7,9+1):
    #     # for j in range(1,3+1):
    #         print(i,j)
    #         j -= 1

    # j = 1 # (y1)
    # # if x1 == y1 AND x2 == y2
    # for i in range(1,3+1):
    #     print(i,j)
    #     j += 1