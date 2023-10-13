import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def draw_scatter_plot(data):
    # Tạo biểu đồ Scatter Plot
    plt.figure(figsize=(10, 6))  # Kích thước của biểu đồ
    sns.set_style("whitegrid")  # Định dạng nền biểu đồ
    
    # Vẽ biểu đồ Scatter với màu sắc thẩm mỹ
    sns.scatterplot(data=data, x="sales_channel_id", y="price", hue="price", palette="viridis")
    
    # Đặt tiêu đề và các nhãn trục
    plt.title("Mối quan hệ giữa price và sales_channel_id")
    plt.xlabel("sales_channel_id")
    plt.ylabel("price")
    
    # Hiển thị biểu đồ
    plt.show()

# Đọc dữ liệu từ file CSV
data = pd.read_csv("C:/HM/HM_Data/300transactionSample.csv")

# Gọi hàm để vẽ biểu đồ Scatter Plot
draw_scatter_plot(data)
