"""
Cau11: B1908338 - Bui Tran Ngoc Ly
Viết chương trình liệt kê tất cả các số nguyên tố có 4 chữ số
"""
import math
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
 
print ("Tất cả số nguyên tố có 4 chữ số:");
count = 0;
for i in range(1001, 9999):
    if (isPrimeNumber(i)):
        print(i);
        count = count + 1;
