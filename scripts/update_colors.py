import nbformat as nbf

# Read notebook
with open('Data_Visualization.ipynb', 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Color scheme definition
# NA: Blue (#1f77b4), EU: Orange (#ff7f0e), JP: Green (#2ca02c), Other: Gray (#a6a6a6)
colors_code = "['#1f77b4', '#ff7f0e', '#2ca02c', '#a6a6a6']"

for cell in nb.cells:
    if cell['cell_type'] == 'code':
        # Pie chart colors
        if "plt.pie" in cell['source']:
            cell['source'] = cell['source'].replace(
                "colors = ['#2b5c8f', '#4682b4', '#90edb7', '#d3d3d3']",
                f"colors = {colors_code}"
            )
        
        # Grouped bar chart colors (NA, EU, JP)
        if "genre_region_sales.plot" in cell['source']:
            cell['source'] = cell['source'].replace(
                "color=['#2b5c8f', '#4682b4', '#90edb7']",
                "color=['#1f77b4', '#ff7f0e', '#2ca02c']"
            )
        
        # Stacked bar chart colors (NA, EU, JP, Other)
        if "kind='bar', stacked=True" in cell['source']:
            cell['source'] = cell['source'].replace(
                "color=['#2b5c8f', '#4682b4', '#90edb7', '#d3d3d3']",
                f"color={colors_code}"
            )

# Write back
with open('Data_Visualization.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
