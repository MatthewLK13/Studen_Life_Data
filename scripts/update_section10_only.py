import nbformat as nbf

# Read notebook
with open('Data_Visualization.ipynb', 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Find Section 10 cell and update ONLY this cell
for i, cell in enumerate(nb.cells):
    if cell['cell_type'] == 'code' and "decade_genre.plot" in cell['source']:
        cell['source'] = """def get_decade(year):
    if year < 1990: return '1980s'
    elif year < 2000: return '1990s'
    elif year < 2010: return '2000s'
    else: return '2010s'

df['Decade'] = df['Year'].apply(get_decade)

top5_g = sales_by_genre.head(5)['Genre'].tolist()
decade_genre = df[df['Genre'].isin(top5_g)].groupby(['Decade', 'Genre'])['Global_Sales'].sum().unstack()

# Chuyển sang Biểu đồ Đường (Line Chart) với marker các điểm thập niên
plt.figure(figsize=(12, 6))
ax = decade_genre.plot(kind='line', marker='o', linewidth=2.5, markersize=8, figsize=(12, 6), colormap='Set1')
plt.title('Sự chuyển dịch doanh thu của Top 5 Thể loại game qua các Thập niên')
plt.xlabel('Thập niên')
plt.ylabel('Tổng doanh thu (Triệu bản)')
plt.legend(title='Thể loại game', frameon=True, facecolor='white', edgecolor='none')
plt.xticks(rotation=0)
sns.despine(top=True, right=True)
plt.tight_layout()
plt.show()"""

# Write notebook back safely
with open('Data_Visualization.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Section 10 updated to Line Chart while preserving all other cells!")
