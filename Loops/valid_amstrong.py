num = input("Enter the Number : ")
count = len(num)
num = int (num)
s = 0
n = int (num)
while (n != 0) :
        s += pow(n%10,count)
        n = n//10
if (s == num) : 
      print("Amstrong")
else :
      print("Not Amstrong")