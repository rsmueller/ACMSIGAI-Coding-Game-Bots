from random import randint
class environment:

    def random_position(self):
        # randint is inclusive, inclusive
        return randint(0, self.width - 1), randint(0, self.length - 1)

    def __init__(self, players = 2):
        # false is empty, true is filled
        self.width = 30
        self.length = 20
        self.grid = [[False for j in range(self.length)] for i in range(self.width)]
        self.player_coordinates = dict()
        self.dead_players = set()
        # each player assigned to a random position
        for player in range(players):
            # just set coord to first element
            coord = self.random_position()
            while coord in self.player_coordinates.values():
                coord = self.random_position()
            self.player_coordinates[player] = coord

        for coord in self.player_coordinates.values():
            x, y = coord
            self.grid[x][y] = True

    # direction is a tuple pair of -1, 1, or 0, where one is 0
    # player is an index integer of player_coordinates
    def move(self,player, direction):
        c_x, c_y = self.player_coordinates[player]
        self.grid[c_x][c_y] = True

        d_x, d_y = direction
        new_coord = (c_x + d_x, c_y + d_y)

        # if the new position is filled
        if self.grid[new_coord[0]][new_coord[1]]:
            self.dead_players.add(player)
        else:
            self.player_coordinates[player] = new_coord

    def render(self):
        disp = {False:' ', True:'X'}
        render_grid = [[ disp[self.grid[x][y]] for y in range(self.length)] for x in range(self.width)]
        for player, coord in enumerate(self.player_coordinates.values()):
            render_grid[coord[0]][coord[1]] = str(player+1)
        for row in render_grid:
            row.append('\n')
        return ''.join([''.join(row) for row in render_grid])