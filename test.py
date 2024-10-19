#code trên tham khảo gemini và chatgpt (chưa được tối ưu)
#cân nhắc khi sử dụng
#thắc mắc ib a Minh đẹp trai
import pandas as pd

# Load dữ liệu, truy xuất dữ liệu cho chương trình
df = pd.read_csv("đường dẫn file dữ liệu gốc") #vd C:/Users/Download/tenfile.csv

# thay đổi dữ liệu về float nếu k phải là float
df['Gold'] = df['Gold'].astype(float)
df['Silver'] = df['Silver'].astype(float)
df['Bronze'] = df['Bronze'].astype(float)

# Tính số Gold mới theo quy luật: 2 Silver = 1 Gold, 3 Bronze = 1 Gold
df['Total_Gold'] = df['Gold'] + df['Silver'] / 2 + df['Bronze'] / 3

# Sắp xếp và xử lý đồng hạng
df_sorted = df.sort_values(by=['Total_Gold'], ascending=False).reset_index(drop=True)
df_sorted['Rank'] = df_sorted.index + 1  # Tạo cột Rank ban đầu

# Xử lý đồng hạng
current_rank = 1
for i in range(1, len(df_sorted)):
    if df_sorted.loc[i, 'Total_Gold'] == df_sorted.loc[i-1, 'Total_Gold']:
        df_sorted.loc[i, 'Rank'] = current_rank  # Gán cùng rank cho các nước đồng hạng
    else:
        current_rank = df_sorted.loc[i, 'Rank']

# Thêm chú thích cho đồng hạng:
ranks = []
for i, rank in enumerate(df_sorted['Rank']):
    count = df_sorted['Rank'].value_counts()[rank]  # Đếm số lần xuất hiện của rank
    if count > 1:
        ranks.append(str(int(rank)) + "trung dai")  # Thêm "trung dai" nếu có đồng hạng
    else:
        ranks.append(str(int(rank)))

#săp xếp theo rank
df_sorted['Rank'] = ranks
# Tạo list danh sách 3 hạng đầu (có thể nhiều hơn 3 nếu đồng hạng)
top_3_list = []
top_3_ranks = df_sorted['Rank'].head(3).unique().tolist() # Lấy danh sách các hạng trong top 3 (unique)

for rank in top_3_ranks:
    countries_in_rank = df_sorted[df_sorted['Rank'] == rank]['Country'].tolist()
    top_3_list.append((rank, countries_in_rank)) # Thêm tuple (rank, [countries]) vào list

# Tạo file dữ liệu, save as vào máy tính
df_sorted.to_csv("đường dẫn file dữ liệu xuất ra", index=False)

# In top 3 với xử lý đồng hạng và list
print("\nTop 3:")
for rank, countries in top_3_list:
    for country in countries:
       Total_Gold = df_sorted[df_sorted['Country'] == country]['Total_Gold'].iloc[0] # Lấy Total_Gold tương ứng
       print(f"{rank} {country} - New Gold: {Total_Gold:.2f}") 

print("\nList top 3:")
print(top_3_list)
