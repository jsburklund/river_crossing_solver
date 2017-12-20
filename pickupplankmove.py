from copy import deepcopy

class PickupPlankMove:

  def __init__(self, board, plank):
    self.board = deepcopy(board)
    # Get the respective plank in the copied board
    plank_idx = board.get_planks().index(plank)
    self.plank = self.board.get_planks()[plank_idx]

  def execute(self):
    self.board.remove_plank(self.plank)
    self.board.player.hold(self.plank)
    return self.board
