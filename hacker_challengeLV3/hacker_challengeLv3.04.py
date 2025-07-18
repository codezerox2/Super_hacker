##### Count how many times each letter appears in a string

word = input("inter your word:").replace(' ', '')
char = {}
for i in word:
        if i not in char:
             char[i] = 1
        else:
             char[i] += 1

print(char)