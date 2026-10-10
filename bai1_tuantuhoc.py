# Bài 1

diem_credit = int(input("Nhập điểm tín dụng (300 - 850): "))

if diem_credit >= 750 and diem_credit <= 850:
    print("Rủi ro Thấp - Duyệt tự động")

elif diem_credit >= 600 and diem_credit < 750:
    print("Rủi ro Trung bình - Cần thẩm định")

elif diem_credit >= 300 and diem_credit < 600:
    print("Rủi ro Cao - Từ chối cấp tín dụng")

else:
    print("Điểm tín dụng không hợp lệ")
    
    
