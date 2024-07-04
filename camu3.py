s="abc"
t="ahbgdc"
a=0
for j in range(0,len(t)):
    for i in range(0,len(s)):
        if t[j]==s[i]:
            j=j+1
            a=a+1
            print("yes",i ,"in t")
        else:
            print("no")
            break
if a==len(s)-1:
    print("true")
