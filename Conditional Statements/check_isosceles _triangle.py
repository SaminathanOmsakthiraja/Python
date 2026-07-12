a1 = int(input('Enter the angle 1 : '))
a2 = int(input('Enter the angle 2 : '))
a3 = int(input('Enter the angle 3 : '))
if (a1 == a2 or a2 == a3 or a3 == a1) and a1 + a2 + a3 == 180:
    print("This is the isosceles Triangle")
else:
    print("This is not the isosceles Triangle")