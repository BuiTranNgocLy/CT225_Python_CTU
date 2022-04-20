"""
Cau1: B1908338 - Bui Tran Ngoc Ly
Viết chương trình nhận vào một câu do người dùng nhập, in ra màn hình số chữ cái
và số chữ số có trong câu vừa nhập
"""
import re
string =input("Nhap chuoi-->")
kitu=string.replace(" ","")
len(kitu)
#đếm số
a=re.findall(r'\d',string)
print("Số chữ số trong chuỗi vừa nhập: ",len(a))
A=len(a)
B=len(kitu)
C=B-A
print("Số chữ trong chuỗi vừa nhập là: ",C)



