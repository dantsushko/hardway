class song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

lyrics = ["There are half liter of vodka", "V dole", "S marijuana"]
birthday = song(lyrics)
birthday.sing_me_a_song()
