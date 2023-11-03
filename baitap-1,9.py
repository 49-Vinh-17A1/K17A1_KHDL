lai_suat_nam=float(input("nhập lãi suất: "))
so_tien_gui=float(input("nhập số tiền gửi: "))
so_thang_gui=int(input("nhập số tháng gửi: "))
tien_lai=(so_tien_gui*so_thang_gui)*(lai_suat_nam/100/12)
tong_so_tien=so_tien_gui+tien_lai
print("tiền lãi =",tien_lai)
print("tiền vỗn +lãi =", tong_so_tien)
