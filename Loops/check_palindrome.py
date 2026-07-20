num = int(input("Enter the Number : "))
n = num
rev = 0
while n != 0 :
    rev += int (n % 10)
    rev *= 10
    n //= 10
rev //= 10
if num == rev :
    print("Valid Palindrome")
else :
    print(n)
    print("Invalid Palindrome")