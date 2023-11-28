#!/usr/bin/python3
import sys

def isSafe(board, row, col, N, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
    if (slashCodeLookup[slashCode[row][col]] or backslashCodeLookup[backslashCode[row][col]] or rowLookup[row]):
        return False
    return True

def solveNQueensUtil(board, col, N, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup, res):
    if (col == N):
        v = []
        for i in range(N):
            s = ""
            for j in range(N):
                if (board[i][j] == 1):
                    s += str([i, j])
            v.append(s)
        res.append(v)
        return True
    resFlag = False
    for i in range(N):
        if (isSafe(board, i, col, N, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup)):
            board[i][col] = 1
            rowLookup[i] = True
            slashCodeLookup[slashCode[i][col]] = True
            backslashCodeLookup[backslashCode[i][col]] = True
            resFlag = solveNQueensUtil(board, col + 1, N, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup, res) or resFlag
            board[i][col] = 0
            rowLookup[i] = False
            slashCodeLookup[slashCode[i][col]] = False
            backslashCodeLookup[backslashCode[i][col]] = False
    return resFlag

def solveNQueens(N):
    if (N < 4):
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for i in range(N)] for j in range(N)]
    slashCode = [[0 for i in range(N)] for j in range(N)]
    backslashCode = [[0 for i in range(N)] for j in range(N)]
    rowLookup = [False] * N
    slashCodeLookup = [False] * (2 * N - 1)
    backslashCodeLookup = [False] * (2 * N - 1)
    for rr in range(N):
        for cc in range(N):
            slashCode[rr][cc] = rr + cc
            backslashCode[rr][cc] = rr - cc + (N - 1)
    res = []
    solveNQueensUtil(board, 0, N, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup, res)
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j] = "[" + res[i][j] + "]"
        print(res[i])
