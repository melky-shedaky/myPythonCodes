#Write a program to determine whether a given year is a century leap year.
year=int(input("Enter a year: "))
if year%100==0:
    if year%400==0:
        print(year,"this a century year and leap year")
    else:
        print(year,"this a century year and not a leap year")
else:
    if year % 4 == 0:
        print(year,"this is not a century year but a leap year")
    else:
        print(year,"this is not a century or leap year")
##DRY-RUN :
#2024 is not a century year but a leap year
#2000 is a century leap year
#1900 is a century year but not a leap year
#2023 is not a leap year
