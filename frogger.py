"""
File: frogger.py
Author: Ananya Thippeswamy
Date: 11/22/2024
Section: 23
E-mail: ho20134@umbc.edu
Description: the frog must avoid getting run over by the cars and cross the road
the frog can jump and it can move using the asdw keys
"""

import os

frog = '\U0001F438'

def select_game_file():
    # gets the list of files in the directory
    root, directories, files = next(os.walk('.'))
    frog_files = []
    for file in files:
        if file[-5:] == '.frog':
            frog_files.append(file)
    return user_select(frog_files)


def user_select(frog_files):
    # chooses the file based on user input
    print("These are the games you can play:")
    print(frog_files)
    which_game = input("Enter the game number or filename: ")
    if which_game == "game1.frog" or which_game == "game1" or which_game == "1":
        return frog_files[0]
    elif which_game == "game2.frog" or which_game == "game2" or which_game == "2":
        return frog_files[1]
    elif which_game == "game3.frog" or which_game == "game3" or which_game == "3":
        return frog_files[2]
    else:
        print("please print valid file")
        user_select(frog_files)


def adjust_file(file):
    # converts the file into a list within a list for
    # manipulation in other functions
    printable_game = []
    frog_line = ""
    last_line = ""
    game = open(file, 'r')
    base_game = game.readlines()
    game.close()
    for i in range(len(base_game)):
        if i == 2:
            frog_line = " " * (len(base_game[2])// 2) + frog +\
                        " " * ((len(base_game[2])// 2)-1) + "\n"
            printable_game.append(frog_line)
            printable_game.append(base_game[i])
        else:
            if base_game[i][-1] != "\n":
                base_game[i] += "\n"
            printable_game.append(base_game[i])
    last_line = " " * (len(base_game[2])-1) + "\n"
    printable_game.append(last_line)
    two_d_list = []
    for i in range(len(printable_game)):
        if i < 2:
            print(printable_game[i])
        else:
            row = []
            for chara in printable_game[i]:
                if chara != '\n':
                    row.append(chara)
                    print(chara, end=" ")
            print()
            two_d_list.append(row)

    return two_d_list


def print_game(round_num, list):
    # prints the current setup of the game
    print(round_num)
    for i in range(len(list)):
        for chara in list[i]:
            print(chara, end=" ")
        print()


def rotate(list, file):
    # rotates the cars
    speed_list = []
    game = open(file, 'r')
    speeds = game.readlines()
    game.close()
    for i in range(len(speeds)):
        if i == 1:
            speeds[i] = speeds[i].split()
            speed_list.append(speeds[i])
    num_rows = len(list)


    for i in range(1, num_rows - 1):
        shift = int(speed_list[0][i-1])
        list[i] = list[i][-shift:] + list[i][:-shift]


    return list


def move(round_num, current_list, jump_count, file, first_time):
    # moves the frog based on the user input and current row speed
    frog_row = 0
    frog_col = 0
    if first_time == True:
        game = open(file, 'r')
        base_game = game.readlines()
        game.close()
        for i in range(len(base_game)):
            if i == 0:
                base_game[i] = base_game[i].split()
                jump_count = int(base_game[0][2])
    for i in range(len(current_list)):
        for j in range(len(current_list[i])):
            if current_list[i][j] == frog:
                frog_row = i
                frog_col = j


    speed_list = []
    real_speed_list = []
    game = open(file, 'r')
    speeds = game.readlines()
    game.close()
    for i in range(len(speeds)):
        if i == 1:
            speeds[i] = speeds[i].split()
            speed_list.append(0)
            speed_list.append(speeds[i])
            speed_list.append(0)
    for item in speed_list:
        if type(item) == list:  # Check if the item is a list
            for sub_item in item:
                real_speed_list.append(int(sub_item))  # Convert each element to an integer
        else:
            real_speed_list.append(int(item))  # Convert non-list elements to integers


    which_move = input("WASDJ >> ").lower()
    if which_move == "w":
        if frog_row - 1 < 0:
            print("invalid")
            return False, jump_count
        elif current_list[frog_row - 1][frog_col] == "_":
            current_list[frog_row][frog_col] = "_"
            current_list[frog_row - 1][frog_col-(real_speed_list[frog_row])] = frog
            print_game(round_num, current_list)
            return False, jump_count
        elif current_list[frog_row - 1][frog_col] == "X":
            current_list[frog_row][frog_col] = "_"
            current_list[frog_row - 1][frog_col-(real_speed_list[frog_row])] = '\U0001318F'
            print_game(round_num, current_list)
            print("You Lost, Sorry Frog")
            return True, jump_count
    elif which_move == "a":
        if frog_col - 1 < 0:
            print("invalid")
            return False, jump_count
        elif current_list[frog_row][frog_col - 1] == "_":
            current_list[frog_row][frog_col] = "_"
            current_list[frog_row][frog_col - 1-(real_speed_list[frog_row])] = frog
            print_game(round_num, current_list)
            return False, jump_count
        elif current_list[frog_row][frog_col - 1] == "X":
            current_list[frog_row][frog_col] = "_"
            current_list[frog_row][frog_col - 1-(real_speed_list[frog_row])] = '\U0001318F'
            print_game(round_num, current_list)
            print("You Lost, Sorry Frog")
            return True, jump_count
    elif which_move == "s":
        if frog_row + 1 == len(current_list)-1:
            current_list[frog_row][frog_col] = "_"
            current_list[frog_row + 1][frog_col-(real_speed_list[frog_row])] = frog
            print_game(round_num, current_list)
            print("You won, Frog lives to cross another day.")
            return True, jump_count
        elif current_list[frog_row + 1][frog_col] == "_":
            current_list[frog_row][frog_col] = "_"
            current_list[frog_row + 1][frog_col-(real_speed_list[frog_row])] = frog
            print_game(round_num, current_list)
            return False, jump_count
        elif current_list[frog_row + 1][frog_col] == "X":
            current_list[frog_row][frog_col] = "_"
            current_list[frog_row + 1][frog_col-(real_speed_list[frog_row])] = '\U0001318F'
            print_game(round_num, current_list)
            print("You Lost, Sorry Frog")
            return True, jump_count
    elif which_move == "d":
        if frog_col + 1 > len(current_list[frog_row])-1:
            print("invalid")
            return False, jump_count
        elif current_list[frog_row][frog_col + 1] == "_":
            current_list[frog_row][frog_col] = "_"
            current_list[frog_row][frog_col + 1-(real_speed_list[frog_row])] = frog
            print_game(round_num, current_list)
            return False, jump_count
        elif current_list[frog_row][frog_col + 1] == "X":
            current_list[frog_row][frog_col] = "_"
            current_list[frog_row][frog_col + 1-(real_speed_list[frog_row])] = '\U0001318F'
            print_game(round_num, current_list)
            print("You Lost, Sorry Frog")
            return True, jump_count
    elif len(which_move) > 0 and which_move[0] == "j":
        which_move = which_move[1:].strip().split()
        row = int(which_move[0])
        col = int(which_move[1])

        if not((frog_row + 1 ==  row or frog_row - 1 == row)\
                and col < len(current_list[frog_row]) and col > 0 and int(jump_count) > 0):
            print("invalid")
            return False, jump_count
        elif current_list[row][col - 1] == "_":
            if row == len(current_list)-1:
                current_list[frog_row][frog_col] = "_"
                current_list[row][col-1-(real_speed_list[frog_row])] = frog
                print_game(round_num, current_list)
                print("You won, Frog lives to cross another day.")
                jump_count -= 1
                return True, jump_count
            else:
                current_list[frog_row][frog_col] = "_"
                current_list[row][col - 1-(real_speed_list[frog_row])] = frog
                print_game(round_num, current_list)
                jump_count -= 1
                return False, jump_count
        elif current_list[row][col - 1] == "X":
            current_list[frog_row][frog_col] = "_"
            current_list[row][col - 1-(real_speed_list[frog_row])] = '\U0001318F'
            print_game(round_num, current_list)
            print("You Lost, Sorry Frog")
            return True, jump_count
    else:
        print_game(round_num, current_list)
        return False, jump_count


def frogger_game(file):
    # controls all the game functions
    game_over = False
    round_num = 2
    start = 1
    printable_game = adjust_file(file)
    while game_over == False:
        if(start > 1):
            new_list = rotate(new_list, file)
            game_over, jump_count = move(round_num, new_list, jump_count, file, False)
        else:
            new_list = rotate(printable_game, file)
            game_over, jump_count = move(round_num, new_list, 0, file, True)
            start+=1

        round_num += 1


if __name__ == '__main__':
    selected_game_file = select_game_file()
    frogger_game(selected_game_file)