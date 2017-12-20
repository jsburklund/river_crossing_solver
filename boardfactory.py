from board import Board
from plank import Plank

class BoardFactoryPack1:
  def make_board(puzzlenum):
   if puzzlenum not in range(1,40+1):
     raise ValueError('Not a valid puzzle Number')
   if puzzlenum in range(3,40+1):
     raise ValueError('Puzzle not yet implemented')

   puzzles = {
     1: Board([(1,4),(1,3),(3,3),(3,2),], (1,6), (3,0), [Plank(1,(1,4),(1,3)), Plank(2,(1,6),(1,4))]),
     2: Board([(4,1),(4,2),(2,2),(2,3),(2,4),(0,4),(0,5)], (0,6), (4,0), [Plank(2,(4,2),(2,2)), Plank(2,(0,4),(2,4)), Plank(1,(0,6),(0,5))]),
   }
   return puzzles[puzzlenum]
   
