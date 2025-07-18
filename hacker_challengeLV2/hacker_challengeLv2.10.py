######## Check if a string is a palindrome.

word = input("inter your word: ")

palindrome = word[:: -1]

if word == palindrome:
    print("palindrome")
else:
    print("not palindrome")