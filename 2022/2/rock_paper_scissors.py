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
    "X": RPS.ROCK,
    "Y": RPS.PAPER,
    "Z": RPS.SCISSORS,
}

with open("input") as f:
    for line in f:
        line = line.strip()
        points.append(0)

        their_choice, our_choice = line.split(" ")

        their_choice = rps_mapping_dict.get(their_choice)
        our_choice = rps_mapping_dict.get(our_choice)

        points[-1] += our_choice

        if their_choice == our_choice:
            points[-1] += Result.DRAW
        elif (
            (their_choice == RPS.ROCK and our_choice == RPS.PAPER)
            or (their_choice == RPS.PAPER and our_choice == RPS.SCISSORS)
            or (their_choice == RPS.SCISSORS and our_choice == RPS.ROCK)
        ):
            points[-1] += Result.WON
        else:
            points[-1] += Result.LOSS


print("Points", sum(points))
