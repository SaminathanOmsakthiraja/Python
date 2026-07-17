n = int(input("Enter the Number : "))
rev = 0
while n != 0 :
    rev += int (n % 10)
    rev *= 10
    n //= 10
print("The reversed value is",rev//10)