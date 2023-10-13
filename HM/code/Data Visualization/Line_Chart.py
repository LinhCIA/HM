import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def ve_line_chart(data):
    # Đảm bảo cột "t_dat" là kiểu dữ liệu datetime
    data['t_dat'] = pd.to_datetime(data['t_dat'])

    # Sắp xếp dữ liệu theo thời gian
    data = data.sort_values(by='t_dat')

    # Tạo biểu đồ Line Chart
    plt.figure(figsize=(12, 6))  # Kích thước của biểu đồ
    sns.set_style("whitegrid")  # Định dạng nền biểu đồ

    # Vẽ biểu đồ Line Chart
    sns.lineplot(data=data, x="t_dat", y="price", color="royalblue")

    # Đặt tiêu đề và các nhãn trục
    plt.title("Xu hướng thay đổi giá trị 'price' theo thời gian")
    plt.xlabel("Ngày/Tháng")
    plt.ylabel("price")

    # Hiển thị biểu đồ
    plt.xticks(rotation=45)  # Xoay nhãn trục x để dễ đọc
    plt.tight_layout()

    # Hiển thị biểu đồ
    plt.show()

# Đọc dữ liệu từ file CSV
data = pd.read_csv("C:/HM/HM_Data/300transactionSample.csv")

# Gọi hàm để vẽ biểu đồ Line Chart
ve_line_chart(data)
