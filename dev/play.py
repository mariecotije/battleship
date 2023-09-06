def play_game():
    game_status = True
    print("test")
    while game_status:
        try:
            answer = str(input("Do you want to start new game? Press 'y' for new game or 'n' for exit: "))
            if answer == 'y':
                print("Let's start!")
            elif answer == 'n':
                game_status = False
                print("Thank you for playing! Bye!")
                break
            else:
                print("Sorry, I don't understand. Please answer 'y' for YES or 'n' for NO")
                continue
        except ValueError:
            print("Please answer 'y' for YES or 'n' for NO")


play_game()
