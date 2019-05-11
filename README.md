# bf2py
## What?
A simple compiler that turns [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) source code in to Python (2 or 3) source code.

## Why?
bf2py (originally known as jjc, an awful acronym of my old GitHub username and the word "compiler") was written as a bit of coursework for my 2nd Year Computer Science Compilers module. While the current code has been cleaned up, the original code can be seen in the [original branch](https://github.com/jamieluckett/bf2py/tree/original). 

## How?
### Usage
bf2py.py input.bf [output.py]

### Arguments
| Argument                               | Usage                                                                                                          |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `-t` or `--two`                        | Produces Python 2 executable code by way of importing print_function from __future__                           |
| `-a length`or`--array-length length` | The length of the memory array used by the Brainfuck program. Defaults to 30,000.                              |
| `-d` or `--debug`                      | With this flag set, some debug information is printed along with any stack traces should the compiler blow up. |
