from boardfactory import BoardFactoryPack1
from getmovescontroller import GetMovesController
from boardviewterminal import BoardViewTerminal

def main():
  print("Hello World")

if __name__ == "__main__":
  board_drawer = BoardViewTerminal()
  board = BoardFactoryPack1.make_board(1)
  board_drawer.draw(board)
  
  # Do the move to walk accross the long plank
  my_moves = GetMovesController.getMoves(board)
  print(my_moves)
  my_moves[0].execute()
  board_drawer.draw(board)


  # Do the move to pickup the long plank
  my_moves = GetMovesController.getMoves(board)
  print(my_moves)
  my_moves[3].execute()
  board_drawer.draw(board)

  # Do the move to walk across the short plank
  my_moves = GetMovesController.getMoves(board)
  print(my_moves)
  my_moves[0].execute()
  board_drawer.draw(board)

  # Do the move to place the long plank down
  my_moves = GetMovesController.getMoves(board)
  print(my_moves)
  my_moves[1].execute()
  board_drawer.draw(board)

  # Do the move to pickup the short plank
  my_moves = GetMovesController.getMoves(board)
  print(my_moves)
  my_moves[2].execute()
  board_drawer.draw(board)

  # Do the move to walk across the long plank
  my_moves = GetMovesController.getMoves(board)
  print(my_moves)
  my_moves[0].execute()
  board_drawer.draw(board)

  # Do the move to place the short plank
  my_moves = GetMovesController.getMoves(board)
  print(my_moves)
  my_moves[1].execute()
  board_drawer.draw(board)

  # Do the move to pickup up the long plank
  my_moves = GetMovesController.getMoves(board)
  print(my_moves)
  my_moves[2].execute()
  board_drawer.draw(board)

  # Do the move to walk across the short plank
  my_moves = GetMovesController.getMoves(board)
  print(my_moves)
  my_moves[0].execute()
  board_drawer.draw(board)

  # Do the move to place the long plank
  my_moves = GetMovesController.getMoves(board)
  print(my_moves)
  my_moves[1].execute()
  board_drawer.draw(board)

  # Walk to the goal
  my_moves = GetMovesController.getMoves(board)
  print(my_moves)
  my_moves[1].execute()
  board_drawer.draw(board)

  if board.complete():
    print("Success!")
