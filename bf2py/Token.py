class Token:
    def __init__(self, value, token_type):
        self.value = value
        self.type = token_type

    def __str__(self):
        return "{0} | {1}".format(self.type, self.value)
