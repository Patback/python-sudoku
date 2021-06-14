import random
import time
import copy

def generateBoard():
    #generate first row of numbers
    validNumbers = [1,2,3,4,5,6,7,8,9]
    x = 0
    while x < 9:
        temp = random.choice(validNumbers)
        board[0][x] = temp
        validNumbers.remove(temp)
        x += 1

    validNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #generate remainder of rows
    y = 1
    while y < 9:
        x = 0
        while x < 9:
            if y == 3 or  y == 6 or  y == 9:
                index = x - 4
            else:
                index = x - 3
            if index > 8:
                index -= 9
            board[y][index] = board[y-1][x]
            x += 1
        y += 1


    numberOfShuffles = 10
    i = 0
    while i < numberOfShuffles:
        #Shuffle rows
        y = 0
        while y < 9:
            if 0 < y < 3:
                randomRowShuffle = random.randint(0,2)
                tempRow = board[y].copy()
                board[y] = board[randomRowShuffle].copy()
                board[randomRowShuffle] = tempRow.copy()
            if 3 < y < 6:
                randomRowShuffle = random.randint(3,5)
                tempRow = board[y].copy()
                board[y] = board[randomRowShuffle].copy()
                board[randomRowShuffle] = tempRow.copy()
            if 6 < y < 9:
                randomRowShuffle = random.randint(6,8)
                tempRow = board[y].copy()
                board[y] = board[randomRowShuffle].copy()
                board[randomRowShuffle] = tempRow.copy()
            y += 1

        #Shuffle columns
        x = 0
        while x < 9:
            #this second loop is needed to extract each column
            #It is very likely you don't need to copy the arrays as often as I did, but seeing as how the entire program falls apart if I take them out I'm just gonna leave them there.
            tempCol = [0,0,0,0,0,0,0,0,0]
            y = 0
            while y < 9:
                tempCol[y] = board[y][x]
                y += 1
            tempCol = tempCol.copy()

            if 0 < x < 3:
                randomColShuffle = random.randint(0,2)
                tempRandCol = [0,0,0,0,0,0,0,0,0]
                y = 0
                while y < 9:
                    tempRandCol[y] = board[y][randomColShuffle]
                    y += 1
                tempRandCol = tempRandCol.copy()
                y = 0
                while y < 9:
                    board[y][x] = int(tempRandCol[y])
                    board[y][randomColShuffle] = int(tempCol[y])
                    y += 1
            if 3 < x < 6:
                randomColShuffle = random.randint(3, 5)
                tempRandCol = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                y = 0
                while y < 9:
                    tempRandCol[y] = board[y][randomColShuffle]
                    y += 1
                tempRandCol = tempRandCol.copy()
                y = 0
                while y < 9:
                    board[y][x] = int(tempRandCol[y])
                    board[y][randomColShuffle] = int(tempCol[y])
                    y += 1
            if 6 < x < 9:
                randomColShuffle = random.randint(6,8)
                tempRandCol = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                y = 0
                while y < 9:
                    tempRandCol[y] = board[y][randomColShuffle]
                    y += 1
                tempRandCol = tempRandCol.copy()
                y = 0
                while y < 9:
                    board[y][x] = int(tempRandCol[y])
                    board[y][randomColShuffle] = int(tempCol[y])
                    y += 1
            x += 1
        i += 1
def generateBoard1():
    i = 0
    while i < 80:
        temp1 = str(int(i/9))
        temp2 = str(i % 9)
        y = int(temp1,9)
        x = int(temp2,9)

        validNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        randomNum = random.choice(validNumbers)
        board[y][x] = randomNum
        validNumbers.remove(randomNum)


        while checkValidBoard() == False:
                randomNum = random.choice(validNumbers)
                board[y][x] = randomNum
                validNumbers.remove(randomNum)

                if len(validNumbers) == 0:
                    break

        i += 1

        if checkSquare(i) == False:
            # put a random value in the current cell
            printBoardCursor(i)
            input("Press to enter crazy looping function")
            crazyLoopingFunction(i)


    print("Finished the loop!")
    printBoardCursor(i)
