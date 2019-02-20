string=input("Enter The String::")
count1=0
count2=0
for i in string:
    if(i.islower()):
        count1=count1+1
    elif(i.isupper()):
        count2=count2+1

print("Number of Lower Letters::",count1)
print("Number of Upper Letters::",count2)
