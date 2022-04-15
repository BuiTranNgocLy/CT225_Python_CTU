'''
Câu 8 : Sử dụng thư viện Numpy và matplotlib, Hãy vẽ đồ thị hàm số y = sin(x) với x chạy từ đoạn
-10 đến 10. (Gợi ý : numpy.linspace() và plt.scatter(), plt.show() )
'''
import numpy as np 
import matplotlib.pyplot as plt  
x = np.linspace(-10, 10)
y = np.sin(x) 
plt.title("sine wave form") 
# Plot the points using matplotlib 
plt.plot(x, y) 
plt.show()
