list=[]
while True:
    x=int(input("nhập giá trị: "))
    hoi=int(input("tiếp tục nhập giá trị? 1:có, 0:không: "))
    list.append(x)
    if hoi == 0:
        break
a=int(input("nhập giá trị càn tìm x: "))
print("list = ",list)
b=list.count(a)
print("{} xuất hiện {} lần trong list".format(a,b))