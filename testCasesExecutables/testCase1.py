import unittest
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../project/src"))
import music


class TestNoteToFreq(unittest.TestCase):

    def test(self):
        self.assertEqual(music.noteToFreq(eval(self.midi)), eval(self.frequency))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        TestNoteToFreq.frequency = sys.argv.pop()
        TestNoteToFreq.midi = sys.argv.pop()
    unittest.main()
