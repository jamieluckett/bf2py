from Chunk import Chunk


def verify_loops(tokens):
    counts = {'LEFTBRAC': 0, 'RIGHTBRAC': 0}
    for token in tokens:
        if token.type in ['LEFTBRAC', 'RIGHTBRAC']:
            counts[token.type] += 1

    return counts['LEFTBRAC'] == counts['RIGHTBRAC']


def get_loop_map(tokens):
    indexes = []
    stack = []
    for i in range(len(tokens)):
        if tokens[i].type == 'LEFTBRAC':
            stack.append(i)
        elif tokens[i].type == 'RIGHTBRAC':
            indexes.append((stack.pop(), i))

    return indexes


def parse(tokens):
    chunks = [Chunk(0)]
    indent = 0
    if len(get_loop_map(tokens)) == 0:
        # No parsing needs to be done, program has no loops and therefore is flat
        chunks[0].add_tokens(tokens)
        return chunks

    for i in range(len(tokens)):
        last_indent = indent
        if tokens[i].type == "LEFTBRAC":
            chunks[-1].add_token(tokens[i])
            indent += 1
            chunks.append(Chunk(indent))
        if tokens[i].type == "RIGHTBRAC":
            indent -= 1
            chunks.append(Chunk(indent))
        if indent == last_indent:
            chunks[-1].add_token(tokens[i])

    return chunks
