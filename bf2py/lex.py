from Token import *

MOVER = "MOVER"
MOVEL = "MOVEL"
INCR = "INCR"
INP = "INP"
DECR = "DECR"
OUT = "OUT"
LEFTBRAC = "LEFTBRAC"
RIGHTBRAC = "RIGHTBRAC"
EOF = "EOF"


class LexicalAnalyser():
    def __init__(self, file):
        self.string = file.read()
        self.string.replace("\n", "")
        self.lines = self.string.split("\n")  # split string into list of lines
        self.lines = [i for i in self.lines if len(i) != 0]  # strip blank lines
        self.lineNo = 0
        self.position = 0  # start at begining of file
        self.currentChar = self.lines[self.lineNo][self.position]

    def get_next_token(self):
        while self.currentChar is not None:
            if self.currentChar.isspace():
                self.advance()
            elif self.currentChar == '>':
                temp = self.get_number_of('>')
                return Token(temp, MOVER)

            elif self.currentChar == '<':
                temp = self.get_number_of('<')
                return Token(temp, MOVEL)

            elif self.currentChar == '+':
                temp = self.get_number_of('+')
                return Token(temp, INCR)

            elif self.currentChar == '-':
                temp = self.get_number_of('-')
                return Token(temp, DECR)

            elif self.currentChar == '.':
                self.advance()
                return Token('.', OUT)

            elif self.currentChar == ',':
                self.advance()
                return Token(',', INP)

            elif self.currentChar == '[':
                self.advance()
                return Token('[', LEFTBRAC)

            elif self.currentChar == ']':
                self.advance()
                return Token(']', RIGHTBRAC)

            else:
                self.advance()
                pass

        return Token(None, EOF)

    def get_number_of(self, symbol):  #TODO rename
        count = 0
        while self.currentChar == symbol:
            count += 1
            self.advance()
        return count

    def advance(self):
        self.position += 1
        if len(self.lines[self.lineNo]) <= self.position:
            self.lineNo += 1
            self.position = 0
        if len(self.lines) <= self.lineNo:
            self.currentChar = None
        else:
            self.currentChar = self.lines[self.lineNo][self.position]


def get_list_of_tokens(file):
    analyser = LexicalAnalyser(file)
    tokens = []
    complete = False
    while not complete:
        temp = analyser.get_next_token()
        if temp.value is None:
            complete = True
        else:
            tokens.append(temp)
    return tokens
