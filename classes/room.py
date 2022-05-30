from classes.guest import Guest

class Room:
    def __init__(self, room_num, capacity, entry_fee):
        self.room_num = room_num
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.playlist = []
        self.guest_list = []
        self.till = 0

    def add_song_to_playlist(self, song_name):
        self.playlist.append(song_name)

#Extension - Capacity Check

    def add_guest_to_guest_list(self, guest):
        if len(self.guest_list) < self.capacity:
            self.guest_list.append(guest)  
        else:
            return "Room at capacity, please choose a different room."

#Extension - Entry Fee

    def guest_entry_check(self, guest):
        if len(self.guest_list) < self.capacity:
            if guest.wallet > self.entry_fee:
                self.guest_list.append(guest.name)
            else:
                return "You do not have enough money for entry to this room."
        else:
            return "Room at capacity, please choose a different room."

    def remove_guest_from_guest_list(self, guest_name):
        self.guest_list.remove(guest_name)
    