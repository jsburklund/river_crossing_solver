from boardfactory import BoardFactoryPack1
from copy import deepcopy
from getmovescontroller import GetMovesController
from boardviewterminal import BoardViewTerminal

# A copy of a board should be the same
board1 = BoardFactoryPack1.make_board(1)
board2 = deepcopy(board1)

print("Deep copy: "+str(board1==board2))

# Same generated board should be the same
board1 = BoardFactoryPack1.make_board(1)
board2 = BoardFactoryPack1.make_board(1)
print("Same factory: "+str(board1==board2))

# Same instance should be the same
board1 = BoardFactoryPack1.make_board(1)
board2 = board1
print("Same instance: "+str(board1==board2))

# Moving the player manually should be the same as moving the player with a move
board1 = BoardFactoryPack1.make_board(1)
walkmove = GetMovesController.getMoves(board1)[0]
board2 = walkmove.execute()
board1.move_player((1,4))
print("Manual move: "+str(board1==board2))

# Holding the same board in different locations should be different
board1 = BoardFactoryPack1.make_board(1)
walkmove = GetMovesController.getMoves(board1)[0]
board1 = walkmove.execute()
pickup_move = GetMovesController.getMoves(board1)[2]
walk_move = GetMovesController.getMoves(board1)[0]
board1 = pickup_move.execute()
board2 = walk_move.execute()
pickup_move = GetMovesController.getMoves(board2)[1]
board2 = pickup_move.execute()
boardview = BoardViewTerminal()
boardview.draw(board1)
boardview.draw(board2)
print("Pickup different loc not equal: "+str(board1!=board2))
