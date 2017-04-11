import sys, lex, parse, codegen

def printTokenList(tokens):
    for item in tokens:
        if type(item) == list:
            print("r")
            printTokenList(item)
        else:
            print(item.__dict__)

def printChunks(chunks):
    for chunk in chunks:
        print("\n", chunk.indent)
        for token in chunk.tokens:
            print(token.__dict__, end = "")

def main():
    if toCompile[-2:] != "bf":
        print("Not a Brainfuck File")
        return -1
    file = open(toCompile, 'r') #open file read only
    tokens = lex.getListOfTokens(file)
    if parse.countLoops(tokens) == False:
        return -1
    else:
        chunks = parse.parse(tokens)
        finalCode = codegen.generateCode(toCompile, chunks)
        codegen.writeFile(destFile, finalCode)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: bf2py.py input.bf [output.py]")

    else:
        toCompile = sys.argv[1]
        if len(sys.argv) == 3:
            destFile = sys.argv[2]
        else:
            destFile = toCompile.split("/")[-1][:-3] + ".py"
        main()
