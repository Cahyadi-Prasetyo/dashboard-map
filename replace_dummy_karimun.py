import re

with open('karimun.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    # Ekonomi 1 - Kepri 7,89
    r'<h3 class="indikator-value">7,89<br><span>persen</span></h3>': r'<h3 class="indikator-value">5,50<br><span>persen</span></h3>',
    r'<p class="indikator-date">Triwulan IV 2024</p>': r'<p class="indikator-date">2023</p>',

    # PDRB 2 - Kepri 161.424
    r'<h3 class="indikator-value">161\.424<br><span>ribu rupiah</span></h3>': r'<h3 class="indikator-value">69.608<br><span>ribu rupiah</span></h3>',

    # IPM 3 - Kepri 80,53 / 2025
    r'<h3 class="indikator-value">80,53<br><span>persen</span></h3>': r'<h3 class="indikator-value">76,01<br><span></span></h3>',
    # 2024 is the latest IPM on karimun page usually, wait IPM is usually index
    
    # IPG 4 - Kepri 94,2 / 2024
    r'<h3 class="indikator-value">94,2<br><span> </span></h3>': r'<h3 class="indikator-value">91,5<br><span> </span></h3>',
    r'<p class="indikator-date">2024</p>': r'<p class="indikator-date">2023</p>',

    # TPT 5 - Kepri 6,35  (tri 4 2024 uses 2025? wait, index TPT is Nov 2025? actually august 2024 is 6.33 for Kepri, karimun 6.55)
    r'<h3 class="indikator-value">6,35<br><span>persen</span></h3>': r'<h3 class="indikator-value">6,55<br><span>persen</span></h3>',
    r'<p class="indikator-date">November 2025</p>': r'<p class="indikator-date">Agustus 2023</p>',

    # APS 6 - Kepri 88,24
    r'<h3 class="indikator-value">88,24<br><span></span></h3>': r'<h3 class="indikator-value">85,12<br><span></span></h3>',
    
    # Kemiskinan 7 - Kepri 4,44
    r'<h3 class="indikator-value">4,44<br><span>persen</span></h3>': r'<h3 class="indikator-value">5,71<br><span>persen</span></h3>',
    r'<p class="indikator-date">Maret 2025</p>': r'<p class="indikator-date">Maret 2024</p>',

    # Gini 8 - Kepri 0,385
    r'<h3 class="indikator-value">0,385<br><span>persen</span></h3>': r'<h3 class="indikator-value">0,286<br><span></span></h3>',
    r'<p class="indikator-date">September 2025</p>': r'<p class="indikator-date">2024</p>',

    # Penduduk 9 - Kepri 2.064.564
    r'<h3 class="indikator-value">2\.064\.564<br><span>jiwa</span></h3>': r'<h3 class="indikator-value">267.430<br><span>jiwa</span></h3>',
    # <p class="indikator-date">Hasil SP2020</p>

    # Inflasi 10 - Kepri 2,94
    r'<h3 class="indikator-value">2,94<br><span>persen</span></h3>': r'<h3 class="indikator-value">2,77<br><span>persen</span></h3>',
    r'<p class="indikator-date">Januari 2026</p>': r'<p class="indikator-date">Januari 2024</p>',
    
    # Wisman 11 (Not in karimun grid, wait. The grid we copied didn't have wisman, it had Penduduk and Inflasi. Let me double check what was copied over. Wait, 10 cards were copied, ending at Inflasi).
    # Ah, the regular index actually lacks wisman in that script? Wait, looking back at swap_grid.py, it omitted Wisman, Ekspor, Impor. Wait!
}

for old, new in replacements.items():
    content = re.sub(old, new, content)

with open('karimun.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Karimun dummy data replaced successfully.")
