"""
Cau6: B1908338 - Bui Tran Ngoc Ly
Viết hàm cho người dùng nhập vào 3 tham số a, b, c của phương trình ax2 + bx + c = 0 và
in ra màn hình nghiệm của phương trình đó
"""
import math
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
delta = b*b - 4*a*c
if(a==0) :
	print("Nhap lai (a>0) ")
if (delta<0) :
	print("Phuong trinh vo nghiem")
if(delta==0) :
	x = float(-b/(2*a))
	print("Phuong trinh co nghiem kep la x = ", x)
if(delta>0) :
	x1 = float(-b + math.sqrt(delta)) / (2*a)
	x2 = float(-b - math.sqrt(delta)) / (2*a)
	print("Nghiem 1 phuong trinh x1 = ",x1)
	print("Nghiem 2 phuong trinh x2 = ",x2)
