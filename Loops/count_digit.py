n = input("Enter the Number : ")
count = 0
for i in n:
    if i.isdigit():
        count += 1
    else :
        print("'",i,"'"," is Invalid input",sep='')
print("The count of the Digit in the input is", count)