my_tuple = ('red', 'green', 'yellow', 'blue', 'black', 'white', 'pink', 'orange', 'red', 'blue')
index_duong=int(input("nhập index dương(0<=index<10): "))
index_am=int(input("nhập index am(-9<=index<=-1): "))
find_str=input("nhập chuỗi cần tìm: ")
count=my_tuple.count(find_str)
if index_duong>=0 and index_duong < 10:
    print("tuple[{}] =".format(index_duong), my_tuple[index_duong])
else:
    print("nhập không hợp lệ")

if index_am>=-9 and index_am<=-1:
    print("tuple[{}] =".format(index_am),my_tuple[index_am])

print("{} xuất hiện".format(find_str), "{} lần".format(count))