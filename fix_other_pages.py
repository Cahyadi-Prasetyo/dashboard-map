import re
import os

files = ["karimun.html", "bintan.html", "natuna.html", "lingga.html", "anambas.html", "batam.html", "tanjungpinang.html"]

rich_modal_html = """
    <!-- MODAL -->
    <div class="modal-overlay" id="modalOverlay" onclick="if(event.target===this)closeModal()">
        <div class="modal-box" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 id="modalTitle">-</h3>
                <button class="modal-close" onclick="closeModal()">&times;</button>
            </div>
            
            <div class="modal-body-split">
                <!-- Kiri: Gambar, Definisi -->
                <div class="modal-left">
                    <img id="modalImg" src="" alt="Indikator" class="modal-img" onerror="this.src='assets/img/potensi.png'">
                    
                    <div class="modal-info-box">
                        <div class="modal-info-title">Definisi</div>
                        <div class="modal-info-text" id="modalDef">-</div>
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

for fpath in files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        # Replace Old Modal HTML or Existing Split HTML for consistency
        if '<!-- MODAL -->' in html:
            html = re.sub(r'<!-- MODAL -->.*?</div>\s*</div>\s*</div>', rich_modal_html.strip(), html, flags=re.DOTALL)
        
        # Also clean up the img path to use the updated standard export/import images
        html = html.replace('assets/img/import-export.png', 'assets/img/import (1).png')
        html = html.replace('assets/img/export (2).png', 'assets/img/export (2).png') # in case
        html = html.replace('onclick="openModal(\'ekspor\',', 'onclick="openModal(\'ekspor\',')
        
        # fix the img source string specifically for impor
        html = re.sub(r'<div class="indikator-icon" style="background-image:url\(\'assets/img/import \(1\)\.png\'\); filter: invert\(1\);"></div>\s*<p class="indikator-title">Impor</p>', 
                      '<div class="indikator-icon" style="background-image:url(\'assets/img/export \\(2\\).png\'); filter: invert(1);"></div>\n                    <p class="indikator-title">Impor</p>', html)

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
    except FileNotFoundError:
        pass
