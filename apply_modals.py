import re

REGIONS = {
    'karimun.html': ('karimun', 'Karimun'),
    'bintan.html': ('bintan', 'Bintan'),
    'natuna.html': ('natuna', 'Natuna'),
    'lingga.html': ('lingga', 'Lingga'),
    'anambas.html': ('kepulauan_anambas', 'Kepulauan Anambas'),
    'batam.html': ('batam', 'Batam'),
    'tanjungpinang.html': ('tanjungpinang', 'Tanjungpinang')
}

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract <div class="style-69"> block
style_69_match = re.search(r'<div class="style-69">.*?</div>\s*</div>\s*</div>', index_content, re.DOTALL)
if not style_69_match:
    print("Could not find style-69 block")
    exit(1)
style_69_block = style_69_match.group(0)

# Extract Modal + Scripts + end of file block
modal_end_match = re.search(r'<!-- MODAL -->.*</html>', index_content, re.DOTALL)
if not modal_end_match:
    print("Could not find modal and scripts block")
    exit(1)
modal_end_block = modal_end_match.group(0)

for filename, (data_key, region_name) in REGIONS.items():
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Find start of the old indicators
    start_match = re.search(r'(<!-- WRAPPER UNTUK INDIKATOR|<div class="detail-wrapper">)', content)
    if not start_match:
        print(f"Start indicator block not found in {filename}")
        continue
    
    start_idx = start_match.start()
    
    # Prefix until the start of indicators
    prefix = content[:start_idx]
    
    # Assemble new content
    new_content = prefix + "\n    " + style_69_block + "\n\n" + modal_end_block
    
    # Replace data_key for modal logic
    new_content = new_content.replace('wilayah.kepulauan_riau', f'wilayah.{data_key}')
    # Replace Region name for Modal titles
    new_content = new_content.replace('Kepulauan Riau', region_name)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully updated {filename}")
