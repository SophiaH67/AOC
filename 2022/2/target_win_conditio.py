import json


class RPS:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result:
    LOSS = 0
    DRAW = 3
    WON = 6


points = []

rps_mapping_dict = {
    "A": RPS.ROCK,
    "B": RPS.PAPER,
    "C": RPS.SCISSORS,
}

target_win_condition_dict = {
    "X": Result.LOSS,
    "Y": Result.DRAW,
    "Z": Result.WON,
}

with open("input") as f:
    for line in f:
        line = line.strip()
        points.append(0)

        their_choice, target_win_condition = line.split(" ")

        their_choice = rps_mapping_dict.get(their_choice)
        our_choice = -1

        target_win_condition = target_win_condition_dict.get(target_win_condition)

        if target_win_condition == Result.DRAW:
            our_choice = their_choice
        elif target_win_condition == Result.LOSS:
            if their_choice == RPS.PAPER:
                our_choice = RPS.ROCK
            elif their_choice == RPS.ROCK:
                our_choice = RPS.SCISSORS
            elif their_choice == RPS.SCISSORS:
                our_choice = RPS.PAPER
        else:
            if their_choice == RPS.PAPER:
                our_choice = RPS.SCISSORS
            elif their_choice == RPS.SCISSORS:
                our_choice = RPS.ROCK
            else:
                our_choice = RPS.PAPER

        points[-1] += our_choice
        points[-1] += target_win_condition


print("Points", sum(points))
