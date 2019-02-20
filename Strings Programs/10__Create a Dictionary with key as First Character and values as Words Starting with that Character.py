string=input("Enter The String:::")
a=string.split()
d={}
for word in a:
    if(word[0] not in d.keys()):
        d[word[0]]=[]
        d[word[0]].append(word)
    else:
        if(word not in d[word[0]]):
            d[word[0]].append(word)
for k,v in d.items():
    print(k,":",v)
