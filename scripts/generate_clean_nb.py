import nbformat as nbf

nb = nbf.v4.new_notebook()

# Title
nb.cells.append(nbf.v4.new_markdown_cell("# Video Game Sales - Báo Cáo Trực Quan Hóa Dữ Liệu (Phối Màu Chuẩn & Tối Giản)\n\nBáo cáo trực quan hóa dữ liệu bán đĩa game toàn cầu từ `vgsales-clean.csv`. Đã cập nhật bộ màu chuẩn: **Bắc Mỹ (Xanh dương)** và **Châu Âu (Cam)** có độ tương phản cao, rõ ràng, không gây rốii mắt."))

# Pip install
nb.cells.append(nbf.v4.new_code_cell("# Cài đặt thư viện nếu cần\n!pip install -q seaborn matplotlib pandas"))

# Config
nb.cells.append(nbf.v4.new_code_cell("""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Thiết lập phong cách trực quan tối giản, dễ nhìn
sns.set_theme(style='whitegrid')
plt.rcParams['font.size'] = 11
plt.rcParams['figure.titlesize'] = 14

# BỘ MÀU CHUẨN CÓ ĐỘ TƯƠNG PHẢN CAO
COLOR_NA = '#1f77b4'      # Xanh dương đậm (Bắc Mỹ)
COLOR_EU = '#ff7f0e'      # Cam tươi (Châu Âu)
COLOR_JP = '#2ca02c'      # Xanh lá (Nhật Bản)
COLOR_OTHER = '#a6a6a6'   # Xám trung tính (Khu vực khác)
"""))

# Load data
nb.cells.append(nbf.v4.new_code_cell("df = pd.read_csv('vgsales-clean.csv')\ndisplay(df.head())"))

# 1. Line Chart: Doanh thu theo năm
nb.cells.append(nbf.v4.new_markdown_cell("## 1. Xu hướng doanh thu toàn cầu theo năm\n**Mô tả:** Biểu đồ đường thể hiện tổng doanh thu bán đĩa game theo thời gian.\n- **Nhận xét:** Thị trường game bùng nổ mạnh mẽ từ năm 1995 và đạt đỉnh vào giai đoạn **2008 - 2009** (thời kỳ của PS3, Xbox 360, Nintendo Wii). Sau đó doanh thu đĩa vật lý giảm dần."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_year = df.groupby('Year')['Global_Sales'].sum().reset_index()

plt.figure(figsize=(12, 5))
sns.lineplot(data=sales_by_year, x='Year', y='Global_Sales', color=COLOR_NA, linewidth=2.5)
plt.title('Xu hướng doanh thu đĩa game toàn cầu qua các năm', fontweight='bold', pad=15)
plt.xlabel('Năm phát hành')
plt.ylabel('Doanh thu (Triệu bản)')
plt.tight_layout()
plt.show()
"""))

# 2. Pie Chart: Tỉ trọng doanh thu các khu vực (Độ tương phản cao)
nb.cells.append(nbf.v4.new_markdown_cell("## 2. Tỉ trọng doanh thu theo từng khu vực\n**Mô tả:** Biểu đồ tròn thể hiện mức độ đóng góp của từng thị trường (Sử dụng Xanh dương cho NA và Cam cho EU để dễ phân biệt).\n- **Nhận xét:** **Bắc Mỹ (NA)** chiếm **48.6%** (Xanh dương) và **Châu Âu (EU)** chiếm **27.3%** (Cam). Đây là 2 thị trường tiêu thụ đĩa game lớn nhất thế giới."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_region = [df['NA_Sales'].sum(), df['EU_Sales'].sum(), df['JP_Sales'].sum(), df['Other_Sales'].sum()]
labels = ['Bắc Mỹ (NA)', 'Châu Âu (EU)', 'Nhật Bản (JP)', 'Khu vực khác']
colors = [COLOR_NA, COLOR_EU, COLOR_JP, COLOR_OTHER]

plt.figure(figsize=(7, 7))
plt.pie(sales_by_region, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, 
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})
plt.title('Tỉ trọng doanh thu bán game theo khu vực', fontweight='bold', pad=15)
plt.tight_layout()
plt.show()
"""))

