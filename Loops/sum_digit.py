n = input("Enter the Number : ")
s = 0
for i in n:
    if i.isdigit():
        s += int (i)
    else :
        print("'",i,"'"," is Invalid input",sep='')
print("The sum of the Digit in the input is", s)