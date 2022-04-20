"""
Cau7: B1908338 - Bui Tran Ngoc Ly
Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không chia hết cho 5, nằm trong
đoạn từ 5000 – 7000
"""
import array as arr 
a = arr.array('i', [])
for i in range(5000,7001) :
	if(i%7==0  and i%5!=0) :
		a.append(i)
print(a)