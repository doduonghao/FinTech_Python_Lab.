# Bài 4

so_tien_goc = float(input("Nhập số tiền gốc: "))
lai_suat_nam = float(input("Nhập lãi suất năm (vd: 0.06): "))
thoi_gian = int(input("Nhập thời gian gửi (năm): "))

tong_tien = so_tien_goc * (1 + lai_suat_nam * thoi_gian)

print(f"Số tiền gốc         : {so_tien_goc:,.0f} VND")
print(f"Lãi suất năm        : {lai_suat_nam * 100:.1f}%")
print(f"Thời gian gửi       : {thoi_gian} năm")
print(f"TỔNG TIỀN NHẬN ĐƯỢC : {tong_tien:,.0f} VND")
