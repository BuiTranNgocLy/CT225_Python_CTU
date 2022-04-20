def danh_sach_so_le(danhSachSo):
   #Cach 1:
   danhSachSoLe = [so for so in danhSachSo if so % 2 != 0]
  
   #Cach 2:

   # danhSachSoLe = []
   # for so in danhSachSo:
   #     if so % 2 != 0:
   #         danhSachSoLe.append(so)
  
   return danhSachSoLe

#Nhap danh sach tu ban phim
danhSach = input().split(',')
#Kiem tra xem danh sach co rong hay khong
if len(danhSach) == 0:
   print("Danh sach rong")
else:
   #Khoi lenh co the phat sinh loi
   try:
       #Ep kieu du lieu sang so thuc
       danhSachSo = list(map(int, danhSach))
       #Goi thuc thi ham va truyen tham so cho ham
       dsSoLe = danh_sach_so_le(danhSachSo)
       #Unpacking arguments
       print(*dsSoLe)
   #Khoi lenh duoc thuc thi khi loi xay ra
   except:
       print("Vui long nhap cac phan tu la so thuc!")