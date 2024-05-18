from gamedata import data
import random
import os
import time

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
    time.sleep(0.1)

should_continue = True
score = 0
acc_b = random.choice(data)

while should_continue:
    acc_a = acc_b
    acc_b = random.choice(data)
    while acc_a == acc_b:
        acc_b = random.choice(data)

    clear_console()
    def format_data(acc):
        acc_name = acc['Name']
        acc_desc = acc['Description']
        acc_coun = acc['Country']

        return f"{acc_name}, {acc_desc} from {acc_coun}."

    print(f"Compare A: {format_data(acc_a)}\nOr\nCompare B: {format_data(acc_b)}")
    guess = str(input("Which has more followers? Type 'A' or 'B': ")).lower()

    a_foll = acc_a['Followers']
    b_foll = acc_b['Followers']

    def check_ans(guess, a_foll, b_foll):
        if a_foll > b_foll:
            return guess == 'a'
        else:
            return guess == 'b'

    is_correct = check_ans(guess, a_foll, b_foll)

    if is_correct == True:
        score += 1
        print(f"You are right! Current score: {score}.")
    elif is_correct == False:
        should_continue = False
        print(f"You are wrong. Final score: {score}.")