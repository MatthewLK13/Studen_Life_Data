import nbformat as nbf

nb = nbf.v4.new_notebook()

# Markdown cell - Title
nb.cells.append(nbf.v4.new_markdown_cell("# Video Game Sales - Phân Tích & Trực Quan Hóa Dữ Liệu\n\nPhân tích và trực quan hóa dữ liệu từ tập dữ liệu `vgsales-clean.csv` sau quá trình làm sạch."))

# Code cell - Import libraries
nb.cells.append(nbf.v4.new_code_cell("import pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n\n# Thiết lập style cho biểu đồ\nsns.set_theme(style='whitegrid')\nplt.rcParams['figure.figsize'] = (10, 6)"))

# Code cell - Load data
nb.cells.append(nbf.v4.new_code_cell("df = pd.read_csv('vgsales-clean.csv')\ndisplay(df.head())"))

# Chart 1: Doanh thu toàn cầu theo năm
nb.cells.append(nbf.v4.new_markdown_cell("## 1. Xu hướng doanh thu toàn cầu theo năm\n**Mô tả phân tích:** Biểu đồ đường dưới đây thể hiện tổng doanh thu game toàn cầu qua các năm. \n- **Xu hướng chung:** Ngành công nghiệp game bắt đầu phát triển mạnh mẽ từ giữa những năm 90 và chứng kiến sự tăng trưởng bùng nổ, đạt đỉnh vào khoảng thời kỳ 2008-2009. \n- **Nguyên nhân:** Đây là giai đoạn hoàng kim của các hệ máy console cực kỳ phổ biến như Nintendo Wii, Xbox 360 và PS3. \n- **Sự sụt giảm:** Kể từ sau 2010, doanh thu đĩa vật lý có xu hướng giảm dần (rất có thể là sự chuyển dịch của thị trường sang mô hình mua game trực tuyến digital hoặc game trên điện thoại di động - điều mà bộ dữ liệu này không bao quát hết)."))
nb.cells.append(nbf.v4.new_code_cell("sales_by_year = df.groupby('Year')['Global_Sales'].sum().reset_index()\n\nplt.figure(figsize=(14, 6))\nsns.lineplot(data=sales_by_year, x='Year', y='Global_Sales', marker='o', color='b', linewidth=2)\nplt.title('Xu hướng tổng doanh thu toàn cầu theo năm', fontsize=16, fontweight='bold')\nplt.xlabel('Năm phát hành', fontsize=12)\nplt.ylabel('Tổng doanh thu toàn cầu (Triệu bản)', fontsize=12)\nplt.xticks(rotation=45)\nplt.show()"))

# Chart 2: Tỉ trọng doanh thu theo các khu vực
nb.cells.append(nbf.v4.new_markdown_cell("## 2. Thị phần doanh thu của các khu vực trên toàn thế giới\n**Mô tả phân tích:** Biểu đồ tròn cho thấy mức độ đóng góp của các thị trường khác nhau vào tổng doanh thu toàn cầu.\n- **Khu vực thống trị:** Thị trường Bắc Mỹ (NA) là thị trường lớn nhất một cách rõ rệt, chiếm đến gần 50% tổng doanh số bán game toàn cầu. \n- **Các thị trường khác:** Tiếp theo là Châu Âu (EU) chiếm hơn 27% và Nhật Bản (JP) chiếm gần 15%. \n- **Kết luận:** Điều này cho thấy nếu một tựa game muốn đạt được doanh thu bùng nổ, việc nhắm tới thị hiếu của game thủ thị trường Bắc Mỹ và Châu Âu là đặc biệt quan trọng."))
nb.cells.append(nbf.v4.new_code_cell("sales_by_region = [df['NA_Sales'].sum(), df['EU_Sales'].sum(), df['JP_Sales'].sum(), df['Other_Sales'].sum()]\nlabels = ['Bắc Mỹ (NA)', 'Châu Âu (EU)', 'Nhật Bản (JP)', 'Khu vực Khác']\ncolors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']\n\nplt.figure(figsize=(8, 8))\nplt.pie(sales_by_region, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, shadow=True, wedgeprops={'edgecolor': 'black'})\nplt.title('Tỉ trọng doanh thu video game theo từng khu vực', fontsize=16, fontweight='bold')\nplt.show()"))

