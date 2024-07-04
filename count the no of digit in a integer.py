a=int(input())
count=0
temp=a
while(temp!=0):
    c=temp%10
    count+=1
    temp=temp//10

print("no of digit is:",count)
