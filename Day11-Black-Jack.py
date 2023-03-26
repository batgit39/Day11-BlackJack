import random, os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players_cards = [0,0]
computers_cards = [0,0]

def players_pts(points):
    print("Your Cards :")
    for i in range(len(players_cards)):
        print(f"Card {i + 1} = {players_cards[i]}")
    print(f"Your Total : {points}\n")

def computer_pts(points):
    print("Computer Cards :")
    for i in range(len(computers_cards)):
        print(f"Card {i + 1} = {computers_cards[i]}")
    print(f"Computer's Total : {points}\n")



def endgame():
    computers_points = 0
    for i in range( len (computers_cards ) ):
        computers_points += computers_cards[i]

    players_points = 0
    for i in range( len (players_cards ) ):
        players_points += players_cards[i]

    if players_points > 21:
        players_pts(players_points)
        computer_pts(computers_points)

        print("You Lost")

    elif players_points > computers_points or computers_points > 21:        
        players_pts(players_points)
        computer_pts(computers_points)

        print("You Won!")

    elif players_points == computers_points:
        players_pts(players_points)
        computer_pts(computers_points)

        print("It's a Draw")

    else:
        players_pts(players_points)
        computer_pts(computers_points)

        print("You Lost")



game = True
while game:
    if input("Do you want to play a game? If yes press y : ") != "y":
        game = False
        break
    
    os.system('clear')
    print(logo)
    players_cards[0] = random.choice(cards)    
    players_cards[1] = random.choice(cards) 
    # print(f"({p_card1} + {p_card2})")
    computers_cards[0] = random.choice(cards)    
    computers_cards[1] = random.choice(cards)


    print("players cards :")
    print(f"Card 1 {players_cards[0]}")
    print(f"Card 2 {players_cards[1]}")
    print(f"Your total is : {sum(players_cards)}")
    print(f"Computer's Card : {computers_cards[0]}\n")

    #ask options
    note = True
    while note:
        choice = input("Now you can either: \n1 - Stand - Press S \n2 - Hit - Press H \nChoice :").lower()
        
        if choice == "h":
            # #new card for user and ask again 
            players_cards += [random.choice(cards)]
            print(f"your card is : {players_cards[2]}\n")
            if sum(players_cards) > 21:
                for i in range(len(players_cards)):
                    players_cards[i-1] = 0
                print("you lost")
                break

        else:
            if choice == "s":
                note = False
                #reveal Computer
                print(f"Computer's 2nd Card is : {computers_cards[1]}\n")
                endgame()      


            else:
                #wrong choice idk but you have to do something here
                print("Wrong input! Please try again")
        

        for i in range(len(players_cards)):
            players_cards[i-1] = 0
