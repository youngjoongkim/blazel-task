"""
Add static image display to all notebooks (01-04 and 07)
This makes them viewable on GitHub
"""
import json
import os

notebooks = [
    'notebooks/01_data_cleaning.ipynb',
    'notebooks/02_exploratory_analysis.ipynb',
    'notebooks/03_statistical_analysis.ipynb',
    'notebooks/04_content_analysis.ipynb',
    'notebooks/07_final_report.ipynb'
]

total_modified = 0

for notebook_path in notebooks:
    if not os.path.exists(notebook_path):
        print(f"Skipping {notebook_path} - not found")
        continue

    print(f"\nProcessing {notebook_path}...")

    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    print(f"  Total cells: {len(nb['cells'])}")

    # Find all cells with fig.show() and modify them
    modified_count = 0

    for i, cell in enumerate(nb['cells']):
        if cell.get('cell_type') != 'code':
            continue

        source = ''.join(cell.get('source', []))

        # Check if this cell creates a Plotly figure
        if 'fig.show()' in source and 'plotly' in source.lower():
            lines = cell['source']

            # Check if already modified
            if 'pio.to_image' in source:
                continue

            # Replace fig.show() with both show() and static image display
            new_lines = []
            for line in lines:
                if 'fig.show()' in line:
                    # Add the line as-is first
                    new_lines.append(line)
                    # Then add static image display
                    new_lines.append("# Display static image for GitHub preview\n")
                    new_lines.append("from IPython.display import Image, display\n")
                    new_lines.append("import plotly.io as pio\n")
                    new_lines.append("try:\n")
                    new_lines.append("    img_bytes = pio.to_image(fig, format='png', width=1200, height=700)\n")
                    new_lines.append("    display(Image(img_bytes))\n")
                    new_lines.append("except Exception as e:\n")
                    new_lines.append("    print(f'Static image export requires kaleido: pip install kaleido')\n")
                else:
                    new_lines.append(line)

            if len(new_lines) > len(lines):
                cell['source'] = new_lines
                modified_count += 1

    if modified_count > 0:
        # Save the modified notebook
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)

        print(f"  Modified {modified_count} cells")
        total_modified += modified_count
    else:
        print(f"  No cells modified (already updated or no visualizations)")

print(f"\n{'='*70}")
print(f"SUMMARY: Modified {total_modified} cells across all notebooks")
print(f"{'='*70}")
print("\nNext steps:")
print("1. Install kaleido: pip install kaleido")
print("2. Re-run all visualization cells in the notebooks")
print("3. The static images will be embedded in the notebook outputs")
print("4. GitHub will display these images in the notebook preview")
