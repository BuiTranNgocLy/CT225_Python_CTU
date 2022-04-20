
"""
Cau5: B1908338 - Bui Tran Ngoc Ly
Viết chương trình tính giai thừa của số nguyên n được người dùng nhập vào từ bàn phím.
Kiểm tra nếu n <0 thì yêu cầu người dùng nhập lại,
"""
n = int(input("Nhap so can tinh giai thua: "))
def giaiThua(n):
	if n == 0:
		return 1
	return n*giaiThua(n-1)
print(giaiThua(n))