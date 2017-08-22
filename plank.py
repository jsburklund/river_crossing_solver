class Plank:
  plank_lengths = [1,2,3]

  def calc_length(self, to_loc, from_loc):
    if to_loc[0] == from_loc[0]:
      return abs(to_loc[1] - from_loc[1])
    elif to_loc[1] == from_loc[1]:
      return abs(to_loc[0] - from_loc[0])
    else:
      raise ValueError('To and from points not in a cardinal direction')


  def __init__(self, length, to_loc, from_loc):
    if self.calc_length(to_loc, from_loc) != length:
      raise ValueError('Length does not match distance between to and from points')
    if length not in self.plank_lengths:
      raise ValueError('Not a standard plank length')
    self.length = length
    self.to_loc = to_loc
    self.from_loc = from_loc

  def move_plank(new_to, new_from):
    if self.calc_length(new_to, new_from) != length:
      raise ValueError('Length does not match distance between new points')
    self.to_loc = new_to
    self.from_loc = new_from

  def get_points(self):
    return (self.to_loc, self.from_loc)

  def get_point_closest_origin(self):
    # Assumes any errors have been caught by set methods
    if self.to_loc[0] == self.from_loc[0]:
      if self.to_loc[1] < self.from_loc[1]:
         return self.to_loc
      else:
         return self.from_loc
    else:
      if self.to_loc[0] < self.from_loc[0]:
         return self.to_loc
      else:
         return self.from_loc

  def is_horizontal(self):
    # Return true if the y heights are the same
    # Assumes set methods have caught any errors
    return (self.to_loc[1] == self.from_loc[1])

  def is_vertical(self):
    # Return true if the x heights are the same
    return (self.to_loc[0] == self.from_loc[0])

  def get_length(self):
    return self.length
