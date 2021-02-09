'''
This module contains functions
https://github.com/vilgurin/Puzzle
'''
def check_rows(board):

    '''
    The function checks the board's rows and returns True if each of them
    contains not more than one number from 1 to 9.
    >>> check_rows(["**** ","***1 ","  3","* 4 1 9","     8 ",\
    " 61  35","3  8   ","      *","2 5"," 2***"," ****"])
    True
    >>> check_rows(["**** ","**11 ","  3","* 4 1 9","     8 ",\
    " 61  35","3  1   ","      *","2 5"," 2***"," ****"])
    False
    '''

    for i in board:
        for sign in i:
            if sign.isdigit() == True and i.count(sign) >1:
                return False

    return True

def check_columns(board):
    '''
    The function checks the board's columns and returns True if each of them
    contains not more than one number from 1 to 9.
    >>> check_columns(["**** ****","***1 ****","**  3****","* 4 1****","     9 5 ",\
    " 6  83  *","3   1  **","  8  2***","  2  ****"])
    False
    '''

    for i in range(len(board)-1):

        numbers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for element in board:
            if element[i].isdigit() == True:
                numbers[int(element[i])] += 1

        for key in numbers:
            if numbers[key] >1:
                return False

    return True

def check_colors(board):

    '''
    The function checks the board's colors areas and returns True if each of them
    contains not more than one number from 1 to 9.
    >>> check_colors(["**** ****","***1 ****","**  3****","* 4 1****",\
    "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    True
    '''

    numbers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    k = 0
    for i in range(len(board[0])):
        for element in range(len(board)-k):
            if element == len(board)-k-1:
                for el_symbol in range(len(board[element])):
                    if board[element][el_symbol].isdigit() == True:
                        numbers[int(board[element][el_symbol])] += 1
                        break
            elif (board[element][i].isdigit() == True and int(board[element][i]) in numbers):
                numbers[int(board[element][i])] += 1
        for key in numbers:
            if numbers[key]>1:
                return False
        for key in numbers:
            numbers[key] = 0
        k += 1
        return True


def validate_board(board):

    '''
    The function checkes it the boardfilled in according to the following rules:

    1)The colored cells of each line must contain the numbers 1 to 9 without
    repetition.

    2)The colored cells of each column must contain the numbers 1 to 9 without
    repetition.

    3) Each block of cells of the same color must contain numbers from 1 to 9 without
    repetition.
    >>> validate_board(["**** ****","***1 ****","**  3****","* 4 1****",\
    "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    False
    '''

    check1 = check_rows(board)
    check2 = check_columns(board)
    check3 = check_colors(board)

    if check1 and check2 and check3:
        return True
        
    return False
    