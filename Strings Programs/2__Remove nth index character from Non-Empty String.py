def remove(string,n):
    first=string[:n]
    last=string[n+1:]
    return first+last
string=input("Enter the String::")
n=int(input("Enter The Index Whom You Want to Remove::"))
print("The Modified String ::")
print(remove(string,n))
