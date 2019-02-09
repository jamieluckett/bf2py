class Chunk:
    def __init__(self, indent):
        self.indent = indent
        self.tokens = []

    def add_token(self, token):
        self.tokens.append(token)

    def add_tokens(self, tokens):
        self.tokens += tokens
