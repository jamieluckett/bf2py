class Token():
    def __init__(self, value, tokType): #using tokType instead of type because type() is a built in
        self.value = value
        self.type = tokType
