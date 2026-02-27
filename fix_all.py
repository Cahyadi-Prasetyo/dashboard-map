import re
import os

files = ["index.html", "karimun.html", "bintan.html", "natuna.html", "lingga.html", "anambas.html", "batam.html", "tanjungpinang.html"]

modal_html = """
    <!-- MODAL -->
    <div class="modal-overlay" id="modalOverlay" onclick="if(event.target===this)closeModal()">
        <div class="modal-box">
            <div class="modal-header">
                <h3 id="modalTitle">-</h3>
                <button class="modal-close" onclick="closeModal()">&times;</button>
            </div>
            <div class="modal-chart"><canvas id="modalChart"></canvas></div>
        </div>
    </div>

    <!-- Data scripts -->
    <script src="assets/data/ekonomi.js"></script>
    <script src="assets/data/ipm.js"></script>
    <script src="assets/data/ipg.js"></script>
    <script src="assets/data/tpt.js"></script>
    <script src="assets/data/aps.js"></script>
    <script src="assets/data/kemiskinan.js"></script>
    <script src="assets/data/gini.js"></script>
    <script src="assets/data/inflasi.js"></script>
    <script src="assets/data/pdrb.js"></script>
    <script src="assets/data/penduduk.js"></script>
    <script src="assets/js/modal.js"></script>
"""

for fpath in files:
    if not os.path.exists(fpath): continue

    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Add modal HTML before generic scripts
    if "<!-- MODAL -->" not in html:
        # insert before <script>let heroIndex
        if "<script>\n\n\nlet heroIndex" in html:
            html = html.replace("<script>\n\n\nlet heroIndex", modal_html + "\n<script>\n\n\nlet heroIndex")

    # 2. Add onclicks based on title
    if "index.html" in fpath:
        html = html.replace('<div class="indikator-card">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/in1.png\')"></div>',
                            '<div class="indikator-card" onclick="openModal(\'ekonomi\')">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/in1.png\')"></div>')
        html = html.replace('<div class="indikator-card">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/in2.png\')"></div>\n                    <p class="indikator-title">Produk Domestik Regional Bruto (PDRB) per Kapita</p>',
                            '<div class="indikator-card" onclick="openModal(\'pdrb\')">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/in2.png\')"></div>\n                    <p class="indikator-title">PDRB per Kapita</p>')
        html = html.replace('<div class="indikator-card">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/IPM.png\')"></div>\n                    <p class="indikator-title">Indeks Pembangunan Manusia (IPM)</p>',
                            '<div class="indikator-card" onclick="openModal(\'ipm\')">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/IPM.png\')"></div>\n                    <p class="indikator-title">IPM</p>')
        html = html.replace('<div class="indikator-card">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/IPG.png\')"></div>\n                    <p class="indikator-title">Indeks Pembangunan Gender (IPG)</p>',
                            '<div class="indikator-card" onclick="openModal(\'ipg\')">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/IPG.png\')"></div>\n                    <p class="indikator-title">IPG</p>')
        html = html.replace('<div class="indikator-card">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/TPT.png\')"></div>\n                    <p class="indikator-title">Tingkat Pengangguran Terbuka (TPT)</p>',
                            '<div class="indikator-card" onclick="openModal(\'tpt\')">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/TPT.png\')"></div>\n                    <p class="indikator-title">TPT</p>')
        html = html.replace('<div class="indikator-card">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/APS.png\')"></div>\n                    <p class="indikator-title">Angka Partisipasi Sekolah (APS) SMA/SMK</p>',
                            '<div class="indikator-card" onclick="openModal(\'aps\')">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/APS.png\')"></div>\n                    <p class="indikator-title">APS SMA/SMK</p>')
        html = html.replace('<div class="indikator-card">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/poverty.png\')"></div>\n                    <p class="indikator-title">Angka Kemiskinan</p>',
                            '<div class="indikator-card" onclick="openModal(\'kemiskinan\')">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/poverty.png\')"></div>\n                    <p class="indikator-title">Kemiskinan</p>')
        html = html.replace('<div class="indikator-card">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/IPM.png\')"></div>\n                    <p class="indikator-title">Gini Ratio</p>',
                            '<div class="indikator-card" onclick="openModal(\'gini\')">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/IPM.png\')"></div>\n                    <p class="indikator-title">Gini Ratio</p>')
        html = html.replace('<div class="indikator-card">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/output-onlinepngtools.png\'); filter: invert(1);"></div>\n                    <p class="indikator-title">Jumlah Penduduk</p>',
                            '<div class="indikator-card" onclick="openModal(\'penduduk\')">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/output-onlinepngtools.png\'); filter: invert(1);"></div>\n                    <p class="indikator-title">Penduduk</p>')
        html = html.replace('<div class="indikator-card">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/indonesian-rupiah.png\'); filter: invert(1);"></div>\n                    <p class="indikator-title">Inflasi</p>',
                            '<div class="indikator-card" onclick="openModal(\'inflasi\')">\n                    <div class="indikator-icon" style="background-image:url(\'assets/img/indonesian-rupiah.png\'); filter: invert(1);"></div>\n                    <p class="indikator-title">Inflasi</p>')

    if "https://cdn.jsdelivr.net/npm/chart.js" not in html:
        html = html.replace('</head>', '    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>\n    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2"></script>\n</head>')

    # 3. Add modal styles if needed
    modal_style = """
    <style>
        .indikator-card { cursor: pointer; transition: transform 0.2s, box-shadow 0.2s; }
        .indikator-card:hover { transform: translateY(-4px); box-shadow: 0 8px 24px rgba(0,0,0,0.12); }
        .modal-overlay { display: none; position: fixed; inset: 0; z-index: 9999; background: rgba(0,0,0,0.5); align-items: center; justify-content: center; backdrop-filter: blur(4px); }
        .modal-overlay.active { display: flex; }
        .modal-box { background: #fff; border-radius: 16px; width: 90%; max-width: 720px; max-height: 85vh; overflow-y: auto; padding: 32px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); animation: modalIn 0.25s ease; }
        @keyframes modalIn { from { opacity: 0; transform: scale(0.95); } to { opacity: 1; transform: scale(1); } }
        .modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px; }
        .modal-header h3 { margin: 0; font-size: 18px; color: #1e293b; font-weight: 700; }
        .modal-close { background: none; border: none; font-size: 28px; cursor: pointer; color: #94a3b8; line-height: 1; padding: 0 4px; }
        .modal-close:hover { color: #ef4444; }
        .modal-chart { position: relative; height: 320px; }
    </style>
"""
    if "/* Modal */" not in html and ".modal-overlay {" not in html: # we added it to shared.css instead! Let me rely on shared.css

        pass

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
