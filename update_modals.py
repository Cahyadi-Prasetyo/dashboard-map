import re
import os

files = ["index.html", "karimun.html", "bintan.html", "natuna.html", "lingga.html", "anambas.html", "batam.html", "tanjungpinang.html"]

rich_modal_html = """
    <!-- MODAL -->
    <div class="modal-overlay" id="modalOverlay" onclick="if(event.target===this)closeModal()">
        <div class="modal-box" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 id="modalTitle">-</h3>
                <button class="modal-close" onclick="closeModal()">&times;</button>
            </div>
            
            <div class="modal-body-split">
                <!-- Kiri: Gambar, Definisi, Metode -->
                <div class="modal-left">
                    <img id="modalImg" src="" alt="Indikator" class="modal-img" onerror="this.src='assets/img/potensi.png'">
                    
                    <div class="modal-info-box">
                        <div class="modal-info-title">Definisi</div>
                        <div class="modal-info-text" id="modalDef">-</div>
                    </div>
                    
                    <div class="modal-info-box">
                        <div class="modal-info-title">Metode Perhitungan</div>
                        <div class="modal-info-text" id="modalMetode">-</div>
                    </div>
                </div>

                <!-- Kanan: Grafik, Insight -->
                <div class="modal-right">
                    <div class="modal-chart"><canvas id="modalChart"></canvas></div>
                    <div class="modal-insight">
                        <strong>Insight</strong>
                        <span id="modalInsight">-</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

small_cards_html = """
                <div class="indikator-container">
                <!-- Card 1 -->
                <div class="indikator-card" onclick="openModal('ekonomi', '{rk}', '{rn}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/in1.png')"></div>
                    <p class="indikator-title">Pertumbuhan Ekonomi</p>
                    <h3 class="indikator-value" id="val-ekonomi-{rk}">-<br><span>persen</span></h3>
                    <p class="indikator-date">2024</p>
                </div>

                <!-- Card 2 -->
                 <div class="indikator-card" onclick="openModal('pdrb', '{rk}', '{rn}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/in2.png')"></div>
                    <p class="indikator-title">PDRB per Kapita</p>
                    <h3 class="indikator-value" id="val-pdrb-{rk}">-<br><span>ribu rupiah</span></h3>
                    <p class="indikator-date">2024</p>
                </div>

                <!-- Card 3 -->
                <div class="indikator-card" onclick="openModal('ipm', '{rk}', '{rn}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/healthy.png')"></div>
                    <p class="indikator-title">IPM</p>
                    <h3 class="indikator-value" id="val-ipm-{rk}">-<br><span>persen</span></h3>
                    <p class="indikator-date">2025</p>
                </div>

                <!-- Card 4 -->
                <div class="indikator-card" onclick="openModal('ipg', '{rk}', '{rn}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/IPG.png')"></div>
                    <p class="indikator-title">IPG</p>
                    <h3 class="indikator-value" id="val-ipg-{rk}">-<br><span> </span></h3>
                    <p class="indikator-date">2024</p>
                </div>

                <!-- Card 5 -->
                <div class="indikator-card" onclick="openModal('tpt', '{rk}', '{rn}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/TPT.png')"></div>
                    <p class="indikator-title">TPT</p>
                    <h3 class="indikator-value" id="val-tpt-{rk}">-<br><span>persen</span></h3>
                    <p class="indikator-date">Agustus 2025</p>
                </div>

                <!-- Card 6 -->
                <div class="indikator-card" onclick="openModal('aps', '{rk}', '{rn}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/APS.png')"></div>
                    <p class="indikator-title">APS SMA/SMK</p>
                    <h3 class="indikator-value" id="val-aps-{rk}">-<br><span></span></h3>
                    <p class="indikator-date">2025</p>
                </div>

                <!-- Card 7 -->
                <div class="indikator-card" onclick="openModal('kemiskinan', '{rk}', '{rn}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/poverty.png')"></div>
                    <p class="indikator-title">Kemiskinan</p>
                    <h3 class="indikator-value" id="val-kemiskinan-{rk}">-<br><span>persen</span></h3>
                    <p class="indikator-date">Maret 2025</p>
                </div>

                <!-- Card 8 -->
                <div class="indikator-card" onclick="openModal('gini', '{rk}', '{rn}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/IPM.png')"></div>
                    <p class="indikator-title">Gini Ratio</p>
                    <h3 class="indikator-value" id="val-gini-{rk}">-<br><span>persen</span></h3>
                    <p class="indikator-date">September 2025</p>
                </div>

                <div class="indikator-card" onclick="openModal('penduduk', '{rk}', '{rn}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/output-onlinepngtools.png'); filter: invert(1);"></div>
                    <p class="indikator-title">Penduduk</p>
                    <h3 class="indikator-value" id="val-penduduk-{rk}">-<br><span>jiwa</span></h3>
                    <p class="indikator-date">Hasil SP2020</p>
                </div>

                <div class="indikator-card" onclick="openModal('inflasi', '{rk}', '{rn}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/indonesian-rupiah.png'); filter: invert(1);"></div>
                    <p class="indikator-title">Inflasi</p>
                    <h3 class="indikator-value" id="val-inflasi-{rk}">-<br><span>persen</span></h3>
                    <p class="indikator-date">Januari 2026</p>
                </div>

                <div class="indikator-card" onclick="openModal('wisman', '{rk}', '{rn}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/wisman.png'); filter: invert(1);"></div>
                    <p class="indikator-title">Wisman</p>
                    <h3 class="indikator-value" id="val-wisman-{rk}">-<br><span>kunjungan</span></h3>
                    <p class="indikator-date">Juli 2025</p>
                </div>

                <div class="indikator-card" onclick="openModal('ekspor', '{rk}', '{rn}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/import-export.png'); filter: invert(1);"></div>
                    <p class="indikator-title">Ekspor</p>
                    <h3 class="indikator-value" id="val-ekspor-{rk}">-<br><span>juta USD</span></h3>
                    <p class="indikator-date">Juli 2025</p>
                </div>

                <div class="indikator-card" onclick="openModal('impor', '{rk}', '{rn}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/import-export.png'); filter: invert(1);"></div>
                    <p class="indikator-title">Impor</p>
                    <h3 class="indikator-value" id="val-impor-{rk}">-<br><span>juta USD</span></h3>
                    <p class="indikator-date">Juli 2025</p>
                </div>
                </div>
            </div>
