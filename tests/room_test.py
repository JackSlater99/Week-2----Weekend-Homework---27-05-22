import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 5, 15)
        self.room_1 = Room(2, 7, 20)
        self.song = Song("Karma Chameleon")
        self.song_1 = Song("Piano Man")
        self.guest = Guest("Arnold Palmer", 100, "Karma Chameleon")
        self.guest_1 = Guest("Tom Watson", 15, "Piano Man")

    def test_room_has_number(self):
        self.assertEqual(1, self.room.room_num)

    def test_room_has_empty_playlist(self):
        self.assertEqual([], self.room.playlist)

    def test_add_song_to_playlist(self):
        self.room.add_song_to_playlist(self.song.name)
        self.assertEqual(["Karma Chameleon"], self.room.playlist)

    def test_add_song_to__playlist(self):
        self.room.add_song_to_playlist(self.song.name)
        self.room.add_song_to_playlist(self.song_1.name)
        self.assertEqual(["Karma Chameleon", "Piano Man"], self.room.playlist)

    def test_room_has_empty_guest_list(self):
        self.assertEqual([], self.room.guest_list)

    def test_add_guest_to_guest_list(self):
        self.room.add_guest_to_guest_list(self.guest.name)
        self.assertEqual(["Arnold Palmer"], self.room.guest_list)

    def test_add_guest_to_guest__list(self):
        self.room.add_guest_to_guest_list(self.guest.name)
        self.room.add_guest_to_guest_list(self.guest_1.name)
        self.assertEqual(["Arnold Palmer", "Tom Watson"], self.room.guest_list)

    def test_remove_guest_from_guest__list(self):
        self.room.add_guest_to_guest_list(self.guest.name)
        self.room.add_guest_to_guest_list(self.guest_1.name)
        self.room.remove_guest_from_guest_list(self.guest.name)
        self.assertEqual(["Tom Watson"], self.room.guest_list)

#Extension - Capacity Check

    def test_check_room_has_capacity(self):
        self.assertEqual(7, self.room_1.capacity)

    def test_check_in_guest_under_capacity(self):
        self.room.guest_list = ["Johnny Cash", "Willie Nelson", "Dolly Parton", "Elvis Presley"]
        self.room.add_guest_to_guest_list(self.guest)
        self.assertEqual(5, len(self.room.guest_list))

    def test_check_in_guest_at_capacity(self):
        self.room.guest_list = ["Johnny Cash", "Willie Nelson", "Dolly Parton", "Elvis Presley", "Kenny Rogers"]
        at_capacity = self.room.add_guest_to_guest_list(self.guest.name)
        self.assertEqual("Room at capacity, please choose a different room.", at_capacity)

    def test_room_has_till(self):
        self.assertEqual(0, self.room.till)

    def test_room_has_entry_fee(self):
        self.assertEqual(15, self.room.entry_fee)

#Extension - Entry Fee

    def test_room_entry_with_capacity_and_money(self):
        self.room.guest_entry_check(self.guest) 
        self.assertEqual(1, len(self.room.guest_list))

    def test_room_entry_with_capacity_and__money(self):
        check = self.room.guest_entry_check(self.guest_1) 
        self.assertEqual("You do not have enough money for entry to this room.", check)