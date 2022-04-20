def show(s):
    count_upper = 0
    count_lower = 0
    for c in s:
        if c.isupper():
            count_upper += 1
        if c.islower():
            count_lower += 1

    print("Chuỗi nhập từ phím:", s)
    print("Số chữ hoa:", count_upper)
    print("Số chữ thường:", count_lower)


s = str(input())
show(s)