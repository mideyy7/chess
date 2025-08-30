"""
    Restoring information about the current state of a chess game.
    Determining the valid moves
    Keeping a move log

"""

class GameState:
    def __init__(self):
        #board is a 8x8 grid with each cell contating 2 characters.
        #1st char is colour and 2nd char is the piece type
        # -- represents empty space with no piece
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]

        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self,move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove

    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove


    def getValidMoves(self):
        return self.getAllPossibleMoves()

    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == "w" and self.whiteToMove) and (turn == "b" and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == "P":
                        self.getPawnMoves(r,c,moves)
                    elif piece == "R":
                        self.getRookMoves(r,c,moves)
                    elif piece == "B":
                        self.getBishopkMoves(r,c,moves)
                    elif piece == "N":
                        self.getKnightMoves(r,c,moves)
                    elif piece == "Q":
                        self.getQueenMoves(r,c,moves)
                    elif piece == "K":
                        self.getKingMoves(r,c,moves)
        return moves
                    

    def getPawnMoves(self, r, c , move):
        pass

    def getRookMoves(self, r, c , move):
        pass

    def getBishopMoves(self, r, c , move):
        pass

    def getKnightMoves(self, r, c , move):
        pass

    def getQueenMoves(self, r, c , move):
        pass

    def getKingMoves(self, r, c , move):
        pass



class Move:

    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2,  "7": 1, "8": 0}
    rowsToRanks = {v:k for k,v in ranksToRows.items()}   
    
    filesToCols = {"a": 0, "b": 1 ,"c": 2, "d": 3, "e": 4, "f": 5,  "g": 17, "h": 8}
    colsToFiles = {v:k for k,v in filesToCols.items()}


    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.col * 100 + self.endRow * 10 + self.endCol



        """
        Overriding the equals method
        """
    def __eq__(self,other):
        if isinstance(other, Move):
            return self.moveID == other.moveID


    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol)


    def getRankFile(self,r,c):
        return self.colsToFiles[c] + self.rowsToRanks[r]

