n = int(input('Enter the number : '))
if n % 7 == 0 and n % 5 ==0 :
    print("Divisible by 5 and 7")
elif n % 5 :
    print("Divisible by 5")
elif n % 7 :
    print("Divisible by 7")
else :
    print("Not Divisible by 5 and 7")