import game

board = game.game()
game.create(board)
print("Initial Game")
game.printState(board)
game.decideWhoIsFirst(board)
while not game.isFinished(board):
    print("continue game")
    if game.isHumTurn(board):
        game.inputMove(board)
    else:

        # board=game.inputComputer(board)
        game.inputMove(board)  # so i can play aginst my self
    game.printState(board)

print("Game Over:")

