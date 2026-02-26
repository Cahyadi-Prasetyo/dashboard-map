import glob
import os

active_css = """
                .style-13.active {
                    background-color: #2563eb;
                    color: white !important;
                    border-radius: 6px;
                    padding: 6px 12px;
                }
"""

files = glob.glob("assets/css/*.css")

for file in files:
    if "karimun.css" in file:
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if ".style-13.active" not in content:
        content += "\n" + active_css
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added to {file}")
    else:
        print(f"Already in {file}")
