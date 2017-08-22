import board
import plank

class BoardFactoryPack1:
  def make_board(puzzlenum):
   if puzzlenum not in range(1,40+1):
     raise ValueError('Not a valid puzzle Number')
   if puzzlenum in range(2,40+1):
     raise ValueError('Puzzle not yet implemented')
   if puzzlenum == 1:
     return board.Board([(1,4),(1,3),(3,3),(3,2),], (1,6), (3,0), [plank.Plank(1,(1,4),(1,3)), plank.Plank(2,(1,6),(1,4))])
