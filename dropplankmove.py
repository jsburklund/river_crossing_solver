from copy import deepcopy

class DropPlankMove:
  def __init__(self, board, new_end):
    self.board = deepcopy(board)
    self.new_end = new_end

  def execute(self):
    player = self.board.get_player()
    plank = player.drop()
    plank.move_plank(self.new_end, player.get_loc())
    self.board.add_plank(plank)
    return self.board
