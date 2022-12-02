import sys

numbers: list[int] = []
larger_than_previous = 0

for line in sys.stdin:
    numbers.append(int(line))

for i in range(len(numbers)):
    previous = numbers[i - 1 : i + 2]
    current = numbers[i : i + 3]

    if not (len(previous) == 3 and len(current) == 3):
        continue

    # print(f"Current: {current}. Previous: {previous}")
    if sum(current) > sum(previous):
        larger_than_previous += 1

print(f"\n================================")
print(f"Large than previous: {larger_than_previous}")
print(f"\n================================")
