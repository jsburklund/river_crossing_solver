from walkmove import WalkMove
from dropplankmove import DropPlankMove 
from pickupplankmove import PickupPlankMove

class GetMovesController:

  def __init__(self):
    self.board = board

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
          my_len = plank.length
          if plank.calc_length(stump, player.get_loc()) == plank.length:
            # Check if there are any stumps in the way
            if stump[0] == player.get_loc()[0]:
              low_end = min(stump[1], player.get_loc()[1])
              high_end = max(stump[1], player.get_loc()[1])
              between_stumps = [(stump[0], i) for i in range(low_end+1, high_end)]
            else: 
              low_end = min(stump[0], player.get_loc()[0])
              high_end = max(stump[0], player.get_loc()[0])
              between_stumps = [(i,stump[1]) for i in range(low_end+1, high_end)]
            blocking = False
            for test_stump in between_stumps:
              if test_stump in board.get_stumps():
                blocking = True
                break

            # Check if this plank crosses others
            if not blocking:
              for my_plank in board.get_planks():
                end_near = my_plank.get_point_closest_origin()
                end_far = my_plank.get_point_furthest_origin()
                if my_plank.is_horizontal():
                  pts = [(i, end_near[1]) for i in range(end_near[0]+1, end_far[0])]
                else:
                  pts = [(end_near[0], i) for i in range(end_near[1]+1, end_far[1])]
                for pt in pts:
                  if pt in between_stumps:
                    blocking = True
                    break
                if blocking: # break early
                   break

            # Only add the point if both the stump and plank check have succeeded
            if not blocking:
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


  def getMoves(board):
    moves = GetMovesController.getWalkMoves(board)
    moves.extend(GetMovesController.getPlankMoves(board))
    return moves

