from art import logo
import random
print(logo)
#function to return random cards
def draw_Card():
    """Returns a Random Card"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

#calculating the score from cards
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2 :
        return 0
    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(pl_score,co_score):
    print(f"Player Score{pl_score}\nComputer Score{co_score}")
    if pl_score == co_score: return "Draw"
    elif co_score == 0: return "Lose , Comuter win"
    elif pl_score == 0: return "You WIn"
    elif pl_score > 21: return 'You Lose'
    elif co_score > 21: return 'You Win'
    elif pl_score > co_score : return 'You Win'
    else: return 'Computer Win You Lose'
        
    

player_Card=[]
com_card=[]
is_game_over = False
#each one get 2 cards to start with
for _ in range(2):
    player_Card.append(draw_Card())
    com_card.append(draw_Card())
    
#checking the score  
while not is_game_over:
    pl_score = calculate_score(player_Card)
    co_score = calculate_score(com_card)
    print(f"player card {player_Card} sum = { pl_score} and computer cards {com_card} and sum = {co_score}")
    
    if pl_score == 0 or co_score == 0 or pl_score >21:
        is_game_over = True
    else:
        play_more = input("type y to get another card else n to pass :")
        if play_more == 'y':
            player_Card.append(draw_Card())
        else:
            is_game_over = True
            
while co_score != 0 and co_score <17 :
    com_card.append(draw_Card())
    co_score = calculate_score(com_card)  
print(compare(pl_score,co_score))
    




