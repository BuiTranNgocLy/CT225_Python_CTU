- Là thư viện toán học -> làm việc với ma trận và mảng lớn
# 1. Cài đăt thư viện
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
### Truy cập phần tử trong mảng
- `arr[i]`: truy cập phần tử thứ i của mảng 1 chiều
- `arr1[i,j]`: Truy cập phần tử hàng i, cột j của mảng 2 chiều.
- `arr2[n,i,j]`: Truy cập phần tử chiều n, hàng i, cột j của mảng 3 chiều.
- `arr[a:b]`: Truy cập các phần tử từ a đến b-1 trong mảng 1 chiều.
- `arr1[:,:i]`: Truy cập phần tử từ cột 0 đến cột i-1, của tất cả các hàng trong mảng 2 chiều.
### Đọc mảng từ file
- Giả sử có file như hình:

![image](https://user-images.githubusercontent.com/88178841/162199612-17e7bbfe-8faa-4285-aa9a-299a3c474242.png)
- `diem_2a = np.loadtxt('Diem_2A.txt', dtype = int, delimiter=',')` 
- `print("File dữ liệu điểm lớp 2A:\n", diem_2a)`
- ở đây tất cả phần tử là số nguyên nên mình để kiểu int cho dễ nhìn, các phần tử phân tách nhau bởi dấu ","
### Các hàm thống kê
- `arr.max() hoặc np.max(arr)`: Lấy giá trị lớn nhất của mảng arr.
- `arr.min() hoặc np.min(arr)`: Lấy giá trị nhỏ nhất của mảng arr.
- `arr.sum() hoặc np.sum(arr)`: Tổng tất cả các phần tử trong mảng arr.
- `arr.mean() hoặc np.mean(arr)`: Trung bình cộng của tất cả các phần tử trong mảng arr.
- `np.median(arr)`: Trả về giá trị trung vị của mảng arr.

##### Link bài viết tham khảo: https://codelearn.io/sharing/tim-hieu-thu-vien-numpy-trong-python

# 3. Cú pháp của Numpy linspace()
`np.linspace(start, stop, num, endpoint, retstep, dtype, axis)`
- `start & stop`: điểm đầu và điểm cuối của khoản cách
- `num`: số điểm cách đều nhau, giá trị mặc định là 50
- `endpoint`: tham số tùy chọn có thể là `True` hoặc `False`, giá trị mặc định là True (bao gồm điểm kết thúc), đặt thành False để loại bỏ điểm kết thúc
- `retstep`: thâm số tùy chọn nhận `Booleans`, khi đặt thành True giá trị bước được trả về
- `dtype`: kiểu dữ liệu
- `axis`: tham số tùy chọn biểu thi trục các số được lưu trữ
# 4. Numpy.arange()
- Returns an array `with evenly` spaced elements as the interval
- `start`: start os interval range
- `stop`: end of interval range
- `step`: step size of interval
- `dtype`: type of output array
- Ex:

![image](https://user-images.githubusercontent.com/88178841/163549315-064505e9-8880-4b2e-b91d-6e9ef6e7f868.png)
- Output:

![image](https://user-images.githubusercontent.com/88178841/163549442-7e2022d6-fec1-4836-93ef-9d82b14bd867.png)

