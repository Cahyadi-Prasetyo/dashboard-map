import os
import glob
import re

modal_html_new = """    <!-- MODAL -->
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
    </div>"""

data_scripts = """    <script src="assets/data/wisman.js"></script>
    <script src="assets/data/ekspor.js"></script>
    <script src="assets/data/impor.js"></script>
"""

files = ['karimun.html', 'bintan.html', 'natuna.html', 'lingga.html', 'anambas.html', 'batam.html', 'tanjungpinang.html']

for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace old modal structure
        # Find the old modal block, which ends before <!-- modal.js (global handler) -->
        old_modal_pattern = re.compile(r'<!-- MODAL -->\s*<div class="modal-overlay".*?<div class="modal-chart"><canvas id="modalChart"></canvas></div>\s*</div>\s*</div>', re.DOTALL)
        content = old_modal_pattern.sub(modal_html_new, content)

        # Ensure we add wisman, ekspor, impor scripts
        if 'wisman.js' not in content:
            script_insert_pattern = re.compile(r'(<script src="assets/data/penduduk\.js"></script>)')
            if script_insert_pattern.search(content):
                content = script_insert_pattern.sub(r'\1\n' + data_scripts, content)
            else:
                # Some might not have penduduk.js, fallback to insert before modal.js
                fallback_pattern = re.compile(r'(<script src="assets/js/modal\.js"></script>)')
                content = fallback_pattern.sub(data_scripts + r'\1', content)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
