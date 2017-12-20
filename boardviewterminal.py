class BoardViewTerminal:
  def draw(self, board):
    size = board.get_size()
    temp = []
    # Board is size*2 to draw planks in between
    for i in range(size[1]*2):
      temp_row = []
      for j in range(size[0]*2):
        temp_row.append('  ')
      temp.append(temp_row)

    #Draw the stumps first
    for stump in board.get_stumps():
      temp[stump[1]*2][stump[0]*2] = 'x '

    #Draw the planks
    for plank in board.get_planks():
      start_point = plank.get_point_closest_origin()
      #Convert length to 0 based for easy drawing
      length = plank.get_length()-1
      if plank.is_horizontal():
        #Plank is horizontal
        for i in range((length*2)+1):
          temp[start_point[1]*2][(start_point[0]*2)+i+1] = '- '
      else:
        #Plank is vertical
        for i in range((length*2)+1):
          temp[(start_point[1]*2)+i+1][start_point[0]*2] = '| '

    #Draw the player
    player_loc = board.get_player().get_loc()
    temp[player_loc[1]*2][player_loc[0]*2] = 'P '

    # Render everything
    str = '--' + '--'*size[0]*2 + '-\n'
    str += '| ' + '    '*size[0] + '|\n'
    for row in temp:
      str += '| '
      for col in row:
        str += col
      str += '|\n'
    # buffer row is already drawn as artifact
    str += '--' + '--'*size[0]*2 + '-'
    print(str)

if __name__ == '__main__':
  import boardfactory
  my_factory = boardfactory.BoardFactoryPack1
  test = my_factory.make_board(1)
  my_drawer = BoardViewTerminal()
  my_drawer.draw(test)
