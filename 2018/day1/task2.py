import sys
import itertools

changes = [int(line) for line in sys.stdin]
start = 0
seen = set([0])
for change in itertools.cycle(changes):
    start += change
    # print >> sys.stderr, change, start
    if start in seen:
        print start
        break
    else:
        seen.add(start)
