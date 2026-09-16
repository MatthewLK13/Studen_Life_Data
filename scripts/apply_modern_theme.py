import nbformat as nbf

nb = nbf.v4.new_notebook()

# Title
nb.cells.append(nbf.v4.new_markdown_cell("# Video Game Sales - Báo Cáo Trực Quan Hóa (Giao Diện Modern & High-Tech UI)\n\nBáo cáo trực quan hóa dữ liệu từ `vgsales-clean.csv` với phong cách thiết kế **hiện đại (Modern Design)**, bảng màu Indigo / Slate theo xu hướng Dashboard mới nhất, đường nét tối giản và góc nhìn phân tích dữ liệu chuyên sâu."))

# Pip install
nb.cells.append(nbf.v4.new_code_cell("# Cài đặt thư viện nếu cần\n!pip install -q seaborn matplotlib pandas"))

# Config Modern Style
nb.cells.append(nbf.v4.new_code_cell("""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# THIẾT LẬP GIAO DIỆN HIỆN ĐẠI (MODERN UI STYLE)
sns.set_theme(style='whitegrid', font='sans-serif')
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.titlepad'] = 15
plt.rcParams['axes.edgecolor'] = '#e2e8f0'
plt.rcParams['grid.color'] = '#f1f5f9'
plt.rcParams['grid.linestyle'] = '--'

# BẢNG MÀU HIỆN ĐẠI (TAILWIND / MODERN DASHBOARD PALETTE)
COLOR_MAIN = '#6366f1'     # Electric Indigo / Violet (Chủ đạo)
COLOR_NA = '#4f46e5'       # Deep Indigo (Bắc Mỹ)
COLOR_EU = '#f97316'       # Modern Coral / Vibrant Orange (Châu Âu)
COLOR_JP = '#10b981'       # Emerald Green (Nhật Bản)
COLOR_OTHER = '#94a3b8'    # Slate Muted Gray (Khác)

PALETTE_REGIONS = [COLOR_NA, COLOR_EU, COLOR_JP, COLOR_OTHER]
"""))

# Load data
nb.cells.append(nbf.v4.new_code_cell("df = pd.read_csv('vgsales-clean.csv')\ndisplay(df.head())"))

# --- PHẦN 1: BỨC TRANH TỔNG QUAN ---

# 1. Line Chart: Doanh thu theo năm
nb.cells.append(nbf.v4.new_markdown_cell("## 1. Xu hướng doanh thu toàn cầu theo năm\n**Mô tả:** Biểu đồ đường thể hiện tổng doanh thu bán đĩa game theo thời gian.\n- **Nhận xét:** Thị trường game bùng nổ mạnh mẽ từ năm 1995 và đạt đỉnh vào giai đoạn **2008 - 2009** (thời kỳ của PS3, Xbox 360, Nintendo Wii). Sau đó doanh thu đĩa vật lý giảm dần."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_year = df.groupby('Year')['Global_Sales'].sum().reset_index()

plt.figure(figsize=(12, 5))
ax = sns.lineplot(data=sales_by_year, x='Year', y='Global_Sales', color=COLOR_MAIN, linewidth=3)
plt.fill_between(sales_by_year['Year'], sales_by_year['Global_Sales'], color=COLOR_MAIN, alpha=0.1)
plt.title('Xu hướng doanh thu đĩa game toàn cầu qua các năm')
plt.xlabel('Năm phát hành')
plt.ylabel('Doanh thu (Triệu bản)')
sns.despine(top=True, right=True)
plt.tight_layout()
plt.show()
"""))

# 2. Pie Chart: Tỉ trọng doanh thu các khu vực
nb.cells.append(nbf.v4.new_markdown_cell("## 2. Tỉ trọng doanh thu theo từng khu vực\n**Mô tả:** Biểu đồ tròn phong cách Donut hiện đại thể hiện mức độ đóng góp của từng thị trường.\n- **Nhận xét:** **Bắc Mỹ (NA)** chiếm **48.6%** (Indigo) và **Châu Âu (EU)** chiếm **27.3%** (Coral Orange). Đây là 2 thị trường tiêu thụ đĩa game lớn nhất thế giới."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_region = [df['NA_Sales'].sum(), df['EU_Sales'].sum(), df['JP_Sales'].sum(), df['Other_Sales'].sum()]
labels = ['Bắc Mỹ (NA)', 'Châu Âu (EU)', 'Nhật Bản (JP)', 'Khu vực khác']

plt.figure(figsize=(7, 7))
# Donut chart hiện đại
plt.pie(sales_by_region, labels=labels, colors=PALETTE_REGIONS, autopct='%1.1f%%', startangle=140, 
        pctdistance=0.75, wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'width': 0.5})
plt.title('Tỉ trọng doanh thu bán game theo khu vực')
plt.tight_layout()
plt.show()
"""))

