from copy import deepcopy

class NullMove():
  def __init__(self, board):
    self.board = deepcopy(board)

  def execute(self):
    return self.board
