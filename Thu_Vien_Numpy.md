- Là thư viện toán học -> làm việc với ma trận và mảng lớn
# 1. Cài đạt thư viện
- Mở cmd -> gõ lệnh `pip install numpy`
# 2. Thao tác
## a. Khai báo thư viện
- `import numpy as np`
## b. Khỏi tạo mảng 
### Mảng 1 chiều
- Khởi tạo
  - Mảng 1 chiều với kiểu dữ liệu là Integer
    - `arr = np.array([1,2,3,4], dtype = int )`
  - Mảng 1 chiều với kiểu dữ liệu mặc định
    - `arr = np.array([1,2,3,4])` 
    - `print(arr)`
    - => Output [1,2,3,4]
### Mảng 2 chiều
- `arr = np.array([(1,2,3), (4,5,6)], dtype = int )`
- `Output`
![image](https://user-images.githubusercontent.com/88178841/162193545-86fe92f3-25bc-4c19-8dd3-6c9ae0a6d9d0.png)

### Khởi tạo với các hàm có sẵn
- `np.zeros((3,4), dtype = int)`: tạo mảng `2 chiều` các phần tử 0 với kích thước 3x4
- `np.ones((2,3,4), dtype = int)`: tạo mảng `3 chiều` các phần tử 1 với kích thước 2x3x4
- `np.arange(1,7,2)`: Tạo mảng với các phần tử từ 1 - 6 với bước nhảy là 2.
- `np.full((2,3),5)`: Tạo mảng 2 chiều các phần tử 5 với kích thước 2x3
- `np.eye(4, dtype=int)`: Tạo ma trận đơn vị với kích thước là 4x4
- `np.random.random((2,3))`: Tạo ma trận các phần tử ngẫu nhiên với kích thước 2x3
## c. Thao tác với mảng
- `dtype`: Kiểu dữ liệu của phần tử trong mảng.
- `shape`: Kích thước của mảng.
- `size`: Số phần tử trong mảng.
- `ndim`: Số chiều của mảng.
### Truy cập phần tử trong 
