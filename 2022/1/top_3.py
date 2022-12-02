elfs: list[list[int]] = [[]]

with open("./input") as f:
    for line in f:
        if len(line) == 1:
            # This is a break between elves
            elfs.append([])
            continue

        current_elf = elfs[-1]
        current_elf.append(int(line))

# Sort the array
sorted_elfs = sorted(elfs, key=lambda x: sum(x))

top_3 = sorted_elfs[-3:]
top_3_summed = [sum(elf) for elf in top_3]

print("Top 3 elfs:", top_3_summed, "total:", sum(top_3_summed))
