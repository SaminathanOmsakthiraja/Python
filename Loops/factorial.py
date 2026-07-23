n = int(input("Enter the Number : "))
fact = 1
for i in range(n,0,-1) :
    fact *= i
print("Factorial of ",n," is ",fact)