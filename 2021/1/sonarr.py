import sys

previous: int | None = None
larger_than_previous = 0

for line in sys.stdin:
    current = int(line)

    if not (previous is None):
        if current > previous:
            larger_than_previous += 1

    previous = current

print(larger_than_previous)
