import os, random, time; from termcolor import cprint; cardValues = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}; playerData = {}; cardcombinations = ["A of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "J of Hearts", "Q of Hearts", "K of Hearts", "A of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "J of Spades", "Q of Spades", "K of Spades", "A of Cloves", "2 of Cloves", "3 of Cloves", "4 of Cloves", "5 of Cloves", "6 of Cloves", "7 of Cloves", "8 of Cloves", "9 of Cloves", "10 of Cloves", "J of Cloves", "Q of Cloves", "K of Cloves", "A of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "J of Diamonds", "Q of Diamonds", "K of Diamonds"]
def clear():
    os.system('clear')
def reset():
    clear()
    print()
    cprint('Welcome to Poker!', 'magenta')
    cprint('=============================', 'magenta')
    print()
    cprint("Type 'I' To Receive Instructions", 'black')
    cprint("Type 'P' To Play Game", 'black')
    print()
    decision = input("Enter Choice: ")
    if decision != 'I' and decision != 'P':
        clear()
        print("Please Enter Either 'P' or 'I'", 'red')
        reset()
    if decision == 'I':
        print()
        cprint("Welcome to the captivating world of console poker! Get ready to immerse yourself in a thrilling and strategic card game. The rules are simple yet offer endless excitement. Each player is dealt a set of private cards, known as hole cards, which only they can see. As the game progresses, five community cards are placed face-up on the table, shared by all players. Your ultimate objective is to create the strongest five-card hand using a combination of your hole cards and the community cards. The hierarchy of hands ranges from a high card to the prestigious royal flush, where the odds of winning soar. Betting is the heart of the game, adding layers of anticipation and tension. Players can either call, matching the previous bet; raise, increasing the bet; or fold, forfeiting their chance to win the current pot. Clever strategy and keen observation will be your allies in determining whether your opponents are bluffing or holding a winning hand. The climax of each round is the showdown, where remaining players reveal their hands, and the best hand wins the pot. It is an art of deception, calculation, and courage. With each hand, you will learn to analyze probabilities, read your opponents, and fine-tune your decision-making skills. Whether you are a seasoned poker pro or a novice eager to learn, this console poker game offers an unparalleled experience of mental prowess and thrills. So, step up to the virtual poker table, test your mettle, and show your opponents that you have got the skills to outplay and outwit them in this captivating Python-based poker adventure!", 'blue')
        print()
        decision2 = input("Enter 'P' To Play Game: ")
        if decision2 == 'P':
            print()
            settings()
        elif decision2 != 'P':
            clear()
            print("Please Enter Either 'P' or 'I'", 'red')
            reset()
    if decision == 'P':
        settings()
def settings():
    numPlayer = input("Enter Number of Players: ")
    if numPlayer.isdigit():
        if int(numPlayer) >= 2 and int(numPlayer) <= 10:
            stackinput = input("Enter starting stack value for each player (without '$'): ")
            if stackinput.isdigit():
                if int(stackinput) >= 1 and int(stackinput) <= 100000:
                    setUpPlayers(int(numPlayer), int(stackinput))
                else:
                    os.system('clear')
                    print("Starting stack must be between $1 and $100000")
                    settings()
            else:
                clear()
                print("Starting stack must be an number!!")
                settings()
        elif int(numPlayer) < 2 or int(numPlayer) > 10:
            clear()
            print('You can only play with 2-10 players')
            settings()
    else:
        settings()
def makeHand(player):

    val = random.randint(1,13)
    selector = random.randint(1, 4)
    playerCard = []
    randomcard = random.randint(0, 51)
    playerData[player]["Hand"].append(cardcombinations[randomcard])
    cardcombinations.remove(cardcombinations[randomcard])
def setUpPlayers(numPlayers, stack):

    player = 1
    numOfPlayers = numPlayers

    while player <= numOfPlayers:
        playername = input("Player {}, enter your name: ".format(player))
        playerData[player] = {"Name" : playername, "Stack": stack, "Hand" : []}
        playerData["Name"] = playername
        playerData["Stack"] = stack
        makeHand(player)
        makeHand(player)
        player += 1

    showHands(numOfPlayers)
def showHands(numplayers):
    clear()
    player = 1
    cprint("During this phase of the game, each player's two-card hand will be displayed. We kindly request that all other players close their eyes while one player receives their hand. After a brief 3-second delay, the hand will be unveiled and remain visible on the screen for 5 seconds, after which the next players hand will be shown (following another 3 second delay)", "green")
    print()
    time.sleep(6)
    clear()
    cprint("The process of revealing the hand will now commence.", "red")
    print()
    time.sleep(2)
    print("Everyone except for " + playerData[player]["Name"] + ", please close your eyes!")
    time.sleep(3)
    clear()
    numplayer = numplayers

    while player < numplayer:       
        print("Hello " + playerData[player]["Name"] + "! Your starting hand is the " + playerData[player]["Hand"][0] + " and the " + playerData[player]["Hand"][1] + "!")
        time.sleep(7)
        clear()
        print("Please tell {} that they can now open their eyes!".format(playerData[player + 1]["Name"]))
        time.sleep(4)
        clear()
        player += 1 
    print("Hello " + playerData[player]["Name"] + "! Your starting hand is the " + playerData[player]["Hand"][0] + " and the " + playerData[player]["Hand"][1] + "!")
    time.sleep(7)
    gamePlay(int(playerData[player]["Stack"]), numplayer, 0)
def remove_player(playernumber):

    del playerData[playernumber]
    for key in range(playernumber + 1, len(playerData) + 2):
        if key in playerData:
            playerData[key - 1] = playerData.pop(key)
            playerData[key - 1]["Name"] = f"Player {key - 1}"
def removePlayersWithNoStack(numplayers):
    players_to_remove = []

    for player in range(1, numplayers + 1):
        if playerData[player]["Stack"] == 0:
            players_to_remove.append(player)

    for player in players_to_remove:
        del playerData[player]
def firstbet(firstchoice, player, pot, call, round, numplayers):
    currentplayer = player
    firsteveraction = True
    targeted = 1

    if firstchoice == 'C':
        playerData[player]["Stack"] -= call
        pot += call
        player += 1
        betting(player, pot, call, round, targeted, numplayers)

    elif firstchoice == 'R':
        amount = input("Raise " + call + "to: ")
        if amount.isDigit() and amount <= playerData[player]["Stack"]:
            call = amount
            pot += call
            playerData[player]["Stack"] -= amount
            currentplayer += 1
            betting(player, pot, call, round, targeted, numplayers)

        elif amount.isDigit() == False:
            os.system('clear')
            print("Please input a digit", "red")
            firstbet(firstchoice, 1, pot, call, 1)
        else:
            os.system('clear')
            print("You cannot bet more than you already have!", "red")
            firstbet(firstchoice, 1, pot, call, 1)

    else:
        remove_player(player)
        betting(player, pot, call, round, targeted, numplayers)
def betting(player, pot, call, round, targeted, numofplayers):

    player = player
    pot = pot
    call = call
    round = round
    targeted = targeted
    firstRound = True
    numplayers = numofplayers
    eventnumber = 0

    while firstRound:
    
        if call == 0:
            choice = input(playerData[player]["Name"] + ", enter Ch to check, R to Raise the bet amount, or F to Fold: ")
            if choice != 'Ch' and choice != 'R' and choice != 'F':
                os.system('clear')
                print()
                cprint("Please only enter accepted inputs", "red")
                numberofplayers = 0
                for i in playerData:
                    numberofplayers += 1
                gamePlay(int(playerData[1]["Stack"]), numberofplayers, eventnumber)

            else:
                if choice == 'R':
                    amount = input("Raise " + call + "to: ")

                    if amount.isDigit() and amount <= playerData[player]["Stack"]:
                        call = amount
                        pot += call
                        if player < numplayers:
                            player += 1
                        else:
                            player = 1
                        playerData[player]["Stack"] -= amount
                        betting(player, pot, call, round, targeted, numplayers)
                    elif amount.isDigit() == False:
                        os.system('clear')
                        print("Please input a digit", "red")
                        betting(player, pot, call, round, targeted)
                    else:
                        os.system('clear')
                        print("You cannot bet more than you already have!", "red")
                        betting(player, pot, call, round, targeted)

                elif choice == 'Ch':
                    call = 0
                    targeted += 1
                    if player < numplayers:
                        player += 1
                    else:
                        player = 1
                    betting(player, pot, call, round, targeted, numplayers)

                else:
                    player += 1
                    remove_player(player)
                    betting(player, pot, call, round, targeted, numplayers)

        else:
            choice = input(playerData[player]["Name"] + ", enter C to call the amount of " + str(call) + ", R to Raise the bet amount, or F to Fold: ")

            if choice != 'C' and choice != 'R' and choice != 'F':
                os.system('clear')
                print()
                cprint("Please only enter accepted inputs", "red")
                numberofplayers = 0
                for i in playerData:
                    numberofplayers += 1
                gamePlay(int(playerData[1]["Stack"]), numberofplayers, eventnumber)

            else:
                if choice == 'R':
                    amount = input("Raise " + call + "to: ")

                    if amount.isDigit() and amount <= playerData[player]["Stack"]:
                        call = amount
                        pot += call
                        if player < numplayers:
                            player += 1
                        else:
                            player = 1
                        playerData[player]["Stack"] -= call
                        betting(player, pot, call, round, targeted, numplayers)

                    elif amount.isDigit() == False:
                        os.system('clear')
                        cprint("Please input a digit", "red")
                        betting(player, pot, call, round, targeted)
                    else:
                        os.system('clear')
                        cprint("You cannot bet more than you already have!", "red")
                        betting(player, pot, call, round, targeted)

                elif choice == 'C':

                    pot += call
                    playerData[player]["Stack"] -= call
                    if player < numplayers:
                        player += 1
                    else:
                        player = 1
                    betting(player, pot, call, round, targeted, numplayers)

                else:
                    remove_player(player)
                    betting(player, pot, call, round, targeted, numplayers)

def gamePlay(stack, numplayers, betevent):

    clear()
    cprint("We will now begin the game!", "magenta")
    time.sleep(3)
    clear()
    ante = 0.05 * stack
    pot = numplayers * ante
    player = 1
    j = 1

    numberofplayers = 0 
    for i in playerData:
        numberofplayers += 1

    while j <= numplayers:
        playerData[j]["Stack"] -= ante
        j += 1
    j = 1
    round = 1
    call = 0.05 * pot

    print()
    print()
    cprint(str("Round " + str(round)), "blue")
    cprint(str("Current Pot: " + str(pot)), "blue")
    print()
    while j <= numplayers:
        cprint("Current Player Stacks:", "green")
        cprint("      " + str(playerData[j]["Name"]) + " : " + str(playerData[j]["Stack"]), "green")
        j += 1

    print()
    removePlayersWithNoStack(numplayers)
    print(playerData[player]["Name"] + ", what would you like to do?")

    if betevent == 0:

        firstchoice = input("Enter C to Bet 1/20 of the current pot, R to Raise the bet amount, or F to Fold: ")

        if firstchoice != 'C' and firstchoice != 'Ch' and firstchoice != 'R' and firstchoice != 'F':
            os.system('clear')
            print()
            cprint("Please only enter accepted inputs", "red")
            gamePlay(int(playerData[1]["Stack"]), numberofplayers)

        else:
            firstbet(firstchoice, 1, pot, call, 1, numberofplayers)

    elif betevent == 1:
        # flop()
        pass
    
    elif betevent == 2:
        # turn()
        pass
    else:
        # river() 
        pass   
reset()
