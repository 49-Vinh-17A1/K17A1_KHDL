def phan_nguyen_cua_phep_chia(a,b):
    if a>b:
        s=a//b
    else:
        s=b//a
    return s

a=int(input("nhập số nguyên a: "))
b=int(input("nhâp số nguyên b: "))
print("phần nguyên của phép chia hai số là",phan_nguyen_cua_phep_chia(a,b))
