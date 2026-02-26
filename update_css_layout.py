import glob
import re

files = glob.glob("assets/css/*.css")

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Image width
    content = re.sub(
        r'(grid-template-columns:\s*minmax\()240px,\s*320px(\)\s*1fr;)',
        r'\g<1>280px, 360px\g<2>',
        content
    )
    # 2. Image height
    content = re.sub(
        r'(\.indikator-top\s*img\s*\{[^}]*?height:\s*)180px;',
        r'\g<1>220px;',
        content
    )
    # 3. Reduce gap by shrinking style-136 padding
    content = re.sub(
        r'(\.style-136\s*\{[^}]*?padding-bottom:)48px;',
        r'\g<1>16px;',
        content
    )
    # 4. Align text to top
    content = re.sub(
        r'(\.style-21\s*\{[^}]*?align-items:)center;',
        r'\g<1>flex-start;',
        content
    )
    content = re.sub(
        r'(\.style-24\s*\{[^}]*?margin-top:)100px;',
        r'\g<1>0px;',
        content
    )
    # 5. Bring definition text back to 13px
    # Note: we also have font-weight: bold; now, so we just match font-size: 14px;
    content = re.sub(
        r'(\.indikator-info-text\s*\{[^}]*?font-size:\s*)14px;',
        r'\g<1>13px;',
        content
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("CSS updated.")
