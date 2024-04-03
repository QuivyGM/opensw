#      |   | 
#   ---+---+---
#      |   |
#   ---+---+---
#      |   |

board= [[' ' for x in range (3)] for y in range(3)]

while True:
#게임보드를그린다.
    for r in range(3):
        print("  " + board[r][0] + "|  " + board[r][1] + "|   " + board[r][2])
        if (r != 2):
            print("---|---|---")

    x = int(input("다음수의x좌표를입력하시오: "))
    y = int(input("다음수의y좌표를입력하시오: "))

    if board[x][y] != ' ':
        print("잘못된위치입니다. ")
        continue
    else:
        board[x][y] = 'X'

    done =False
    for x  in range(3): 
        for y in range(3): 
            if board[x][y] == ' 'and not done:
                board[x][y] = 'O'
                done = True
                break

    win = 0
    for x  in range(3): 
        if board[x][0] == board[x][1] == board[x][2] and board[x][0] != ' ':
            if board[x][0] == 'X':
                win = 1
            else:
                win = 2

    for y in range(3):
        if board[0][y] == board[1][y] == board[2][y] and board[0][y] != ' ':
            if board[0][y] == 'X':
                win = 1
            else:
                win = 2

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        if board[0][0] == 'X':
                win = 1
        else:
            win = 2

    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != ' ':
        if board[2][0] == 'X':
                win = 1
        else:
            win = 2



    if win == 1:
        print("!!! You Won !!!")
        break
    if win == 2:
        print("!!! PC Won !!!")
        break