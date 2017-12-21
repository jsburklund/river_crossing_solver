from getmovescontroller import GetMovesController
from queue import Queue
from boardviewterminal import BoardViewTerminal

class MultiMoveTree:
  def __init__(self, move, parent, children):
    self.move = move
    self.children = children
    self.parent = parent

class Solver:

  def __init__(self, board):
    if board == None:
      raise ValueError('Null board object')

    self.board = board



  def unwind_tree(self, tree_item):
    actions = []
    curr_tree = tree_item
    while curr_tree.parent != None:
      actions.append(curr_tree.move)
      curr_tree = curr_tree.parent
    return actions

  def solve(self):
    # Bootstrap the search with the first items to evaulaute
    to_evaluate = Queue()
    evaluated = Queue()
    seen_boards = [self.board]
    getMoves = GetMovesController.getMoves

    for move in getMoves(self.board):
      to_evaluate.put_nowait(MultiMoveTree(move, None, None))

    bv = BoardViewTerminal()
    while not to_evaluate.empty():
      print(to_evaluate.qsize())
      # Get the next move to evaluate
      my_move_tree = to_evaluate.get_nowait()
      # Execute the move and check if the move completes the game
      new_board = my_move_tree.move.execute()

      # If this move completes the game, we're done
      if new_board.complete():
        print("Found solution")
        return self.unwind_tree(my_move_tree)

      # Check that the mutated board state hasn't already been evaluated
      if len([seen_board for seen_board in seen_boards if new_board == seen_board]) > 0:
        continue
      seen_boards.append(new_board)

      # Otherwise, get a list of all possible next moves
      my_children = [MultiMoveTree(next_move, my_move_tree, None) for next_move in getMoves(new_board)]

      # Add the children to this tree node
      my_move_tree.children = my_children 
      # Add all the children actions to the list to evaluate
      for child in my_children:
        to_evaluate.put_nowait(child)

      # Save this object
      evaluated.put_nowait(my_move_tree)
      

    print("No solutions found")
    return [None]
