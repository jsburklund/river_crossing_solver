class DropPlankMove:
  def __init__(self, board, new_end):
    self.board = board
    self.player = board.get_player()
    self.new_end = new_end

  def execute(self):
    plank = self.player.drop()
    plank.move_plank(self.new_end, self.player.get_loc())
    self.board.add_plank(plank)
