import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

path = "D:/University Stuff/pypy"  # đường tới file
file = "Temperature.xlsx"  # tên file

# Tạo một dataframe
dataset = pd.read_excel(os.path.join(path, file))

# BIỂU ĐỒ CỘT VÀ ĐƯỜNG
# Bộ dữ liệu nhiệt độ & độ mặn trung bình ở khu vực GM theo tháng năm 2005
def_cols = dataset.loc[:, ["Temperature", "Salinity"]]

temp_1 = dataset.loc[(dataset["Area"] == "GM") & (dataset["Year"] == 2005), ["Month", "Temperature", "Salinity"]]
test_1 = temp_1.groupby("Month").mean()
print(test_1)
print("---")

ax_1 = test_1.plot.bar(y="Temperature", rot=0)
ax_1.set_title("Nhiệt độ khu GM trong năm 2005")
plt.show()
ax_2 = test_1.plot.line(y="Salinity", rot=0, color={'Salinity':'orange'})
ax_2.set_title("Sự biến đổi độ mặn khu GM từng tháng trong năm 2005")
plt.show()

# BIỂU ĐỒ TRÒN
# Tính số tháng có nhiệt độ trong một khoảng nhất định ở khu WZ 1990-2005
temp_2 = dataset.loc[(dataset["Area"] == "WZ"), ["Month", "Temperature"]]
test_2 = pd.cut(temp_2["Month"], bins=(0, 2.5, 5, 7.5, 10, 12.5)).value_counts()
print(test_2)
print("---")

ax_3 = test_2.plot.pie(autopct='%1.1f%%')
ax_3.set_title("Những khoảng nhiệt độ ở khu WZ 1990-2005")
plt.show()

# BIỂU ĐỒ CỘT GHÉP/CHỒNG
# Bộ dữ liệu nhiệt độ & độ mặn trung bình ở khu vực VD theo tháng năm 2001 (đã được chuẩn hóa)
temp_3 = dataset.loc[(dataset["Area"] == "VD") & (dataset["Year"] == 2001), ["Month", "Temperature", "Salinity"]]
print(temp_3)
temp_3.loc[:, ["Temperature", "Salinity"]] = (def_cols - def_cols.min()) / (def_cols.max() - def_cols.min())
##
test_3 = temp_3.groupby("Month").mean()
print("---")

ax_4 = test_3.plot.bar(stacked=True, rot=0)
ax_4.set_title("Nhiệt độ và độ mặn ở khu VD năm 2001")
plt.show()
ax_5 = test_3.plot.bar(rot=0)
ax_5.set_title("Nhiệt độ và độ mặn ở khu VD năm 2001")
plt.show()

# BIỂU ĐỒ HISTOGRAM
test_4 = dataset.loc[(dataset["Area"] == "ED"), "Temperature"]
ax_6 = test_4.plot.hist(bins=np.linspace(0,27,10))
ax_6.set_title("Tần số của từng khoảng nhiệt độ ở khu vực ED (theo tháng)")
ax_6.set_ylabel("Tháng")

temp_4 = dataset.loc[(dataset["Area"] == "ED"), ["Month", "Temperature"]]
print(temp_4.sort_values("Temperature", ascending=False, ignore_index=True))
print("---")
plt.show()