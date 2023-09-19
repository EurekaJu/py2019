#Studnent Name:An Ju
#Student ID: 30391113
#Assignment1


#Part A
#Task 1

def readBoard(filename):
    
    sampleList = []
    positivesColumn = []
    negativesColumn = []
    positivesRow = []
    negativesRow = []
    orientations = []
    workingBoard = []
    
    fid = open(filename,'r')

    M = int(fid.readline())
    N = int(fid.readline())
    
    for line in fid:
        line = line.strip()
        line = line.split(',')
        sampleList.append(line)

    line = sampleList[0][0]
    line = line.split(' ')
    for i in line:
        positivesColumn.append(int(i))

    line = sampleList[1][0]
    line = line.split(' ')
    for i in line:
        negativesColumn.append(int(i))

    line = sampleList[2][0]
    line = line.split(' ')
    for i in line:
        positivesRow.append(int(i))

    line = sampleList[3][0]
    line = line.split(' ')
    for i in line:
        negativesRow.append(int(i))

    for i in range(4, 4+M):
        line = sampleList[i][0]
        line = line.strip('\n')
        mid=[]
        for j in range(len(line)):
            mid.append(line[j])
        orientations.append(mid)

    for i in range(4+M, len(sampleList)):
        line = sampleList[i][0]
        line = line.strip('\n')
        mid=[]
        for j in range(len(line)):
            mid.append(line[j])
        workingBoard.append(mid)

    return M, N, positivesColumn, negativesColumn, positivesRow, negativesRow, orientations,workingBoard

#Task 2

def printBoard(M, N, positivesColumn, negativesColumn, positivesRow , negativesRow , orientations, workingBoard):

    print('M = ',M)
    print('N = ',N)
    print('positivesColumn = ',positivesColumn)
    print('negativesColumn = ',negativesColumn)
    print('positivesRow    = ',positivesRow)
    print('negativesRow    = ',negativesRow)
    print('orientations    = ',orientations)
    print('workingBoard    = ',workingBoard)

    row = len(positivesRow)
    col = len(positivesColumn)

    #Print the first line
    print(' + | ',end = '')
    for i in range(col):
        if positivesColumn[i] == -1:
            print(' ',end = ' | ')
        else:
            print(positivesColumn[i],end = ' | ')
    print('  ')
    for i in range(0, col+2):
        if i == col+1:
            print('---')
        else:
            print('---',end = '|')

    #Print the board
    for m in range(0, row):  #The whole working bording
        
        #Positive row
        if positivesRow[m] == -1:
            print('   | ',end = '')
        else:
            print(' ' + str(positivesRow[m])+' | ', end = '')

        for n in range(0,col):
            if orientations[m][n] == 'L':
                if workingBoard[m][n] == 'E':
                    print(' ',end = '   ')
                else:
                    print(workingBoard[m][n],end = '   ')
            else:
                if workingBoard[m][n] == 'E':
                    print(' ',end = ' | ')
                else:
                    print(workingBoard[m][n], end = ' | ')
                    
        #Negative Row
        if negativesRow[m] == -1:
            print('   ')
        else:
            print('' + str(negativesRow[m])+ '   ')
        
        print('---',end = '|')
        for i in range(0,col):
            if orientations[m][i]=='T':
                  print('   ',end = '|')
            else:
                  print('---',end = '|')
        print('---')

    #End line
    print('   | ',end = '')
    for i in range(col):
        if negativesColumn[i]  == -1:
            print(' ',end = ' | ')
        else:
            print(negativesColumn[i],end = ' | ')
            
    print('- ',end = '')


#Part B
#Task 1

def canPlacePole(row, col, pole, workingBoard):
    print()
    if row > 0 and workingBoard[row][col] != workingBoard[row-1][col]:
        if row < len(workingBoard) - 1 and workingBoard[row][col] != workingBoard[row + 1][col]:
            if col > 0 and workingBoard[row][col] != workingBoard[row][col - 1]:
                if col < len(workingBoard[0]) - 1 and workingBoard[row][col] == workingBoard[row][col + 1]:
                    print('True')
                else:
                    print('False')
            else:
                print('Flase')
        else:
            print('False')
    else:
        print('False')

#Task 2
def getBlockOrientation(row, col, orientations):
    oppositeRow = 0
    oppositeCol = 0
    if orientations[row][col] == 'L':
        oppositeRow = row
        oppositeCol = col+1
        resultOrientation = 'LR'
    elif orientations[row][col] == 'R':
        oppositeRow = row
        oppositeCol = col-1
        resultOrientation = 'LR'
    elif orientations[row][col] == 'T':
        oppositeRow = row+1
        oppositeCol = col
        resultOrientation = 'TB'
    elif orientations[row][col] == 'B':
        oppositeRow = row-1
        oppositeCol = col
        resultOrientation = 'TB'
                  
    return resultOrientation, oppositeRow, oppositeCol

#Task 3
def poleCount(rowOrCol, index, pole, workingBoard):
    counter = 0
    if rowOrCol == 'r':
        for i in range(len(workingBoard[index])):
            if pole == '-' and workingBoard[index][i] == '-' or pole == '+' and workingBoard[index][i] == '+':
                counter += 1
    elif rowOrCol == 'c':
        for i in range(len(workingBoard)):
            if pole == '+' and workingBoard[i][index] == '+' or pole == '-' and workingBoard[i][index] == '-':
                counter += 1
    return counter
    
#Task 4
def randomPoleFlip(aList,percentage,flipValue):
    import random
    import math
    ranNO = math.floor(percentage * len(aList)) #Convert float number to interger number
    while ranNO > 0: #When it is in the length of the list
        index = random.randrange(len(aList)) 
        if aList[index] != flipValue: 
            aList[index] = flipValue
            ranNO -= 1
    return aList


#Part C
#Task 1
def orientationGenerator(M, N):
    import random
    newTable = []
    if M%2 == 0:
        for i in range(M):
            temp = []
            for j in range(N):
                 if i%2 == 0:
                     temp.append('T')
                 else:
                     temp.append('B')
            newTable.append(temp)
    for k in range(1000):
        randRow = random.randrange(M)
        randCol = random.randrange(N)
        
    

M, N, positivesColumn, negativesColumn, positivesRow , negativesRow , orientations, workingBoard = readBoard('sampleFile2.txt')
printBoard(M, N, positivesColumn, negativesColumn, positivesRow , negativesRow , orientations, workingBoard)
canPlacePole(1, 1, '+', workingBoard)
resultOrientation, oppositeRow, oppositeCol = getBlockOrientation(3, 2, orientations)
print()
print('counter = ',poleCount('r',3,'+', workingBoard))
print('counter = ',poleCount ('r',2,'-', workingBoard))
print('counter = ',poleCount ('c',1,'-', workingBoard))
alist=[1,2,3,4,5,6,7,8,9,10]
randomPoleFlip(alist,0.5,-1)
print(alist)

