"""
Câu 2 : Sử dụng thư viện Numpy, Hãy khởi tạo một mảng hai chiều gồm các giá trị của dòng thứ
nhất: 1, 3, 5, 7, 9 và dòng thứ hai : 2, 4, 6, 8 ,10 sau đó in mảng đó ra màn hình ( Gợi ý : numpy.array()
)
"""
import numpy as np
arr = np.array(([(1,3,5,7,9)], [(2,4,6,8,10)]), dtype=int)
print(arr)