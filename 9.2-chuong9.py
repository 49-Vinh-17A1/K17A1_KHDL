nam=int(input("nhap nam: "))
#tính can
if nam % 10 == 0:
    a="Canh"
elif nam%10 ==1:
    a="Tân"
elif nam % 10 ==2:
    a="Nhâm"
elif nam % 10 ==3:
    a="Quý"
elif nam % 10 == 4:
    a="Giáp"
elif nam % 10 ==5:
    a="Át"
elif nam % 10 ==6:
    a="Bính"
elif nam % 10 ==7:
    a="Đinh"
elif nam % 10 ==8:
    a="Mậu"
else:
    nam="Kỳ"
#tính chi
if nam%12==0:
    b="Thân"
elif nam % 12 ==1:
    b="Dậu"
elif nam % 12 ==2:
    b="Tuất"
elif nam % 12 ==3:
    b="Dậu"
elif nam % 12 ==4:
    b="Tý"
elif nam % 12 ==5:
    b="Sửu"
elif nam % 12 ==6:
    b="Dần"
elif nam % 12 ==7:
    b="Mão"
elif nam % 12 ==8:
    b="Thìn"
elif nam % 12 ==9:
    b='Tỵ'
elif nam % 12 ==10:
    b="Ngọ"
else:
    b="mùi"

print("năm",nam,"có lịch âm là",a,b)