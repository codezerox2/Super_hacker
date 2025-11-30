## Generate random MAC addresses.
import string
import random

char = string.hexdigits
x = []
for macadd in range(6):
    mac = ''.join(random.choice(char) for i in range(2))
    x += f'{mac}:'


print(''.join(x[:-1]))
