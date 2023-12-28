def testdate(ngay,thang,nam):
    if thang == 1 or thang ==3 or thang == 5 or thang ==7 or thang ==8 or thang ==10 or thang ==12:
        max=31
    elif thang == 4 or thang ==6 or thang == 9 or thang ==1:
        max =30
    elif thang ==2:
        if (nam % 4 ==0 and nam %100 !=0) or nam% 400==0:
            max = 29
        else:
            max =28
    if thang <1 or thang >12:
        return False 
    elif ngay<1 or ngay >max:
        return False
    elif nam <1 or nam>10000000:
        return False
    return True


ngay = int(input("nhập ngày: "))
thang = int(input("nhập tháng: "))
nam  = int(input("nhập năm: "))
if testdate(ngay,thang,nam) == False:
    print("ngày không hợp lệ")
else:

    print("ngày thắng năm vừa nhập:",ngay,"-",thang,"-",nam)
    if (nam % 4 ==0 and nam %100 !=0) or nam% 400==0:
        print("năm",nam,"là năm nhuận")
    else:
        print("năm",nam,"không là năm nhuận")
    import calendar
    x=calendar.weekday(nam,thang,ngay)
    if x == 0:
        y= "thứ hai"
    elif x ==1:
        y= "thứ ba"
    elif x ==2:
        y="thứ tư"
    elif x ==3:
        y="thứ năm"
    elif x ==4:
        y="thứ sáu"
    elif x ==5:
        y="thứ 7"
    elif x ==6:
        y = "chủ nhật"
    print(ngay,"-",thang,"-",nam,"là",y)
    if thang in(1,3,5,7,8,10,12):
        print("tháng",thang,"có 31 ngày")
    elif thang in(4,6,9,11):
        print("tháng",thang,"có 30 ngày")
    elif thang ==2:
        if (nam % 4 ==0 and nam %100 !=0) or nam% 400==0:
            print("tháng",thang,"có 29 ngày")
        else:
            print("tháng",thang,"có 28 ngày")    