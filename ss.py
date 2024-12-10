class Alpha:
    def fun(self):
        print('Alpha class fun()')
        
print(dir(Alpha))




class customer:
     def __init__(self,name,ph,email):
         self.name=name
         self.ph=ph
         self.email=email
class platinium_cust(customer):
     def __init__(self,name,ph,email):
         super().__init__(name,ph,email)
         print("pgm running succesfully")
p=platinium_cust("arjun",33333,"sss")





