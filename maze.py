from cell import cell
import movements

class Maze:
    def __init__(self, rows, cols) -> None:
        maze = [[None for i in range(cols)] for j in range(rows)]
        self.rows = rows
        self.cols = cols

        for i in range(cols):
            for j in range(rows):
                maze[i][j] = cell(i+1, j+1)

        self.position = 1+1j
        self.orientation = 0 + 1j #j-cap

    def show_position_orientation(self):
        print("position: ", self.position.real, ", ", self.position.imag)
        print("orientation: ", self.orientation)

    def move_fwd(self):
        self.position += self.orientation
        movements.fwd() #command to actually move the micromouse

    def turn_left(self):
        self.orientation *= 1j
        movements.left() #command to actually move the micromouse

    def turn_right(self):
        self.orientation *= -1j
        movements.right() #command to actually move the micromouse

    def move_bwd(self):
        self.position -= self.orientation
        movements.bwd() #command to actually move the micromouse

    def block_north(self):
        self.maze[self.position.real - 1][self.position.imag - 1].block_north()

    def block_south(self):
        self.maze[self.position.real - 1][self.position.imag - 1].block_south()

    def block_east(self):
        self.maze[self.position.real - 1][self.position.imag - 1].block_east()

    def block_west(self):
        self.maze[self.position.real - 1][self.position.imag - 1].block_west()