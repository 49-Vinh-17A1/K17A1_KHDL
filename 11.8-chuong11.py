list=[]
while True:
    x=int(input("nhập giá trị: "))
    hoi=int(input("tiếp tục nhập giá trị? 1:có, 0:không: "))
    list.append(x)
    if hoi == 0:
        break

def so_may_man(x):
    flag = False
    if x % 7==0:
        flag=True
    return flag

for i in list:
    if so_may_man(i) == True:
        print(1)
        break
else:    
    print("2")
    