# 3. Bar Chart: Top 10 Genre
nb.cells.append(nbf.v4.new_markdown_cell("## 3. Top 10 Thể loại game (Genre) bán chạy nhất (Tổng doanh thu)\n**Mô tả:** Thống kê tổng doanh thu theo thể loại game.\n- **Nhận xét:** **Action (Hành động)** và **Sports (Thể thao)** là hai thể loại áp đảo về tổng doanh số."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_genre = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 5))
ax = sns.barplot(data=sales_by_genre, x='Global_Sales', y='Genre', color=COLOR_MAIN, alpha=0.9)
plt.title('Top 10 thể loại game có tổng doanh thu cao nhất')
plt.xlabel('Tổng doanh thu toàn cầu (Triệu bản)')
plt.ylabel('Thể loại')

for p in ax.patches:
    width = p.get_width()
    ax.annotate(f'{width:.1f}', (width + 15, p.get_y() + p.get_height() / 2),
                ha='left', va='center', fontsize=10, fontweight='bold', color='#334155')

sns.despine(top=True, right=True)
plt.tight_layout()
plt.show()
"""))

# 4. Bar Chart: Top 10 Publisher
nb.cells.append(nbf.v4.new_markdown_cell("## 4. Top 10 Nhà phát hành (Publisher) có tổng doanh thu cao nhất\n**Mô tả:** Xếp hạng các hãng phát hành game lớn nhất thế giới theo tổng doanh số.\n- **Nhận xét:** **Nintendo** giữ vị trí số 1 tuyệt đối với hơn 1780 triệu bản."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_publisher = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 5))
ax = sns.barplot(data=sales_by_publisher, x='Global_Sales', y='Publisher', color=COLOR_MAIN, alpha=0.9)
plt.title('Top 10 Nhà phát hành game có tổng doanh thu cao nhất')
plt.xlabel('Tổng doanh thu toàn cầu (Triệu bản)')
plt.ylabel('Nhà phát hành')

for p in ax.patches:
    width = p.get_width()
    ax.annotate(f'{width:.1f}', (width + 20, p.get_y() + p.get_height() / 2),
                ha='left', va='center', fontsize=10, fontweight='bold', color='#334155')

sns.despine(top=True, right=True)
plt.tight_layout()
plt.show()
"""))

# 5. Bar Chart: Top 10 Platform
nb.cells.append(nbf.v4.new_markdown_cell("## 5. Top 10 Hệ máy (Platform) phổ biến nhất\n**Mô tả:** Thống kê doanh thu đĩa game theo từng hệ máy.\n- **Nhận xét:** **PS2** và **X360** là hai hệ máy dẫn đầu về lượng tiêu thụ đĩa game."))
nb.cells.append(nbf.v4.new_code_cell("""sales_by_platform = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 5))
ax = sns.barplot(data=sales_by_platform, x='Global_Sales', y='Platform', color=COLOR_MAIN, alpha=0.9)
plt.title('Top 10 Hệ máy mang lại doanh thu đĩa game cao nhất')
plt.xlabel('Doanh thu toàn cầu (Triệu bản)')
plt.ylabel('Hệ máy (Platform)')

for p in ax.patches:
    width = p.get_width()
    ax.annotate(f'{width:.1f}', (width + 15, p.get_y() + p.get_height() / 2),
                ha='left', va='center', fontsize=10, fontweight='bold', color='#334155')

sns.despine(top=True, right=True)
plt.tight_layout()
plt.show()
"""))

