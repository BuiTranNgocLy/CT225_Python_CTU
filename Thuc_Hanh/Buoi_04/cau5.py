"""
Câu 5 : Sử dụng thư viện Numpy, Hãy khởi tạo một mảng hai chiều với kích thước 3x3
mà giá trị các phần tử đều là 1. Sau đó thêm 1 đường viền bao bên ngoài theo cả 2 chiều
với toàn giá trị 0 vào mảng vừa rồi. In mảng kết quả ra màn hình
(Gợi ý : numpy.ones() và numpy.pad())
"""
import numpy as np
arr=np.ones((3,3), dtype=int)
arr = np.pad(arr, (1, 1), 'constant', 
                 constant_values=(0, 0))
print(arr)