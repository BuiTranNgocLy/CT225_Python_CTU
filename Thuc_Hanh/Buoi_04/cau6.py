"""
Câu 6 : Sử dụng thư viện Numpy, Hãy khởi tạo mảng thứ nhất gồm các phần tử : [10, 20, 40, 60,
70] và màng thứ 2 gồm các phần tử : [10, 30, 50, 60]. Hãy tìm các phần tử chung của 2 mảng và in
kết quả ra màn hình (Gợi ý : numpy.intersect1d() )
"""
import numpy as np
arr1=np.array([10, 20, 40, 60,70], dtype=int)
arr2=np.array([10, 30, 50, 60], dtype=int)
arr = np.intersect1d(arr1,arr2)
print(arr)