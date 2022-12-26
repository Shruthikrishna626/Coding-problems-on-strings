s=input("Enter a string:\n")
k=True
s1=s.split()
l=""
#print(s1)
for ele in s1:
    for j in ele:
        l=l+j
    print(len(l))
    l=""
