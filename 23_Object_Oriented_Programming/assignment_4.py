class Games:
    def __init__(self, myGames):
        self.games = myGames
    
    def show_games(self):
      if (not isinstance(self.games,list)) and (not isinstance(self.games,int)):
          print(f"I Have One Game Called \"{self.games}\"")
      elif isinstance(self.games,list):
          print("I Have Many Games:")
          for game in self.games:
              print(f"-- {game}")
      else:
          print(f"I Have {self.games} Game ")

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# Ouput
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.
