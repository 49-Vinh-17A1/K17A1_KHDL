list=[74,74,72,72,73,69,69,71,76,71]
list_inch=[]
for i in list:
    inch=i*0.0254
    list_inch.append(inch)

print("3 chiều cao đầu tiên: ")
print(list_inch[:3])
print("3 chiều cao cuối cùng: ")
print(list_inch[-3:])
print("chiều cao trung bình là: ",sum(list_inch)/len(list_inch))
print("chiều cao lớn nhất là: ",max(list_inch))
print("chiều cao nhỏ nhất là: ",min(list_inch))
print("list theo thứ tự tăng dần: ",sorted(list_inch))
print("list theo thứ tự giảm dần: ",sorted(list_inch,reverse=True))

