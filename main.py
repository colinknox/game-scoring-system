class Game:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name

    def calculate_score(self, player1_data, player2_data):
        raise NotImplementedError("Must implement score logic")

    def determine_winner(self, player1_score, player2_score):
        raise NotImplementedError("Must implement winner logic")



game = Game("Chris", "Corey")

print(f"""
PLAYER 1 NAME = {game.player1_name}
PLAYER 2 NAME = {game.player2_name}
DETERMINE WINNER = {game.determine_winner(game.player1_name, game.player2_name)}
""")

# print(f"""
# PLAYER 1 NAME = {game.player1_name}
# PLAYER 2 NAME = {game.player2_name}
# CALCULATE SCORE = {game.calculate_score(game.player1_name, game.player2_name)}
# DETERMINE WINNER = {game.determine_winner(game.player1_name, game.player2_name)}
# """)