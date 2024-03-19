import random as rn
def deal():
    cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return rn.choice(cartas)

def score(mano):
    print(sum(mano))
    if sum(mano)==21 and len(mano)==2:
    
        return 0
    if 11 in mano and sum(mano)>21:
        mano.remove(11)
        mano.append(1)
        
    return sum(mano)


def compare(score_j,score_c):
    #Bug fix. If you and the computer are both over, you lose.
    if score_j > 21 and score_c > 21:
        return "You went over. You lose 😤"


    if score_j == score_c:
        return "Draw 🙃"
    elif score_c == 0:
        return "Lose, opponent has Blackjack 😱"
    elif score_j == 0:
        return "Win with a Blackjack 😎"
    elif score_j > 21:
        return "You went over. You lose 😭"
    elif score_c > 21:
        return "Opponent went over. You win 😁"
    elif score_j > score_c:
        return "You win 😃"
    else:
        return "You lose 😤"  

def otro_juego():
  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  mis_cartas = []
  comp_cartas = []
  fin_juego = False

  for i in range(2):
    mis_cartas.append(deal())
    comp_cartas.append(deal())

  while  not fin_juego:
    score_j = score(mis_cartas)
    score_c = score(comp_cartas)
    print(f"   Your cards: {mis_cartas}, current score: {score_j}")
    print(f"   Computer's first card: {comp_cartas[0]}")
    if score_c==0 or score_j==0 or score_j>21:
        fin_juego = True
    else:
        mas_cartas = input('Mas cartas? stand or hit:  ')
        if mas_cartas == 'hit':
            mis_cartas.append(deal())
        else:
            fin_juego = True

  while score_c != 0 and score_c <17:
    comp_cartas.append(deal())
    score_c = score(comp_cartas)
  print(f"   Your final hand: {mis_cartas}, final score: {score_j}")
  print(f"   Computer's final hand: {comp_cartas}, final score: {score_c}")
  print(compare(score_j,score_c))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
 
  otro_juego()







