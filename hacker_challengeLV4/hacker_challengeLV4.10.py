## Extract all vowels from a string

word = 'super_hacker!'
vowels = 'aeiouAEIOU'
count = {}
outvowels = ''
for char in word:
    if char not in count and char in vowels:
        count[char] = 1
    elif char in count and char in vowels:
        count[char] += 1
    else:
        outvowels += char

print(f"word without vowels: {outvowels}, how many vowels in the word: {count}")
