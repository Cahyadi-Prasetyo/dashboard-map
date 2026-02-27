import re
with open("karimun.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add onclicks to the detail-cards in karimun
html = html.replace('<div class="detail-card">\n\n            <!-- JUDUL -->\n            <h3>Pertumbuhan Ekonomi</h3>',
                    '<div class="detail-card" style="cursor:pointer;" onclick="openModal(\'ekonomi\', \'karimun\', \'Kabupaten Karimun\')">\n\n            <!-- JUDUL -->\n            <h3>Pertumbuhan Ekonomi</h3>')

html = html.replace('<div class="detail-card">\n\n            <!-- JUDUL -->\n            <h3>PDRB dan PDRB Per Kapita</h3>',
                    '<div class="detail-card" style="cursor:pointer;" onclick="openModal(\'pdrb\', \'karimun\', \'Kabupaten Karimun\')">\n\n            <!-- JUDUL -->\n            <h3>PDRB dan PDRB Per Kapita</h3>')

html = html.replace('<div class="detail-card">\n\n            <!-- JUDUL -->\n            <h3>Indeks Pembangunan Manusia (IPM)</h3>',
                    '<div class="detail-card" style="cursor:pointer;" onclick="openModal(\'ipm\', \'karimun\', \'Kabupaten Karimun\')">\n\n            <!-- JUDUL -->\n            <h3>Indeks Pembangunan Manusia (IPM)</h3>')

html = html.replace('<div class="detail-card">\n\n            <!-- JUDUL -->\n            <h3>Indeks Pemberdayaan Gender (IPG)</h3>',
                    '<div class="detail-card" style="cursor:pointer;" onclick="openModal(\'ipg\', \'karimun\', \'Kabupaten Karimun\')">\n\n            <!-- JUDUL -->\n            <h3>Indeks Pemberdayaan Gender (IPG)</h3>')

html = html.replace('<div class="detail-card">\n            <h3>Tingkat Pengangguran Terbuka (TPT)</h3>',
                    '<div class="detail-card" style="cursor:pointer;" onclick="openModal(\'tpt\', \'karimun\', \'Kabupaten Karimun\')">\n            <h3>Tingkat Pengangguran Terbuka (TPT)</h3>')

html = html.replace('<div class="detail-card">\n            <h3>Angka Partisipasi Sekolah (APS)</h3>',
                    '<div class="detail-card" style="cursor:pointer;" onclick="openModal(\'aps\', \'karimun\', \'Kabupaten Karimun\')">\n            <h3>Angka Partisipasi Sekolah (APS)</h3>')

html = html.replace('<div class="detail-card">\n            <h3>Persentase Penduduk Miskin</h3>',
                    '<div class="detail-card" style="cursor:pointer;" onclick="openModal(\'kemiskinan\', \'karimun\', \'Kabupaten Karimun\')">\n            <h3>Persentase Penduduk Miskin</h3>')

html = html.replace('<div class="detail-card">\n            <h3>Rasio Gini</h3>',
                    '<div class="detail-card" style="cursor:pointer;" onclick="openModal(\'gini\', \'karimun\', \'Kabupaten Karimun\')">\n            <h3>Rasio Gini</h3>')

html = html.replace('<div class="detail-card">\n            <h3>Inflasi Kepulauan Riau</h3>',
                    '<div class="detail-card" style="cursor:pointer;" onclick="openModal(\'inflasi\', \'karimun\', \'Kabupaten Karimun\')">\n            <h3>Inflasi Kepulauan Riau</h3>')

html = html.replace('<div class="detail-card">\n            <h3>Jumlah Penduduk</h3>',
                    '<div class="detail-card" style="cursor:pointer;" onclick="openModal(\'penduduk\', \'karimun\', \'Kabupaten Karimun\')">\n            <h3>Jumlah Penduduk</h3>')

with open("karimun.html", "w", encoding="utf-8") as f:
    f.write(html)
