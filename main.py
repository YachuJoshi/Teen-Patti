from game import Game

game_on = True

while game_on:
    game = Game()
    game.start()

    while True:
        game_choice = input("Would you like to continue? Yes or No: ")

        if game_choice[0].lower() == "y":
            game_on = True
            break
        elif game_choice[0].lower() == "n":
            print('Thanks for playing!')
            game_on = False
            break
        else:
            print("I dont quite understand that")
