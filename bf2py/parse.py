from Chunk import *

def countLoops(tokens):
    counts = [0, 0]
    for token in tokens:
        if token.type == "LEFTBRAC":
            counts[0] += 1
        elif token.type == "RIGHTBRAC":
            counts[1] += 1

    if counts[0] == counts[1]:
        return True
    else:
        print("Loops not properly configured")
        return False

# [ LEFT BRAC ZERO LOOP
# ] RIGHT BRAC NON ZERO LOOP

def getLoopMap(tokens):
    indexes = []
    stack = []
    for i in range(len(tokens)):
        if tokens[i].type == "LEFTBRAC":
            stack.append(i)
        elif tokens[i].type == "RIGHTBRAC":
            indexes.append( (stack.pop(), i) )

    return indexes

def parse(tokens):
    chunks = [Chunk(0)]
    indent = 0
    lastindent = 0
    if len(getLoopMap(tokens)) == 0:
        # No parsing needs to be done, program has no loops and therefore is flat
        chunks[0].addTokens(tokens)
        return chunks

    for i in range(len(tokens)):
        lastindent = indent
        if tokens[i].type == "LEFTBRAC":
            chunks[-1].addToken(tokens[i])
            indent += 1
            chunks.append(Chunk(indent))
        if tokens[i].type == "RIGHTBRAC":
            indent -= 1
            chunks.append(Chunk(indent))
        if indent == lastindent:
            chunks[-1].addToken(tokens[i])

    return chunks