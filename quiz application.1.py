c_ans=0
w_ans=0
print("what is the capital india?")
user=input("enter answer:").lower()
if user=="delhi":
    print("correct answer")
    c_ans+=1
else:
        print("wrong ans")
        w_ans+=1
print("what is the capital kar?")
user=input("enter answer:").lower()
if user=="bengalure":
    print("correct answer")
    c_ans+=1
else:
     print("wrong ans")
     w_ans+=1
     print("total correct ans",c_ans)
     print("total wrong correct ans",w_ans)