"""

regions_meta = {
    "index.html": ("kepri", "Provinsi Kepulauan Riau"),
    "karimun.html": ("karimun", "Kabupaten Karimun"),
    "bintan.html": ("bintan", "Kabupaten Bintan"),
    "batam.html": ("batam", "Kota Batam"),
    "tanjungpinang.html": ("tanjungpinang", "Kota Tanjungpinang"),
    "lingga.html": ("lingga", "Kabupaten Lingga"),
    "natuna.html": ("natuna", "Kabupaten Natuna"),
    "anambas.html": ("anambas", "Kabupaten Kepulauan Anambas")
}

for fpath in files:
    rk, rn = regions_meta[fpath]
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace Modal HTML
    if '<!-- MODAL -->' in html:
        html = re.sub(r'<!-- MODAL -->.*?</button>\s*</div>.*?</div>\s*</div>', rich_modal_html.strip(), html, flags=re.DOTALL)
    
    # Scripts logic
    if '<script src="assets/data/wisman.js"></script>' not in html and '<script src="assets/js/modal.js"></script>' in html:
        added_scripts = """    <script src="assets/data/wisman.js"></script>
    <script src="assets/data/ekspor.js"></script>
    <script src="assets/data/impor.js"></script>
"""
        html = html.replace('<script src="assets/js/modal.js"></script>', added_scripts + '    <script src="assets/js/modal.js"></script>')

    # For Regional Pages: Replace large old `detail-wrapper` big cards with Opsi 2 Compact Cards
    if fpath != "index.html" and '<!-- WRAPPER UNTUK INDIKATOR' in html:
        # We need to remove all detail-wrapper blocks completely
        html = re.sub(r'<!-- WRAPPER UNTUK INDIKATOR.*?<!-- ROW 5 -->.*?</div>\s*</div>\s*</div>', '', html, flags=re.DOTALL)

        # Remove the remaining chunk of old structure safely using precise strings or regex
        # I'll just clear out any <div class="detail-wrapper".*?</div>\s*</div> (might take a few passes based on nesting)
        while '<div class="detail-wrapper"' in html:
           html = re.sub(r'<div class="detail-wrapper"[^>]*>.*?(?=<!-- ROW|<script src="https://cdn|<footer)', '', html, count=1, flags=re.DOTALL)

        # Now insert the small cards structure right after the <div class="style-136"></div>
        if '<div class="style-136"></div>\n    </div>' in html:
            html = html.replace('<div class="style-136"></div>\n    </div>', '<div class="style-136"></div>\n    </div>\n    <!-- Cards Container -->\n    <div class="style-69">\n' + small_cards_html.replace('{rk}', rk).replace('{rn}', rn))

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
