meals_1=[]
count=0
while True:
    x=input("nhập tên món ăn thực đơn 1: ")
    meals_1.append(x)
    if count<4:
        count+=1
    else:
        break

meals_2=[]
count_2=0
count=0
while True:
    x=input("nhập tên món ăn thực đơn 2: ")
    meals_2.append(x)
    if count_2<4:
        count_2+=1
    else:
        break

def menu_is_boring(meals):
    for i in range(len(meals)-1):
        if meals[i]==meals[i+1]:
            return False
    return True

print("Thực đơn 1 có nhàm chán không?", menu_is_boring(meals_1))
print("Thực đơn 2 có nhàm chán không?", menu_is_boring(meals_2))