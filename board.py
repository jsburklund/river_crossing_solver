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
    self.player_loc = start_stump

  def print_stumps(self):
    print(self.stumps)

  def print_planks(self):
    print(self.planks)

  def get_stumps(self):
    return self.stumps

  def get_planks(self):
    return self.planks

  def get_size(self):
    return self.size

  def get_player_loc(self):
    return self.player_loc