# 6. Grouped Bar: NA vs EU Thể loại (Modern Palette)
nb.cells.append(nbf.v4.new_markdown_cell("## 6. So sánh trực tiếp doanh số Bắc Mỹ (NA) vs Châu Âu (EU) theo Thể loại\n**Mô tả:** So sánh thị hiếu giữa Bắc Mỹ (Indigo) và Châu Âu (Modern Orange).\n- **Nhận xét:** Bắc Mỹ áp đảo Châu Âu ở tất cả các thể loại, nhưng cơ cấu tỷ lệ chênh lệch rất tương đồng."))
nb.cells.append(nbf.v4.new_code_cell("""top_genres = sales_by_genre.head(6)['Genre'].tolist()
df_top_g = df[df['Genre'].isin(top_genres)]

na_vs_eu_genre = df_top_g.groupby('Genre')[['NA_Sales', 'EU_Sales']].sum().loc[top_genres]

ax = na_vs_eu_genre.plot(kind='bar', figsize=(11, 5.5), width=0.7, color=[COLOR_NA, COLOR_EU], edgecolor='none')
plt.title('So sánh doanh thu Bắc Mỹ (NA) vs Châu Âu (EU) theo Thể loại game')
plt.xlabel('Thể loại game')
plt.ylabel('Doanh thu (Triệu bản)')
plt.legend(['Bắc Mỹ (NA)', 'Châu Âu (EU)'], frameon=True, facecolor='white', edgecolor='none')
plt.xticks(rotation=0)
sns.despine(top=True, right=True)
plt.tight_layout()
plt.show()
"""))

# 7. Grouped Bar: NA vs EU Top 10 Game
nb.cells.append(nbf.v4.new_markdown_cell("## 7. So sánh trực tiếp doanh số Bắc Mỹ (NA) vs Châu Âu (EU) ở Top 10 Game\n**Mô tả:** So sánh doanh số bán đĩa ở 2 thị trường lớn của 10 tựa game lớn nhất.\n- **Nhận xét:** Riêng *Mario Kart Wii*, doanh thu ở Châu Âu tiệm cận rất sát với Bắc Mỹ."))
nb.cells.append(nbf.v4.new_code_cell("""top_10_games = df.head(10)

ax = top_10_games.set_index('Name')[['NA_Sales', 'EU_Sales']].plot(
    kind='bar', figsize=(12, 5.5), width=0.7, color=[COLOR_NA, COLOR_EU], edgecolor='none'
)

plt.title('So sánh doanh thu Bắc Mỹ (NA) vs Châu Âu (EU) của Top 10 Game bán chạy nhất')
plt.xlabel('Tên Game')
plt.ylabel('Doanh thu (Triệu bản)')
plt.legend(['Bắc Mỹ (NA)', 'Châu Âu (EU)'], frameon=True, facecolor='white', edgecolor='none')
plt.xticks(rotation=45, ha='right')
sns.despine(top=True, right=True)
plt.tight_layout()
plt.show()
"""))

# 8. Stacked Bar: Cấu trúc 4 khu vực Top 10 Game
nb.cells.append(nbf.v4.new_markdown_cell("## 8. Cấu trúc doanh thu đầy đủ theo 4 khu vực của Top 10 Game\n**Mô tả:** Xem xét tỷ lệ đóng góp của cả 4 khu vực vào doanh số của 10 siêu phẩm.\n- **Nhận xét:** *Pokemon Red/Blue* có đóng góp từ Nhật Bản (Emerald Green) cực kỳ ấn tượng."))
nb.cells.append(nbf.v4.new_code_cell("""ax = top_10_games.set_index('Name')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].plot(
    kind='bar', stacked=True, figsize=(12, 6), color=PALETTE_REGIONS, edgecolor='white', linewidth=1
)

plt.title('Cấu trúc doanh thu khu vực đầy đủ của Top 10 Game bán chạy nhất')
plt.xlabel('Tên Game')
plt.ylabel('Doanh thu (Triệu bản)')
plt.legend(['Bắc Mỹ (NA)', 'Châu Âu (EU)', 'Nhật Bản (JP)', 'Khu vực khác'], frameon=True, facecolor='white', edgecolor='none')
plt.xticks(rotation=45, ha='right')
sns.despine(top=True, right=True)
plt.tight_layout()
plt.show()
"""))

# --- PHẦN 2: PHÂN TÍCH CHUYÊN SÂU (ADVANCED INSIGHTS) ---

