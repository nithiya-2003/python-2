def vowels(a):
    v="aeiouAEIOU"
    a=list(a)
    i=0
    j=len(a)-1
    while i<j:
        if a[i] not in v:
            i=i+1
        if a[j] not in v:
            j=j-1
        a[i],a[j]=a[j],a[i]
        i=i+1
        j=j-1
    print("".join(a),end="")


a="hello"
vowels(a)
