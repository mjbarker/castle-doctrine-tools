import core.map
import io.input
import parsers.recording_file
import writers.castle_fortify
import writers.simple

from optparse import OptionParser

class Parser:
    def __init__(self, name, desc, parser):
        self.name = name
        self.desc = desc
        self.parser = parser

class Writer:
    def __init__(self, name, desc, writer):
        self.name = name
        self.desc = desc
        self.writer = writer
        
def main():
    if_recording = 'r'    
    supported_parser_list = [
               Parser(if_recording,
                      'recording file',
                      parsers.recording_file.RecordingFileMapParser),
               ]
    
    of_castle_fortify = 'cf'
    of_grid = 'g'
    supported_writer_list = [
               Writer(of_castle_fortify,
                      'Castle Fortify (see http://castlefortify.com/)',
                      writers.castle_fortify.Writer),
               Writer(of_grid,
                      'simple grid',
                      writers.simple.Writer),
               ]

    valid_input_formats = [parser.name for parser in supported_parser_list] 
    valid_output_formats = [writer.name for writer in supported_writer_list]

    parser = OptionParser()
    parser.add_option('-f', '--input-file', type = 'string',
                      dest = 'input_filename', default = '',
                      help = 'Input filename')
    parser.add_option('-i', '--input-format', type = 'choice',
                      dest = 'input_format', default = if_recording, choices = valid_input_formats,
                      help = 'Input format: ' +
                             ', '.join(p.name + ' - ' + p.desc for p in supported_parser_list))
    parser.add_option('-o', '--output-format', type = 'choice',
                      dest = 'output_format', default = of_grid, choices = valid_output_formats,
                      help = 'Output format: ' +
                             ', '.join(w.name + ' - ' + w.desc for w in supported_writer_list))
    parser.add_option('-O', '--output-format-list', type = 'string',
                      dest = 'output_formats', default = '',
                      help = 'Output formats separated by a comma, see --output-format')
    (options, args) = parser.parse_args()

    input_format = options.input_format
    output_formats = []
    for output_format in options.output_formats.split(','):
        if output_format in valid_output_formats and not output_format in output_formats:
            output_formats += [output_format]
    if len(output_formats) == 0:
        output_formats = [options.output_format]
        
    try:
        input = io.input.FileInput(options.input_filename)
    except:
        print 'Could not open: \'' + options.input_filename + '\''

    parser = [parser.parser(input) for parser in supported_parser_list if parser.name == input_format][0]

    converting = True
    while converting:
        parsed_map = core.map.Map()
        try:
            parsed = parser.parse(parsed_map)
    
            if parsed:
                writer_list = []
                for format in output_formats:
                    writer_list += [writer.writer() for writer in supported_writer_list if writer.name == format]
                for writer in writer_list:
                    writer.write(parsed_map)
                
        except parsers.recording_file.ParseError as e:
            print 'Failed to parse file:', e.message
            
        converting = not input.eof()
        
if __name__ == '__main__':
    main()
    
