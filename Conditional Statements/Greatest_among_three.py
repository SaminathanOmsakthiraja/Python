a = int(input("Enter the A number : "))
b = int(input("Enter the B number : "))
c = int(input("Enter the C number : "))
if (a > b and a > c):
    print("The A is Greater than B and C")
elif b > c:
    print("The B is Greater than A and C")
else:
    print("The C is Greater than A and B")