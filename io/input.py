
class FileInput:
    '''
    Input stream from a file.
    '''

    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')
        self.at_eof = False

    def eof(self):
        return self.at_eof
    
    def readline(self):
        line = self.file.readline()
        if len(line) == 0:
            self.at_eof = True
        return line.rstrip('\n')
