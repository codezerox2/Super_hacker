########### . Check if a given year is a leap year

year = int(input("input your year: "))

if year % 4 == 0 :
    print("this leap year")
else:
    print("this not leap year")