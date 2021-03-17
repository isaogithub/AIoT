theBoard = {"topL":" ","topM":" ","topR":" ",
            "midL":" ","midM":" ","midR":" ",
            "botL":" ","botM":" ","botR":" "}

def printBoard(board):
    print(board["topL"]+'|'+board["topM"]+'|'+board["topR"])
    print("-+-+-")
    print(f'{board["midL"]}|{board["midM"]}|{board["midR"]}')
    print("-+-+-")
    print("{0}|{1}|{2}".format(board["botL"],board["botM"],board["botR"]))
printBoard(theBoard)

def NumtoBoard(num):
    ls = ["topL","topM","topR",
          "midL","midM","midR",
          "botL","botM","botR"]
    return ls[num - 1]

def validInput(input):
    try:
        temp = int(input)
        return True
    except:
        return False

turn = "X"
for i in range(9):
    printBoard(theBoard)
    print(f'Turn for{turn},Move on which space?')
    move = input(">> ")
    #if(move != "X"||move != "O"):
    while True:
        if not validInput(move):
            print(f'Turn for {turn}. move on which space?')
            move = input(">> ")
        if int(move) > 0 and int(move) < 10:
            if theBoard[NumtoBoard(int(move))] == ' ':
                break
            else:
                print(f'Invalid movement.Turn for {turn} . Move on which space?')
                move = input(">> ")
        else:
            print(f"Invalid movement.Turn for {turn} . Move on which space?")
            move = input (">> ")
    theBoard[NumtoBoard(int (move))] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = "X"
printBoard(theBoard) 



