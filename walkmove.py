from copy import deepcopy

class WalkMove:

  def __init__(self, board, end_loc):
    self.board = deepcopy(board)
    if not self.board.valid_player_loc(end_loc):
      raise ValueError('Not a valid player location') 
    self.new_loc = end_loc

  def execute(self):
    self.board.move_player(self.new_loc)
    return self.board
