string=input("Enter The String::")
line=0
with open(string,'r') as f:
    for i in f:
        line=line+1
    print(line)
