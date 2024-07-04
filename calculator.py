def calculator():
    print("================================================================================================================")
    print("+-*/%**+-*/%**+-*/%**+-*/%**+-*/%**+-*/%**welcome to calculator+-*/%**+-*/%**+-*/%**+-*/%**+-*/%**+-*/%**+-*/%**")
    while True:
        print("==================================================================================================================")
        print("here your choices:")
        print("1=addition(+)")
        print("2=subraction(-)")
        print("3=multiplication(*)")
        print("4=division(/)")
        print("5=modulo(%)")
        print("6=power(**)")
        print("7=square root(**0.5)")
        print("8=no to percentage((a/b)*100)here,b is total")
        print("9=percentage to num((a/100)*b here ,b is total")
        print("exit  for ending the calculator")

        ch=input("enter your choice")
        if ch=="1":
            a=float(input("enter a num1"))
            b=float(input("enter a num2"))
            c=a+b
            print("==================================================================================================================")
            print("the answer is:",c)

        elif ch=="2":
            a=float(input("enter a num1"))
            b=float(input("enter a num2"))
            c=a-b
            print("==================================================================================================================")
            print("the answer is:",c)
        elif ch=="3":
            a=float(input("enter a num1"))
            b=float(input("enter a num2"))
            c=a*b
            print("==================================================================================================================")
            print("the answer is:",c)
        elif ch=="4":
            a=float(input("enter a num1"))
            b=float(input("enter a num2"))
            c=a/b
            print("==================================================================================================================")
            print("the answer is:",c)
        elif ch=="5":
            a=float(input("enter a num1"))
            b=float(input("enter a num2"))
            c=a%b
            print("==================================================================================================================")
            print("the answer is:",c)
        elif ch=="6":
            a=float(input("enter a num1"))
            b=float(input("enter a num2"))
            c=a**b
            print("==================================================================================================================")
            print("the answer is :",c)
        elif ch=="7":
            a=float(input("enter a num1"))
            c=a**0.5
            print("==================================================================================================================")
            print("the answer is:",c)
        elif ch=="8":
            a=float(input("enter a num1"))
            b=float(input("enter a num2"))
            c=(a/b)*100
            print("==================================================================================================================")
            print("the answer is:",c)
        elif ch=="9":
            a=float(input("enter a num1"))
            b=float(input("enter a num2"))
            c=(a/100)*b
            print("==================================================================================================================")
            print("the answer is:",c)

            
        elif ch=="exit" or ch=="EXIT":
            print("******************************************************************************************************************")
            print("you are existing the calculator ....thank you...")
            break
        else:
            print("##################################################################################################################")
            print("print  any other choices")


print(calculator())            
            
            
            
            
            
            
            
            
