f=open("nithiya...txt","r")
f2=open("meena...txt","w")
for lines in f:
    
    f2.write(lines)
    print(lines)
    

f.close()
f2.close()

