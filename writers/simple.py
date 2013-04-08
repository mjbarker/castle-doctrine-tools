import core.map

class Writer:
    '''
    Writes a map in simple grid format. 
    '''

    cell_map = { \
                 core.map.Cell.ext_wall : '*',
                 core.map.Cell.wooden_wall : 'w',
                 core.map.Cell.steel_wall : 's',
                 core.map.Cell.concrete_wall : "c",
                 core.map.Cell.blank : ' ',
                 core.map.Cell.doors : '=',
                 core.map.Cell.window : '-',
                 core.map.Cell.pit : 'X',
                 core.map.Cell.generator : 'g',
                 core.map.Cell.wire : '+',
                 core.map.Cell.wired_wooden_wall : 'W',
                 core.map.Cell.pressure_switch_off : 'o',
                 core.map.Cell.pressure_switch_on : 'O',
                 core.map.Cell.sticking_switch : '@',
                 core.map.Cell.rotary_switch : 'r',
                 core.map.Cell.wire_bridge : 'b',
                 core.map.Cell.voltage_switch : '^',
                 core.map.Cell.voltage_switch_inverted : 'v',
                 core.map.Cell.powered_door : 'D',
                 core.map.Cell.electric_floor : '#',
                 core.map.Cell.trap_door : 'T',
                 core.map.Cell.pitbull : '~',
                 core.map.Cell.chihuahua : '.',
                 core.map.Cell.cat : ',',
                 core.map.Cell.vault : '$',
                 core.map.Cell.start : '>',
                 core.map.Cell.player : '%',
                 core.map.Cell.son : 's',
                 core.map.Cell.daughter : 'd',
                 core.map.Cell.wife : 'm',
                 }

    def __init__(self):
        pass
    
    def write(self, map_data):
        lines = []
        for y in range(0, map_data.height):
            line = ''
            for x in range(0, map_data.width):
                cell = map_data.getCell(x, y)
                line += self.cell_map[cell]
            lines.append(line)

        for line in lines:
            print line
