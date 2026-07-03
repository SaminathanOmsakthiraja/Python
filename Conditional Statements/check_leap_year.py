year = int(input("Enter the Year : "))
if (year % 4 == 0 or year % 400 == 0):
    print("The Entered year is Leap year")
else:
    print("The Entered year is Not a Leap year")