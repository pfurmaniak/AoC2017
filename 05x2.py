_input = ""
with open("05_input.txt", "r") as f:
    _input = f.read().split("\n")

_list = [int(n) for n in _input]

index = 0
counter = 0
while True:
    try:
        offset = _list[index]
        _list[index] += (-1 if offset >= 3 else 1)
        index += offset
        counter += 1
    except IndexError as ex:
        break

print(counter)