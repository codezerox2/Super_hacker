########## Replace all vowels in "P@ssw0rd" with "*"

word = input("input your word: ")
resulte = ""
for i in word:
    if i in "aeiouAEIOU":
        resulte = resulte + "*"
    else:
        resulte = resulte + i

print(resulte)