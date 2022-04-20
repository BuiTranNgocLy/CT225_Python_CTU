def setStudent():
    ten = input("Nhập tên sinh viên :")
    while(len(ten)>25):
        print("Tên không dài quá 25 kí tự")
        ten = input("Nhập tên sinh viên")

    namsinh = input("Nhập năm sinh sinh viên : ")
    while( namsinh.isalpha() or len(namsinh)>4):
        print("Năm sinh có 4 chữ số")
        namsinh = input("Nhập năm sinh sinh viên: ")

    quequan = input("Nhập quê quán sinh viên : ")
while(len(quequan)>50):
        print("Quê quán không quá 50 kí tự")
        quequan = input("Nhập quê quán sinh viên : ")
    
    MSSV = input("Nhập MSSV : ")
    while(MSSV.isalpha() or len(MSSV)>5):
        print("MSSV chỉ có kí tư số")
        MSSV = input("Nhập MSSV : ")

    nganhhoc = input("Nhập ngành học sinh viên : ")
    while(len(nganhhoc)>40):
        print("Ngành học không vượt quá 40 kí tự")
        nganhhoc = input("Nhập ngành học sinh viên : ")

    diemtrungbinh = int(input("Nhập điểm trung bình : "))
    while(diemtrungbinh<0 or diemtrungbinh>10):
        diemtrungbinh = input("Nhập điểm trung bình : ")

setStudent()