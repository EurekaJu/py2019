'''
## NOT FOR RE-DISTRIBUTION. NOT TO BE MODIFIED.
## Do not share or upload this elsewhere. 
## To be used SOLELY as the basis for assignment 2 without modification.

## MCD4710 - T3 - 2019 Sample Solution
##
##     Author: M.V.
##     Credits: Based on previous work by Ammar Al-Jodah 
##
##     Filename: MCD4710_T3_2019_A1_SolutionVer1.7_Student_Release.py
##     Created: 20/10/2019
##     Last Modified: 18/12/2019
##     Version:1.6
##
##     Description & Notes:
##         Assignment 1 Sample solution for teaching purposes only.  
##         To be used as basis for assignment 2 without any modifications.
##         This might be different to how you did your assignment; however,
##         to ensure consistency and stability you must use this code base.
##
##         Please note: this code base will be excluded when checking for
##         plagiarism. So please make sure that you do not modify it.
##         
##         If you spot any errors/issues/concerns please contact the subject
##         leader for MCD4710. 
##
##     Copyright 2019-2020 - All Rights Reserved. 
##     Modification/redistribution are NOT allowed without explicit permission of the Author. 

'''
import math
import random

##############################################################################
##                      Do not change this part                               
##                      Start of Assignment 1 Code Base                         
##############################################################################

# Part A: Representation and display (15 marks)

# Part A - Task 1 - Initial setup (5 marks)
def readBoard(fileName):
    M = 0
    N = 0
    positivesColumn = []
    negativesColumn = []
    positivesRow = []
    negativesRow = []
    orientations = []
    workingBoard = []

    file = open(fileName)
    fileContent = []

    for line in file:
        fileContent.append(line.strip())

    M = int(fileContent[0])  # line 1 in file
    N = int(fileContent[1])  # line 2 in file

    positivesColumn = convertStringListToIntList(
        fileContent[2].split())  # line 3 in file
    negativesColumn = convertStringListToIntList(
        fileContent[3].split())  # line 4 in file
    positivesRow = convertStringListToIntList(
        fileContent[4].split())     # line 5 in file
    negativesRow = convertStringListToIntList(
        fileContent[5].split())     # line 6 in file

    # next M lines after line 6
    for counter in range(M):
        orientations.append(list(str(fileContent[counter+6])))

    # remaining M lines in file
    for counter in range(M):
        workingBoard.append(list(str(fileContent[counter+M+6])))
    file.close()
    return (positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard)

def convertStringListToIntList(lst):
    for item in range(len(lst)):
        lst[item] = int(lst[item])
    return lst

# Part A - Task 2 - Display (10 marks)
def printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard):
    M = len(orientations)
    N = len(orientations[0])

    # print the positivesColumn -> the top positive
    print(" + |",end="")
    for rowCounter in range(N):
        if positivesColumn[rowCounter]>=0:
            print(" " + str(positivesColumn[rowCounter])+ " ",end="")
        elif positivesColumn[rowCounter]==-1:
            # -1 to empty square
            print("   ", end="")
        print("|",end="")
    print("")

    # print the following line
    print("--- "*(N+2))

    # print the workingBoard one row at a time
    for rowCounter in range(M):

        #print the positivesRow first
        if positivesRow[rowCounter]>=0:
            print(" " + str(positivesRow[rowCounter]) + " ", end="")
        elif positivesRow[rowCounter]==-1:
            print("   ", end="")
        print("|",end="")
       

        #print the workingBoard Row
        for colCounter in range(N):
            #if E print blank square
            if (workingBoard[rowCounter][colCounter]=='E'):
                print("   ", end="")
            else:
                print (" " + workingBoard[rowCounter][colCounter]  + " ", end="")
            #Check orientations board if current magnet is horizontal or vertical 
            #if horizontal 
            if (orientations[rowCounter][colCounter]=='L'):
                print(" ",end="")
            else:
                #if vertical
                print("|",end="")

        #print the negatives row 
        if negativesRow[rowCounter]>=0:
            print(" " + str(negativesRow[rowCounter]) + " ", end="")
        elif negativesRow[rowCounter]==-1:
            print("   ", end="")
        

        print("")
        print("--- ",end="")
        # print line below row check orientation
        for colCounter in range(N):
            if (orientations[rowCounter][colCounter]!='T'):
                print("--- ",end="")
            else:
                #if vertical
                print("    ",end="") 
        print("--- ",end="")
        print("")
    
    # print the negativeColumn at the bottom
    print("   |", end="")
    for rowCounter in range(len(negativesColumn)):
        if negativesColumn[rowCounter] >= 0:
            print(" " + str(negativesColumn[rowCounter]) + " ", end="")
        else:
            print("   ", end="")
        print("|",end="")
    print(" - ")
    print("")
    return


