import random

#BLACKJACKKKKKKKKKdwwde





value_card_dict = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Knight": 10, "Queen": 10, "King": 10}
card_list = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knight", "Queen", "King"]
def play_game():
    total_balance = int(input("\n\nHello and welcome to the game of BlackJack, please input the total balance you wish to use:  "))
    print("\nYour available balance is now: " + str(total_balance)+ "\n\n\n\n")
    while total_balance > 0:
        stake = staking()
        dealer_card = draw_dealer_first()
        player_value = draw_player()
        if player_value > 21:
            total_balance -= stake
        else:
            dealer_value = draw_dealer_until_stop(dealer_card)
            print("\n\nYour value is: " + str(player_value) + "\n\n" )
            bool = check_win(dealer_value, player_value)
            total_balance = win_lose(total_balance, stake, bool)
        if total_balance == 0:
            choice = int(input(print("You just lost all of your money, input more to continue to play:  ")))
            total_balance = choice
            return total_balance
        elif total_balance > 0:
            print("\n\nNow the next round begins: \n\n\n\n\n")
            continue
        else:
            print("Thanks for playing with us today! ")
    #Testchangefwefew
def staking():
    stake = int(input("\nHow much would you like to stake this round?   "))
    print("\nYou are currently risking: " + str(stake) + "\n\n")
    return stake

def draw_dealer_first():
    card = random.choice(card_list)
    for key, value in value_card_dict.items():
        if key == card:
            dealer_card_key = key
            dealer_card_value = value_card_dict[key]
            break
                
    if dealer_card_key == "Ace":
        dealer_card_value += 10
    print("\nCards are now being drawn.... \n\n\n")
    print("\n\nThe dealer drew: " + dealer_card_key + "\n")
    print("The dealers value is: " + str(dealer_card_value) + "\n")
    
    return [dealer_card_key, dealer_card_value]

def draw_dealer_until_stop(card):
    dealer_list_keys = []
    dealer_list_keys.append(card[0])

    dealer_list_values = []
    dealer_list_values.append(card[1])

    return_value = sum(dealer_list_values)

    while return_value < 17:
        card = random.choice(card_list)
        for key, value in value_card_dict.items():
            if key == card:
                dealer_list_keys.append(key)
                dealer_list_values.append(value)
                break
        return_value = sum(dealer_list_values) 
        
    for card in dealer_list_keys:
        if card == "Ace":
            return_value += 10
    
    for card in dealer_list_keys:
       if card == "Ace" and return_value > 21:
            return_value -= 10 


    print("\n\n\nThe dealer draws until 16 and stops on 17")
    print("\n\nThe dealer now has the cards: " + str(dealer_list_keys) + "\n")
    print("The dealers value is: " + str(return_value) + "\n")

    return return_value

def draw_player(count = 1, return_value = 0, choice = False):
    player_cards_value = []
    player_cards_key = []
    while count == 1 and len(player_cards_key) != 2 or choice == True:
        choice = False
        card = random.choice(card_list)
        for key, value in value_card_dict.items():
            if key == card:
                player_cards_key.append(key)
                player_cards_value.append(value)
                break
        cards_value = sum(player_cards_value) 
        
    for card in player_cards_key:
        if card == "Ace":
            cards_value += 10

    return_value += cards_value
        
    for card in player_cards_key:
        if card == "Ace" and return_value > 21:
            return_value -= 10 
    
    count += 1

    print("You drew: " + str(player_cards_key) + "\n")
    print("Your value is: " + str(return_value) + "\n\n\n")

    
    if return_value > 21:
        print("You busted")
        return return_value

    choice = input("Do you want another card? Yes / No :  ")
    if choice == "Yes":
        return draw_player(count, return_value, True)  
    else:
         print("\nYour value is: " + str(return_value) + "\n" )
         return return_value

def check_win(dealer_hand, player_hand):
   
    result = ""
    if player_hand == 21 and dealer_hand != 21:
        result = "blackjack"
        return result
    elif player_hand > 21:
        result = "lose"
        return result   
    elif player_hand < 21 and dealer_hand > 21:
        result = "win"
        return result   
    elif player_hand < dealer_hand and dealer_hand < 21 :  
        result = "lose"      
        return result
    elif player_hand == dealer_hand:
        result = "lose"
        return result
    else:
        result = "win"
        return result
   
def win_lose(total_balance, stake, bool):

    if bool == "blackjack":
        total_balance += 1.5*stake
        print("BLACKJACK! You won, you balance is now:  " + str(total_balance)) 
        return total_balance
    elif bool == "win":    
        total_balance += stake
        print("You won, you balance is now:  " + str(total_balance)) 
        return total_balance
    else:
        total_balance -= stake
        print("You lost, you balance is now:  " + str(total_balance)) 
        return total_balance


play_game()