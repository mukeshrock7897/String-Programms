string=input("Enter The String::")
vowels=0
for i in string:
    if not (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowels=vowels+1
print("Number of Vowels::",vowels)
