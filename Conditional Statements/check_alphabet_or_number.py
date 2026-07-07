a = input("Enter the character : ")
print("The character is ",end='')
if a.isalpha():
    print("Alphabet")
elif a.isdigit():
    print("Number")