"""
Cau3: B1908338 - Bui Tran Ngoc Ly
Viết chương trình cho phép người dùng nhập vào 2 số a và b. Nếu b = 0 thì yêu cầu người
dùng nhập lại cho đến khi b khác 0. In ra màn hình các kết quả của các phép toán sau : + - * / % **.
"""
import math
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = 0
if b != 0 :
    print(a + b)
    print(a - b)
    print(a * b)
    c = a / b
    print(c)
    c = a % b
    print(c)
    c =a ** b
    print(c)
else :
	print("Nhap lai b di cai thang chet tiec: ")
