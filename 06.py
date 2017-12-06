import operator

_input = ""
with open("06_input.txt", "r") as f:
    _input = f.read().split("\t")

blocks = [int(i) for i in _input]
history = [blocks]
counter = 0

while True:
    blocks = blocks[:]

    index, value = max(enumerate(blocks), key=operator.itemgetter(1))
    blocks[index] = 0
    for n in range(value, 0, -1):
        index = index + 1 if index < len(blocks) - 1 else 0
        blocks[index] += 1
    
    counter += 1
    if blocks in history:
        break
    history.append(blocks)

print("Part 1: {0}".format(counter))
print("Part 2: {0}".format(len(history)-history.index(blocks)))