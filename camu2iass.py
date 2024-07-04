def camu_2i(a):
    for i in range(0,len(a)):
        if i=="e":
            a=a.replace("e","o",1)
            print(a)
            i=i+1
        else:   
            if i=="o":
                a=a.replace("o","e",1)
                print(a)
                i=i+1        
            

           
                
a="hello"
a=a.split()

camu_2i(a)

print(a)
