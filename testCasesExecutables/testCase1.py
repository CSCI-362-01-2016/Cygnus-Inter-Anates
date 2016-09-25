import unittest
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../project/src"))
import music


class TestNoteToFreq(unittest.TestCase):

    def test(self):
        self.assertEqual(music.noteToFreq(69), 440)
        self.assertEqual(music.noteToFreq(71), 493.8833012561241)

if __name__ == '__main__':
    unittest.main()
