# Câu 3
class Student(Human):
    def __init__(self, ten, namsinh, quequan, nghenghiep, MSSV, nganhhoc, diemtrungbinh):
        self.ten = ten
        self.namsinh = namsinh
        self.quequan = quequan
        self.nghenghiep = "student"
        self.MSSV = MSSV
        self.nganhhoc = nganhhoc
        self.diemtrungbinh = diemtrungbinh
    
    def Study(self, phong):
        print("Sinh viên {} có {} thuộc {} đang học tại phòng {}".format(self.ten, self.MSSV, self.nganhhoc, phong))

    def Rank(self):
        if(self.diemtrungbinh<4):
            print("Sinh vien {} có MSSV {} với điểm trung bình {} được xếp loại Yếu ".format(self.ten, self.MSSV, self.diemtrungbinh))
        elif(self.diemtrungbinh>=4 and self.diemtrungbinh<6):
            print("Sinh vien {} có MSSV {} với điểm trung bình {} được xếp loại Trung bình ".format(self.ten, self.MSSV, self.diemtrungbinh))
        elif(self.diemtrungbinh>=6 and self.diemtrungbinh<8):
            print("Sinh vien {} có MSSV {} với điểm trung bình {} được xếp loại Khá ".format(self.ten, self.MSSV, self.diemtrungbinh))
        elif(self.diemtrungbinh>=8 and self.diemtrungbinh<10):
            print("Sinh vien {} có MSSV {} với điểm trung bình {} được xếp loại Giỏi ".format(self.ten, self.MSSV, self.diemtrungbinh))

BuiTranNgocLy = Student("Bui Tran Ngoc Ly", 2001, "Hau Giang",Student, "B19083", "Mạng máy tính và truyền thông dữ liệu", 
BuiTranNgoccLy.Rank()