# bai2
ten_san_pham    = input("Nhập tên sản phẩm: ")
so_luong        = int(input("so_luong: "))
don_gia         = float(input("don_gia: "))
tong_tien_hang  = so_luong * don_gia
thue_VAT        = 0.08 * tong_tien_hang
tong_thanh_toan = tong_tien_hang + thue_VAT
print("\n" + "="* 36 )
print("====HÓA ĐƠN BÁN HÀNG====")
print("="* 36)
print(f"Tên sản phẩm: {ten_san_pham}")
print(f"Số lượng: {so_luong}")
print(f"Đơn giá: {don_gia:,.0f} VND")
print("-" * 36)
print(f"Tổng tiền hàng: {tong_tien_hang:,.0f} VND")
print(f"Thuế VAT (8%): {thue_VAT:,.0f} VND")
print(f"Tổng thanh toán: {tong_thanh_toan:,.0f} VND")
print("="* 36)
                         
