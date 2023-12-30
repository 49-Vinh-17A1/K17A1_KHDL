list=[]
while True:
    x=int(input("nhập giá trị: "))
    hoi=int(input("tiếp tục nhập giá trị? 1:có, 0:không: "))
    list.append(x)
    if hoi == 0:
        break
so_nguyen_to=[]
def ham_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

for x in list:
    if ham_so_nguyen_to(x):
        so_nguyen_to.append(x)

phan_tu_am=[]
for x in list:
    if x < 0:
        phan_tu_am.append(x)
print("Danh sách số:", list)
print("Các số nguyên tố trong danh sách:", so_nguyen_to)
print("phần tử âm là: ",phan_tu_am)
if len(phan_tu_am) > 0:
    TBC_phan_tu_am = sum(phan_tu_am) / len(phan_tu_am)
    print("Trung bình cộng của các phần tử âm:", TBC_phan_tu_am)
print("giá trị max trong list là: ",max(list))
print("giá trị min trong list là: ",min(list))
print("list sắp tăng dần: ",sorted(list))