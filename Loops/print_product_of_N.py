n = int(input("Enter the Nth number : "))
s = 0
for i in range(n+1) :
    s *= i
print("The Product of the 0 to",n,'is',s)