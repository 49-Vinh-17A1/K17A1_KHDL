x = int(input("Nhập số tiền muốn đổi:"))
so_to_500k=x//500000
tien_con_lai=x%500000
so_to_200k=tien_con_lai//200000
tien_con_lai=tien_con_lai%200000  
so_to_100k=tien_con_lai//100000
tien_con_lai=tien_con_lai%100000
so_to_50k=tien_con_lai//50000
tien_con_lai=tien_con_lai%50000
print('số tờ 500k =', so_to_500k)
print('số tờ 200k =', so_to_200k)
print('số tờ 100k =', so_to_100k)
print('soó tờ 50k =', so_to_50k)
print('số tiền còn lại', tien_con_lai)
