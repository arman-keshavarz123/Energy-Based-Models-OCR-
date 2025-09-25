import json
import nbformat

# Read the notebook
with open('/Users/shinobi/Downloads/NYU/DL/HW4/energy_based_models.ipynb', 'r') as f:
    nb = nbformat.read(f, as_version=4)

# Remove widget metadata from all cells
for cell in nb.cells:
    if 'metadata' in cell and 'widgets' in cell['metadata']:
        del cell['metadata']['widgets']

# Write the cleaned notebook
with open('/Users/shinobi/Downloads/NYU/DL/HW4/energy_based_models.ipynb', 'w') as f:
    nbformat.write(nb, f)

print("Notebook cleaned successfully!")