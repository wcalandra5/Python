class Song(object):
    def __init__(self, lyrics, number): # All these have to be passed, can't just pass 2 of these for the class
        self.lyrics = lyrics # If you hardcode these, it will always be this value
        self.number = number

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def displayNum(self):
        print self.number


happy_bday = Song(["Happy birthday to you", 
                "I don't want to get sued",     
                "So I'll stop right there."], 0)

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells."], 0)

new_song = Song(["Here's a one liner."], 0)

numberToAdd = Song("text",3)


happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
new_song.sing_me_a_song()

# Hopefully this prints 3
numberToAdd.displayNum() # it does