#Part B: Helper functions (25 marks)

#Part B - Task 1 - Safe placing (10 marks)
def canPlacePole(row, col, pole, workingBoard):
    M= len (workingBoard)
    N= len (workingBoard[0])

    if (row>M-1 or col>N-1):
        return False

    # check surrounding squares (diagonals are not checked )
    if ((row > 0 and workingBoard[row - 1][col] == pole) or (row < M - 1 and workingBoard[row + 1][col] == pole) or
    (col > 0 and workingBoard[row][col - 1] == pole)or(col < N - 1 and workingBoard[row][col + 1] == pole)):
        return False
    return True

#Part B - Task 2 - Block orientation (5 marks)
def getBlockOrientation(row, col, orientations):
    M= len (orientations)
    N= len (orientations[0])
    
    if (row>M-1 or col>N-1):
        return None

    #if TB (Top Bottom/Vertical) orientation
    #if Top return Bottom coordinates
    if (orientations[row][col] == 'T'):
        return "TB",row+1,col
    #else if Bottom return Top coordinates
    elif (orientations[row][col] == 'B'):
        return "TB",row-1,col
    #else if Left return Right coordinates
    elif (orientations[row][col] == 'L'):
        return "LR",row,col+1
    #else if Right return Left coordinates
    elif (orientations[row][col] == 'R'):
        return "LR",row,col-1
    else:
        return None

#Part B - Task 3 - Pole Count (5 marks)
def poleCount(rowOrCol, index, pole, workingBoard):
    M= len (workingBoard)
    N= len (workingBoard[0])

    if ((index >M-1 and rowOrCol == 'r')  or (index > N-1 and rowOrCol == 'c')):
        return None


    poleCounter=0

    if str(rowOrCol).lower() =='r':
        for iterator in range(N):
            if workingBoard[index][iterator]== pole:
                poleCounter+=1
    elif str(rowOrCol).lower() == 'c':
        for iterator in range(M):
            if workingBoard[iterator][index]== pole:
                poleCounter+=1
    return poleCounter

#Part B - Task 4 - Random Magnetic Pole Distribution (5 marks)
def randomPoleFlip(aList, percentage, flipValue):
    listLength = len(aList)
    
    noOfFlips =  math.floor(listLength*percentage)
    #Keep repeating until desired number of flips is fulfilled 
    while aList.count(flipValue) < noOfFlips:
        randomIndex= random.randint(0,listLength-1)
        if aList[randomIndex]!=flipValue:
            aList[randomIndex] = flipValue

# Part C: Board Generation Functions (30 marks)

# Part C - Task 1: Orientations generation (10 marks)
def orientationsGenerator(M,N):
    
    # Generating a new M by N board with all orientations set as vertical blocks
    # Note: be mindful of copy
    orientations=[['']*N]*M 
    
    for row in range(0,M-1,2):
        orientations[row]=['T']*N
        orientations[row+1]=['B']*N
    
    # Repeat the process at least 1000 times
    for repeat in range(1000):
        # Picking random block
        randomRow = random.randint(0,M-1)
        randomCol = random.randint(0,N-1)
        otherEndRow = getBlockOrientation(randomRow, randomCol, orientations)[1]
        otherEndCol = getBlockOrientation(randomRow, randomCol, orientations)[2]
        
        # If it is a LR block, check the block that is immediately above it. 
        # If it is also an LR block and it is perfectly aligned with the picked 
        # block then change both blocks to become TB blocks. 
        # If it is not possible to do this with the top block, then try with the bottom block.
        if randomRow>0  and orientations[randomRow][randomCol] == orientations[randomRow-1][randomCol] and getBlockOrientation(randomRow, randomCol, orientations)[0] == 'LR':
            #Change bottom block to 'B's
            orientations[randomRow][randomCol]='B'
            #other end
            orientations[otherEndRow][otherEndCol]='B'
            #Change top block to 'T's
            orientations[randomRow-1][randomCol]='T'
            orientations[otherEndRow-1][otherEndCol]='T'
        elif randomCol>0  and orientations[randomRow][randomCol] == orientations[randomRow][randomCol-1] and getBlockOrientation(randomRow, randomCol, orientations)[0] == 'TB':
            #Change right block to 'R's
            orientations[randomRow][randomCol]='R'
            #other end
            orientations[otherEndRow][otherEndCol]='R'
            #Change left block to 'L's
            orientations[randomRow][randomCol-1]='L'
            orientations[otherEndRow][otherEndCol-1]='L'
    
    return orientations

