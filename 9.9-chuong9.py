S_hinh_tron=lambda r: 3.14*r*r
P_hinh_tron=lambda r: 2*3.14*r
S_hinh_chu_nhat=lambda a,b: a*b 
P_hinh_chu_nhat=lambda a,b: (a+b)/2
r=int(input("nhập bán kính: "))
a=int(input("nhập chiều dài: "))
b=int(input("nhập chiều rộng: "))

print("S P hình tròn là",S_hinh_tron(r),P_hinh_tron(r))
print("S P hình chữ nhật là",S_hinh_chu_nhat(a,b),P_hinh_chu_nhat(a,b))