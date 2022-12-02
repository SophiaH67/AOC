elfs: list[list[int]] = [[]]

with open("./input") as f:
    for line in f:
        if len(line) == 1:
            # This is a break between elves
            elfs.append([])
            continue

        current_elf = elfs[-1]
        current_elf.append(int(line))

# Get highest value
highest = 0

for elf in elfs:
    value = sum(elf)

    if value > highest:
        highest = value

print("highest", highest)
