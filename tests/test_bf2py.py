import unittest
import bf2py.bf2py as bf2py
from bf2py.Token import Token
from bf2py.Chunk import Chunk


class Testbf2py(unittest.TestCase):
    def test_get_dest_file_valid(self):
        # "dest_file" generated should be identical as this is already a .py
        self.assertEqual(__file__, bf2py.get_dest_file(__file__))

    def test_get_dest_file_nonexistent_file(self):
        try:
            bf2py.get_dest_file("test")
        except FileNotFoundError:
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)


class TestChunk(unittest.TestCase):
    def setUp(self):
        self.chunk = Chunk(4)

    def test_chunk_str(self):
        self.assertEqual(str(self.chunk), "Indent [4]")

    def test_chunk_add_token(self):
        token = Token(6, 'INCR')
        self.chunk.add_token(Token(6, 'INCR'))
        self.assertEqual((self.chunk.tokens[0].value, self.chunk.tokens[0].type), (token.value, token.type))

    def test_chunk_add_tokens(self):
        tokens = [Token(6, 'INCR'), Token(3, 'DECR')]
        self.chunk.add_tokens(tokens)
        self.assertEqual((self.chunk.tokens[0].value, self.chunk.tokens[0].type,
                          self.chunk.tokens[1].value, self.chunk.tokens[1].type),
                         (tokens[0].value, tokens[0].type,
                          tokens[1].value, tokens[1].type))


class TestToken(unittest.TestCase):
    def setUp(self):
        self.token = Token(6, 'INCR')

    def test_token_str(self):
        self.assertEqual(str(self.token), "INCR | 6")

