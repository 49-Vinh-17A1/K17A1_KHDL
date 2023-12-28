def so_hoan_hao(x):
    flag=False
    s=0
    for i in range(1,x):
        if x % i ==0:
            s=s+i
            print(s)
    if s== x:
       flag=True
       return flag
    
x=int(input("nhập số nguyên dương x: "))
if x<0:
    print("đây không là số nguyên dương")
else:
    if so_hoan_hao(x) == True:
        print(x,"là số hoàn hảo")
    else:
        print(x,"không là số hoàn hảo")
