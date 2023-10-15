#define the base class player
class player:
     def play (self):
            print("The player is playing cricket.")

#define the derived class batsman
class Batsman (player):
    def play(self):
           print("The batsman is batting.")

#define the derived class bowler
class Bowler (player):
    def play(self):
           print("The bowler is bowling")

#create objects of batsman and bowler classes
batsman = Batsman( )
bowler = Bowler( )
#call the play( ) method to each object
batsman.play( )
bowler.play( )