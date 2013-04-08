
class Cell:
    ext_wall = 'exterior-wall'
    wooden_wall = 'wooden-wall'
    steel_wall = 'steel-wall'
    concrete_wall = 'concrete-wall'
    blank = 'blank'
    doors = 'doors'
    window = 'window'
    pit = 'pit'
    generator = 'generator'
    wire = 'wire'
    wired_wooden_wall = 'wired-wooden-wall'
    pressure_switch_off = 'pressure_switch_off'
    pressure_switch_on = 'pressure_switch_on'
    sticking_switch = 'sticking_switch'
    rotary_switch = 'rotary-switch'
    wire_bridge = 'wire_bridge'
    voltage_switch = "voltage-switch"
    voltage_switch_inverted = 'voltage-switch-inverted'
    powered_door = 'powered-door'
    electric_floor = 'electric-floor'
    trap_door = 'trap-door'
    pitbull = 'pitbull'
    chihuahua = 'chihuahua'
    cat = 'cat'
    vault = 'vault'
    start = 'start'
    player = 'player'
    son = 'son'
    daughter = 'daughter'
    wife = 'wife'
    
class Map():
    '''
    Represents a Castle Doctrine map.
    
    Each cell has an 'x', 'y' and a 'type' dictionary entry.
    '''

    width = 32
    height = 32
    
    def __init__(self):
        self.cells = {}

    def __repr__(self):
        cells = ''
        for pos in sorted(self.cells):
            cells += '({}, {}, {}) '.format(pos[0], pos[1], self.cells[pos])
        return '<Map: {} >'.format(cells)

    def setCell(self, x, y, cell_type):
        self.cells[(x, y)] = cell_type

    def getCell(self, x, y):
        return self.cells[(x, y)]
