from player import Player

class Board:
  planks = []
  stumps = []
  size = (5,7)

  def __init__(self, stumps, start_stump, end_stump, planks):
    self.stumps = stumps
    if (start_stump not in self.stumps):
      self.stumps.append(start_stump)
    if (end_stump not in self.stumps):
      self.stumps.append(end_stump)
    self.planks = planks
    self.player = Player(start_stump)

  # Stumps implemented as a simple tuples
  def get_stumps(self):
    return self.stumps

  def get_planks(self):
    return self.planks

  def get_size(self):
    return self.size

  def get_player(self):
    return self.player

  def move_player(self, new_loc):
    # Check that the new position is valid
    if not self.valid_player_loc(new_loc):
      raise ValueError('New player location is not on a stump')
    self.player.set_loc(new_loc)

  def valid_player_loc(self, player_loc):
    return player_loc in self.get_stumps()

  def remove_plank(self, plank):
    if plank not in self.planks:
      raise ValueError('Not a plank in the current board set')
    self.planks.remove(plank)

  def add_plank(self, plank):
    if plank in self.planks:
      raise ValueError('Plank already on the board')
    self.planks.append(plank)
