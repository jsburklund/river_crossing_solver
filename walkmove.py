class WalkMove:

  def __init__(self, board, end_loc):
    if not board.valid_player_loc(end_loc):
      raise ValueError('Not a valid player location') 
    self.new_loc = end_loc
    self.board = board

  def execute(self):
    self.board.move_player(self.new_loc)
