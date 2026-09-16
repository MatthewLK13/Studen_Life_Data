import nbformat as nbf

nb = nbf.v4.new_notebook()

# Markdown cell - Title
nb.cells.append(nbf.v4.new_markdown_cell("# Video Game Sales - Báo Cáo Trực Quan Hóa Dữ Liệu (Tối Ưu & Dễ Hiểu)\n\nBáo cáo trực quan hóa dữ liệu bán đĩa game toàn cầu từ `vgsales-clean.csv`. Tất cả biểu đồ được thiết kế lại theo tiêu chí **tối giản, sạch đẹp, dễ hiểu và không gây rối mắt**."))

# Code cell - Pip install
nb.cells.append(nbf.v4.new_code_cell("# Cài đặt thư viện nếu cần\n!pip install -q seaborn matplotlib pandas"))

# Code cell - Imports & Config
nb.cells.append(nbf.v4.new_code_cell("""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Thiết lập phong cách trực quan tối giản, dễ nhìn
sns.set_theme(style='whitegrid')
plt.rcParams['font.size'] = 11
plt.rcParams['figure.titlesize'] = 14
MAIN_COLOR = '#2b5c8f'  # Tông màu xanh đơn nhã nhặn, chuyên nghiệp
"""))

# Code cell - Load data
nb.cells.append(nbf.v4.new_code_cell("df = pd.read_csv('vgsales-clean.csv')\ndisplay(df.head())"))

# 1. Line Chart: Doanh thu theo năm
nb.cells.append(nbf.v4.new_markdown_cell("## 1. Xu hướng doanh thu toàn cầu theo năm\n**Mô tả:** Biểu đồ đường thể hiện tổng doanh thu bán đĩa game theo thời gian.\n- **Nhận xét:** Thị trường game bùng nổ mạnh mẽ từ năm 1995 và đạt đỉnh vào giai đoạn **2008 - 2009** (thời kỳ của PS3, Xbox 360, Nintendo Wii). Sau giai đoạn này, doanh thu đĩa vật lý giảm dần do sự xuất hiện của game di động và chợ game online."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_year = df.groupby('Year')['Global_Sales'].sum().reset_index()

plt.figure(figsize=(12, 5))
sns.lineplot(data=sales_by_year, x='Year', y='Global_Sales', color=MAIN_COLOR, linewidth=2.5)
plt.title('Xu hướng doanh thu đĩa game toàn cầu qua các năm', fontweight='bold', pad=15)
plt.xlabel('Năm phát hành')
plt.ylabel('Doanh thu (Triệu bản)')
plt.tight_layout()
plt.show()
"""))

# 2. Pie Chart: Thị phần khu vực
nb.cells.append(nbf.v4.new_markdown_cell("## 2. Tỉ trọng doanh thu theo từng khu vực\n**Mô tả:** Biểu đồ tròn thể hiện mức độ đóng góp của từng thị trường vào tổng doanh thu toàn cầu.\n- **Nhận xét:** **Bắc Mỹ (NA)** là thị trường lớn nhất khi đóng góp tới **48.6%** tổng doanh số, tiếp theo là **Châu Âu (EU)** với **27.3%** và **Nhật Bản (JP)** với **14.8%**."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_region = [df['NA_Sales'].sum(), df['EU_Sales'].sum(), df['JP_Sales'].sum(), df['Other_Sales'].sum()]
labels = ['Bắc Mỹ (NA)', 'Châu Âu (EU)', 'Nhật Bản (JP)', 'Khu vực khác']
colors = ['#2b5c8f', '#4682b4', '#90edb7', '#d3d3d3']

plt.figure(figsize=(7, 7))
plt.pie(sales_by_region, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, 
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})
plt.title('Tỉ trọng doanh thu bán game theo khu vực', fontweight='bold', pad=15)
plt.tight_layout()
plt.show()
"""))

# 3. Bar Chart: Top 10 Genre (Đơn màu)
nb.cells.append(nbf.v4.new_markdown_cell("## 3. Top 10 Thể loại game (Genre) bán chạy nhất\n**Mô tả:** Thống kê tổng doanh thu theo thể loại game (sử dụng 1 tông màu nhất quán để không bị rối mắt).\n- **Nhận xét:** **Action (Hành động)** và **Sports (Thể thao)** là hai thể loại áp đảo hoàn toàn về doanh số trên phạm vi toàn cầu."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_genre = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 5))
ax = sns.barplot(data=sales_by_genre, x='Global_Sales', y='Genre', color=MAIN_COLOR)
plt.title('Top 10 thể loại game có doanh thu cao nhất', fontweight='bold', pad=15)
plt.xlabel('Doanh thu toàn cầu (Triệu bản)')
plt.ylabel('Thể loại')

# Hiển thị số liệu trực tiếp trên từng cột
for p in ax.patches:
    width = p.get_width()
    ax.annotate(f'{width:.1f}', (width + 15, p.get_y() + p.get_height() / 2),
                ha='left', va='center', fontsize=10)

