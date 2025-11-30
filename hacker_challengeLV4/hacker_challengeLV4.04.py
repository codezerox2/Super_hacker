## Create an MD5 hash of a user-entered string using hashlib.
import hashlib

username = input("inter your username:")
hash = hashlib.md5(username.encode('utf-8')).hexdigest()

print(hash)