def bubble_sort(a):
    
    n=len(a)
    for i in range(0,n):
        c=0
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                c=1
            
        if c!=1:
            break
        
    
        
    return a    

a=[]
n=int(input("enter the no of values"))
for i in range (1,n+1) :
    a.append((int(input("enter the value"))))
    
print("the sorted a is:",bubble_sort(a))
