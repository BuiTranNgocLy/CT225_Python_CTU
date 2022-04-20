"""
Cau9: B1908338 - Bui Tran Ngoc Ly
Viết chương trình tìm ước chung lớn nhất và bội chung nhỏ nhất của 2 số nguyên dương a
và b được nhập vào từ bàn phím
"""
#Tìm ước số chung lớn nhất (USCLN)
def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);
#Tìm bội số chung nhỏ nhất (BSCNN)
def bscnn(a, b):
    return int((a * b) / uscln(a, b));
 
a = int(input("Nhập số nguyên dương a = "));
b = int(input("Nhập số nguyên dương b = "));
#tính USCLN của a và b
print("USCLN của", a, "và", b, "là:", uscln(a, b));
#tính BSCNN của a và b
print("BSCNN của", a, "và", b, "là:", bscnn(a, b));
