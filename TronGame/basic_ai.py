import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class basic_ai:

    def __init__(self):
        self.current_command_index = 0
        self.commands = [(1, 0), (0, -1), (-1, 0), (-1, 0)]

        self.valid_position = []
        for i in range(30):
            arr = []
            for i in range(20):
                arr.append(True)
            self.valid_position.append(arr)

    def isValidMove(self, current_position, direction):
        next_x = current_position[0] + direction[0]
        next_y = current_position[1] + direction[1]
        if next_x < 0 or next_x == len(self.valid_position):
            return False
        if next_y < 0 or next_y == len(self.valid_position[next_x]):
            return False
        return self.valid_position[next_x][next_y]


    # game loop
    def next_move(self, num_players, player_number, player_coordinates):

        for coords in player_coordinates.values():
            self.valid_position[coords[0]][coords[1]] = False

        myX, myY = player_coordinates[player_number]

        attempts = 0
        while attempts < 4 and not self.isValidMove((myX, myY), self.commands[self.current_command_index]):
            print(self.commands[self.current_command_index], " was decreed invalid", file=sys.stderr)
            self.current_command_index = (self.current_command_index + 1) % 4
            attempts += 1

        return self.commands[self.current_command_index]