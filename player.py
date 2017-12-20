class Player:

  def __init__(self, start_pos):
    self.pos = start_pos
    self.holding = None

  def hold(self, plank):
    self.holding = plank

  def drop(self):
    plank = self.holding
    self.holding = None
    return plank

  def get_plank(self):
    return plank

  def is_holding_plank(self):
    return plank != None

  def get_loc(self):
    return self.pos

  def set_loc(self, new_pos):
    self.pos = new_pos
