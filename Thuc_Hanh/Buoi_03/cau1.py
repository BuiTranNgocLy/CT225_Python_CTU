"""
Câu 1:Viết chương trình khởi tạo lớp human gồm có những thông tin sau : họ tên, năm sinh, quê
quán, nghề nghiệp. Viết phương thức :
- live(self, noicutru) : in ra màn hình người đó tên gì đang sống ở đâu
- work(self, diachicoquan) : in ra màn hình người đó tên gì đang làm nghề gì tại cơ quan nào
(địa chỉ cơ quan)
"""
# creates a class named human 
class human: 
        hoTen = "Ngoc ly"
        namSinh = "2001"
        que = "Hau Giang"
        job = "Dev"
        # Creating a method named live 
        def live(self, noicutru:str):      
                self.noicutru=noicutru
        # Creating a method named work 
        def work(self, diachicoquan:str):      
                self.diachicoquan=diachicoquan
        
  
def Main(): 
        # me is an object of class human
        me = human()    
        # Passing values to the function live 
        # by using dot(.) operator. 
        me.live("Hau Giang")
        print("Ten: " + str(me.hoTen))       
        print("Noi cu tru: " + str(me.noicutru))
        # Passing values to the function live
        me.work("Can Tho")
        print("Ten: " + str(me.hoTen))
        print("Cong viec: " + str(me.job))
        print("Dia chi co quan: " + str(me.diachicoquan))
  
if __name__=='__main__': 
        Main()