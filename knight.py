import random

BOARD = '''
  +---+---+---+---+---+---+---+---+
8 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
7 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
6 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
5 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
4 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
3 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
2 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
1 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
    A   B   C   D   E   F   G   H
'''

# makes sure that all of the squares are visited
def check_board(board_data):
    for i in range(len(board_data)):
        for j in range(len(board_data[i])):
            if board_data[i][j] == 0:
                return False
            
    print("The Tour is completed!")
    return True

# checks a given position on the board
def check(pos, board_data):
    # check for out of bounds exception  and if the square is already taken
    if pos[0] > 7 or pos[0] < 0 or pos[1] > 7 or pos[1] < 0 or board_data[pos[0]][pos[1]] != 0:
        return False
    else:
        return True
    
def possible(pos, board_data):
    num = []

    # check for number 1
    if check([pos[0] - 2, pos[1] - 1], board_data):
        num.append(1)
    # check for number 2
    if check([pos[0] - 2, pos[1] + 1], board_data):
        num.append(2)
    # check for number 3
    if check([pos[0] - 1, pos[1] + 2], board_data):
        num.append(3)
    # check for number 4
    if check([pos[0] + 1, pos[1] + 2], board_data):
        num.append(4)
    # check for number 5
    if check([pos[0] + 2, pos[1] + 1], board_data):
        num.append(5)
    # check for number 6
    if check([pos[0] + 2, pos[1] - 1], board_data):
        num.append(6)
    # check for number 7
    if check([pos[0] + 1, pos[1] - 2], board_data):
        num.append(7)
    # check for number 8
    if check([pos[0] - 1, pos[1] - 2], board_data):
        num.append(8)

    return num

#corresponding number 1
def up_left(pos, board_data, count):
    pos[0] -= 2 
    pos[1] -= 1

    board_data[pos[0]][pos[1]] = count
    count += 1

    return count

#corresponding number 2
def up_right(pos, board_data, count):
    pos[0] -= 2 
    pos[1] += 1

    board_data[pos[0]][pos[1]] = count
    count += 1

    return count

#corresponding number 3
def right_up(pos, board_data, count):
    pos[0] -= 1 
    pos[1] += 2

    board_data[pos[0]][pos[1]] = count
    count += 1

    return count

#corresponding number 4
def right_down(pos, board_data, count):
    pos[0] += 1
    pos[1] += 2

    board_data[pos[0]][pos[1]] = count
    count += 1

    return count

#corresponding number 5
def down_right(pos, board_data, count):
    pos[0] += 2
    pos[1] += 1

    board_data[pos[0]][pos[1]] = count
    count += 1

    return count

#corresponding number 6
def down_left(pos, board_data, count):
    pos[0] += 2 
    pos[1] -= 1

    board_data[pos[0]][pos[1]] = count
    count += 1

    return count

#corresponding number 7
def left_down(pos, board_data, count):
    pos[0] += 1
    pos[1] -= 2

    board_data[pos[0]][pos[1]] = count
    count += 1

    return count

#corresponding number 8
def left_up(pos, board_data, count):
    pos[0] -= 1
    pos[1] -= 2

    board_data[pos[0]][pos[1]] = count
    count += 1

    return count

def random_method(pos, board_data):

    count = 1
    board_data[pos[0]][pos[1]] = count
    count += 1

    num = possible(pos, board_data)

    while count <= 64 or len(num) == 0:

        num = possible(pos, board_data)

        if len(num) == 0:
            printBoard(board_data)
            #Have to subtract since there is an overcount of 1
            count -= 1
            print("Amount of moves made:",count)
            if count >= 64:
                return 1
            
            print("Out of possible moves. Tour Over")
            return 1

        # the program will randomly pick the knights path based on index values of the num list
        rnum = random.randint(0, len(num)-1)
        if num[rnum] == 1:
            count = up_left(pos, board_data, count)

        if num[rnum] == 2:
            count = up_right(pos, board_data, count)

        if num[rnum] == 3:
            count = right_up(pos, board_data, count)

        if num[rnum] == 4:
            count = right_down(pos, board_data, count)
         
        if num[rnum] == 5:
            count = down_right(pos, board_data, count)
         
        if num[rnum] == 6:
            count = down_left(pos, board_data, count)
         
        if num[rnum] == 7:
            count = left_down(pos, board_data, count)
         
        if num[rnum] == 8:
            count = left_up(pos, board_data, count)

    printBoard(board_data)
         
                    
def printBoard(board_data):
    global BOARD
    # Strings are immutable so I must convert the board string to a list then convert it back
    board_list = list(BOARD)


    for i in range(8):
        for j in range(8):
            if board_data[i][j] < 10:
                board_list[1 + ((15-2*i)*36 ) + (4+4*j)] = str(board_data[i][j])
            else:
                #once the count goes to the double digits there is no way to center it so I just align it left of the box
                board_list[1 + ((15-2*i)*36 ) + (4+4*j)] = str(board_data[i][j])[0]
                board_list[1 + ((15-2*i)*36 ) + (4+4*j) + 1] = str(board_data[i][j])[1]
                
    BOARD = ''.join(board_list)

    print(BOARD)


if __name__ == '__main__':

    # pos[0 , 1] = pos[y, x]
    # stores info that tells the program if the knight has visited the square before
    board_data = [[0]*8 for i in range(8)]

    print("How do you want to do the knights tour.\n ")
    print("1. Random")
    print("2. Other method")

    ans = str(input("Pick one: "))
    ans = ans.lower()

    if ans == '1' or 'random':

        # print the board
        print(BOARD)
        # find out where the user wants to start
        str_pos = str(input("Where on the chess board do you want to start the tour? ")).lower()

        pos = [0,0]
        # Example: d4(xy)
        pos[0] = int(str_pos[1]) - 1

        #I need to convert the letters to numbers
        decode = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}
        pos[1] = decode[str_pos[0]]
        random_method(pos,board_data)

    elif ans == '2' or 'other method':
        print("To be made")
    else:
        print("Error: pick an avaliable option")

