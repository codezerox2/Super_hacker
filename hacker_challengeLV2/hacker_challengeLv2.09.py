########## 9. Continuously ask for a password until the correct one is entered.
passwd = "password123@"

while True:
    login = input("inter your password: ")
    if passwd == login :
        print("login succss")
        break
    else:
        print("login failed")