try:
   #Nhap hai so tu ban phim
   a = int(input())
   b = int(input())
  
   if a>b:
       print("So thu nhat lon hon so thu hai!")
   else:       
       dem = 0
       #Su dung vong lap for duyet cac gia tri tu a den b
       for i in range(a, b+1):
           #Kiem tra dieu kien chia het cho 2
           if i % 2 == 0:
               #Dem cac so thoa dieu kien
               dem += 1
               print(i, end=" ")
       else:
           if dem == 0:
               print("Khong co so nao chan")
           else:
               print("\nDa in het cac so chan")
              
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")