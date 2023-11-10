n = int(input("Nhập số n :"))
tong =0
if n<=0:
    print("Mời nhập lại số thực dương")
else:
    for i in range(1,n):
        if n%i==0:
            tong+=i
    if tong ==n:
        print(f" {n} là số hoàn hảo")
    else:
        print(f"{n} không phải số hoàn hảo")     