def inputBoard1():
    global board
    board =         [[5, 1, 9, 6, 2, 3, 8, 4, 7],
                     [6, 8, 4, 9, 1, 7, 5, 2, 3],
                     [7, 2, 3, 5, 8, 4, 9, 6, 1],
                     [3, 9, 6, 7, 4, 8, 1, 5, 2],
                     [4, 7, 1, 2, 5, 6, 3, 9, 8],
                     [8, 5, 2, 1, 3, 9, 6, 7, 4],
                     [9, 6, 8, 3, 7, 2, 4, 1, 5],
                     [2, 4, 5, 8, 6, 1, 7, 3, 9],
                     [1, 3, 7, 4, 9, 5, 2, 8, 6]]
    global hiddenBoard
    hiddenBoard =   [[5, " ", 9, " ", " ", " ", " ", " ", 7],
                     [" ", 8, " ", " ", 1, " ", 5, 2, " "],
                     [" ", " ", 3, " ", 8, 4, " ", " ", 1],
                     [" ", 9, " ", 7, " ", " ", " ", " ", 2],
                     [4, " ", " ", " ", 5, " ", 3, 9, " "],
                     [8, " ", 2, 1, " ", " ", " ", " ", 4],
                     [" ", " ", " ", 3, " ", 2, " ", " ", 5],
                     [" ", 4, " ", " ", " ", " ", 7, " ", " "],
                     [1, " ", 7, " ", 9, " ", " ", 8, " "]]
def inputBoard2():
    global board
    board = [[2, 7, 1, 3, 5, 6, 9, 4, 8],
             [6, 8, 3, 9, 7, 4, 5, 1, 2],
             [5, 4, 9, 1, 2, 8, 6, 3, 7],
             [3, 6, 5, 8, 4, 7, 2, 9, 1],
             [4, 9, 7, 2, 1, 5, 3, 8, 6],
             [8, 1, 2, 6, 3, 9, 7, 5, 4],
             [7, 2, 8, 5, 9, 1, 4, 6, 3],
             [1, 5, 4, 7, 6, 3, 8, 2, 9],
             [9, 3, 6, 4, 8, 2, 1, 7, 5]]

    global hiddenBoard
    hiddenBoard =   [[2, " ", 1, " ", " ", " ", 9, " ", " "],
                     [" ", " ", " ", " ", 7, " ", " ", 1, " "],
                     [5, " ", " ", " ", " ", 8, " ", 3, 7],
                     [" ", 6, " ", 8, " ", " ", 2, " ", " "],
                     [4, " ", 7, " ", 1, " ", " ", 8, " "],
                     [" ", " ", 2, " ", " ", 9, " ", 5, 4],
                     [" ", " ", 8, 5, " ", " ", 4, " ", " "],
                     [1, 5, " ", " ", 6, " ", " ", " ", 9],
                     [9, " ", " ", 4, " ", 2, " ", 7, " "]]
def inputBoard3():
    global hiddenBoard
    hiddenBoard =   [[8, " ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", 3, 6, " ", " ", " ", " ", " "],
                     [" ", 7, " ", " ", 9, " ", 2, " ", " "],
                     [" ", 5, " ", " ", " ", 7, " ", " ", " "],
                     [" ", " ", " ", " ", 4, 5, 7, " ", " "],
                     [" ", " ", " ", 1, " ", " ", " ", 3, " "],
                     [" ", " ", 1, " ", " ", " ", " ", 6, 8],
                     [" ", " ", 8, 5, " ", " ", " ", 1, " "],
                     [" ", 9, " ", " ", " ", " ", 4, " ", " "],
                     ]


def crazyLoopingFunction(i):
    i -= 1
    temp1 = str(int(i / 9))
    temp2 = str(i % 9)
    y = int(temp1, 9)
    x = int(temp2, 9)
    temp = board[y][x]


    printBoardCursor(i)
    input("press to enter next iteration")

    incrementBoard(y,x)

    if checkValidBoard() == True and checkSquare(i+1):
        input("incrementing by one has fixed the solution")
        i += 1
        return

    index = 0
    while checkValidBoard() == False:
        index += 1

        incrementBoard(y,x)

        printBoardCursor(i)

        if index > 7:
            board[y][x] = 0
            input("WARNING: ABOUT TO ENTER RECURSIVE")
            crazyLoopingFunction(i)
            break


def checkSquare(i):
    temp1 = str(int(i / 9))
    temp2 = str(i % 9)
    y = int(temp1, 9)
    x = int(temp2, 9)
    isZero = False

    if board[y][x] == 0:
        isZero = True

    j = 0
    squareIsGood = False
    while j < 9:
        incrementBoard(y,x)
        if checkValidBoard() == True:
            squareIsGood = True
        j += 1
    if isZero == True:
        board[y][x] = 0

    print("Coordinate of checkSquare is (" + str(y) + "," + str(x) + ") and is " + str(squareIsGood))
    return squareIsGood
