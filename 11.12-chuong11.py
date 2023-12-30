print("nhập 4 số nguyên dương đầu tiên: ")
tuple_a=tuple(int(input(f"nhập số nguyên thứ {i+1}: ")) for i in range(4))
print("nhập 4 số nguyên dương tiếp theo")
tuple_b = tuple(int(input(f"nhập số nguyên thứ {i+5}")) for i in range(4))
tuple_c=tuple_a+tuple_b 
tuple_d=tuple(sorted(tuple_c))   
print("tuple_c: ", tuple_c)
print("tuple_d: ", tuple_d)
print("tuple[2]= ",tuple_d[2])
print("3 phần tử cuối cùng của tuple d ",tuple_d[-3:])


