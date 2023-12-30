arrivals=[]
count=0
while True:
    x=input("nhập tên khách mời: ")
    arrivals.append(x)
    if count<6:
        count+=1
    else:
        break

def party_late(arrivals,name):
    flag = True
    for name_to_check in arrivals[4:6]:
        if name == name_to_check:
            flag = False
    return flag
x=input("nhập tên cần kiểm tra: ")    
print(party_late(arrivals,name = x))
