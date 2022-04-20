"""
Cau10: B1908338 - Bui Tran Ngoc Ly
Viết chương trình liệt kê tất cả các số nguyên tố nhỏ hơn n, với n được nhập vào từ bàn
phím
"""
import math
#ham kiem tra so nguyen to
def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;
 
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False;
    return True;
 
n = int(input("Nhập số nguyên dương n = "));
print ("Tất cả số nguyên tố nhỏ hơn", n, "là:");
ngTo = "";
if (n >= 2):
    ngTo = ngTo + "2" + " ";
for i in range (3, n+1):
    if (isPrimeNumber(i)):
        ngTo = ngTo + str(i) + " ";
    i = i + 2;
print(ngTo);