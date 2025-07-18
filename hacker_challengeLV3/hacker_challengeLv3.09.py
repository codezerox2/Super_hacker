####### Find the longest word in a list
words = ['hi', 'super_hacker','hello', 'nmap', 'metasploit', 'kali linux']
wordic = {}

for i in words:
    wordic[i] = len(i)
    word_sort = dict(sorted(wordic.items(), key=lambda sorts: sorts[1]))

print(list(word_sort)[-1])