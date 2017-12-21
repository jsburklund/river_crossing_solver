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
    self.end_stump = end_stump

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

  def complete(self):
    return self.player.get_loc() == self.end_stump
  
  def __eq__(self, other):
    if self is other:
      return True
    if isinstance(self, other.__class__):
      is_player_loc_same = self.get_player().get_loc() == other.get_player().get_loc()
      try:
        is_player_holding_same = self.get_player().get_plank().get_length() == other.get_player().get_plank().get_length()
      except:
        is_player_holding_same = self.get_player().get_plank()==None and other.get_player().get_plank()==None
      # Check if the same length planks are in the same locations
      my_dict = self.get_plank_dict()
      your_dict = other.get_plank_dict()
      is_planks_same = True
      for key in my_dict.keys():
        for plank_loc in my_dict[key]:
          if plank_loc not in your_dict.get(key, []):
            is_planks_same = False
            break
        if not is_planks_same:
          break
      return is_player_loc_same & is_player_holding_same & is_planks_same
    # Not the same instance, so can't be the same
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  def get_plank_dict(self):
    plank_dict = {}
    for plank in self.planks:
      key_val = plank_dict.get(plank.get_length(), [])
      key_val.append([plank.get_point_closest_origin(), plank.get_point_furthest_origin()])
      plank_dict[plank.get_length()] = key_val
    return plank_dict
