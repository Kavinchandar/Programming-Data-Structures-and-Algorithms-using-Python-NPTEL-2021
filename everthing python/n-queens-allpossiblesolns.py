import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

count = []


def Initialize(n, board):
    for key in ['queen', 'row', 'col', 'd1', 'd2']:
        board[key] = {}
    for i in range(n):
        board['queen'][i] = -1
        board['row'][i] = 0
        board['col'][i] = 0
    for i in range(0, 2*(n+1)):
        board['d1'][i] = 0
    for i in range(-(n-1), n):
        board['d2'][i] = 0


def free(i, j, board):
    return(board['row'][i] == 0 and board['col'][j] == 0 and board['d1'][i+j] == 0 and board['d2'][i-j] == 0)


def addqueen(i, j):
    board['queen'][i] = j
    board['row'][i] = 1
    board['col'][j] = 1
    board['d1'][i+j] = 1
    board['d2'][i-j] = 1


def undoqueen(i, j):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['col'][j] = 0
    board['d1'][i+j] = 0
    board['d2'][i-j] = 0


def placequeen(i):
    n = len(board['queen'].keys())
    for j in range(n):
        if free(i, j, board):
            addqueen(i, j)
            if i == n-1:
                printboard(board)

            else:
                placequeen(i+1)
            undoqueen(i, j)


def printboard(board):
    count.append(1)
    lst = []
    n = len(board['queen'].keys())
    for x in range(n):
        lst.append((x, board['queen'][x]))

    matrix = []
    for i in range(n):
        inner = []
        for j in range(n):
            if(i, j) == lst[i]:
                inner.append(1)
            else:
                inner.append(0)
        matrix.append(inner)
    print(matrix)
    """
    sns.heatmap(matrix, linewidth=0.5, cbar=False,
                xticklabels=False, yticklabels=False)
    plt.show()
    """


board = {}
n = int(input("Enter Number of Queens: "))
Initialize(n, board)
if placequeen(0):
    printboard(board)
print(len(count))
