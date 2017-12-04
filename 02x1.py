_input = ""
with open("02_input.txt", "r") as f:
    _input = f.read()

lines = _input.split("\n")
lines = lines[:len(lines)-1]
spreadsheet = [[int(s) for s in l.split("\t")] for l in lines]

result = sum([max(s)-min(s) for s in spreadsheet])
print(result)