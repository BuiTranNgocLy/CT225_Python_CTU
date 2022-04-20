"""
Cau2: B1908338 - Bui Tran Ngoc Ly
Viết chương trình cho người dùng nhập vào số 0 <n < 10. Nếu n nằm ngoài khoản quy định
thì yêu cầu người dùng nhập lại. Sau đó in ra màn hình kết quả của n + nn + nnn + nnnn (ví dụ : n
= 2 thì in ra màn hình : 2 + 22 + 222 + 2222 = 2468)
"""
n = int(input())
if n>0 or n<10 :
	print(n + n)
else :
	print("Nhap lai n")