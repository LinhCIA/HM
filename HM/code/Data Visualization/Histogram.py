import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def draw_histogram(data):
    # Tạo biểu đồ Histogram
    plt.figure(figsize=(10, 6))  # Kích thước của biểu đồ
    sns.set_style("whitegrid")  # Định dạng nền biểu đồ

    # Chọn một palette màu sắc sặc sỡ
    sasco_palette = sns.color_palette("hsv", as_cmap=True)

    # Vẽ biểu đồ Histogram với palette màu sắc sặc sỡ
    sns.histplot(data=data, x="price", bins=20, kde=True, palette=sasco_palette)

    # Đặt tiêu đề và các nhãn trục
    plt.title("Phân phối của giá trị 'price'")
    plt.xlabel("price")
    plt.ylabel("Số lượng")

    # Hiển thị biểu đồ
    plt.show()

# Đọc dữ liệu từ file CSV
data = pd.read_csv("C:/HM/HM_Data/300transactionSample.csv")

# Gọi hàm để vẽ biểu đồ Histogram
draw_histogram(data)
