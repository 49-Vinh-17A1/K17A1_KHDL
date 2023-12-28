def kiem_tra_so_nguyen_to(x):
    flag=False
    for i in range(2,x):
        if x % i ==0:
            return flag
        flag = True
        return flag
    
x=int(input("nhập số nguyên dương: "))
if x<=0:
    print("đây không là số nguyên dương")
else:
    if kiem_tra_so_nguyen_to(x) == True:
        print(x,"là số nguyên tố")
    else:
        print(x,"không là số nguyên tố")