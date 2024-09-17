import random
from art import logo
def deal_card():
    """Return a random card Drawn from deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def final_result(u_score,c_score):
    """Print the final result of the Game"""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

wannaPlay = input("Wanna play Blackjack ? y/n : ")
while wannaPlay == "y":
    print("\n"*20)
    print(logo)
    computer_card = []
    user_card = []

    computer_card.append(deal_card())
    user_card.append(deal_card())
    user_card.append(deal_card())

    userSum = user_card[0] + user_card[1]
    computerSum = computer_card[0]

    draw = "y"
    while draw == "y":
        print(f"Your Cards: {user_card}, current score {userSum}")
        print(f"Computer first card : {computer_card[0]}")
        draw = input("Wanna darw(y) or Pass(n): ")
        if draw == "y":
            value = deal_card()
            if value == 11 and (userSum+value) > 21:
                userSum += 1
                user_card.append(1)
            else:
                userSum += value
                user_card.append(value)
        if userSum > 21:
            draw = "n"
    if userSum <= 21:
        while computerSum < 17:
            value = int( deal_card())
            if value == 11 and (userSum + value) > 21:
                computerSum += 1
                computer_card.append(1)
            else:
                computerSum += value
                computer_card.append(value)

    print(f"Your Final Cards {user_card} , Final Score {userSum}")
    print(f"Computer's Final Hands{computer_card}, Final score: {computerSum}")
    print(final_result(user_card,computer_card, userSum, computerSum))

    wannaPlay = input("Wanna play jackBlack ? y/n : ")