# 9. Top 10 Publisher theo Doanh thu Trung bình / Game
nb.cells.append(nbf.v4.new_markdown_cell("## 9. Phân tích Chuyên sâu 1: Top 10 Nhà phát hành có Hiệu suất Trung bình / Game cao nhất\n*(Điều kiện lọc: Đã phát hành tối thiểu 20 tựa game)*\n\n**Mô tả:** Đo lường **Doanh thu Trung bình trên mỗi đầu game** phát hành.\n- **Nhận xét bất ngờ:** **Take-Two Interactive** (hãng mẹ của Rockstar Games với dòng *GTA*) vọt lên vị trí số 2 với **1.56 triệu bản / game**, chứng minh chiến lược \"ít nhưng chất\" cực kỳ hiệu quả."))
nb.cells.append(nbf.v4.new_code_cell("""pub_stats = df.groupby('Publisher').agg(
    Total_Games=('Name', 'count'),
    Avg_Sales=('Global_Sales', 'mean'),
    Total_Sales=('Global_Sales', 'sum')
).reset_index()

top_avg_pub = pub_stats[pub_stats['Total_Games'] >= 20].sort_values('Avg_Sales', ascending=False).head(10)

plt.figure(figsize=(10, 5))
ax = sns.barplot(data=top_avg_pub, x='Avg_Sales', y='Publisher', color=COLOR_JP, alpha=0.9)
plt.title('Top 10 Nhà phát hành có Doanh thu Trung bình / Game cao nhất (>= 20 Game)')
plt.xlabel('Doanh thu trung bình trên mỗi tựa game (Triệu bản)')
plt.ylabel('Nhà phát hành')

for p in ax.patches:
    width = p.get_width()
    ax.annotate(f'{width:.2f}', (width + 0.05, p.get_y() + p.get_height() / 2),
                ha='left', va='center', fontsize=10, fontweight='bold', color='#334155')

sns.despine(top=True, right=True)
plt.tight_layout()
plt.show()
"""))

# 10. Sự chuyển dịch Thể loại game qua các Thập niên
nb.cells.append(nbf.v4.new_markdown_cell("## 10. Phân tích Chuyên sâu 2: Sự chuyển dịch Thể loại game qua các Thập niên (80s, 90s, 2000s, 2010s)\n**Mô tả:** Biểu đồ thể hiện sự thay đổi thị hiếu chơi game của thế giới qua 4 thập kỷ.\n- **Nhận xét:** Sự bùng nổ của **Action** và **Shooter** ở thập niên 2000s và 2010s."))
nb.cells.append(nbf.v4.new_code_cell("""def get_decade(year):
    if year < 1990: return '1980s'
    elif year < 2000: return '1990s'
    elif year < 2010: return '2000s'
    else: return '2010s'

df['Decade'] = df['Year'].apply(get_decade)

top5_g = sales_by_genre.head(5)['Genre'].tolist()
decade_genre = df[df['Genre'].isin(top5_g)].groupby(['Decade', 'Genre'])['Global_Sales'].sum().unstack()

# Modern palette for categories
ax = decade_genre.plot(kind='bar', figsize=(12, 6), width=0.8, colormap='Spectral', edgecolor='white')
plt.title('Sự chuyển dịch doanh thu của Top 5 Thể loại game qua các Thập niên')
plt.xlabel('Thập niên')
plt.ylabel('Tổng doanh thu (Triệu bản)')
plt.legend(title='Thể loại game', frameon=True, facecolor='white', edgecolor='none')
plt.xticks(rotation=0)
sns.despine(top=True, right=True)
plt.tight_layout()
plt.show()
"""))

# 11. Cơ cấu Thể loại game trên Top 5 Nền tảng
nb.cells.append(nbf.v4.new_markdown_cell("## 11. Phân tích Chuyên sâu 3: Cơ cấu Thể loại game trên Top 5 Hệ máy bán chạy nhất\n**Mô tả:** Biểu đồ tỷ lệ 100% (Stacked 100%) giải thích yếu tố giúp từng hệ máy thành công.\n- **Nhận xét:** Wii/DS mạnh về Misc/Sports/RPG; PS2/PS3/X360 áp đảo về Action/Shooter."))
nb.cells.append(nbf.v4.new_code_cell("""top5_platforms = sales_by_platform.head(5)['Platform'].tolist()
df_top_p = df[df['Platform'].isin(top5_platforms)].copy()

top6_genres = sales_by_genre.head(6)['Genre'].tolist()
df_top_p['Genre_Group'] = df_top_p['Genre'].apply(lambda x: x if x in top6_genres else 'Khác')

platform_genre = df_top_p.groupby(['Platform', 'Genre_Group'])['Global_Sales'].sum().unstack()
platform_genre_pct = platform_genre.div(platform_genre.sum(axis=1), axis=0) * 100

ax = platform_genre_pct.loc[top5_platforms].plot(
    kind='bar', stacked=True, figsize=(12, 6), colormap='Pastel1', edgecolor='white', linewidth=1
)
plt.title('Tỉ trọng cơ cấu Thể loại game trên Top 5 Hệ máy bán chạy nhất (%)')
plt.xlabel('Hệ máy (Platform)')
plt.ylabel('Tỉ lệ đóng góp (%)')
plt.legend(title='Thể loại', bbox_to_anchor=(1.02, 1), loc='upper left', frameon=True, facecolor='white')
plt.xticks(rotation=0)
sns.despine(top=True, right=True)
plt.tight_layout()
plt.show()
"""))

