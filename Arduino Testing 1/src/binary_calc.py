

def findValue(left_bit, right_bit, middle_bit):
    value = left_bit*(2**2) + middle_bit*(2**1) + right_bit*(2**0)
    return value

# void loop
left = 1
right = 1
middle = 1

findValue(left, right, middle)
