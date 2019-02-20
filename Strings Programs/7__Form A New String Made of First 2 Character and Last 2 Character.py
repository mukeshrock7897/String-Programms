string=input("Enter The String::")
count=0
for i in string:
    count=count+1
new=string[0:2]+string[count-2:count]
print("Newly Formated String::")
print(new)