# 12. Biểu đồ Scatter Plot: Ma trận Chiến lược Nhà phát hành (Modern High-Tech Style)
nb.cells.append(nbf.v4.new_markdown_cell("## 12. Phân tích Chuyên sâu 4 (Scatter Plot): Ma trận Chiến lược của các Nhà phát hành Game\n**Mô tả:** Biểu đồ phân tán (Scatter Plot) thiết kế hiện đại ứng dụng phân tích **Số lượng Game phát hành (X)** và **Doanh thu Trung bình / Game (Y)**.\n\n4 Ô Chiến lược chia bởi đường ranh giới trung vị:\n1. **Góc Trái - Trên (Chất lượng cao / Ít game):** **Take-Two (Rockstar)** & **Bethesda**.\n2. **Góc Phải - Trên (Thống trị):** **Nintendo**.\n3. **Góc Phải - Dưới (Sản xuất công nghiệp):** **EA, Ubisoft, Activision, Namco**.\n4. **Góc Trái - Dưới (Quy mô nhỏ):** Các hãng nhỏ hơn."))
nb.cells.append(nbf.v4.new_code_cell("""pub_scatter_data = pub_stats[pub_stats['Total_Games'] >= 25]

plt.figure(figsize=(13, 7))

sns.scatterplot(
    data=pub_scatter_data, 
    x='Total_Games', 
    y='Avg_Sales', 
    size='Total_Sales', 
    sizes=(80, 700), 
    color=COLOR_MAIN, 
    alpha=0.6, 
    edgecolor='#4338ca',
    linewidth=1.5,
    legend=False
)

med_x = pub_scatter_data['Total_Games'].median()
med_y = pub_scatter_data['Avg_Sales'].median()

plt.axvline(med_x, color='#ef4444', linestyle='--', linewidth=1.5, alpha=0.8)
plt.axhline(med_y, color='#ef4444', linestyle='--', linewidth=1.5, alpha=0.8)

key_pubs = ['Nintendo', 'Electronic Arts', 'Activision', 'Ubisoft', 'Take-Two Interactive', 
            'Sony Computer Entertainment', 'Bethesda Softworks', 'Namco Bandai Games', 'Square Enix']

for _, row in pub_scatter_data.iterrows():
    if row['Publisher'] in key_pubs:
        plt.annotate(
            row['Publisher'], 
            (row['Total_Games'], row['Avg_Sales']),
            textcoords="offset points", 
            xytext=(6, 6), 
            ha='left', 
            fontsize=10, 
            fontweight='bold',
            color='#1e293b'
        )

plt.title('Ma trận Chiến lược Nhà phát hành: Số lượng Game vs Doanh thu Trung bình / Game')
plt.xlabel('Tổng số lượng tựa game đã phát hành (Số lượng)', fontsize=12)
plt.ylabel('Doanh thu Trung bình trên mỗi tựa game (Triệu bản)', fontsize=12)

plt.text(med_x * 0.2, pub_scatter_data['Avg_Sales'].max() * 0.9, 'CHẤT LƯỢNG CAO (Take-Two, Bethesda)', color='#059669', fontweight='bold')
plt.text(pub_scatter_data['Total_Games'].max() * 0.7, pub_scatter_data['Avg_Sales'].max() * 0.9, 'THỐNG TRỊ (Nintendo)', color='#1d4ed8', fontweight='bold')
plt.text(pub_scatter_data['Total_Games'].max() * 0.7, med_y * 0.3, 'SẢN XUẤT CÔNG NGHIỆP (EA, Ubisoft)', color='#dc2626', fontweight='bold')

sns.despine(top=True, right=True)
plt.tight_layout()
plt.show()
"""))

# Write directly to notebook file
with open('Data_Visualization.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Modern Theme Notebook generated successfully!")
