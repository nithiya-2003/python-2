def fun_merge2(a,b):
    i=0
    j=0
    for i in range(0,len(a)):
        if a[i] in a:
            print(a[i])
            if b[j] in b:
                print(b[j])
                i=i+1
                j=j+1
            
    for j in range (j,len(b)):
        if b[j] in b:
            print(b[j])
            
        
     


a="abc"
b="pqrst"
fun_merge2(a,b)
