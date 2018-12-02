import sys

start = 0
for line in sys.stdin:
    change = int(line)
    start += change
print start
