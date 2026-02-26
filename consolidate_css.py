import glob
import re

# 1. Update shared.css - reduce nav font size from 14px to 13px in .style-13
with open('assets/css/shared.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find .style-13 and change font-size
css = re.sub(
    r'(\.style-13\s*\{[^}]*?font-size:)\s*14px;',
    r'\g<1> 13px;',
    css
)

with open('assets/css/shared.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("shared.css font updated.")

# 2. Update all regional HTML files to use shared.css instead of their own
html_files = glob.glob('*.html')
regional_css_files = [
    'karimun.css', 'bintan.css', 'natuna.css', 'lingga.css',
    'anambas.css', 'batam.css', 'tanjungpinang.css'
]

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    for css_name in regional_css_files:
        old_ref = f'assets/css/{css_name}'
        if old_ref in content:
            content = content.replace(old_ref, 'assets/css/shared.css')
            changed = True

    if changed:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {html_file} -> shared.css")
    else:
        print(f"Skipped {html_file} (no regional CSS ref found)")

print("Done.")
