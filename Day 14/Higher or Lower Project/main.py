from art import logo,vs
import random
from game_data import data

print(logo)


def random_data():
    return random.choice(data)

def compare(celeb_a,celeb_b):
    print(f"Compare A : {celeb_a['name']},a {celeb_a['description']}, from {celeb_a['country']}.")
    print(vs)
    print(f"Against B : {celeb_b['name']},a {celeb_b['description']}, from {celeb_b['country']}.")

    if celeb_a['follower_count'] > celeb_b['follower_count']:
        return "A"
    else:
        return "B"

correct = True
score = 0
celeb_a = random_data()

while correct:
    celeb_b = random_data()
    correct_answer = compare(celeb_a,celeb_b)

    if celeb_a == celeb_b:
        celeb_b = random_data()

    answer = input("Who has more followers? A or B : ")

    print("\n" * 20)
    print(logo)

    if correct_answer == answer.upper():
        score += 1
        celeb_a = celeb_b
        print(f"You're Right, current score : {score}\n")
    else:
        correct = False
        print(f"You're wrong, Final score : {score}")
