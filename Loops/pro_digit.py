n = input("Enter the Number : ")
pro = 1
for i in n:
    if i.isdigit():
        pro *= int (i)
    else :
        print("'",i,"'"," is Invalid input",sep='')
print("The Product of the Digit in the input is", pro)