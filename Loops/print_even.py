n = int(input("Enter the Nth number : "))
print("The Even numbers in the range are : ")
for i in range(n) :
    if i % 2 == 0 :
        print(i,end = ' ')