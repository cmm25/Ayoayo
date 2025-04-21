from Ayoayo import Ayoayo
if __name__ == "__main__":
    game = Ayoayo()
    player1 = game.createPlayer("Jensen")
    player2 = game.createPlayer("Brian")
    
    print(game.playGame(1, 4))
    print(game.playGame(1, 1))
    print(game.playGame(2, 3))
    print(game.playGame(2, 4))
    game.playGame(1, 2)
    game.playGame(2, 2)
    game.playGame(1, 1)
    
    game.printBoard()
    print(game.returnWinner())