def incrementBoard(y,x):
    board[y][x] += 1
    if board[y][x] > 9:
        board[y][x] = 1
def incrementHiddenBoard(y,x):
    if hiddenBoard[y][x] == " ":
        hiddenBoard[y][x] = 1
        return
    hiddenBoard[y][x] += 1
    if hiddenBoard[y][x] > 9:
        hiddenBoard[y][x] = 1
def checkValidBoard():
    counter = 1
    invalidFlag = True
    y = 0
    while y < 9:
        x = 0
        while x < 9:
            temp = board[y][x]

            if temp == 0:
                return invalidFlag
            #determine which row we're in
            row = board[y].copy()
            try:
                row.remove(temp)
            except:
                print("Can't remove " + str(temp) + " from the row: " + str(row) + ".")

            #determine which column we're in
            col = [board[0][x], board[1][x], board[2][x], board[3][x], board[4][x], board[5][x], board[6][x],
                   board[7][x], board[8][x]].copy()
            try:
                col.remove(temp)
            except:
                print("Can't remove " + str(temp) + " from the col: " + str(col) + ".")

            # determine which box we're currently in
            if 0 <= y <= 2:
                if 0 <= x <= 2:
                    box = [board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0],
                           board[2][1], board[2][2]]
                elif 3 <= x <= 5:
                    box = [board[0][3], board[0][4], board[0][5], board[1][3], board[1][4], board[1][5], board[2][3],
                           board[2][4], board[2][5]].copy()
                elif 6 <= x <= 8:
                    box = [board[0][6], board[0][7], board[0][8], board[1][6], board[1][7], board[1][8], board[2][6],
                           board[2][7], board[2][8]].copy()
            elif 3 <= y <= 5:
                if 0 <= x <= 2:
                    box = [board[3][0], board[3][1], board[3][2], board[4][0], board[4][1], board[4][2], board[5][0],
                           board[5][1], board[5][2]].copy()
                elif 3 <= x <= 5:
                    box = [board[3][3], board[3][4], board[3][5], board[4][3], board[4][4], board[4][5], board[5][3],
                           board[5][4], board[5][5]].copy()
                elif 6 <= x <= 8:
                    box = [board[3][6], board[3][7], board[3][8], board[4][6], board[4][7], board[4][8], board[5][6],
                           board[5][7], board[5][8]].copy()
            elif 6 <= y <= 8:
                if 0 <= x <= 2:
                    box = [board[6][0], board[6][1], board[6][2], board[7][0], board[7][1], board[7][2], board[8][0],
                           board[8][1], board[8][2]].copy()
                elif 3 <= x <= 5:
                    box = [board[6][3], board[6][4], board[6][5], board[7][3], board[7][4], board[7][5], board[8][3],
                           board[8][4], board[8][5]].copy()
                elif 6 <= x <= 8:
                    box = [board[6][6], board[6][7], board[6][8], board[7][6], board[7][7], board[7][8], board[8][6],
                           board[8][7], board[8][8]].copy()

            try:
                box.remove(temp)
            except:
                print("Can't remove " + str(temp) + " from the box: " + str(box) + ".")

            # check row
            if temp in row:
                #print("Duplicate " + str(temp) + " detected in row at X=" + str(x) + " Y=" + str(y))
                #print("The row is " + str(row))
                invalidFlag = False
                return invalidFlag
            # check col
            if temp in col:
                #print("Duplicate " + str(temp) + " detected in col at X=" + str(x) + " Y=" + str(y))
                #print("The col is " + str(col))
                invalidFlag = False
                return invalidFlag
            # check box
            if temp in box:
                #print("Duplicate " + str(temp) + " detected in box at X=" + str(x) + " Y=" + str(y))
                #print("The box is " + str(box))
                #print("The box number is " + str(determineBoxNumber(x,y)))
                invalidFlag = False
                return invalidFlag
            x += 1
            counter += 1
        y += 1
    print("The board is valid!!! :)\n")
    return invalidFlag
