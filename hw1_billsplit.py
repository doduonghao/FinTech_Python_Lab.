#1 hw1_billsplit

#Thông tin 
X = float(input("Tổng hoá đơn(VND): "))
Y = float(input("Tiền tip(Y %): "))
N = float(input("Tổng số người(N): "))

#tổng tiền + tip
tip_amount   = X * (Y / 100)
total_amount = tip_amount + X

#số tiền mỗi người phải trả
per_person   = total_amount / N

#Làm tròn số nguyên
result       = round(per_person)
#In biên
print(f"Số tiền mỗi người phải trả: {result:,.0f} VND")
 




