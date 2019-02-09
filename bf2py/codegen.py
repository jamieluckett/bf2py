codeDict = {"MOVER": "ptr += ", "MOVEL": "ptr -= ", "INCR": "array[ptr] += ", "DECR" : "array[ptr] -= ",
            "OUT": "print(chr(array[ptr]), end='')\n", "INP": "array[ptr] = ord(input())\n",
            "LEFTBRAC": "while array[ptr] != 0:\n"}

INDENT = "    "

PYTHON2_SETUP = "from __future__ import print_function\n\n"
SETUP = "array = [0 for i in range(30000)]\n" + "ptr = 0\n"


def create_file(filename):
    file = open(filename, 'w')
    file.close()


def write_file(filename, python_code):
    file = open(filename, 'w')
    file.write(python_code)
    file.close()


def generate_code(source_file, chunks, python_two):
    string = ""
    if python_two:
        string += PYTHON2_SETUP
    string += SETUP

    for chunk in chunks:
        for token in chunk.tokens:
            string += INDENT * chunk.indent
            string += codeDict[token.type]
            if token.type in ["INCR", "DECR", "MOVEL", "MOVER"]:
                string += str(token.value) + "\n"

    return string
