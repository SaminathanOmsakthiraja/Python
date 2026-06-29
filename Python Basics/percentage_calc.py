n = int(input("Enter the number of subjects : "))
lst = []
for i in range(n):
    lst.append(int(input()))
value = sum(lst)
total = n * 100;
print('The percentage of the marks is ', (value / total) * 100,' % ')