# 3. Bar Chart: Top 10 Genre (Đơn màu)
nb.cells.append(nbf.v4.new_markdown_cell("## 3. Top 10 Thể loại game (Genre) bán chạy nhất\n**Mô tả:** Thống kê tổng doanh thu theo thể loại game (Dùng 1 màu đơn gọn gàng).\n- **Nhận xét:** **Action (Hành động)** và **Sports (Thể thao)** là hai thể loại áp đảo về doanh số."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_genre = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 5))
ax = sns.barplot(data=sales_by_genre, x='Global_Sales', y='Genre', color=COLOR_NA)
plt.title('Top 10 thể loại game có doanh thu cao nhất', fontweight='bold', pad=15)
plt.xlabel('Doanh thu toàn cầu (Triệu bản)')
plt.ylabel('Thể loại')

for p in ax.patches:
    width = p.get_width()
    ax.annotate(f'{width:.1f}', (width + 15, p.get_y() + p.get_height() / 2),
                ha='left', va='center', fontsize=10)

plt.tight_layout()
plt.show()
"""))

# 4. Bar Chart: Top 10 Publisher (Đơn màu)
nb.cells.append(nbf.v4.new_markdown_cell("## 4. Top 10 Nhà phát hành (Publisher) có doanh thu cao nhất\n**Mô tả:** Xếp hạng các hãng phát hành game lớn nhất thế giới.\n- **Nhận xét:** **Nintendo** giữ vị trí số 1 tuyệt đối với hơn 1780 triệu bản."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_publisher = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 5))
ax = sns.barplot(data=sales_by_publisher, x='Global_Sales', y='Publisher', color=COLOR_NA)
plt.title('Top 10 Nhà phát hành game bán chạy nhất toàn cầu', fontweight='bold', pad=15)
plt.xlabel('Doanh thu toàn cầu (Triệu bản)')
plt.ylabel('Nhà phát hành')

for p in ax.patches:
    width = p.get_width()
    ax.annotate(f'{width:.1f}', (width + 20, p.get_y() + p.get_height() / 2),
                ha='left', va='center', fontsize=10)

plt.tight_layout()
plt.show()
"""))

# 5. Bar Chart: Top 10 Platform (Đơn màu)
nb.cells.append(nbf.v4.new_markdown_cell("## 5. Top 10 Hệ máy (Platform) phổ biến nhất\n**Mô tả:** Thống kê doanh thu đĩa game theo từng hệ máy.\n- **Nhận xét:** **PS2** và **X360** là hai hệ máy dẫn đầu."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_platform = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 5))
ax = sns.barplot(data=sales_by_platform, x='Global_Sales', y='Platform', color=COLOR_NA)
plt.title('Top 10 Hệ máy mang lại doanh thu đĩa game cao nhất', fontweight='bold', pad=15)
plt.xlabel('Doanh thu toàn cầu (Triệu bản)')
plt.ylabel('Hệ máy (Platform)')

for p in ax.patches:
    width = p.get_width()
    ax.annotate(f'{width:.1f}', (width + 15, p.get_y() + p.get_height() / 2),
                ha='left', va='center', fontsize=10)

plt.tight_layout()
plt.show()
"""))

# 6. Grouped Bar Chart: So sánh NA vs EU theo Thể loại (Chỉ 2 màu)
nb.cells.append(nbf.v4.new_markdown_cell("## 6. So sánh trực tiếp doanh số Bắc Mỹ (NA) vs Châu Âu (EU) theo Thể loại\n**Mô tả:** Sử dụng đúng **2 MÀU DUY NHẤT** (Bắc Mỹ = Xanh dương, Châu Âu = Cam) để so sánh thị hiếu 2 thị trường lớn nhất.\n- **Nhận xét:** Thị trường Bắc Mỹ luôn áp đảo Châu Âu ở tất cả các thể loại, nhưng tỷ lệ chênh lệch là rất tương đồng giữa các thể loại lớn như Action, Sports và Shooter."))
nb.cells.append(nbf.v4.new_code_cell("""top_genres = sales_by_genre.head(6)['Genre'].tolist()
df_top_g = df[df['Genre'].isin(top_genres)]

