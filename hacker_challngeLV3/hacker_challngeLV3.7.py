######### Function to remove duplicates from a list
lists = ["python", "python", "hacker", "super", 1, 43, 43 , "ssh"]
check = {}

for i in lists:
    if i not in check:
        check[i] = 1
    else:
        lists.remove(i)

print(lists)
print(check)