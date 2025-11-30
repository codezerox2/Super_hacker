## Check if a password is strong (≥8 chars, includes number & special character).
import re
password = input("input your pass:")

check = re.findall("[a-z,A-Z,0-9,!,@,#,$,%,^,&,*,(,)}{',\",/]", password)
test = ''.join(check)
lenght = len(test)
if password == test and lenght >= 8:
    print('your pass is strong')

else: 
    print("your pass is weak")