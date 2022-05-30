import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("John Smith", 50, "Uptown Girl")

    def test_guest_has_name(self):
        self.assertEqual("John Smith", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Uptown Girl", self.guest.fav_song)

    def test_guest_reaction_to_favourite_song(self):
        playlist = ["Uptown Girl", "Ring of Fire", "Hotel California"]
        reaction = self.guest.react_favourite_song(playlist)
        self.assertEqual("Whoo!", reaction)
