def samp(s):
    pos=""
    l=len(s)
    for i in range(l):
        if s[i].isdigit()==True:
            pos=pos+str(i)
    return pos
s=input("Enter a string")
print(samp(s))