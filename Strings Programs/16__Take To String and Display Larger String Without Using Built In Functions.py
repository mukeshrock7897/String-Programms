string1=input("Enter the 1st String::")
string2=input("Enter The 2nd String::")
count1=0
count2=0
for i in string1:
    count1=count1+1
for j in string2:
    count2=count2+1
if(count1>count2):
    print(string1,"1st is Larger String")
elif(count1==count2):
    print("Both String is Equal")
else:
    print(string2,"2nd is Larger String")