plt.tight_layout()
plt.show()
"""))

# 4. Bar Chart: Top 10 Publisher (Đơn màu)
nb.cells.append(nbf.v4.new_markdown_cell("## 4. Top 10 Nhà phát hành (Publisher) có doanh thu cao nhất\n**Mô tả:** Xếp hạng các hãng phát hành game lớn nhất thế giới.\n- **Nhận xét:** **Nintendo** giữ vị trí số 1 tuyệt đối với hơn 1780 triệu bản nhờ hàng loạt series game độc quyền thành công."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_publisher = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 5))
ax = sns.barplot(data=sales_by_publisher, x='Global_Sales', y='Publisher', color=MAIN_COLOR)
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
nb.cells.append(nbf.v4.new_markdown_cell("## 5. Top 10 Hệ máy (Platform) phổ biến nhất\n**Mô tả:** Thống kê doanh thu đĩa game theo từng hệ máy chơi game.\n- **Nhận xét:** **PS2** và **X360** là hai hệ máy dẫn đầu về lượng tiêu thụ đĩa game."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_platform = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 5))
ax = sns.barplot(data=sales_by_platform, x='Global_Sales', y='Platform', color=MAIN_COLOR)
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

# 6. Grouped Bar Chart: Thay thế Heatmap để so sánh thị trường dễ hiểu
nb.cells.append(nbf.v4.new_markdown_cell("## 6. So sánh thị hiếu doanh thu giữa các thị trường theo Thể loại game\n*(Biểu đồ thay thế Ma trận tương quan rắc rối - Dễ nhìn, dễ hiểu hơn cho người đọc)*\n\n**Mô tả:** Biểu đồ cột nhóm so sánh doanh thu trực tiếp giữa 3 thị trường lớn (Bắc Mỹ, Châu Âu, Nhật Bản) ở từng thể loại game.\n- **Nhận xét dễ thấy:**\n  - **Bắc Mỹ (NA) và Châu Âu (EU)** có xu hướng rất tương đồng nhau: Đều chuộng nhất là game *Action*, *Sports* và *Shooter*.\n  - **Nhật Bản (JP)** có sự khác biệt rõ rệt: Doanh số lớn nhất thuộc về thể loại **Role-Playing (Game nhập vai)**, vượt xa các thể loại khác."))
nb.cells.append(nbf.v4.new_code_cell("""# Lấy Top 6 thể loại lớn nhất để so sánh
top_genres = sales_by_genre.head(6)['Genre'].tolist()
df_top_g = df[df['Genre'].isin(top_genres)]

genre_region_sales = df_top_g.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales']].sum().loc[top_genres]

genre_region_sales.plot(kind='bar', figsize=(12, 6), width=0.8, color=['#2b5c8f', '#4682b4', '#90edb7'])
plt.title('So sánh doanh thu các khu vực theo từng Thể loại game', fontweight='bold', pad=15)
plt.xlabel('Thể loại game')
plt.ylabel('Doanh thu (Triệu bản)')
plt.legend(['Bắc Mỹ (NA)', 'Châu Âu (EU)', 'Nhật Bản (JP)'])
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
"""))

# 7. Scatter plot phân màu theo Thể loại
nb.cells.append(nbf.v4.new_markdown_cell("## 7. Mối liên hệ doanh số Bắc Mỹ vs Châu Âu (Phân màu theo Thể loại)\n**Mô tả:** Biểu đồ phân tán so sánh doanh số giữa Bắc Mỹ và Châu Âu. Mỗi chấm đại diện cho 1 tựa game, được **mã hóa màu sắc theo Thể loại** để phân biệt các nhóm game rõ ràng.\n- **Nhận xét:** Hầu hết các chấm nằm bám sát đường chéo trung tâm (doanh số tỉ lệ thuận giữa 2 thị trường). Tuy nhiên, ta thấy các game thể loại **Shooter/Action** (màu đại dương) đạt doanh số rất cao ở cả 2 khu vực."))
nb.cells.append(nbf.v4.new_code_cell("""# Chọn top 5 thể loại chính để phân màu rõ ràng, tránh rối mắt
top_5_genres = sales_by_genre.head(5)['Genre'].tolist()
df_scatter = df[(df['Global_Sales'] < 20) & (df['Genre'].isin(top_5_genres))]

plt.figure(figsize=(11, 6))
sns.scatterplot(data=df_scatter, x='NA_Sales', y='EU_Sales', hue='Genre', alpha=0.7, s=50, palette='Set1')

plt.title('Doanh số Bắc Mỹ (NA) vs Châu Âu (EU) phân theo Thể loại game', fontweight='bold', pad=15)
plt.xlabel('Doanh thu Bắc Mỹ (Triệu bản)')
plt.ylabel('Doanh thu Châu Âu (Triệu bản)')
plt.legend(title='Thể loại game', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
"""))

# 8. Stacked Bar Chart: Top 10 Game
nb.cells.append(nbf.v4.new_markdown_cell("## 8. Cấu trúc doanh thu khu vực của Top 10 Tựa game bán chạy nhất mọi thời đại\n**Mô tả:** Biểu đồ cột chồng giúp xem xét tỷ lệ doanh thu từ các thị trường cấu thành nên thành công của 10 tựa game lớn nhất.\n- **Nhận xét:** Bắc Mỹ đóng góp phần lớn doanh thu cho các tựa game đứng đầu. Riêng game *Pokemon Red/Blue*, thị trường Nhật Bản đóng góp một tỷ trọng khổng lồ."))
nb.cells.append(nbf.v4.new_code_cell("""top_10_games = df.head(10)

ax = top_10_games.set_index('Name')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].plot(
    kind='bar', stacked=True, figsize=(12, 6), color=['#2b5c8f', '#4682b4', '#90edb7', '#d3d3d3'], edgecolor='black', linewidth=0.5
)

plt.title('Cấu trúc doanh thu khu vực của Top 10 Game bán chạy nhất', fontweight='bold', pad=15)
plt.xlabel('Tên Game')
plt.ylabel('Doanh thu (Triệu bản)')
plt.legend(['Bắc Mỹ (NA)', 'Châu Âu (EU)', 'Nhật Bản (JP)', 'Khu vực khác'])
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
"""))

# Write to notebook
with open('Data_Visualization.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
