"""
Cau8: B1908338 - Bui Tran Ngoc Ly
Viết chương trình chuyển số thập phân sang số nhị phân
"""
# Nhập n (n>0)
n = -1
while (n<=0):
    n = int(input("Nhap n>0: "))
# Chuyển từ thập phân sang nhị phân
x = n
ketQua = ""
while(n>0):
    ketQua = str(n%2)+ketQua
    n = n//2
print("Kết quả: ", ketQua)