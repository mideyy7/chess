"""
    This is the driver file and is responsible for getting user input

"""

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

"""
Initialize a global dictionary of images
"""
def loadImages():
    pieces = ["wP","wR","wB","wN","wK","wQ","bP","bR","bB","bN","bK","bQ"]
    for piece in pieces:
        IMAGES[piece] = p.image.load("images/" + piece + ".png")

# loadImages()
# print(IMAGES)


def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    # print(gs.board)
    loadImages()
    drawGameState(screen,gs)
    validMoves = gs.getValidMoves()
    moveMade = False  #flag for when a move is made
    sqSelected = ()  #no square selected.. to keep track of last click of the user
    playerClicks = [] #keep track of player clicks
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row,col):    #if user selects the same square it means undo
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    move = ChessEngine.Move(playerClicks[0],playerClicks[1],gs.board)
                    print(move.getChessNotation)
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                    sqSelected = ()
                    playerClicks = []
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = False
        # clock.tick(MAX_FPS)
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False
        drawGameState(screen,gs)
        p.display.flip()

"""
Responsible for all graphics within a current game state

"""
def drawGameState(screen, gs):
    drawBoard(screen)  #draws squares on the board
    drawPieces(screen, gs.board)    #draw pieces on top of the squares

def drawBoard(screen):
    colors = [p.Color("white"),p.Color("gray")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            if (row + col) % 2 == 0:
                color = colors[0]
            else:
                color = colors[1]
            p.draw.rect(screen,color,p.Rect(col*SQ_SIZE,row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen,board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()
