from argparse import ArgumentParser
import os
import sys
import traceback

import lex
import parse
import codegen


def get_dest_file(source_file):
    if not os.path.isfile(source_file):
        print("Error: {0} is not a file".format(source_file))
        raise FileNotFoundError

    filename = os.path.basename(source_file)
    directory = source_file.replace(filename, '')
    basename = os.path.splitext(filename)[0]

    return "{0}{1}.py".format(directory, basename)


def get_args():
    parser = ArgumentParser()
    parser.add_argument('source_file', help="brainfuck source code to compile")
    parser.add_argument('dest_file', nargs='?',
                        help="path of the output python file(default: input file appended with .py)")
    parser.add_argument('-t', '--two', help="whether to output python 2 code or not", action='store_true')
    parser.add_argument('-a', '--array-length', help="length of the brainfuck array (default=30000)", default=30000)
    parser.add_argument('-d', '--debug', help="whether or not to print debug information and stack traces",
                        action='store_true')

    args = parser.parse_args()
    args.dest_file = args.dest_file or get_dest_file(args.source_file)

    return args


def main(args):
    source_file = args.source_file
    dest_file = args.dest_file
    import_future = args.two
    array_length = args.array_length

    with open(source_file, 'r') as f:
        source_code = f.read()
        tokens = lex.get_list_of_tokens(source_code)
    if not parse.verify_loops(tokens):
        print("Error: Brainfuck source has non-equal numbers of [ and ]")
        return 1
    else:
        chunks = parse.parse(tokens)
        python_code = codegen.generate_code(chunks, import_future, array_length)
        if not python_code:
            print("Error: Compiled program is empty, invalid input?")
        else:
            with open(dest_file, 'w') as f:
                f.write(python_code)
    print("Compilation complete, output at {0}".format(dest_file))


if __name__ == "__main__":
    args = get_args()
    debug = args.debug
    try:
        sys.exit(main(args))
    except FileNotFoundError:
        if debug:
            traceback.print_exc()
        sys.exit(1)
    except Exception as e:
        print("Error: {0}".format(e))
        if debug:
            traceback.print_exc()
        sys.exit(1)
