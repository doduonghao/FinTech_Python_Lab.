# Bài 3

ma_giao_dich = input("Nhập mã giao dịch: ")

vi_tri_dau = ma_giao_dich.find("-")

vi_tri_cuoi = ma_giao_dich.find("-")

so_tien_str = ma_giao_dich

so_tien = int(so_tien_str)

print(f"Số tiền giao dịch trích xuất được: {so_tien:,} VND")

if so_tien >= 5000000:
    print("Giao dịch cần xác thực OTP")
    
else:
    print("Giao dịch thành công")
