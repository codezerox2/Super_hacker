######## Simulate a login system that locks after 3 failed attempts.

password = "super_hacker"
attempts = 3


while attempts >= 1:
    login = input("please inter your password: ")
  
    if login == password:
        print("welcome user")
        break
    else:
         attempts -= 1
         print(f"password wrong {attempts} try lift")
       