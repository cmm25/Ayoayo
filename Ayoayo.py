class Player:
    def __init__(self, name):
        self.name = name
    
class Ayoayo:
    def __init__(self):
        self._board = [4]*6+[0]+[4]*6+[0]
        self._game_ended = False
        self._players = []
        
    def createPlayer(self, name):
        player = Player(name)
        self._players.append(player)
        return player
    
    def printBoard(self):
        if len(self._players) < 2:
            return "Not enough players"
        print("player1:")
        print(f"store: {self._board[6]}")
        print(self._board[:6])
        print("player2:")
        print(f"store: {self._board[13]}")
        print(self._board[7:13])
        
    def returnWinner(self):
        if not self._game_ended:
            return "Game has not ended"        
        p1_score, p2_score = self._board[6], self.board[13]        
        if p1_score > p2_score:
            return f"Winner is player 1: {self.players[0].name}"
        elif p2_score > p1_score:  
            return f"Winner is player 2: {self.players[1].name}"
        else:
            return "It's a tie"
        
    def check_game_end(self):
        """Check if the game has ended and collect remaining seeds if needed"""
        p1_empty = not any(self._board[:6])
        p2_empty = not any(self._board[7:13])
        
        if not (p1_empty or p2_empty):
            return False
        if p1_empty:
            self._board[13] += sum(self._board[7:13])
            for i in range(7, 13):
                self._board[i] = 0
        else: 
            self._board[6] += sum(self._board[:6])
            for i in range(6):
                self._board[i] = 0        
        self._game_ended = True
        return True
    
    def playGame(self, player_idx, pit_idx):
        if not 1 <= pit_idx <= 6:
            return "Invalid number for pit index"
        
        if self._game_ended:
            return "Game is ended"
        board_idx = pit_idx - 1 if player_idx == 1 else pit_idx + 6
        if self._board[board_idx] == 0:
            return "Cannot select an empty pit"
        seeds = self._board[board_idx]
        self._board[board_idx] = 0
        player_store = 6 if player_idx == 1 else 13
        opponent_store = 13 if player_idx == 1 else 6
        current_idx = board_idx
        while seeds > 0:
            current_idx = (current_idx + 1) % 14
            if current_idx == opponent_store:
                continue            
            self._board[current_idx] += 1
            seeds -= 1

        if current_idx == player_store:
            print(f"player {player_idx} take another turn")
        elif ((player_idx == 1 and 0 <= current_idx < 6) or (player_idx == 2 and 7 <= current_idx < 13)) and self._board[current_idx] == 1:            
            opposite_idx = 12 - current_idx            
            if self._board[opposite_idx] > 0:
                self._board[player_store] += self._board[opposite_idx] + 1
                self._board[opposite_idx] = 0
                self._board[current_idx] = 0
        if self.check_game_end():
            return "Game is ended"
        
        return self._board