# Part C - Task 2: Filling board with magnets (10 marks)
def fillWithMagnets(orientations):
    M= len (orientations)
    N= len (orientations[0])
    # Create a new M by N  empty workingBoard
    # be mindful of copying
    workingBoard=[[''] * N for i in range(M)]

    for rowCounter in range(M):
        for colCounter in range(N):
            if (canPlacePole(rowCounter,colCounter,'+',workingBoard)):
                workingBoard[rowCounter][colCounter]='+'
            else:
                workingBoard[rowCounter][colCounter]='-'
        
    return workingBoard

# Part C - Task 3: Generating random new board (10 marks)
def randomNewBoard (M,N):
    # 1. Generate the orientations board of size M x N randomly. (1 mark)
    # Note: use orientationsGenerator function for this.
    orientations = orientationsGenerator(M, N)

    # 2. Fill the board with magnet blocks.  (1 mark)
    # Note: use fillWithMagnets function for this.
    workingBoard = fillWithMagnets(orientations)

    # 3. Randomly replace 30% of the blocks with blank blocks (‘X’ blocks)  (3 marks)
    # Cover the board from top to bottom and the decision to swap with a
    # blank block is based on a random chance for each block and repeated 
    # until 30% of board is replaced. Other end of a checked block will be ignored.
    blockCount = M * N / 2
    requiredReplacements =  math.ceil(0.3 * blockCount)
    replacementChance=0.2
    replacementCount=0

    while (replacementCount <requiredReplacements):
        for rowCounter in range(M):
            for colCounter in range(N):
                rand = random.random()
                #blockOrientation = getBlockOrientation(rowCounter, colCounter, orientations)[0]  # unused
                otherEndRow = getBlockOrientation(rowCounter, colCounter, orientations)[1]
                otherEndCol = getBlockOrientation(rowCounter, colCounter, orientations)[2]
                if (otherEndRow > rowCounter or otherEndCol > colCounter):
                    if (rand<=replacementChance and replacementCount <requiredReplacements):
                        workingBoard[rowCounter][colCounter]='X'
                        workingBoard[otherEndRow][otherEndCol]='X'
                        replacementCount+=1

    # 4. Generate the resulting positivesColumn, negativesColumn, positivesRow, and negativesRow lists. (3 marks)
    # Note: use poleCount function for this.
    positivesColumn=[]
    negativesColumn=[]
    positivesRow=[]
    negativesRow=[]

    for counter in range(N):
        positivesColumn.append( poleCount('c',counter,'+',workingBoard))
        negativesColumn.append( poleCount('c',counter,'-',workingBoard))
    for counter in range(M):
        positivesRow.append( poleCount('r',counter,'+',workingBoard))
        negativesRow.append( poleCount('r',counter,'-',workingBoard))

    # 5. Replace 50% of the numbers in each of positivesColumn, negativesColumn, positivesRow, and 
    # negativesRow lists with -1. (2 marks)
    # Note: use randomPoleFlip function for this.
    randomPoleFlip(positivesColumn,0.5,-1)
    randomPoleFlip(negativesColumn,0.5,-1)
    randomPoleFlip(positivesRow,0.5,-1)
    randomPoleFlip(negativesRow,0.5,-1)
   
    return (positivesColumn, negativesColumn, positivesRow, negativesRow, workingBoard, orientations)

##############################################################################
##                      Do not change this part                               
##                      End of Assignment 1 Code Base                         
##############################################################################


#Student Name:An Ju
#Student ID: 30391113
#Date: 08/01/2020
#Assignment2


