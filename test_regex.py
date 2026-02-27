import re
with open('karimun.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<div class="indikator-container">.*?</div>\s*</div>\s*</div>\s*<div class="style', html, re.DOTALL)
print("Matched indikator-container:", bool(m))

m2 = re.search(r'<div class="detail-container">.*?</div>\s*</div>\s*</div>\s*<div class="style', html, re.DOTALL)
print("Matched detail-container:", bool(m2))

print("indikator-container in html:", "indikator-container" in html)
print("detail-container in html:", "detail-container" in html)
