while True:
    def permute(s):
        
    s=input("enter a character to be processed")
    print("1-length")
    print("2-reverse")
    print("3-1st character")
    print("4-capitalize")
    print("5-print in list")
    print("6-all permutations using recursion")
    print("7-concat 2 strings")
    choice=int(input("enter your choice /n"))
    if(not s):
        print("wrong value entered")
    else:
        if choice>=1 and choice<=7 :
            if choice==1: # to print length
                print(len(s))
            elif choice==2: #to reverse
                s1=""
                for i in range(len(s)):
                    s1=s[i]+s1
                print("your REVERSED STRING IS :  {}".format(s1) )   
            elif choice==3:
                print(s[0])
            elif choice==4:
                print(s.capitalize())
            elif choice==5:
                print(list(s))
            elif choice==6:

                

                    
                
                
            



                    


        

    break