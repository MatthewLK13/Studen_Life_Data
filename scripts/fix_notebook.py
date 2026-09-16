import nbformat as nbf

# Read notebook
with open('Data_Visualization.ipynb', 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

for cell in nb.cells:
    if cell['cell_type'] == 'code':
        # Fix Heatmap vmin
        if "sns.heatmap" in cell['source']:
            cell['source'] = cell['source'].replace('vmin=0', 'vmin=-1')
        
        # Fix Pairplot blank figure
        if "sns.pairplot" in cell['source']:
            lines = cell['source'].split('\n')
            new_lines = [line for line in lines if "plt.figure" not in line]
            cell['source'] = '\n'.join(new_lines)

# Write notebook
with open('Data_Visualization.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
