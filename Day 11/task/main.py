import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

wannaPlay = input("Wanna play Blackjack ? y/n : ")
while wannaPlay == "y":
    print("\n"*20)
    print(logo)
    computer_card = []
    user_card = []
    computer_card.append(random.choice(cards))
    user_card.append(random.choice(cards))
    user_card.append(random.choice(cards))
    userSum = user_card[0] + user_card[1]
    computersum = computer_card[0]

    draw = "y"
    while draw == "y":
        print(f"Your Cards: {user_card}, current score {userSum}")
        print(f"Computer first card : {computer_card[0]}")
        draw = input("Wanna darw(y) or Pass(n): ")
        if draw == "y":
            value = random.choice(cards)
            if value == 11 and (userSum+value) > 21:
                userSum += 1
                user_card.append(1)
            else:
                userSum += value
                user_card.append(value)
        if userSum > 21:
            draw = "n"
    if userSum <= 21:
        while computersum < 17:
            value = random.choice(cards)
            if value == 11 and (userSum + value) > 21:
                computersum += 1
                computer_card.append(1)
            else:
                computersum += value
                computer_card.append(value)

    print(f"Your Final Cards {user_card} , Final Score {userSum}")
    print(f"Computer's Final Hands{computer_card}, Final score: {computersum}")

    if userSum == computersum:
        print("It's Draw ")
    elif computersum >21:
        print("Opponent went Over! You Won")
    elif userSum > 21:
        print("You went Over! Computer Won")
    elif userSum > computersum:
        print("You won")
    else:
        print("Computer won")
    wannaPlay = input("Wanna play jackBlack ? y/n : ")