na_vs_eu_genre = df_top_g.groupby('Genre')[['NA_Sales', 'EU_Sales']].sum().loc[top_genres]

na_vs_eu_genre.plot(kind='bar', figsize=(11, 5.5), width=0.7, color=[COLOR_NA, COLOR_EU])
plt.title('So sánh doanh thu Bắc Mỹ (NA) vs Châu Âu (EU) theo Thể loại game', fontweight='bold', pad=15)
plt.xlabel('Thể loại game')
plt.ylabel('Doanh thu (Triệu bản)')
plt.legend(['Bắc Mỹ (NA)', 'Châu Âu (EU)'])
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
"""))

# 7. Grouped Bar Chart: So sánh NA vs EU ở Top 10 Game (Chỉ 2 màu)
nb.cells.append(nbf.v4.new_markdown_cell("## 7. So sánh trực tiếp doanh số Bắc Mỹ (NA) vs Châu Âu (EU) ở Top 10 Game bán chạy nhất\n**Mô tả:** So sánh chi tiết doanh số bán đĩa ở Bắc Mỹ và Châu Âu của 10 tựa game lớn nhất (Chỉ dùng **2 màu Xanh dương & Cam** giúp người đọc phân biệt ngay lập tức).\n- **Nhận xét:** Đa số các siêu phẩm (như Wii Sports, Super Mario Bros) bán chạy vượt trội ở Bắc Mỹ. Riêng tựa game **Mario Kart Wii**, doanh thu ở Châu Âu (Cam) tiệm cận rất sát với Bắc Mỹ (Xanh dương)."))
nb.cells.append(nbf.v4.new_code_cell("""top_10_games = df.head(10)

top_10_games.set_index('Name')[['NA_Sales', 'EU_Sales']].plot(
    kind='bar', figsize=(12, 5.5), width=0.7, color=[COLOR_NA, COLOR_EU]
)

plt.title('So sánh doanh thu Bắc Mỹ (NA) vs Châu Âu (EU) của Top 10 Game bán chạy nhất', fontweight='bold', pad=15)
plt.xlabel('Tên Game')
plt.ylabel('Doanh thu (Triệu bản)')
plt.legend(['Bắc Mỹ (NA)', 'Châu Âu (EU)'])
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
"""))

# 8. Stacked Bar Chart: Cấu trúc 4 khu vực của Top 10 Game
nb.cells.append(nbf.v4.new_markdown_cell("## 8. Cấu trúc doanh thu đầy đủ theo 4 khu vực của Top 10 Game\n**Mô tả:** Biểu đồ cột chồng giúp xem xét tổng thể mức độ đóng góp của cả 4 khu vực (NA = Xanh dương, EU = Cam, JP = Xanh lá, Khác = Xám).\n- **Nhận xét:** Sự kết hợp 4 màu rõ rệt giúp phân định rõ mảng đóng góp từ Nhật Bản (Xanh lá) ở tựa game *Pokemon Red/Blue* mà không làm mờ đi 2 thị trường Bắc Mỹ và Châu Âu."))
nb.cells.append(nbf.v4.new_code_cell("""top_10_games.set_index('Name')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].plot(
    kind='bar', stacked=True, figsize=(12, 6), color=[COLOR_NA, COLOR_EU, COLOR_JP, COLOR_OTHER], edgecolor='black', linewidth=0.5
)

plt.title('Cấu trúc doanh thu khu vực đầy đủ của Top 10 Game bán chạy nhất', fontweight='bold', pad=15)
plt.xlabel('Tên Game')
plt.ylabel('Doanh thu (Triệu bản)')
plt.legend(['Bắc Mỹ (NA)', 'Châu Âu (EU)', 'Nhật Bản (JP)', 'Khu vực khác'])
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
"""))

# Write directly to notebook file
with open('Data_Visualization.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Notebook regenerated successfully!")
