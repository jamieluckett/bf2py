class Chunk:
    def __init__(self, indent):
        self.indent = indent
        self.tokens = []

    def addToken(self, token):
        self.tokens.append(token)

    def addTokens(self, tokens):
        self.tokens += tokens