def setToBoard(my_set,orientations):
    M = len(orientations)
    N = len(orientations[0])
    workingBoard = []
    # create a list and filled it with 'E'
    for i in range(M):
        temp = []
        for j in range(N):
            temp.append('E')
        workingBoard.append(temp)
    # print(workingBoard)   (to test the loop when debugging)
    counter = 0
    for k in range(M):
        for l in range(N):
            if counter < len(my_set) and workingBoard[k][l] == 'E':
                # the element in workingBoard[i][j] might be changed because of 'T' and 'L'
                # therefore it can't be used in the loop again
                # and the counter is the index for my_set it only worked when there is element in my_set to change the board
                # print(my_set[counter]) (to test the loop when debugging)
                if my_set[counter] == 0:
                    if orientations[k][l] == 'T':
                        workingBoard[k][l] = '+'
                        workingBoard[k+1][l] = '-'
                    elif orientations[k][l] == 'L':
                        workingBoard[k][l] = '+'
                        workingBoard[k][l+1] = '-'
                elif my_set[counter] == 1:
                    if orientations[k][l] == 'T':
                        workingBoard[k][l] = '-'
                        workingBoard[k+1][l] = '+'
                    elif orientations[k][l] == 'L':
                        workingBoard[k][l] = '-'
                        workingBoard[k][l+1] = '+'
                else:
                    if orientations[k][l] == 'T':
                        workingBoard[k][l] = 'X'
                        workingBoard[k+1][l] = 'X'
                    elif orientations[k][l] == 'L':
                        workingBoard[k][l] = 'X'
                        workingBoard[k][l+1] = 'X'
                counter += 1
    # print(workingBoard)
    return workingBoard

def isSolution(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations,
workingBoard):
    flag = True
    M = len(orientations)
    N = len(orientations[0])
    for row in range(M):
        for col in range(N):
            # when the element is equal to 'X' it always can be placed
            if workingBoard[row][col] != 'X':
                if canPlacePole(row, col, workingBoard[row][col], workingBoard) == False:
                    flag = False
    # print(flag, 1) (to test the loop when debugging)
    for i in range(M):
        if positivesRow[i] != -1 and poleCount('r', i, '+', workingBoard) != positivesRow[i]:
            flag = False
        if negativesRow[i] != -1 and poleCount('r', i, '-', workingBoard) != negativesRow[i]:
            flag = False
        # print("row",i,flag)
    for j in range(N):
        if positivesColumn[i] != -1 and poleCount('c', i, '+', workingBoard) != positivesColumn[i]:
            flag = False
        if negativesColumn[i] != -1 and poleCount('c', i, '-', workingBoard) != negativesColumn[i]:
            flag = False
        # print("col",j,flag)
    return flag

def bruteforce(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations):
    M = len(orientations)
    N = len(orientations[0])
    all_sol = []
    sol_len = 3 ** ((M * N) // 2)
    num = (M * N) // 2
    # append each possiblesolution to the list to generate all the solution
    for k in range(sol_len):
        # call the function every time to append the possible solution one by one
        all_sol.append(dec2base3_sol(k,num))
    for sol in all_sol:
        # set each possible solution to a board
        solution = setToBoard(sol, orientations)
        # call the isSolution function to justify whether it is the solution for the board
        if isSolution(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, solution):
            print(solution)
            print(sol)
            return solution

# there are 0, 1, 2 three possibility therefore can use base 3 to represent the possible solution 
def dec2base3_sol(dec,num):
    lst = [0] * num
    index = 0
    temp = dec
    flag = True
    while flag == True:
        lst[index] = dec % 3
        dec = dec // 3
        index += 1
        temp = dec - 1
        if temp < 0:
            flag = False
    lst.reverse()
    return lst

    



 #Testing sample
positivesColumn = [2, 1, 1, -1, -1]
negativesColumn = [1, -1, -1, 2, 1]
positivesRow = [2, -1, -1, 1]
negativesRow = [1, 3, -1, -1]
orientations = [['T', 'L', 'R', 'L', 'R'],
                    ['B', 'L', 'R', 'L', 'R'],
                    ['L', 'R', 'L', 'R', 'T'],
                    ['L', 'R', 'L', 'R', 'B']]
printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow,
               orientations, orientations)
print("#############################################")
solution = []
solution = bruteforce(positivesColumn, negativesColumn, positivesRow, negativesRow,
                          orientations)
printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow,
               orientations, solution)
