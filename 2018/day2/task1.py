import sys

total_two = 0
total_three = 0
for line in sys.stdin:
    word = line.strip()
    counts = {}
    for c in word:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    two, three = 0, 0
    for c, cnt in counts.items():
        if cnt == 2:
            two = 1
        elif cnt == 3:
            three = 1
    total_two += two
    total_three += three
print total_two * total_three
