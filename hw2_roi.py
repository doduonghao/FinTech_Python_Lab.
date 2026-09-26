#2 hw2_roi

#Nhập thông tin
initial_investment = float(input("Tổng số tiền ban đầu: "))
gross_revenue      = float(input("Tổng số tiền bán được: "))

#Tính toán
net_profit = gross_revenue - initial_investment
ROI        = (net_profit / initial_investment) * 100

#In biên
print(f"Lợi nhuận ròng: {net_profit:,.0f} VND")
print(f"Tỷ lệ ROI(%): {ROI:,.0f} %")


