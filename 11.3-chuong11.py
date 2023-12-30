a=[]
while True:
    x=input("nhập vào các con thú: ")
    if x =='*':
        break
    a.append(x)

print("list of animal: ",a)
print("number of animal: ",len(a))
find_animals=input("i want to find: ")
find = find_animals in a
if find == True:
    print("there is {} in animals".format(find_animals))
else:
    print("there is not {} in animals".format(find_animals))
