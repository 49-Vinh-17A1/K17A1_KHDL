def tinh_BMI(chieu_cao,can_nang):
    bmi=can_nang/(chieu_cao*chieu_cao)
    return bmi

chieu_cao=float(input("Nhập chiều cao(kg): "))
can_nang=float(input("nhập cân nặng(m): "))
BMI=tinh_BMI(chieu_cao,can_nang)
print("Số BMI là: ",BMI)
if BMI < 18.5:
    print("gấy")
elif BMI>= 18.5 and BMI<=24.99:
    print("Bình Thường")
else:
    print("Thừa Cân")