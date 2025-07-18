###### . Given a dictionary of usernames and passwords, print the password for a given username
login = input("inter your username to get your password:")

database = {
    "ahmed" : "Password",
    "admin": "admin",
    "yahya": "super_hacker123"
}

if login in database:
    print(f"your password is : {database[login]}")
else:
    print("sorry your username didnt found")