alphabet=0
numeric=0
spl=0
password=input("enter the password")
if len(password)>=9 and len(password)<=13:
   for x in password:
       if x .isalpha():
          alphabet+=1
       elif x.isnameric():
           numeric+=1
       else:
            spl+=1
       if alphabet>=4 and numeric>=4 and spl>=1:
           print ("valid password",password)
       else:
           print("invalid password")
            
