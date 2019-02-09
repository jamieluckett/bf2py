TOKEN_MAPPING = {
    "MOVER": "ptr += {value}",
    "MOVEL": "ptr -= {value}",
    "INCR": "array[ptr] += {value}",
    "DECR": "array[ptr] -= {value}",
    "OUT": "print(chr(array[ptr]), end='')",
    "INP": "array[ptr] = ord(input())",
    "LEFTBRAC": "while array[ptr] != 0:"
}

INDENT = "    "

PYTHON2_SETUP = "from __future__ import print_function\n\n"
SETUP = "array = [0 for i in range({0})]\nptr = 0\n\n"


def generate_code(chunks, python_two, array_length):
    string = ""
    if python_two:
        string += PYTHON2_SETUP
    string += SETUP.format(array_length)

    for chunk in chunks:
        for token in chunk.tokens:
            string += INDENT * chunk.indent
            string += TOKEN_MAPPING[token.type].format(value=token.value)
            string += "\n"

    return string
