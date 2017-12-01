_input = ""
with open("01_input.txt", "r") as f:
    _input = f.read()

_sum = 0
sequence = [int(digit) for digit in _input]
length = len(sequence)
for index, digit in enumerate(sequence):
    next_digit = sequence[(index+int(length/2))%length]
    
    if digit == next_digit:
        _sum += digit

print(_sum)