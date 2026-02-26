import glob
import re

# Classes to rename in REGIONAL pages and shared.css
# Old name -> New name
renames = {
    'indikator-card': 'detail-card',
    'indikator-wrapper': 'detail-wrapper',
    'indikator-chart': 'detail-chart',
    'indikator-desc': 'detail-desc',
    'indikator-info-header': 'detail-info-header',
    'indikator-info-text': 'detail-info-text',
    'indikator-info': 'detail-info',
    'indikator-insight': 'detail-insight',
    'indikator-top': 'detail-top',
    'indikator-triwulanan': 'detail-triwulanan',
}

# Sort by longest key first to avoid partial matches
# e.g. indikator-info-header before indikator-info
sorted_renames = sorted(renames.items(), key=lambda x: -len(x[0]))

# 1. Update regional HTML files (NOT landingpage.html)
regional_files = [
    'karimun.html', 'bintan.html', 'natuna.html', 'lingga.html',
    'anambas.html', 'batam.html', 'tanjungpinang.html'
]

for f in regional_files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    for old, new in sorted_renames:
        content = content.replace(old, new)
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(content)
    print(f"Renamed classes in {f}")

# 2. Update shared.css - rename the class definitions
with open('assets/css/shared.css', 'r', encoding='utf-8') as f:
    css = f.read()

for old, new in sorted_renames:
    css = css.replace(old, new)

with open('assets/css/shared.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Renamed classes in shared.css")

# 3. Now merge landingpage.css INTO shared.css
# We need to append the landing page specific styles to shared.css
# But first, let's identify which styles in landingpage.css are NOT already in shared.css
# Since they share .style-* classes, the shared ones are already there.
# We only need to append landing-page-specific classes:
# .indikator-container, .indikator-card (landing version), .indikator-icon,
# .indikator-title, .indikator-value, .indikator-date
with open('assets/css/landingpage.css', 'r', encoding='utf-8') as f:
    lp_css = f.read()

# Extract landing-page-specific indicator CSS blocks
# Find all CSS rules that contain 'indikator-' in landingpage.css
lp_blocks = []
# Use regex to find all blocks with indikator- classes
pattern = r'(\s*\.indikator-[^{]*\{[^}]*\})'
matches = re.findall(pattern, lp_css)
for m in matches:
    lp_blocks.append(m.strip())

if lp_blocks:
    with open('assets/css/shared.css', 'a', encoding='utf-8') as f:
        f.write('\n\n/* ===== LANDING PAGE INDICATOR STYLES ===== */\n')
        for block in lp_blocks:
            f.write('\n' + block + '\n')
    print(f"Appended {len(lp_blocks)} landing page indicator blocks to shared.css")

# 4. Update landingpage.html to use shared.css
with open('landingpage.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('assets/css/landingpage.css', 'assets/css/shared.css')

with open('landingpage.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated landingpage.html -> shared.css")

print("Done!")
