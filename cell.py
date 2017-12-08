

class Cell(object):

    def __init__(self):
        self.status = 'dead'
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.live_cell_neighbourgh = 0

    def get_status(self):
        return self.status

    def is_live_left(self):
        if self.left is None:
            return False
        else:
            if self.left.get_status() == 'live':
                return True
            else:
                return False

    def has_right(self):
        if self.right is None:
            return False
        else:
            if self.right.get_status() == 'live':
                return True
            else:
                return False

    def has_up(self):
        if self.up is None:
            return False
        else:
            if self.up.get_status() == 'live':
                return True
            else:
                return False

    def has_down(self):
        if self.down is None:
            return False
        else:
            if self.down.get_status() == 'live':
                return True
            else:
                return False

    def is_control(self, cell):
        if cell.get_status() == 'live':
            self.live_cell_neighbourgh++
        if self.live_cell_neighbourgh > 2:
            self.status = 'live'

    def set_left(self, cell):
        self.is_control(cell)
        self.left = cell

    def set_right(self, cell):
        self.is_control(cell)
        self.right = cell

    def set_up(self, cell):
        self.is_control(cell)
        self.up = cell

    def set_down(self, cell):
        self.is_control(cell)
        self.down = cell


if __name__ == '__main__':
    cell = new Cell()
    print cell.get_status()