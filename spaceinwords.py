s=input("Enter a string")
print(s.isalpha())
words=s.split()
res=""
al=[]
sum1=0
print(words)
for ele in words:
    if ele.isalpha():
        res=res+ele
    else:
        al.append(ele)
for i in al:
    sum1=sum1+int(i)
            
print(res)
print(sum1)
