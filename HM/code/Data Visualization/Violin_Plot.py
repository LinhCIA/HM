import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def ve_violin_plot(data):
    # Tạo biểu đồ Violin Plot
    plt.figure(figsize=(10, 6))  # Kích thước của biểu đồ
    sns.set_style("whitegrid")  # Định dạng nền biểu đồ

    # Vẽ biểu đồ Violin Plot
    sns.violinplot(data=data, x="sales_channel_id", y="price", palette="Set1", inner="stick")

    # Đặt tiêu đề và các nhãn trục
    plt.title("Biểu đồ Violin Plot - Phân phối 'price' theo 'sales_channel_id'")
    plt.xlabel("sales_channel_id")
    plt.ylabel("price")

    # Hiển thị biểu đồ
    plt.xticks(rotation=45)  # Xoay nhãn trục x để dễ đọc
    plt.tight_layout()
    plt.show()

# Đọc dữ liệu từ file CSV
data = pd.read_csv("C:/HM/HM_Data/300transactionSample.csv")

# Gọi hàm để vẽ biểu đồ Violin Plot
ve_violin_plot(data)
