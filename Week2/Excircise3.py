from numpy.random import rand

a = 1e+6 # so tien toi thieu trong tai khoan
b = 1e+9 # so tien toi da trong tai khoan
n = 50000 # tong cong co 50000 tai khoan 
tai_khoan_hacker = 0
ngay = 0

list_money = a + (b - a) * rand(n, 1)

def hack():
    global ngay
    global tai_khoan_hacker
    global list_money
    # print(list_money)
    while(tai_khoan_hacker <= 1e+9):
        tai_khoan_hacker += tai_khoan_hacker * (0.05 / 365)
        for i in range(n):
            money = list_money[i][0] * 0.05/365
            if(money < 1e+3):
                tai_khoan_hacker += money 
            else:
                list_money[i][0] += money - (money % 1000)
                tai_khoan_hacker += money % 1000 
            # print(tai_khoan_hacker)
        ngay += 1
    

hack()
print("Can",ngay, " de hacker tro thanh ty phu")





