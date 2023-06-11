import pandas as pd  # Dataframe
import os  # File

path = "D:/University Stuff/pypy"  # đường tới file
file = "Temperature.xlsx"  # tên file

dataset = pd.read_excel(os.path.join(path, file))

# Gộp trường có các giá trị lặp lại dùng groupby()
# Thêm các câu lệnh như mean(), median() sau groupby() để xác định kiểu gộp

# VD: Thống kê nhiệt độ trung bình các năm dưới năm 2000
subset_one = dataset.loc[dataset["Year"] < 2000, ["Year", "Temperature"]]
avg_temp = subset_one.groupby("Year").mean()
print("Mean Temperature")
print(avg_temp)
print("---")

subset_two = dataset[["Area", "Temperature"]]
# VD: Thống kê nhiệt độ thấp nhất của từng khu vực
min_temp = subset_two.groupby("Area").min()
print("Min Temperature")
print(min_temp)
print("---")

# VD: Thống kê nhiệt độ cao nhất của từng khu vực
print("Max Temperature")
max_temp = subset_two.groupby("Area").max()
print(max_temp)
print("---")

subset_three = dataset[["Area", "Salinity"]]
# VD: Thống kê trung vị độ mặn của từng khu vực
med_sal = subset_three.groupby("Area").median()
print("Median Salinity")
print(med_sal)
print("---")

# VD: Thống kê phương sai độ mặn của từng khu vực
var_sal = subset_three.groupby("Area").var()
print("Variance Salinity")
print(var_sal)
print("---")

# VD: Thống kê độ lệch chuẩn độ mặn của từng khu vực
std_sal = subset_three.groupby("Area").std()
print("Standard Deviation Salinity")
print(std_sal)
print("---")

# Sử dụng lệnh crosstab() của pandas để tạo bảng tần số hai thuộc tính
# Sử dụng lệnh cut() để xếp các giá trị vào các khoảng đặt sẵn

# VD: Bảng phân tổ nhiệt độ theo từng tháng trong cả nước với các khoảng nhiệt độ như sau:
# -5-0, 0-5, 5-10, 10-15, 15-20, 20-25, 25-30 độ
# Đếm tất cả các tháng mà nhiệt độ nằm trong những khoảng trên
print("Bảng phân tổ nhiệt độ")
freq = dataset[["Month", "Temperature"]]
crosstab = pd.crosstab(freq["Month"], pd.cut(freq["Temperature"], bins=[-5, 0, 5, 10, 15, 20, 25, 30]))
print(crosstab)
print("-----")