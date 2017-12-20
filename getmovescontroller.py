from walkmove import WalkMove
from dropplankmove import DropPlankMove 
from pickupplankmove import PickupPlankMove

class GetMovesController:

  def __init__(self):
    self.board = board

  def getMoves(board):
    return []

  def getWalkMoves(board):
    player_pos = board.get_player().get_loc()
    planks = board.get_planks()

    possible_walks = []
    for plank in planks:
      end_pts = plank.get_points()
      if end_pts[0] == player_pos:
        possible_walks.append(WalkMove(board, end_pts[1]))
      elif end_pts[1] == player_pos:
        possible_walks.append(WalkMove(board, end_pts[0]))

    return possible_walks

  def getPlankMoves(board):
    plank_moves = []
    player = board.get_player()
    if player.is_holding_plank():
      plank = player.get_plank()
      for stump in board.get_stumps():
        try:
          if plank.calc_length(stump, player.get_loc()) == plank.length:
            plank_moves.append(DropPlankMove(board, stump))
        except:
          pass

    else:
      player_pos = player.get_loc()
      for plank in board.get_planks():
        end_pts = plank.get_points()
        if (end_pts[0] == player_pos) or (end_pts[1] == player_pos):
          plank_moves.append(PickupPlankMove(board, plank))

    return plank_moves
