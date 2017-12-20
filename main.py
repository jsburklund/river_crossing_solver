from boardfactory import BoardFactoryPack1
from getmovescontroller import GetMovesController
from boardviewterminal import BoardViewTerminal

def main():
  print("Hello World")

if __name__ == "__main__":
  board_drawer = BoardViewTerminal()
  board = BoardFactoryPack1.make_board(1)
  print('Test Walk moves')
  my_moves = GetMovesController.getWalkMoves(board)
  board_drawer.draw(board)
  my_moves[0].execute()
  board_drawer.draw(board)

  print('Test pickup')
  board = BoardFactoryPack1.make_board(1)
  # Should get a move to pickup the plank
  my_moves = GetMovesController.getPlankMoves(board)
  board_drawer.draw(board)
  print('Pickup moves')
  my_moves[0].execute()
  board_drawer.draw(board)

  print('Test Drop')
  # Should get a move to place the plank
  my_moves = GetMovesController.getPlankMoves(board)
  print(my_moves)
  my_moves[0].execute()
  board_drawer.draw(board)
