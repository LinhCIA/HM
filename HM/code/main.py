""" Yêu cầu:
- Cần phải tách cột t_dat -> Day| Month| Year
          VD: 2020-03-18  -> 18 | 3    | 2020 """


import pandas as pd
import matplotlib.pyplot as plt

# Bước 1: Đọc dữ liệu
def read_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        print(f"Lỗi: Tệp không tồn tại. Hãy kiểm tra lại đường dẫn. Lỗi: {e}")
        return None

# Bước 2: Tiền xử lý dữ liệu
def data_preprocessing(data):
    if data is not None:
        # Xử lý dữ liệu lỗi hoặc dư thừa (nếu cần)
        # Ví dụ: Loại bỏ các hàng chứa giá trị null
        data = data.dropna()

        return data

# Bước 3: Tách cột t_dat thành Day, Month và Year
def split_t_dat(data):
    if data is not None:
        data['t_dat'] = pd.to_datetime(data['t_dat'])
        data['Day'] = data['t_dat'].dt.day
        data['Month'] = data['t_dat'].dt.month
        data['Year'] = data['t_dat'].dt.year

        return data

# Bước 4: Trực quan hóa dữ liệu EDA
def visualize_data(data):
    if data is not None:
        # Ví dụ: Vẽ biểu đồ cột số lượng giao dịch theo tháng
        monthly_transactions = data.groupby('Month')['transaction_id'].count()
        monthly_transactions.plot(kind='bar')
        plt.xlabel('Tháng')
        plt.ylabel('Số lượng giao dịch')
        plt.title('Số lượng giao dịch theo tháng')
        plt.show()

if __name__ == "__main__":
    # Thay đổi đường dẫn dưới đây thành tên tệp CSV cụ thể của bạn
    file_path = "C:/HM/HM_Data/300transactionSample.csv"

    # Bước 1: Đọc dữ liệu
    data = read_data(file_path)

    # Bước 2: Tiền xử lý dữ liệu
    data = data_preprocessing(data)

    # Bước 3: Tách cột t_dat
    data = split_t_dat(data)

    # Hiển thị dữ liệu sau khi đã xử lý, tách và làm sạch. (Đã hoàn thành yêu cầu!)
    print(data)

    # Bước 4: Trực quan hóa dữ liệu EDA
    visualize_data(data)
