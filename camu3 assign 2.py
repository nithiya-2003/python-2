def subsequence(a,b):
    j=0
    i=0
    while i<len(a) and j<len(b):
        if a[i]==b[j]:
            i=i+1
        j=j+1
    if i==len(a):
        print("true")
    else:
        print("no")


a="abs"
b="pabs"
subsequence(a,b)
