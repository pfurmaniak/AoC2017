_input = ""
with open("02_input.txt", "r") as f:
    _input = f.read()

lines = _input.split("\n")
lines = lines[:len(lines)-1]
spreadsheet = [[int(s) for s in l.split("\t")] for l in lines]

result = 0
for line in spreadsheet:
    for n in line:
        for m in line:
            if n == m:
                continue
            if n % m == 0:
                result += n/m

print(int(result))