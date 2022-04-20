"""
Câu 8 : Sử dụng thư viện Numpy và matplotlib, Hãy vẽ đồ thị hàm số y = sin(x) với x chạy từ đoạn
-10 đến 10. (Gợi ý : numpy.linspace() và plt.scatter(), plt.show() )
"""
import numpy as np
import matplotlib.pyplot as plt

#arr = np.linspace(-10, 10, dtype=float)
x = [-7.85,-6.28,-4.71,-3.14, -1.57 ,0, 1.57, 3.14, 4.71, 6.28, 7.85]
y = [-1,-6.28,1,-3.14, -1, 0, 1, 3.14, -1, 4.71, 1]
plt.scatter(x, y)
plt.show()
