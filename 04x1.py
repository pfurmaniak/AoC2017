_input = ""
with open("04_input.txt", "r") as f:
    _input = f.read().split("\n")

passphrases = [[p for p in i.split(" ")] for i in _input]
valid_count = 0
for p in passphrases:
    if len(p) == len(set(p)):
        valid_count += 1

print(valid_count)