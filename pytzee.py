"""
File: pytzee
Author: Ananya Thippeswamy
Date: 11/1/2024
Section: 23
E-mail: ho20134@umbc.edu
Description: yahtzee
"""

import random

curr_round_num = 0
num_counts = 6
selection = ""
roll = [0, 0, 0, 0, 0]
scorecard = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
v_three_of_kind = False
four_of_kind = False
full_house = False
chance = False
pytzee = False
small_straight = False
large_straight = False


def roll_dice():
    """
    :return: a list containing five integers representing dice rolls between 1 and 6.
    """
    for i in range(5):
        roll[i] = random.randint(1, 6)
    return roll


def user_choice(roll, curr_round_num, scorecard):
    selection = input("How would you like to count this dice roll?").lower()
    if selection in ["three of a kind", "3 of a kind"]:
        three_of_kind(roll, curr_round_num, scorecard, v_three_of_kind)
    elif selection in ["four of a kind", "4 of a kind"]:
        four_of_kind(roll, curr_round_num, scorecard, four_of_kind)
    elif selection == "full house":
        full_house(roll, curr_round_num, scorecard, full_house)
    elif selection == "chance":
        chance(roll, curr_round_num, scorecard, chance)
    elif selection == "pytzee":
        pytzee(roll, curr_round_num, scorecard)
    elif selection == "small straight":
        small_straight(roll, curr_round_num, scorecard, small_straight)
    elif selection == "large straight":
        large_straight(roll, curr_round_num, scorecard, large_straight)
    elif "count " in selection:
        num = int(selection.split()[1])
        if num in [1, 2, 3, 4, 5, 6]:
            count_num(curr_round_num, num)
        else:
            print("choose 1, 2, 3, 4, 5, or 6.")
    else:
        print("Try again.")


def print_score(scorecard):
    sum = 0
    scorecard_names = ["1's: ", "2's: ", "3's: ", "4's: ", "5's: ", "6's': ", \
                       "three of a kind: ", "four of a kind: ", "full house: ", \
                       "small straight: ", "large straight: ", "yahtzee: ", "chance: "]
    for i in range(13):
        print(scorecard_names[i] + str(scorecard[i]))
        sum += scorecard[i]
    print(str(sum) + "is your score")


def count_num(curr_round_num, num):
    # (count 1's, 2's, 3's, 4's, 5's, or 6's)
    count_sum = 0
    count = 0
    for r in roll:
        if num == r:
            count+=1
    if count > 0:
        count_sum += count * num
        scorecard[num - 1] = count_sum
        curr_round_num += 1
    else:
        print("Make a different choice.")
        user_choice(roll, curr_round_num, scorecard)


def three_of_kind(roll, curr_round_num, scorecard, v_three_of_kind):
    three_sum = 0
    for i in range(1, 7):
        count = 0
        for r in roll:
            if r == i:
                count += 1
                if count >= 3:
                    three_sum += 3*r
                    v_three_of_kind = True
                    curr_round_num += 1
                    scorecard[6] = three_sum

    if v_three_of_kind == False:
        print("Make a different choice.")
        user_choice(roll, curr_round_num, scorecard)


def four_of_kind(roll, curr_round_num, scorecard, four_of_kind):
    four_sum = 0
    for i in range(1, 7):
        count = 0
        for r in roll:
            if r == i:
                count += 1
                if count >= 4:
                    four_sum += 4*r
                    four_of_kind = True
                    curr_round_num += 1
                    scorecard[7] = 25
    if four_of_kind == False:
        print("Make a different choice.")
        user_choice(roll, curr_round_num, scorecard)


def full_house(roll, curr_round_num, scorecard, full_house):
    for i in range(1, 7):
        count1 = 0
        val3 = 0
        count2 = 0
        for r in roll:
            if r == i:
                count1 += 1
                if count1 == 3:
                    val3 = r
        if count1 == 3:
            for j in range(1, 7):
                if j != val3:
                    count2 = 0
                    for r in roll:
                        if r == j:
                            count2 += 1

    if count1 == 3 and count2 == 2:
        full_house = True
        curr_round_num += 1
        scorecard[8] = 25
    if full_house == False:
        print("Make a different choice.")
        user_choice(roll, curr_round_num, scorecard)


def chance(roll, curr_round_num, scorecard, chance):
    chance_sum = 0
    for i in roll:
        chance_sum += i
    chance = True
    curr_round_num += 1
    scorecard[12] = chance_sum


def pytzee(roll, curr_round_num, scorecard):
    if roll[0] == roll[1] == roll[2] == roll[3] == roll[4]:
        if pytzee == True:
            scorecard[11] += 100
        else:
            scorecard[11] += 50
    else:
        print("Make a different choice.")
        user_choice(roll, curr_round_num, scorecard)


def small_straight(roll, curr_round_num, scorecard, small_straight):
    if ((roll[0] + 1 ) == roll[1]) and \
            ((roll[0] + 2) == roll[2]) and \
            ((roll[0] +3) == roll[3]):
        small_straight = True
        curr_round_num += 1
        scorecard[9] += 30

    elif ((roll[1] + 1) == roll[2]) and \
            ((roll[1] + 2) == roll[3]) and \
            ((roll[1] + 3) == roll[4]):
        small_straight = True
        curr_round_num += 1
        scorecard[9] += 30
    else:
        print("Make a different choice.")
        user_choice(roll, curr_round_num, scorecard)


def large_straight(roll, curr_round_num, scorecard, large_straight):
    if ((roll[0] + 1) == roll[1]) and \
            ((roll[0] + 2) == roll[2]) and \
            ((roll[0] + 3) == roll[3]) and \
            ((roll[0] + 4) == roll[4]):
        large_straight = True
        curr_round_num += 1
        scorecard[10] += 40
    else:
        print("Make a different choice.")
        user_choice(roll, curr_round_num, scorecard)


def play_game(num_rounds):
    while num_rounds >= curr_round_num:
        roll_dice()
        print(roll)
        user_choice(roll,curr_round_num,scorecard)
        print_score(scorecard)


if __name__ == '__main__':
    num_rounds = int(input('What is the number of rounds that you want to play? '))
    seed = int(input('Enter the seed or 0 to use a random seed: '))
    if seed:
        random.seed(seed)
    play_game(num_rounds)





