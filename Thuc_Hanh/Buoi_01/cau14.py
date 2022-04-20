""""
 Cau14: B1908338 - Bui Tran Ngoc Ly
 Viết chương trình tính 1/2 + 2/3 + 3/4 + 4/5 + … + n/(n+1) với số n được nhập từ bàn
phím. Nếu n < 0 thì yêu cầu người dùng nhập lại.
"""
n = int(input())

s = 0

for i in range(0, n):

   s += i/(i + 1)
print(s)