def checkValidHiddenBoard():
    counter = 1
    invalidFlag = True
    y = 0
    while y < 9:
        x = 0
        while x < 9:
            temp = hiddenBoard[y][x]

            if temp == 0:
                return invalidFlag

            if temp == " ":
                break

            #determine which row we're in
            row = hiddenBoard[y].copy()
            try:
                row.remove(temp)
            except:
                print("Can't remove " + str(temp) + " from the row: " + str(row) + ".")

            #determine which column we're in
            col = [hiddenBoard[0][x], hiddenBoard[1][x], hiddenBoard[2][x], hiddenBoard[3][x], hiddenBoard[4][x], hiddenBoard[5][x], hiddenBoard[6][x],
                   hiddenBoard[7][x], hiddenBoard[8][x]].copy()
            try:
                col.remove(temp)
            except:
                print("Can't remove " + str(temp) + " from the col: " + str(col) + ".")

            # determine which box we're currently in
            if 0 <= y <= 2:
                if 0 <= x <= 2:
                    box = [hiddenBoard[0][0], hiddenBoard[0][1], hiddenBoard[0][2], hiddenBoard[1][0], hiddenBoard[1][1], hiddenBoard[1][2], hiddenBoard[2][0],
                           hiddenBoard[2][1], hiddenBoard[2][2]]
                elif 3 <= x <= 5:
                    box = [hiddenBoard[0][3], hiddenBoard[0][4], hiddenBoard[0][5], hiddenBoard[1][3], hiddenBoard[1][4], hiddenBoard[1][5], hiddenBoard[2][3],
                           hiddenBoard[2][4], hiddenBoard[2][5]].copy()
                elif 6 <= x <= 8:
                    box = [hiddenBoard[0][6], hiddenBoard[0][7], hiddenBoard[0][8], hiddenBoard[1][6], hiddenBoard[1][7], hiddenBoard[1][8], hiddenBoard[2][6],
                           hiddenBoard[2][7], hiddenBoard[2][8]].copy()
            elif 3 <= y <= 5:
                if 0 <= x <= 2:
                    box = [hiddenBoard[3][0], hiddenBoard[3][1], hiddenBoard[3][2], hiddenBoard[4][0], hiddenBoard[4][1], hiddenBoard[4][2], hiddenBoard[5][0],
                           hiddenBoard[5][1], hiddenBoard[5][2]].copy()
                elif 3 <= x <= 5:
                    box = [hiddenBoard[3][3], hiddenBoard[3][4], hiddenBoard[3][5], hiddenBoard[4][3], hiddenBoard[4][4], hiddenBoard[4][5], hiddenBoard[5][3],
                           hiddenBoard[5][4], hiddenBoard[5][5]].copy()
                elif 6 <= x <= 8:
                    box = [hiddenBoard[3][6], hiddenBoard[3][7], hiddenBoard[3][8], hiddenBoard[4][6], hiddenBoard[4][7], hiddenBoard[4][8], hiddenBoard[5][6],
                           hiddenBoard[5][7], hiddenBoard[5][8]].copy()
            elif 6 <= y <= 8:
                if 0 <= x <= 2:
                    box = [hiddenBoard[6][0], hiddenBoard[6][1], hiddenBoard[6][2], hiddenBoard[7][0], hiddenBoard[7][1], hiddenBoard[7][2], hiddenBoard[8][0],
                           hiddenBoard[8][1], hiddenBoard[8][2]].copy()
                elif 3 <= x <= 5:
                    box = [hiddenBoard[6][3], hiddenBoard[6][4], hiddenBoard[6][5], hiddenBoard[7][3], hiddenBoard[7][4], hiddenBoard[7][5], hiddenBoard[8][3],
                           hiddenBoard[8][4], hiddenBoard[8][5]].copy()
                elif 6 <= x <= 8:
                    box = [hiddenBoard[6][6], hiddenBoard[6][7], hiddenBoard[6][8], hiddenBoard[7][6], hiddenBoard[7][7], hiddenBoard[7][8], hiddenBoard[8][6],
                           hiddenBoard[8][7], hiddenBoard[8][8]].copy()

            try:
                box.remove(temp)
            except:
                print("Can't remove " + str(temp) + " from the box: " + str(box) + ".")


            # check row
            if temp in row:
                #print("Duplicate " + str(temp) + " detected in row at X=" + str(x) + " Y=" + str(y))
                #print("The row is " + str(row))
                invalidFlag = False
                return invalidFlag
            # check col
            if temp in col:
                #print("Duplicate " + str(temp) + " detected in col at X=" + str(x) + " Y=" + str(y))
                #print("The col is " + str(col))
                invalidFlag = False
                return invalidFlag
            # check box
            if temp in box:
                #print("Duplicate " + str(temp) + " detected in box at X=" + str(x) + " Y=" + str(y))
                #print("The box is " + str(box))
                #print("The box number is " + str(determineBoxNumber(x,y)))
                invalidFlag = False
                return invalidFlag
            x += 1
            counter += 1
        y += 1
    print("The board is valid!!! :)\n")
    return invalidFlag
