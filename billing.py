itema = input("item1 name")
itemb = input("item2 name")
itemc = input("item3 name")
itemd = input("item4 name")
costa = int(input("cost of item 1"))
costb = int(input("cost of item 2"))
costc = int(input("cost of item 3"))
costd = int(input("cost of item 4"))
qa = int(input(" enter the quantity"))
qb = int(input(" enter the quantity"))
qc = int(input(" enter the quantity"))
qd = int(input(" enter the quantity"))
totalc1 =costa*qa
totalc2 =costb*qb
totalc3 =costc*qc
totalc4 =costd*qd
totalprice=totalc1 +totalc2 +totalc3 +totalc4
print("s.no" , "  item name    "  , "  cost of the item  "     ,"     quantity   "   ,  "   total cost of the item")
print( "1"   ,itema               ," :", "   ",       costa      , " : "  ,"   ",        qa     , " :",  totalc1)
print( "2"   ,itemb               ," :", "   ",       costb      , " : "  ,"   ",        qb     , " :",   totalc2)
print( "3"   ,itemc               ," :", "   ",       costc      , " : "  ,"   ",         qc    , " :",  totalc3)
print( "4"   ,itemd               ," :", "   ",       costd      , " : "  ,"   ",         qd    , " :",   totalc4)

print("          total price            ", totalprice)
