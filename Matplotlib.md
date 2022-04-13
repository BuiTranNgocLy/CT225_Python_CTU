# Vẽ đồ thị với Matplotlib
## 1. import 
`import matplotlib.pyplot as plt`
## 2. Ví dụ
`import matplotlib.pyplot as plt`

`import numpy as np`

`xpoints = np.array([0, 6])`

`ypoints = np.array([0, 250])`

`plt.plot(xpoints, ypoints)`

`plt.show()`
- Kết quả
- ![image](https://user-images.githubusercontent.com/88178841/163044224-962bd785-e0e3-49b0-a084-cdbab0728132.png)

## 3. Vẽ biểu đồ điểm x và y
- `plot()`: vẽ các điểm (điểm đánh dấu) trong một sơ đồ, mặc định vẽ đường thẳng
- Tham số 1: 1 mảng chứa các điểm trên `trục x`
- THam số 2: 1 mảng chứa các điểm trên `trục y`
- Ví dụ vẽ 1 đường thẳng từ (1,3) đến (8,10)
- ![image](https://user-images.githubusercontent.com/88178841/163045278-5baa842b-ce2c-41c7-9ec2-222ef9391871.png)

- kết quả:
![image](https://user-images.githubusercontent.com/88178841/163046181-0c30ee8b-2a21-4128-a5ca-89256e55b1b5.png)


## Error: No module named matplotlib.pyplot
- => You can run the command below to install matplotlib package in Python 3
- `python3 -m pip install matplotlib --user`
