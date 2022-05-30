import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Karma Chameleon")

    def test_song_has_name(self):
        self.assertEqual("Karma Chameleon", self.song.name)


