class PickupPlankMove:

  def __init__(self, board, plank):
    self.board = board
    self.plank = plank

  def execute(self):
    self.board.remove_plank(self.plank)
    self.board.player.hold(self.plank)
