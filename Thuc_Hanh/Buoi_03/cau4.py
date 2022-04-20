# Câu 4
SV1 = Student("Lê Văn An", 2005, "Vĩnh Long", Student, 12345, "CNTT", 7.6)
SV2 = Student("Trần Văn Bình", 2007, "Trà Vinh",Student, 56789, "Tài chính ngân hàng", 4.5)
if(SV1.diemtrungbinh > SV2.diemtrungbinh):
    print("{} đạt hạng nhất, {} đạt hạng nhì".format(SV1.ten, SV2.ten))
else:
    print("{} đạt hạng nhất, {} đạt hạng nhì".format(SV2.ten, SV1.ten))
