import core.map

class Writer:
    '''
    Writes a map in 'Castle Fortify' format.
    See http://castlefortify.com/ 
    '''

    cell_map = { \
                 core.map.Cell.wooden_wall : "wooden-wall",
                 core.map.Cell.steel_wall : "steel-wall",
                 core.map.Cell.concrete_wall : "concrete-wall",
                 core.map.Cell.doors : "doors",
                 core.map.Cell.window : "window",
                 core.map.Cell.pit : "pit",
                 core.map.Cell.generator : "power",
                 core.map.Cell.wire : "wire",
                 core.map.Cell.wired_wooden_wall : "wired-wooden-wall",
                 core.map.Cell.pressure_switch_off : "pressure-toggle-switch-off",
                 core.map.Cell.pressure_switch_on : "pressure-toggle-switch-on",
                 core.map.Cell.sticking_switch : "sticking-pressure-switch",
                 core.map.Cell.rotary_switch : "rotary-toggle-switch",
                 core.map.Cell.wire_bridge : "wire-bridge",
                 core.map.Cell.voltage_switch : "voltage-triggered-switch",
                 core.map.Cell.voltage_switch_inverted : "voltage-triggered-inverted-switch",
                 core.map.Cell.powered_door : "powered-door",
                 core.map.Cell.electric_floor : "electric-floor",
                 core.map.Cell.trap_door : "trap-door",
                 core.map.Cell.pitbull : "pitbull",
                 core.map.Cell.chihuahua : "chiwawa",
                 core.map.Cell.cat : "cat",
                 core.map.Cell.vault : "vault",
                 core.map.Cell.start : "empty-floor",
                 core.map.Cell.player : "empty-floor",
                 core.map.Cell.son : "daughter",
                 core.map.Cell.daughter : "daughter",
                 core.map.Cell.wife : "wife",
                 }

    def __init__(self):
        pass
    
    def write(self, map_data):
        lines = []
        start_line = '{ "map" : ['
        lines.append(start_line)

        cell_lines = []
        for y in range(1, map_data.height - 1):
            for x in range(1, map_data.width - 1):
                line = '  {{ \"x\" : {}, \"y\" : {}, \"tile\" : {} }}'
                cell = map_data.getCell(x, y)
                if cell != core.map.Cell.blank:
                    try:
                        tile = '\"{}\"'.format(self.cell_map[cell])
                    except:
                        raise
                    cell_lines.append(line.format(x - 1, y - 1, tile))

        # We must not put a comma on the last line!
        for line in cell_lines[0:-1]:
            lines.append('{},'.format(line))
        for line in cell_lines[-1:]:
            lines.append(line)

        end_line = '] }'
        lines.append(end_line)

        for line in lines:
            print line
