class player:
    def play(self):
        print("the player is playing cricket.")
class batsman(player):
    def play(self):
        print("the batsman is bating.")
class bowler(player):
    def play(self):
        print("the bowler is bowling.")
batsman=batsman()
bowler=bowler()
player=player()
batsman.play()
bowler.play()
player.play()
    
