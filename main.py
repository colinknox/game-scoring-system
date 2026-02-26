class Game:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name

    def calculate_score(self, player1_data, player2_data):
        raise NotImplementedError("Must implement score logic")

    def determine_winner(self, player1_score, player2_score):
        raise NotImplementedError("Must implement winner logic")

class HighScoreGame(Game):
    def __init__(self, player1_name, player2_name):
        super().__init__(player1_name, player2_name)

    def calculate_score(self, player1_data, player2_data):
        return (player1_data, player2_data)

    def determine_winner(self, player1_score, player2_score):
        if player1_score > player2_score:
            return self.player1_name
        elif player2_score > player1_score:
            return self.player2_name 
        else:
            return "Tie"

class LowScoreGame(Game):
    def __init__(self, player1_name, player2_name):
        super().__init__(player1_name, player2_name)

    def calculate_score(self, player1_data, player2_data):
        return (player1_data, player2_data)
    
    def determine_winner(self, player1_score, player2_score):
        if player1_score < player2_score:
            return self.player1_name
        elif player2_score < player1_score:
            return self.player2_name
        else:
            return "Tie"



# game = Game("Chris", "Corey")
# high_score_game = HighScoreGame("Big Boss", "Eva")
low_score_game = LowScoreGame("Ed", "Nazz")

print(f"""
PLAYER 1 NAME = {low_score_game.player1_name}
PLAYER 2 NAME = {low_score_game.player2_name}
CALCULATE SCORE = {low_score_game.calculate_score(93, 45)}
DETERMINE WINNER = {low_score_game.determine_winner(53, 54)}
""")