# Chart 3: Top 10 Thể loại game bán chạy nhất
nb.cells.append(nbf.v4.new_markdown_cell("## 3. Top 10 Thể loại game (Genre) bán chạy nhất toàn cầu\n**Mô tả phân tích:** Biểu đồ cột ngang thống kê tổng doanh thu toàn cầu của từng thể loại game.\n- **Thể loại ăn khách nhất:** *Action (Hành động)*, *Sports (Thể thao)* và *Shooter (Bắn súng)* là 3 thể loại phổ biến nhất mang lại doanh thu khổng lồ. \n- **Đánh giá:** Thể loại hành động có lượng người chơi rất đông đảo do tính giải trí cao, cốt truyện cuốn hút. Thể loại thể thao và bắn súng thường là các dòng game có tính cạnh tranh cao (Esports, Multiplayer), được phát hành thường niên (như FIFA, Call of Duty) nên luôn đảm bảo mức doanh thu ổn định qua các năm."))
nb.cells.append(nbf.v4.new_code_cell("sales_by_genre = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()\n\nplt.figure(figsize=(12, 6))\nsns.barplot(data=sales_by_genre, x='Global_Sales', y='Genre', hue='Genre', legend=False, palette='viridis')\nplt.title('Top 10 thể loại game có doanh thu cao nhất', fontsize=16, fontweight='bold')\nplt.xlabel('Doanh thu toàn cầu (Triệu bản)', fontsize=12)\nplt.ylabel('Thể loại (Genre)', fontsize=12)\nplt.show()"))

# Chart 4: Top 10 Nhà phát hành (Publisher) thành công nhất
nb.cells.append(nbf.v4.new_markdown_cell("## 4. Top 10 Nhà phát hành (Publisher) quyền lực nhất\n**Mô tả phân tích:** Sự thống trị của các ông lớn trong ngành sản xuất và phát hành game.\n- **Sự vượt trội:** Nintendo chứng tỏ vị thế vô đối của mình, nắm giữ doanh số khủng khiếp và bỏ xa hoàn toàn các đối thủ. Nguyên nhân chính là do Nintendo sở hữu các tựa game độc quyền gắn liền với tuổi thơ như Mario, Pokemon, Zelda cùng với các hệ máy console riêng của họ.\n- **Nhóm bám đuổi:** Electronic Arts (EA - nổi tiếng với dòng game FIFA), Activision (Call of Duty) và Sony Computer Entertainment là những nhà phát hành xếp sau, đại diện cho những công ty thống trị ở dòng game thể thao và bắn súng AAA."))
nb.cells.append(nbf.v4.new_code_cell("sales_by_publisher = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()\n\nplt.figure(figsize=(12, 6))\nsns.barplot(data=sales_by_publisher, x='Global_Sales', y='Publisher', hue='Publisher', legend=False, palette='magma')\nplt.title('Top 10 Nhà phát hành có doanh thu cao nhất toàn cầu', fontsize=16, fontweight='bold')\nplt.xlabel('Doanh thu toàn cầu (Triệu bản)', fontsize=12)\nplt.ylabel('Nhà phát hành (Publisher)', fontsize=12)\nplt.show()"))

# Chart 5: Top 10 Hệ máy (Platform) phổ biến nhất
nb.cells.append(nbf.v4.new_markdown_cell("## 5. Top 10 Hệ máy (Platform) thống trị thị trường\n**Mô tả phân tích:** Biểu đồ cột này thể hiện doanh thu toàn cầu phân bổ theo các nền tảng máy chơi game.\n- **Ngai vàng console:** PS2 (PlayStation 2) là nền tảng dẫn đầu về doanh số bán game vật lý. Điều này không có gì ngạc nhiên vì PS2 được mệnh danh là hệ máy console bán chạy nhất lịch sử.\n- **Cuộc chiến đa nền tảng:** Tiếp theo là Xbox 360 (X360) và PS3 - thế hệ console cạnh tranh khốc liệt nhất mang lại doanh thu cực kỳ cao. Wii và DS của Nintendo bám ngay sát sau nhờ chiến lược tập trung vào lối chơi gia đình và cầm tay giải trí."))
nb.cells.append(nbf.v4.new_code_cell("sales_by_platform = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10).reset_index()\n\nplt.figure(figsize=(12, 6))\nsns.barplot(data=sales_by_platform, x='Global_Sales', y='Platform', hue='Platform', legend=False, palette='coolwarm')\nplt.title('Top 10 Nền tảng (Platform) mang lại doanh thu cao nhất', fontsize=16, fontweight='bold')\nplt.xlabel('Doanh thu toàn cầu (Triệu bản)', fontsize=12)\nplt.ylabel('Hệ máy (Platform)', fontsize=12)\nplt.show()"))


with open('Data_Visualization.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
