string=input("Enter The String::")
char=0
word=1
for i in string:
    char=char+1
    if(i==" "):
        word=word+1

print("Number of Words",word)
print("Number of Charcter",char)
