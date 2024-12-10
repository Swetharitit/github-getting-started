b="rama is going to school 123hg646488  77@"
s=" "
n=" "
spec=" "
for i in b:
    if i.isalpha():
        s+=i
    elif i.isnumeric():
            n+=i
    else:
        spec+=i
print("alphabets",s)
print("numbers",n)
print("special",spec)


a=[1,334,4,55,77,[4,7,8,0,7,7,[44,4,5,6]]]
a[5][6].sort()
print(a)

a=[7,4,9,66,74]
r=[x for x in a if x%2==1]
print(sum(r))
print(r)


c="ravi is my friend"
d=c.split()
print(d)
f=[]
for x in d:
    f.append(len(x))
    print(f)


    
d=[10,20,4,3,5]
v=[x for x in d if x%2==1]
print(v)

        
