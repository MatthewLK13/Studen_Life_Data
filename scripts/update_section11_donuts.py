import nbformat as nbf

# Read notebook
with open('Data_Visualization.ipynb', 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Find Section 11 cell and update ONLY this cell with Donut Subplots layout
for i, cell in enumerate(nb.cells):
    if cell['cell_type'] == 'code' and "platform_genre" in cell['source']:
        cell['source'] = """top5_platforms = sales_by_platform.head(5)['Platform'].tolist()
top6_genres = sales_by_genre.head(6)['Genre'].tolist()

fig, axes = plt.subplots(2, 3, figsize=(15, 9.5))
axes = axes.flatten()

# Bảng màu nhất quán cho các thể loại trên tất cả biểu đồ
palette_genres = sns.color_palette("Set2", len(top6_genres))
genre_colors = {g: palette_genres[i] for i, g in enumerate(top6_genres)}
genre_colors['Khác'] = '#cbd5e1'

for idx, platform in enumerate(top5_platforms):
    df_p = df[df['Platform'] == platform].copy()
    df_p['Genre_Group'] = df_p['Genre'].apply(lambda x: x if x in top6_genres else 'Khác')
    p_genre_sales = df_p.groupby('Genre_Group')['Global_Sales'].sum()
    
    ordered_labels = [g for g in top6_genres if g in p_genre_sales.index] + (['Khác'] if 'Khác' in p_genre_sales.index else [])
    p_values = [p_genre_sales[g] for g in ordered_labels]
    p_colors = [genre_colors[g] for g in ordered_labels]
    
    ax = axes[idx]
    ax.pie(p_values, labels=ordered_labels, colors=p_colors, autopct='%1.0f%%', startangle=140,
           pctdistance=0.75, wedgeprops={'edgecolor': 'white', 'linewidth': 1.5, 'width': 0.45},
           textprops={'fontsize': 9.5})
    ax.set_title(f'Hệ máy: {platform}', fontweight='bold', fontsize=12, pad=10)

# Tắt subplot thứ 6 dư thừa
axes[5].axis('off')

plt.suptitle('Cơ cấu Thể loại game trên từng Hệ máy trong Top 5 (Donut Charts)', fontweight='bold', fontsize=15, y=0.98)
plt.tight_layout()
plt.show()"""

# Write notebook back safely
with open('Data_Visualization.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Section 11 updated to Donut Subplots layout while preserving all other cells!")
