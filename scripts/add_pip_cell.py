import nbformat as nbf

# Read notebook
with open('Data_Visualization.ipynb', 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Create pip install cell
pip_cell = nbf.v4.new_code_cell("# Cài đặt các thư viện cần thiết nếu môi trường Jupyter chưa có\n!pip install -q seaborn matplotlib pandas")

# Insert at the beginning of notebook cells
nb.cells.insert(0, pip_cell)

# Write notebook
with open('Data_Visualization.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
