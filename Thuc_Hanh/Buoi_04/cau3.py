"""
Câu 3 : Sử dụng thư viện Numpy, Hãy khởi tạo một mảng gồm 10 giá trị 0 và sau đó cập nhật giá
trị thứ 6 thành số 13. In mảng đó ra màn hình (Gợi ý : numpy.zeros() )
"""
import numpy as np
#khởi tạo mảng gồm 10 giá trị 0
arr=np.zeros((10), dtype=int)
arr[6]=13
print(arr, arr[6])
