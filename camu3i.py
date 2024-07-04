def func_3cam(a,b):
    c=0
    i=0
    for j in range(len(b)):
            if a[i]==b[j] :
                j=j+1
                i=i+1
            else:
                
                i=i+0
            
    if i==len(a):
        print("c")
                

a="ahs"
b="aphjsk"
func_3cam(a,b)
