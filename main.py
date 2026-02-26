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

def play_game(game, data1, data2):
    score = game.calculate_score(data1, data2)
    winner = game.determine_winner(score[0], score[1])
    
    return f"{winner} wins!"