sales=[11,33,22,33,44,55,11]
op=[]
for x in sales:
    if x in op:
        pass
    else:
        op.append(x)
        print(op)



op=[]
[op.append(x) for x in sales if x not in op]
print(op)



sales=[11,33,22,33,44,55,11]
op=[]
k=[]
for x in sales:
    if x in op:
        k.append(x)
    else:
         op.append(x)
print(k)



op=[]
[op.append(k) for x in sales if x not in op]
print(k)


print(list(set(sales)))
    
