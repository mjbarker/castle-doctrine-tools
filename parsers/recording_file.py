import core.map
 
class ParseError():
    def __init__(self, message = 'unknown'):
        self.message = message

class RecordingFileMapParser:
    '''
    Parses Castle Doctrine recording file format. 
    '''

    items = { 0 :    core.map.Cell.blank,
              1 :    core.map.Cell.wooden_wall,
              2 :    core.map.Cell.steel_wall,
              3 :    core.map.Cell.concrete_wall,
              20 :   core.map.Cell.window,
              21 :   core.map.Cell.doors,
              30 :   core.map.Cell.powered_door,
              51 :   core.map.Cell.wired_wooden_wall,
              70 :   core.map.Cell.pitbull,
              71 :   core.map.Cell.chihuahua,
              72 :   core.map.Cell.cat,
              100 :  core.map.Cell.sticking_switch,
              101 :  core.map.Cell.pressure_switch_off,
              102 :  core.map.Cell.wire,
              103 :  core.map.Cell.generator,
              104 :  core.map.Cell.voltage_switch,
              105 :  core.map.Cell.voltage_switch_inverted,
              106 :  core.map.Cell.wire_bridge,
              107 :  core.map.Cell.rotary_switch,
              108 :  core.map.Cell.pressure_switch_on,
              110 :  core.map.Cell.electric_floor,
              111 :  core.map.Cell.pit,
              112 :  core.map.Cell.trap_door,
              997 :  core.map.Cell.start,
              998 :  core.map.Cell.ext_wall,
              999 :  core.map.Cell.vault,
              1000 : core.map.Cell.player,
              1010 : core.map.Cell.wife,
              1011 : core.map.Cell.wife,
              1012 : core.map.Cell.wife,
              1013 : core.map.Cell.wife,
              1020 : core.map.Cell.son,
              1021 : core.map.Cell.son,
              1022 : core.map.Cell.son,
              1023 : core.map.Cell.son,
              1040 : core.map.Cell.daughter,
              1041 : core.map.Cell.daughter,
              1042 : core.map.Cell.daughter,
              1043 : core.map.Cell.daughter,
              }
    
    def __init__(self, input_stream):
        self.input = input_stream
   
    def parse(self, map_data):
        try:
            x = 0
            y = map_data.height - 1

            reading = True            
            line = self.input.readline()
            while reading and not self.input.eof():
                tokens = line.split('#')
                #print tokens
                for token in tokens:
                    try:
                        # MJB TODO: For now, ignore statuses, just get the tile.
                        tile = token.split(',')[0]
                        tile = tile.split(':')[0]
                        cell = self.items[int(tile)]
                    except:
                        raise ParseError('item ' + token + ' is not recognised')
                    map_data.setCell(x, y, cell)
                    #print cell
                    x = x + 1
                    if x == map_data.width:
                        x = 0
                        y = y - 1
                    if y < 0:
                        #print 'Finished reading map'
                        reading = False
                        break
                if reading:
                    line = self.input.readline()
        except:
            raise
