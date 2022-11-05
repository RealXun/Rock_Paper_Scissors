def is_odd(first_input):
    if first_input % 2 != 0:
        return True
    else:
        False
        
def is_more_or_equal_3(first_input):
    if first_input >= 3:
        return True
    else:
        return False
        
while 1:
    first_input = int(input("Maximum number of games? (minimum3): "))
    if is_odd(first_input) and is_more_or_equal_3(first_input):
        print("Input taken successfully.","Number is odd and greater than five.","The game starts now:")
        partidasplayed=0
        max_rounds=first_input
        played=0
        machine_win=0
        users_win=0
        to_win=int((max_rounds/2)+0.5)
        games_left=max_rounds-1
        while played<max_rounds:
            import sys
            import random
            random = random.randrange(0, 3)
            print("1)rock")
            print("2)paper")
            print("3)scissors")
            if random == 0:
                machine = "rock"
            elif random == 1:
                machine = "paper"
            elif random == 2:
                machine = "scissors"
            option = int(input("What do you want to use?:"))
            while option > 3 or option==0:
                print("Incorrect option.")# pick again
            if option == 1:
                user = "rock"
            elif option == 2:
                user = "paper"
            elif option == 3:
                user = "scissors"
            print("\nYou choose: ", user)
            print("The machine has chosen: ", machine)
            if (machine == "rock" and user == "paper") or (machine == "paper" and user == "scissors") or (machine == "scissors" and user == "rock"):
                users_win+=1
            elif machine == user:
                print("\nTIE!!!")
            else:
                machine_win+=1   
            print("Just",games_left,"game left to play")               
            print("\nPlayer won",users_win ,"games")
            print("The machine won",machine_win ,"games\n")
            played+=1
            games_left-=1
            if users_win==to_win or machine_win==to_win:
                    break
        if users_win<machine_win or machine_win==to_win:
            print("The machine is the winner!!!! Machine did win ",machine_win ,"games")
        elif users_win==to_win or machine_win<users_win:
            print("User is the winner!!!! User did win ",users_win ,"games")           
        else:
            print("There are no winners, TIE!!!!")
        sys.exit() #I have put it so that the infinite loop ends when reaching the number of games that were wanted to be played
    else:
        if not is_odd(first_input) or is_more_or_equal_3(first_input):
            print("Failed! The number of games must be odd and greater than or equal to 5")
            continue