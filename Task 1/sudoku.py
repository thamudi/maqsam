board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board_two = [
    [3,0,6,5,0,8,4,0,0],
    [5,2,0,0,0,0,0,0,0],
    [0,8,7,0,0,0,0,3,1],
    [0,0,3,0,1,0,0,8,0],
    [9,0,0,8,6,3,0,0,5],
    [0,5,0,0,9,0,6,0,0],
    [1,3,0,0,0,0,2,5,0],
    [0,0,0,0,0,0,0,7,4],
    [0,0,5,2,0,6,3,0,0]
]

def solve(board):
    found = find_empty_cell(board)
    if not found:
        return True # Exit Script
    else:
        row, column = found # Assign found empty cell row by column respectuvly

    for i in range(1,10): # Loop through the options from 1-9
        if valid(board, i, (row, column)): # Validate 
            board[row][column] = i # Assigne the current number to the cell

            if solve(board): # Recusive Check if the board has been solved
                return True

            board[row][column] = 0 # Reset Cell

    return False

def find_empty_cell(board):
    '''
    Name: find_empty_cell
    Description: Checks if the current position of a cell equels 0, which indicates if empty or not
    Returns: Tuple (row, column)
    '''
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return (row, column)

    return None

def valid(board, number, position):
    '''
    Name: valid
    Description: Validate if the currnet position of the assigned number can work for each row and column
    Returns: Boolean
    '''
   
   # Check row
    if not (check_row(board, number, position)):
       return False

    # Check column
    if not (check_column(board, number, position)):
        return False

    # Check box
    if not (check_box(board, number, position)):
        return False

    return True

def check_row(board, number, position):
    '''
    Name: check_row
    Description: Validate if the currnet row has the assigned number already
    Returns: Boolean
    '''
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    return True

def check_column(board, number, position):
    '''
    Name: check_column
    Description: Validate if the currnet column has the assigned number already
    Returns: Boolean
    '''
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False
    return True

def check_box(board, number, position):
    '''
    Name: check_box
    Description: 
    Returns: Boolean
    '''
    box_x = position[1] // 3
    box_y = position[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False
    return True

def print_board(board):
    '''
    Name: print_board
    Description: Prints the sudko board onto a command line interface
    Returns: Void
    '''
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

#######################
# Program starts here # 
#######################
print_board(board) # print board before solving
solve(board) # Run the solving script
print("=============================") # Spacer
print("============= First Board ===============") # Spacer
print_board(board) # Print the board after solving  
print("=============================") # Spacer
print("============= Second Board ===============") # Spacer
print_board(board_two) # print board before solving
solve(board_two) # Run the solving script
print("=============================") # Spacer
print_board(board_two) # Print the board after solving  
#######################
##### End Script ######
#######################