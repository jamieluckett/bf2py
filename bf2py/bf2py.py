import argparse
import sys
import os

import lex
import parse
import codegen


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_file', help="brainfuck source code to compile")
    parser.add_argument('dest_file', nargs='?',
                        help="path of the output python file(default: input file appended with .py)")
    parser.add_argument('-t', '--two', help="whether to output python 2 code or not", action='store_true')
    parser.add_argument('-a', '--array-length', help="length of the brainfuck array (default=30000)", default=30000)

    args = parser.parse_args()
    if not args.dest_file:
        args.dest_file = args.source_file + '.py'

    return args


def main():
    args = get_args()
    source_file = args.source_file
    dest_file = args.dest_file
    import_future = args.two
    array_length = args.array_length

    if not os.path.isfile(source_file):
        print("Error: {0} is not a file".format(source_file))
        sys.exit(1)

    with open(source_file, 'r') as f:
        tokens = lex.get_list_of_tokens(f)

    if not parse.count_loops(tokens):
        return -1
    else:
        chunks = parse.parse(tokens)
        python_code = codegen.generate_code(source_file, chunks, import_future)
        if not python_code:
            print("Error: Compiled program is empty, invalid input?")
        else:
            codegen.write_file(dest_file, python_code)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        raise e
