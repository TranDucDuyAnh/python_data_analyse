import pandas as pd  # Dataframe
import scipy.stats as stats # Kiểm định t-test và ANOVA
from statsmodels.stats.proportion import proportions_ztest # Kiểm định z-test
import os  # File
import numpy as np

path = "D:/University Stuff/pypy"  # đường tới file
file = "Temperature.xlsx"  # tên file

# Tạo biến dataset: 1 dataframe
# Gán giá trị cho biến này bằng cách đọc dataframe từ excel dùng địa chỉ nói trên
dataset = pd.read_excel(os.path.join(path, file))

# KIỂM ĐỊNH KÌ VỌNG BẰNG T-TEST
# Bài toán: Nhiệt độ trung bình thông thường ở khu OS là 12 độ. Kiểm định giả thuyết với mức ý nghĩa là 5%
# Lấy dữ liệu ở khu OS, cột nhiệt độ và lọc giá trị NA nếu có
required_one = dataset.loc[dataset["Area"] == "OS", ["Temperature"]].dropna()

# Chuyển sang dạng list
req_list_1 = required_one["Temperature"].tolist()

# ttest_1samp(a, popmean) với a là bộ dữ liệu, popmean là trung bình dự kiến
print(stats.ttest_1samp(req_list_1, 12))
print("---")
# Giá trị p-value = 0.0222 nhỏ hơn mức ý nghĩa 5%. Nên ta sẽ bác bỏ giả thiết rằng
# nhiệt độ trung bình ở khu OS là 12 độ

# KIỂM ĐỊNH TỈ LỆ BẰNG Z-TEST
# Bài toán: Từ 1990 đến 2005 có 50% tháng quan sát mà nồng độ CHLFa ở khu WS lớn hơn 5. Kiểm định giả
# thuyết với mức ý nghĩa là 5%
# Lấy dữ liệu ở khu WS, cột CHLFa và lọc giá trị NA nếu có
required_two = dataset.loc[dataset["Area"] == "WS", ["CHLFa"]].dropna()

# Chuyển sang dạng list
req_list_2 = required_two["CHLFa"].tolist()

# Đếm số tháng quan sát mà CHLFa lớn hơn 5
counter = 0
for i in req_list_2:
    if i > 5:
        counter += 1

# proportions_ztest(count, nobs, value)
# với count là số quan sát thỏa mãn, nobs là tổng số quan sát, value là giá trị kiểm định
print(proportions_ztest(counter, len(req_list_2), 0.5))
print("---")
# Giá trị p-value là 0.6026 lớn hơn mức ý nghĩa 5%. Ta chấp nhận giả thuyết là trong các tháng từ 1990 - 2005 thì
# có 50% tháng có nồng độ CHLFa lớn hơn 5 ở khu WS

# KIỂM ĐỊNH PHƯƠNG SAI BẰNG ANOVA TEST
# Bài toán: Từ năm 2000 trở về sau, độ mặn trung bình ở 3 khu vực VD, ED, GM là như nhau với mức ý nghĩa 5%
# Lấy dữ liệu ở khu VD, ED, GM từ năm 2000 về sau, cột độ mặn và lọc giá trị NA nếu có
required_VD = dataset.loc[(dataset["Area"] == "VD") & (dataset["Year"] >= 2000), ["Salinity"]].dropna()
required_ED = dataset.loc[(dataset["Area"] == "ED") & (dataset["Year"] >= 2000), ["Salinity"]].dropna()
required_GM = dataset.loc[(dataset["Area"] == "GM") & (dataset["Year"] >= 2000), ["Salinity"]].dropna()

# Chuyển sang dạng list
req_list_VD = required_VD["Salinity"].tolist()
req_list_ED = required_ED["Salinity"].tolist()
req_list_GM = required_GM["Salinity"].tolist()

# Thực hiện ANOVA một chiều dùng f_oneway(data)
print(stats.f_oneway(req_list_VD, req_list_ED, req_list_GM))
# Giá trị p-value là 2.0497e-31 nhỏ hơn 5%. Ta bác bỏ giá thuyết độ mặn trung bình từ 2000 trở về sau trong 3 khu vực
# này là giống nhau
