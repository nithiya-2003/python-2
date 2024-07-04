
a="The String is Awesome"
c=print(len(a))
i=0
n=0
while n<=21+1:
    while n<=3:
        for i in a[0:3]:
            i=i.capitalize()
            print(i)
            a+=a
            n=n+1
        break
    

   while n<=10 and n>3:
       
       for i in a[4:10]:
           i=i.lower()
           print(i)
           a+=a
           n=n+1
        break


   while n<=21 and n>10:
       for i in a[10:]:
           i=i.swapcase()
           print(i)
           a+=a
           n=n+1
           break           

    


