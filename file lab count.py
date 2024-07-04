F=open("nithiya...txt","r")
count=0
for line in F:
    words=line.split(" ")
    count=count+len(words)
F.close()
print("the no of words in a file is:",count)





