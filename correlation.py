import pandas as pd  # Dataframe
import matplotlib.pyplot as plt  # Biểu đồ
import os  # File

path = "D:/University Stuff/pypy"  # đường tới file
file = "Temperature.xlsx"  # tên file

# Tạo biến dataset: 1 dataframe
# Gán giá trị cho biến này bằng cách đọc dataframe từ excel dùng địa chỉ nói trên
dataset = pd.read_excel(os.path.join(path, file))

# Giả sử bây giờ ta chỉ xét ở khu vực VD để xét tương quan giữa độ mặn và nhiệt độ
# Bây giờ ta tạo một biến để lưu các bản ghi có giá trị Area là VD chứa 2 thuộc tính: độ mặn và nhiệt độ
required = dataset.loc[dataset["Area"] == "VD", ["Salinity","Temperature"]]
print(required)

# Tuyệt! Ta đã lọc ra những dữ liệu ta cần. Tuy nhiên chúng ta cần lọc thêm một lần nữa bởi sẽ có giá trị NA
# Dùng dropna() để bỏ những bản ghi có giá trị NA

# Vì ta sử dụng lại dataframe required trên, ta dùng inplace=True để bỏ bản ghi có giá trị NA từ 1 dataframe
# đã tồn tại
required.dropna(inplace=True)
print(required)

# Bây giờ ta sẽ tính độ tương quan giữa 2 thuộc tính này
# May mắn thay là pandas đã có sẵn hàm để tính tương quan giữa 2 thuộc tính này (mặc định là tương quan Pearson)
pear_corr = required["Salinity"].corr(required["Temperature"])
print(pear_corr)

# Giá trị trả về là -0.003, có nghĩa là độ mặn và nhiệt độ hầu như không tương quan với nhau
# Ta sẽ kiểm tra bằng biểu đồ phân tán (scatter plot), biểu đồ để xét tương quan giữa 2 biến
ax1 = required.plot.scatter(x='Salinity', y='Temperature', c='DarkBlue')
plt.show()

