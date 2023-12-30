while True:
 try:
  a=int(input("giá trị cạnh thứ 1:"))
  b=int(input("giá trị cạnh thứ 2:"))
  c=int(input("giá trị cạnh thứ 3:"))
  if a<=0 or b<=0 or c<=0:
     raise TypeError ("nhập giá trị lớn hơn 0!!!")
  if a+b<=c or a+c<=b or b+c<=a:
     raise TypeError ("nhập lại giá trị!!!")        
 except ValueError as f:
    print("nhập giá trị là số nguyên dương!!!")
 except TypeError as q:
     print(q)
 else:
     q=int(a+b+c)/2
     import math
     s=math.sqrt(q*(q-a)*(q-b)*(q-c))
     print("diện tích tam giác:",s)
     break