numbers = None
BOARDS = []
SELECTED = []
tempboard = []

# parses input into 2d array of boards:
# below is 2 boards
# [ [ [r0], [r1], [r2], [r3], [r4] ], [ [r0], [r1], [r2], [r3], [r4] ] ] ]
for line in open('input.txt'):
    line = line.strip()
    if numbers is None:
        numbers = [int(x) for x in line.split(',')]
    else:
        if line:
            tempboard.append([int(x) for x in line.split()])
        else:
            if tempboard:
                BOARDS.append(tempboard)
            tempboard = []
BOARDS.append(tempboard)

# for each board, create array that copies format, except every num is False
# append False for every row and col (5 for nums in row), (5 for num rows)
for board in BOARDS:
    SELECTED.append([[False for x in range(5)] for x in range(5)])

# init array that stores win state of each board, False initially
WINNERS = [False for x in range(len(BOARDS))]

# goes through each number in the number list
for number in numbers:
    # for each board
    for i in range(len(BOARDS)):
        # for each row
        for row in range(5):
            # for each column
            for col in range(5):
                # if that specific num of the board is the same as the current number
                if BOARDS[i][row][col] == number:
                    # toggle corresponding item in True/False array True
                    SELECTED[i][row][col] = True

        # var that stores current board win state
        didwin = False

        # checks if row has won
        for row in range(5):
            # assume it has
            win = True
            # explicitly check each item, all must be True in order for row to win
            for col in range(5):
                # if any of them are false
                if SELECTED[i][row][col] == False:
                    # board has not won
                    win = False
            # if the board has won
            if win:
                # it wins
                didwin = True
        
        # checks if column has won: same thing as above
        for col in range(5):
            win = True
            for row in range(5):
                if SELECTED[i][row][col] == False:
                    win = False
            if win:
                didwin = True
        
        # if the board has won, and has not won previously (checks array to see if it has)
        # the reason for this is because if a row fills up, it wins, then if a second row fills up, it would "win again"
        if (didwin == True) and (WINNERS[i] == False):
            WINNERS[i] = True
            # check if this was the first board to win
            # creates array of winners, consitsting of only the winners
            # array of index for index in range of the length of the boards only if the corresponding board at index has won (== True)
            numofwinners = len([i for i in range(len(BOARDS)) if WINNERS[i] == True])
            # if the number of winners is one (first board to win) OR
            # if the number of winners is ALL of the boards (last board to win will have last num to win and last squares unfilled)
            if numofwinners == 1 or numofwinners == len(BOARDS):
                sumUnmarked = 0
                # sum all the unmarked spots
                for row in range(5):
                    for col in range(5):
                        # if the spot is not selected
                        if SELECTED[i][row][col] == False:
                            # add to the sum
                            sumUnmarked += BOARDS[i][row][col]
                # prints answer: the sum of the unmarked squares times the number it took to make the first square win
                # because this is all inside the for number in numbers loop, number === the winning number
                print(sumUnmarked * number)