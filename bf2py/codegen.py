codeDict = {"MOVER": "ptr += ", "MOVEL": "ptr -= ", "INCR": "array[ptr] += ", "DECR" : "array[ptr] -= ",
            "OUT": "print(chr(array[ptr]), end = '')\n", "INP": "array[ptr] = ord(input())\n",
            "LEFTBRAC": "while array[ptr] != 0:\n"}

SETUP = "array = [0 for i in range(30000)]\n" + "ptr = 0\n"

#"MOVER", "MOVEL", "INCR", "DECR", "OUT", "INP", "LEFTBRAC", "RIGHTBRAC", "EOF"

def createFile(filename):
    file = open(filename, 'w')
    file.close()

def writeFile(filename, finalCode):
    file = open(filename, 'w')
    file.write(finalCode)
    file.close()

def generateCode(sourceFile, chunks):
    string = '#'
    string += sourceFile + " compiled in to Python using bf2py github.com/jamieluckett/bf2py\n\n"
    string += SETUP

    for chunk in chunks:
        for token in chunk.tokens:
            string += "\t" * chunk.indent
            string += codeDict[token.type]
            if token.type in ["INCR", "DECR", "MOVEL", "MOVER"]:
                string += str(token.value) + "\n"

    return string
