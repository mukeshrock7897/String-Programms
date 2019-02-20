a=[]
n=int(input("Enter The Number of Elements in List::"))
for x in range(n):
    element=input("Enter Element"+str(x+1)+":")
    a.append(element)
max=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max):
        max=len(i)
        temp=i
print("The Longest Word Length is::",temp)
