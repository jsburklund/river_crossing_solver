from boardfactory import BoardFactoryPack1
from getmovescontroller import GetMovesController
from boardviewterminal import BoardViewTerminal
from solver import Solver


def main():
  print("Hello World")

if __name__ == "__main__":
  board_drawer = BoardViewTerminal()
  board = BoardFactoryPack1.make_board(2)
  board_drawer.draw(board)
  my_solver = Solver(board)

  moves = my_solver.solve()
  moves = moves
  for move in moves:
    board_drawer.draw(move.board)
