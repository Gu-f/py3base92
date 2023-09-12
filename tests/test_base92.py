import unittest
from py3base92 import Base92
from py3base92 import b92encode, b92decode
import hashlib
import random


class TestBase92(unittest.TestCase):

    @staticmethod
    def _gen_bytes(s):
        return hashlib.sha512(s.encode()).digest()[:random.randint(1, 64)]

    def test_base92_chr(self):
        for i in range(0, 91, 1):
            self.assertIn(Base92.base92_chr(i), Base92.CHARACTER_SET)

    def test_base92_ord(self):
        for i in Base92.CHARACTER_SET:
            self.assertLess(Base92.base92_ord(i), 91)
            self.assertLessEqual(0, Base92.base92_ord(i))

    def test_b92encode(self):
        self.assertEqual(b92encode("\x00"), '!!')
        self.assertEqual(b92encode("\x01"), '!B')
        self.assertEqual(b92encode("\xff"), '|_')
        self.assertEqual(b92encode("aa"), 'D8*')
        self.assertEqual(b92encode("aaaaaaaaaaaaa"), 'D81RPya.)hgNA(%s')
        self.assertEqual(b92encode([16, 32, 48]), "'_$,")

    def test_b92decode(self):
        self.assertEqual(b92decode(""), b"")
        self.assertEqual(b92decode("~"), b"")
        self.assertEqual(b92decode("!!"), b'\x00')
        self.assertEqual(b92decode("!B"), b'\x01')
        self.assertEqual(b92decode("|_"), b'\xff')
        self.assertEqual(b92decode("D8*"), b'aa')
        self.assertEqual(b92decode("D81RPya.)hgNA(%s"), b'aaaaaaaaaaaaa')

    def test_random_overall(self):
        for i in range(10000):
            s = self._gen_bytes(str(random.random()))
            assert s == Base92.b92decode(Base92.b92encode(s))
        print('correctness spot check passed')


# 运行测试
if __name__ == '__main__':
    unittest.main()
