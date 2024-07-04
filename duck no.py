n=int(input ("num"))
c=0
while(n>0):
    a=n%10
    if(a==0):
        c=c+1
        n=n//10
    else:
        n=n//10


if(c>=1):
    print("given no is duck number")
else:
    print("oops,not a duck bro")