def determineBoxNumber(x,y):
    if 0 <= y <= 2:
        if 0 <= x <= 2:
            boxNumber = 1
        elif 3 <= x <= 5:
            boxNumber = 2
        elif 6 <= x <= 8:
            boxNumber = 3
    elif 3 <= y <= 5:
        if 0 <= x <= 2:
            boxNumber = 4
        elif 3 <= x <= 5:
            boxNumber = 5
        elif 6 <= x <= 8:
            boxNumber = 6
    elif 6 <= y <= 8:
        if 0 <= x <= 2:
            boxNumber = 7
        elif 3 <= x <= 5:
            boxNumber = 8
        elif 6 <= x <= 8:
            boxNumber = 9
    return boxNumber
def printBoard(boardType, i):
    if i == 0:
        cursorY = 0
        cursorX = 0
    elif 0 < i < 81:
        temp1 = str(int(i / 9))
        temp2 = str(i % 9)
        cursorY = int(temp1, 9)
        cursorX = int(temp2, 9)
    else:
        print("i must be between 0 and 81")
        return
    if boardType == 0:
        y = 0
        while y < 9:
            x = 0
            while x < 9:
                if x == 3 or x == 6:
                    print("|" + "  ", end = '')
                if cursorY == y and cursorX == x:
                    if board[y][x] == 1:
                        print("\033[4m1\033[0m  ", end='')
                    if board[y][x] == 2:
                        print("\033[4m2\033[0m  ", end='')
                    if board[y][x] == 3:
                        print("\033[4m3\033[0m  ", end='')
                    if board[y][x] == 4:
                        print("\033[4m4\033[0m  ", end='')
                    if board[y][x] == 5:
                        print("\033[4m5\033[0m  ", end='')
                    if board[y][x] == 6:
                        print("\033[4m6\033[0m  ", end='')
                    if board[y][x] == 7:
                        print("\033[4m7\033[0m  ", end='')
                    if board[y][x] == 8:
                        print("\033[4m8\033[0m  ", end='')
                    if board[y][x] == 9:
                        print("\033[4m9\033[0m  ", end='')
                    if board[y][x] == 0:
                        print("\033[4m0\033[0m  ", end='')
                    if board[y][x] == " ":
                        print("\033[4mOogaooga\033[0m  ", end='')
                else:
                    print(board[y][x], " ", end = '')
                x += 1
            print("")
            if y == 2 or y == 5:
                print("-------------------------------")
            y += 1
        print("")
    if boardType == 1:
        y = 0
        while y < 9:
            x = 0
            while x < 9:
                if x == 3 or x == 6:
                    print("|" + "  ", end = '')
                if cursorY == y and cursorX == x:
                    if hiddenBoard[y][x] == 1:
                        print("\033[4m1\033[0m  ", end='')
                    if hiddenBoard[y][x] == 2:
                        print("\033[4m2\033[0m  ", end='')
                    if hiddenBoard[y][x] == 3:
                        print("\033[4m3\033[0m  ", end='')
                    if hiddenBoard[y][x] == 4:
                        print("\033[4m4\033[0m  ", end='')
                    if hiddenBoard[y][x] == 5:
                        print("\033[4m5\033[0m  ", end='')
                    if hiddenBoard[y][x] == 6:
                        print("\033[4m6\033[0m  ", end='')
                    if hiddenBoard[y][x] == 7:
                        print("\033[4m7\033[0m  ", end='')
                    if hiddenBoard[y][x] == 8:
                        print("\033[4m8\033[0m  ", end='')
                    if hiddenBoard[y][x] == 9:
                        print("\033[4m9\033[0m  ", end='')
                    if hiddenBoard[y][x] == 0:
                        print("\033[4m0\033[0m  ", end='')
                    if hiddenBoard[y][x] == " ":
                        print("\033[4m \033[0m  ", end='')
                else:
                    print(hiddenBoard[y][x], " ", end = '')
                x += 1
            print("")
            if y == 2 or y == 5:
                print("-------------------------------")
            y += 1
        print("")
def printSimpleBoard():
    print("\n")
    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print(board[4])
    print(board[5])
    print(board[6])
    print(board[7])
    print(board[8])
    print("\n")
