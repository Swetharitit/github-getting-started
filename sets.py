d=[10,20,4,3,5]
v=[x for x in d if x%2==1]
print(v)


c="ravi is my friend"
d=c.split()
print(d)
f=[]
for x in d:
 f.append(len(x))
print(f)



c="ravi is my friend"
d=(len(x)for x in c)
print(d)



a=[7,4,9,66,74]
r=[x for x in a if x%2==1]
print(sum(r))
print(r)



a=[1,334,44,55,77,[4,7,8,0,7,7,[44,4,5,6]]]
a[5][6].sort()
print(a)









class demo:
    def receive(self,a,b):
        c=a+b
        print(c)
s=demo()
s.receive(100,20)            
             



