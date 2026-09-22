#bài 1
ho_ten            = input("Nhập họ và tên khách hàng: ")
so_dien_thoai     = input("Nhập số điện thoại khách hàng: ")
cccd              = input("Nhập số Căn cước công dân (CCCD): ")
so_tien_nap       = float(input("Nhập số tiền nạp ban đầu vào ví (VND): "))
phi_mo_vi = 50000
so_du_kha_dung = so_tien_nap-phi_mo_vi
ho_ten_raw = ho_ten.upper()
bon_so_cuoi_cccd = cccd[-4:]
print("\n" + "="*36)
print("==== BIÊN LAI TẠO VÍ ĐIỆN TỬ ====")
print(f"Họ và tên khách hàng : {ho_ten_raw}")
print(f"4 số cuối CCCD : {bon_so_cuoi_cccd}")
print(f"Số tiền nạp : {so_tien_nap: } VND")
print(f"Phí mở ví : {phi_mo_vi: } VND")
print(f"Số dư khả dụng thực tế: {so_du_kha_dung: } VND")
print("="*36)

                        

