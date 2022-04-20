"""
Câu 4 : Sử dụng thư viện Numpy, Hãy khởi tạo một mảng hai chiều với kích thước 5x5 mà giá trị
các đường viền đều là số 1, giá trị các phần tử còn lại là 0. (Gợi ý : numpy.ones() )
"""
import numpy as np
#khởi tạo mảng 2 chiều kích thước 5x5
arr=np.ones((5,5), dtype=int)
arr[1,1]=0
arr[1,2]=0
arr[1,3]=0
arr[2,1]=0
arr[2,2]=0
arr[2,3]=0
arr[3,1]=0
arr[3,2]=0
arr[3,3]=0
print(arr)