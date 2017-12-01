_input = ""
with open("01_input.txt", "r") as f:
    _input = f.read()

_sum = 0
sequence = [int(digit) for digit in _input]
for index, digit in enumerate(sequence):
    try:
        next_digit = sequence[index+1]
        # print("{0} {1}".format(digit, next_digit))
    except IndexError:
        next_digit = sequence[0]
    
    if digit == next_digit:
        _sum += digit

print(_sum)