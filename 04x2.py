import itertools


def checkpass(password):
    for a, b in itertools.combinations(password, 2):
        if sorted(list(a)) == sorted(list(b)):
            return False
    return True


_input = ""
with open("04_input.txt", "r") as f:
    _input = f.read().split("\n")

passphrases = [[p for p in i.split(" ")] for i in _input]
valid_count = 0
for p in passphrases:
    if checkpass(p):
        valid_count += 1

print(valid_count)
