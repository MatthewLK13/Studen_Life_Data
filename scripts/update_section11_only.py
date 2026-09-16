import nbformat as nbf

# Read notebook
with open('Data_Visualization.ipynb', 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Find Section 11 cell and update ONLY this cell
for i, cell in enumerate(nb.cells):
    if cell['cell_type'] == 'code' and "platform_genre_pct" in cell['source']:
        cell['source'] = """top5_platforms = sales_by_platform.head(5)['Platform'].tolist()
df_top_p = df[df['Platform'].isin(top5_platforms)].copy()

top6_genres = sales_by_genre.head(6)['Genre'].tolist()
df_top_p['Genre_Group'] = df_top_p['Genre'].apply(lambda x: x if x in top6_genres else 'Khác')

# Sử dụng Doanh thu thực tế (Triệu bản) thay vì ép về 100% để thấy được quy mô thực của từng hệ máy
platform_genre = df_top_p.groupby(['Platform', 'Genre_Group'])['Global_Sales'].sum().unstack()

ax = platform_genre.loc[top5_platforms].plot(
    kind='bar', stacked=True, figsize=(12, 6), colormap='Set3', edgecolor='white', linewidth=1
)
plt.title('Cơ cấu Doanh thu Thể loại game trên Top 5 Hệ máy bán chạy nhất')
plt.xlabel('Hệ máy (Platform)')
plt.ylabel('Doanh thu (Triệu bản)')
plt.legend(title='Thể loại', bbox_to_anchor=(1.02, 1), loc='upper left', frameon=True, facecolor='white')
plt.xticks(rotation=0)
sns.despine(top=True, right=True)
plt.tight_layout()
plt.show()"""

# Write notebook back safely
with open('Data_Visualization.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Section 11 updated to absolute sales stacked bar chart while preserving all other cells!")
