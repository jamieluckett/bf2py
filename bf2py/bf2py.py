import sys, lex, parse, codegen

def main():
    file = open(toCompile, 'r') #open file read only
    tokens = lex.getListOfTokens(file)
    if parse.countLoops(tokens) == False:
        return -1
    else:
        chunks = parse.parse(tokens)
        finalCode = codegen.generateCode(toCompile, chunks)
        if len(finalCode) == 0:
            print("Compiled program is empty, invalid input?")
        else:
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
