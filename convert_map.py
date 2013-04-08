import core.map
import io.input
import parsers.recording_file
import writers.castle_fortify
import writers.simple

def main():
    # MJB TODO: Command line options parsing, etc.
    filename = 'test4.txt'
    try:
        input = io.input.FileInput(filename)
    except:
        print 'Could not find file: \'' + filename + '\''
     
    parser = parsers.recording_file.RecordingFileMapParser(input)
    
    parsed_map = core.map.Map()
    try:
        parser.parse(parsed_map)
        #print parsed_map
        
        writer = writers.castle_fortify.Writer()
        writer.write(parsed_map)
        writer = writers.simple.Writer()
        writer.write(parsed_map)
        
    except parsers.recording_file.ParseError as e:
        print 'Failed to parse file:', e.message
        
if __name__ == '__main__':
    main()
    
