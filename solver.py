import os
board = [
                [0,3,0,0,0,0,0,0,0],
                [0,5,0,0,0,2,0,0,7],
                [0,8,0,0,4,0,6,9,0],
                [7,0,6,0,8,0,0,1,0],
                [0,0,0,6,7,5,0,0,0],
                [8,9,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,0,3],
                [0,0,4,7,2,0,0,8,6]
]

indexes = []

def check_row(row, n):
    return n in board[row]

def check_col(col, n):
    for row in range(len(board)):
        if(n == board[row][col]):
            return True
    return False

def check_box(row, col, n):
    #determine which box the coordinates are in
    x = int(col/3)
    y = int(row/3)
    #set limits for loop
    i=0
    j=0
    #loop
    while i < 3:
        while j < 3:
            if(n == board[i+y*3][j+x*3]):
                return True
            j += 1
        j = 0
        i += 1
    return False

def display():
    #os.system("cls")
    for col in range(len(board[0])-1):
        print("---", end="")
    print("-")

    for row in range(len(board)):
        print("|", end="")
        for col in range(len(board[row])):
            print("", board[row][col],end="")
            if(col==2 or col==5):
                print(" |", end="")
        print(" |")
        if(row==2 or row==5):
            print("|", end="")
            for col in range(len(board[row])):
                print("--", end="")
                if(col==2 or col==5):
                    print("-|", end="")
            print("-|")

    for col in range(len(board[0])-1):
        print("---", end="")
    print("-")

def get_indexes():
    for row in range(len(board)):
        for col in range(len(board[0])):
            if(board[row][col]==0):
                indexes.append([row,col])


def solve(r):
    if r == len(indexes):
        display()
        return
    row = indexes[r][0]
    col = indexes[r][1]
    for n in range(1,10):
        if(check_row(row, n) or check_col(col, n) or check_box(row, col, n)):
            continue
        
        board[row][col] = n
        #display()

        solve(r+1)

        board[row][col] = 0

get_indexes()
solve(0)