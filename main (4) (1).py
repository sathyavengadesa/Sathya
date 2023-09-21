class Batsman:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is batting.")

class Bowler:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is bowling.")

# Creating objects of Batsman and Bowler classes
batsman1 = Batsman("Batsman 1")
batsman2 = Batsman("Batsman 2")
bowler1 = Bowler("Bowler 1")
bowler2 = Bowler("Bowler 2")

# Calling the play() method for each object
batsman1.play()
batsman2.play()
bowler1.play()
bowler2.play()
