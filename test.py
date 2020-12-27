from algo import KMP
import unittest


class Sollution(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(4, KMP("baaaab", "abaabaaaabaabaaab"))

    def testcase_2(self):
        self.assertEqual(0, KMP("ggg", "ggg"))

    def testcase_3(self):
        self.assertEqual(-1, KMP("ggg", "fgfhrtwerqwdsvdbhregaf"))

    def testcase_4(self):
        self.assertEqual(-1, KMP("ggegrwfdsvfdsgg", "ggg"))