def hideBoard():
    difficulty = 0
    tempDif = 40

    if tempDif > 81:
        print ("The number of hidden squares exceeds number of squares on board")
        return

    #hiddenBoard = board.copy()
    global hiddenBoard
    hiddenBoard = copy.deepcopy(board)


    randomHiddens = random.sample(range(81), tempDif)

    for i in randomHiddens:
        temp1 = str(int(i/9))
        temp2 = str(i % 9)
        randomY = int(temp1,9)
        randomX = int(temp2,9)

        hiddenBoard[randomY][randomX] = " "
def solveBoard():
    print("Starting solveBoard function")
    y = 0
    while y < 9:
        x = 0
        while x < 9:
            if hiddenBoard[y][x] == " ":
                indexArray.append(y*9 + x)
            x += 1
        y += 1







    i = 0
    while i < len(indexArray):
        index = indexArray[i]
        if index == 0:
            y = 0
            x = 0
        elif 0 < index < 81:
            temp1 = str(int(index / 9))
            temp2 = str(index % 9)
            y = int(temp1, 9)
            x = int(temp2, 9)
        else:
            print("Error in solve board function: Index exceeded 81")
            return

        printBoard(1, index)
        incrementHiddenBoard(y,x)

        loopHell = False
        j = 0
        while j < 9:
            if not checkValidHiddenBoard():
                incrementHiddenBoard(y,x)
            else:
                break
            if j > 7:
                print("----------------------------------------------------------------------------------------------------------------------------------------------")
                print("")
                print("")
                print("")
                print("")
                print("")
                hiddenBoard[y][x] = " "
                printBoard(1, index)
                loopHell = True
                break
            j += 1


        if loopHell == True:
            print("i value before loopHELLs. i = " + str(i))
            i = loopHELL(i)
            index = indexArray[i]
            print("loopHELLs concluded. i = " + str(i))

            global attemptMatrix
            attemptMatrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0]]


        i += 1


    print("The board should now be solved!! Compare answers: :)")
    printBoard(0 , 80)
    printBoard(1, 80)


    print(indexArray)
    print(i)


def loopHELL(i):
    global attemptMatrix
    i -= 1
    if i < 0:
        print("Error, i is less than 0")
        time.sleep(1000)

    index = indexArray[i]

    if index == 0:
        y = 0
        x = 0
    elif 0 < index < 81:
        temp1 = str(int(index / 9))
        temp2 = str(index % 9)
        y = int(temp1, 9)
        x = int(temp2, 9)
    else:
        print("Error in solve board function: Index exceeded 81")
        return

    attemptMatrix[index].append(hiddenBoard[y][x])




    if hiddenBoard[y][x] is not 9:
        incrementHiddenBoard(y, x)
        print("Before second thing:")
        print("Answer board:")
        printBoard(0, index)
        print("Hidden board:")
        printBoard(1, index)


    if checkValidHiddenBoard() and hiddenBoard[y][x] not in attemptMatrix[index]:
        attemptMatrix[index].append(hiddenBoard[y][x])
        print("breaking out of loopHELL. Boards:")
        print("Answer board:")
        printBoard(0, index)
        print("Hidden board:")
        printBoard(1, index)
        return i
    attemptMatrix[index].append(hiddenBoard[y][x])


    if not checkValidHiddenBoard():
        while hiddenBoard[y][x] < 9:
            incrementHiddenBoard(y, x)
            if checkValidHiddenBoard() and hiddenBoard[y][x] not in attemptMatrix[index]:
                attemptMatrix[index].append(hiddenBoard[y][x])
                print("breaking out of loopHELL. Boards:")
                print("Answer board:")
                printBoard(0, index)
                print("Hidden board:")
                printBoard(1, index)
                return i
            if not checkValidHiddenBoard():
                attemptMatrix[index].append(hiddenBoard[y][x])
                print("not a valid board, incrementing by 2")
                continue
            attemptMatrix[index].append(hiddenBoard[y][x])
    print("After second thing:")
    print("Answer board:")
    printBoard(0, index)
    print("Hidden board:")
    printBoard(1, index)


    hiddenBoard[y][x] = " "
    i = loopHELL(i)


    return i


board =         [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 ]
hiddenBoard =   [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 ]
indexArray =    []
attemptMatrix =    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]


#generateBoard()
#hideBoard()
inputBoard1()
#inputBoard2()
#inputBoard3()

printBoard(1, 0)
input("This is the sudoku to solve")

solveBoard()


#printSimpleBoard()

#checkValidBoard()

#hideBoard()