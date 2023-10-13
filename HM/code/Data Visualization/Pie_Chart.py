import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def draw_pie_chart(data):
    # Tạo biểu đồ Pie Chart
    plt.figure(figsize=(8, 8))  # Kích thước của biểu đồ
    sns.set_style("whitegrid")  # Định dạng nền biểu đồ

    # Lấy dữ liệu phần trăm theo "sales_channel_id"
    sales_channel_percentages = data['sales_channel_id'].value_counts(normalize=True) * 100

    # Vẽ biểu đồ Pie Chart với màu sắc thẩm mỹ
    colors = sns.color_palette('pastel', len(sales_channel_percentages))
    plt.pie(sales_channel_percentages, labels=sales_channel_percentages.index[::-1], autopct='%1.1f%%',
            startangle=140, colors=colors)

    # Thêm chú thích trên và dưới biểu đồ
    plt.legend(sales_channel_percentages.index[::-1], loc='lower left')
    plt.title("Phân phối phần trăm của 'sales_channel_id'")
    
    # Hiển thị biểu đồ
    plt.show()

# Đọc dữ liệu từ file CSV
data = pd.read_csv("C:/HM/HM_Data/300transactionSample.csv")

# Gọi hàm để vẽ biểu đồ Pie Chart
draw_pie_chart(data)
