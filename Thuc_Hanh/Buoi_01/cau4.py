"""
Cau4: B1908338 - Bui Tran Ngoc Ly
Viết chương trình cho phép người dùng nhập vào bán kính hình tròn. In ra màn hình chu vi
và diện tích tương ứng
"""
r = int(input("Nhap vao ban kinh R = "))
s = float(r*r*3.14)
cv = float(r*2*3.14)
print("Chu vi hinh tron la: ", cv)
print("Dien tich hinh tron la: ", s)
