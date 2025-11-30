## Generate a random password of 12 characters.
import string
import random
char = string.printable
passwd = ''.join(random.choice(char) for i in range(12))

print(passwd)