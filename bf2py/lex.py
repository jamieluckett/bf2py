from Token import Token

CHAR_MAP = {
    '>': "MOVER",
    '<': "MOVEL",
    '+': "INCR",
    '-': "DECR",
    '.': "OUT",
    ',': "INP",
    '[': "LEFTBRAC",
    ']': "RIGHTBRAC",
    None: "EOF"
}


class LexicalAnalyser:
    def __init__(self, source_code):
        self.source_code = "".join([char for char in source_code if char in CHAR_MAP])
        self.position = 0
        self._set_current_char()

    def get_next_token(self):
        while self.currentChar is not None:
            if self.currentChar in ['>', '<', '+', '-']:
                symbol = self.currentChar
                quantity = self.get_number_of(self.currentChar)
                return Token(quantity, CHAR_MAP[symbol])
            else:
                # No token returned for an empty loop []
                if self.currentChar == '[' and self._next_character() == ']':
                    self.advance(2)
                else:
                    token = Token(self.currentChar, CHAR_MAP[self.currentChar])
                    self.advance()
                    return token

        return Token(self.currentChar, CHAR_MAP[self.currentChar])

    def get_number_of(self, symbol):
        count = 0
        while self.currentChar == symbol:
            count += 1
            self.advance()
        return count

    def _set_current_char(self):
        try:
            self.currentChar = self.source_code[self.position]
        except IndexError:
            self.currentChar = None

    def _next_character(self):
        return self.source_code[self.position + 1]

    def advance(self, jumps=1):
        self.position += jumps
        self._set_current_char()


def get_list_of_tokens(source_code):
    analyser = LexicalAnalyser(source_code)
    tokens = []
    complete = False
    while not complete:
        temp = analyser.get_next_token()
        if temp.value is None:
            complete = True
        else:
            tokens.append(temp)
    return tokens
