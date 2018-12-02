import sys

words = set()
for line in sys.stdin:
    word = line.strip()
    seen = set()
    for i in range(len(word)):
        prefix = word[:i]
        suffix = word[i+1:]
        w = prefix + suffix
        print >> sys.stderr, w
        if w in words:
            print w
            break
        seen.add(w)
    words.update(seen)
