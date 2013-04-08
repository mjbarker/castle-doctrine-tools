import core.map
import io.input
import parsers.recording_file

from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option('-f', '--input-file', type = 'string',
                      dest = 'recording_filename', default = '',
                      help = 'Recording filename')
    (options, args) = parser.parse_args()

    try:
        input = io.input.FileInput(options.recording_filename)
    except:
        print 'Could not open: \'' + options.recording_filename + '\''

    reading = True            
    line = input.readline()
    while reading and not input.eof():
        start = line.find('#'.join(['998'] * core.map.Map.width))
        if start >= 0:
            print line[start:] 
        if reading:
            line = input.readline()
         
if __name__ == '__main__':
    main()
