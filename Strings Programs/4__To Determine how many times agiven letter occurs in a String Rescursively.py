def check(string,ch):
    if not string:
        return 0
    elif string[0]==ch:
        return 1+check(string[1:],ch)
    else:
        return check(string[1:],ch)
string=input("Enter the String::")
ch=input("Enter The Character::")
print("Count Is::",check(string,ch))

