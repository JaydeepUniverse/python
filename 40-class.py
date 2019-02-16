class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                    "Happy birthday dear Jaydeep",
                    "Happy birthday to you"])

aashiqui2 = Song(["Tum hi ho",
"Chahu mein ya na",
"Milne he mujhse aayi"])

happy_bday.sing_me_a_song()
aashiqui2.sing_me_a_song()
