""""
 Cau12: B1908338 - Bui Tran Ngoc Ly
 Viết chương trình tính tổng của các chữ số của một số nguyên n. Nếu n nhỏ hơn 0 thì yêu
cầu người dùng nhập lại. (ví dụ : n = 123 thì tổng là 1 + 2 + 3 = 6)
"""
def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
 
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n , "là", totalDigitsOfNumber(n));