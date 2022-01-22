x=2
n=0
y=int(input("enter number"))
while x>1:
    count=0
    i=1
    while i<=x:
        if x%i==0:
            count=count+1
        i=i+1
    if count==2:
        n+=1
        print(x,n)
    x=x+1