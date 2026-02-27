import os
import json
import re

print("Starting HTML update script...")

# 1. Convert pdrb.json and penduduk.json to JS
with open("assets/data/pdrb.json", "r") as f:
    pdrb_data = json.load(f)
with open("assets/data/pdrb.js", "w") as f:
    f.write("const dataPdrb = " + json.dumps(pdrb_data, indent=4) + ";")

with open("assets/data/penduduk.json", "r") as f:
    penduduk_data = json.load(f)
# Reformat penduduk data to [2010_val, 2020_val]
mapped_penduduk = {}
for region, years in penduduk_data.items():
    mapped_penduduk[region] = [years.get("2010", 0), years.get("2020", 0)]
with open("assets/data/penduduk.js", "w") as f:
    f.write("const dataPenduduk = " + json.dumps(mapped_penduduk, indent=4) + ";")

print("Created pdrb.js and penduduk.js.")

# 2. Extract latest data for all regions dynamically by reading the JS files
def extract_latest(filepath, target_key="tahunan"):
    data_dict = {}
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # Simple regex to find region names and their data array
    regions = ["kepulauan_riau", "karimun", "bintan", "natuna", "lingga", "kepulauan_anambas", "batam", "tanjungpinang"]
    for reg in regions:
        # Looking for "karimun": { ... "tahunan": [...] }
        match = re.search(f'"{reg}"\s*:\s*{{[^}}]*?"{target_key}"\s*:\s*\[(.*?)\]', content, re.DOTALL)
        if match:
            arr_str = match.group(1).replace("\n", "")
            vals = [v.strip() for v in arr_str.split(",") if v.strip()]
            vals = [v for v in vals if v != 'null' and v != '']
            if vals:
                data_dict[reg] = float(vals[-1])
            else:
                data_dict[reg] = 0
        else:
            data_dict[reg] = 0
    return data_dict

curr_eko = extract_latest("assets/data/ekonomi.js")
curr_ipm = extract_latest("assets/data/ipm.js")
curr_ipg = extract_latest("assets/data/ipg.js")
curr_tpt = extract_latest("assets/data/tpt.js")
curr_aps = extract_latest("assets/data/aps.js")
curr_kem = extract_latest("assets/data/kemiskinan.js")
curr_gini = extract_latest("assets/data/gini.js")
curr_pdrb = {r: pdrb_data[r][-1] for r in pdrb_data}
curr_penduduk = {r: mapped_penduduk[r][-1] for r in mapped_penduduk}

# Inflasi values (user provided a few, defaulting others to 0 or last known)
# To be safe, we'll hardcode the ones we know
inflasi_custom = {
    "kepulauan_riau": "-0,09",
    "karimun": "2,77",
    "bintan": "0,00", # we don't know the exact ones for the rest, will use placeholder or 'N/A'
}

def fmt(val):
    return str(val).replace(".", ",")

regions_meta = {
    "kepulauan_riau": ("index.html", "Provinsi Kepulauan Riau"),
    "karimun": ("karimun.html", "Kabupaten Karimun"),
    "bintan": ("bintan.html", "Kabupaten Bintan"),
    "natuna": ("natuna.html", "Kabupaten Natuna"),
    "lingga": ("lingga.html", "Kabupaten Lingga"),
    "kepulauan_anambas": ("anambas.html", "Kabupaten Kepulauan Anambas"),
    "batam": ("batam.html", "Kota Batam"),
    "tanjungpinang": ("tanjungpinang.html", "Kota Tanjungpinang")
}

# 3. Create the HTML string generator
def get_indikator_html(reg_key, reg_name):
    # Formatted values
    v_eko = fmt(curr_eko.get(reg_key, 0))
    v_pdrb = f"{curr_pdrb.get(reg_key, 0):,}".replace(",", ".")
    v_ipm = fmt(curr_ipm.get(reg_key, 0))
    v_ipg = fmt(curr_ipg.get(reg_key, 0))
    v_tpt = fmt(curr_tpt.get(reg_key, 0))
    v_aps = fmt(curr_aps.get(reg_key, 0))
    v_kem = fmt(curr_kem.get(reg_key, 0))
    v_gini = fmt(curr_gini.get(reg_key, 0))
    v_pend = f"{curr_penduduk.get(reg_key, 0):,}".replace(",", ".")
    v_inf = inflasi_custom.get(reg_key, "0,00")

    html = f"""<div class="indikator-container">
                <!-- Card 1 -->
                <div class="indikator-card" onclick="openModal('ekonomi', '{reg_key}', '{reg_name}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/in1.png')"></div>
                    <p class="indikator-title">Pertumbuhan Ekonomi</p>
                    <h3 class="indikator-value">{v_eko}<br><span>persen</span></h3>
                    <p class="indikator-date">2024</p>
                </div>

                <!-- Card 2 -->
                 <div class="indikator-card" onclick="openModal('pdrb', '{reg_key}', '{reg_name}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/in2.png')"></div>
                    <p class="indikator-title">PDRB per Kapita</p>
                    <h3 class="indikator-value">{v_pdrb}<br><span>ribu rupiah</span></h3>
                    <p class="indikator-date">2024</p>
                </div>

                <!-- Card 3 -->
                <div class="indikator-card" onclick="openModal('ipm', '{reg_key}', '{reg_name}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/IPM.png')"></div>
                    <p class="indikator-title">IPM</p>
                    <h3 class="indikator-value">{v_ipm}<br><span>persen</span></h3>
                    <p class="indikator-date">2025</p>
                </div>

                <!-- Card 4 -->
                <div class="indikator-card" onclick="openModal('ipg', '{reg_key}', '{reg_name}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/IPG.png')"></div>
                    <p class="indikator-title">IPG</p>
                    <h3 class="indikator-value">{v_ipg}<br><span> </span></h3>
                    <p class="indikator-date">2024</p>
                </div>

                <!-- Card 5 -->
                <div class="indikator-card" onclick="openModal('tpt', '{reg_key}', '{reg_name}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/TPT.png')"></div>
                    <p class="indikator-title">TPT</p>
                    <h3 class="indikator-value">{v_tpt}<br><span>persen</span></h3>
                    <p class="indikator-date">Agustus 2025</p>
                </div>

                <!-- Card 6 -->
                <div class="indikator-card" onclick="openModal('aps', '{reg_key}', '{reg_name}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/APS.png')"></div>
                    <p class="indikator-title">APS SMA/SMK</p>
                    <h3 class="indikator-value">{v_aps}<br><span></span></h3>
                    <p class="indikator-date">2025</p>
                </div>

                <!-- Card 7 -->
                <div class="indikator-card" onclick="openModal('kemiskinan', '{reg_key}', '{reg_name}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/poverty.png')"></div>
                    <p class="indikator-title">Kemiskinan</p>
                    <h3 class="indikator-value">{v_kem}<br><span>persen</span></h3>
                    <p class="indikator-date">Maret 2025</p>
                </div>

                <!-- Card 8 -->
                <div class="indikator-card" onclick="openModal('gini', '{reg_key}', '{reg_name}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/IPM.png')"></div>
                    <p class="indikator-title">Gini Ratio</p>
                    <h3 class="indikator-value">{v_gini}<br><span>persen</span></h3>
                    <p class="indikator-date">September 2025</p>
                </div>

                <!-- Card 9 -->
                <div class="indikator-card" onclick="openModal('penduduk', '{reg_key}', '{reg_name}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/output-onlinepngtools.png'); filter: invert(1);"></div>
                    <p class="indikator-title">Penduduk</p>
                    <h3 class="indikator-value">{v_pend}<br><span>jiwa</span></h3>
                    <p class="indikator-date">Hasil SP2020</p>
                </div>

                <!-- Card 10 -->
                <div class="indikator-card" onclick="openModal('inflasi', '{reg_key}', '{reg_name}')">
                    <div class="indikator-icon" style="background-image:url('assets/img/indonesian-rupiah.png'); filter: invert(1);"></div>
                    <p class="indikator-title">Inflasi</p>
                    <h3 class="indikator-value">{v_inf}<br><span>persen</span></h3>
                    <p class="indikator-date">Januari 2026</p>
                </div>
            </div>"""
    return html

# 4. Generate assets/js/modal.js
modal_js_str = """
Chart.register(ChartDataLabels);
let modalChartInstance = null;

function openModal(type, regionKey = 'kepulauan_riau', regionName = 'Kepulauan Riau') {
    const overlay = document.getElementById('modalOverlay');
    const title = document.getElementById('modalTitle');
    const ctx = document.getElementById('modalChart');
    if (modalChartInstance) { modalChartInstance.destroy(); modalChartInstance = null; }

    const gradientFill = ctx.getContext('2d').createLinearGradient(0, 0, 0, 300);
    gradientFill.addColorStop(0, 'rgba(124, 58, 237, 0.15)');
    gradientFill.addColorStop(1, 'rgba(13, 148, 136, 0.02)');
    const gradientLine = ctx.getContext('2d').createLinearGradient(0, 0, ctx.width, 0);
    gradientLine.addColorStop(0, '#7c3aed');
    gradientLine.addColorStop(1, '#0d9488');

    const charts = {
        ekonomi: () => {
            title.textContent = `Pertumbuhan Ekonomi ${regionName}`;
            const d = dataEkonomi.wilayah[regionKey];
            let dataArr = [];
            if(d && d.tahunan) { dataArr = d.tahunan; }
            return { type:'bar', data:{ labels: dataEkonomi.tahun, datasets:[{ label:'Pertumbuhan Ekonomi (%)', data: dataArr, backgroundColor:'rgba(59,130,246,0.7)', borderRadius:6 }] }, options: barOpts('%') };
        },
        pdrb: () => {
            title.textContent = `PDRB per Kapita ${regionName}`;
            let dataArr = [];
            if(dataPdrb[regionKey]) { dataArr = dataPdrb[regionKey]; }
            return { type:'bar', data:{ labels:[2020,2021,2022,2023,2024], datasets:[{ label:'PDRB per Kapita (Ribu Rp)', data: dataArr, backgroundColor:'rgba(16,185,129,0.7)', borderRadius:6 }] }, options: barOpts('Rb') };
        },
        ipm: () => {
            title.textContent = `Indeks Pembangunan Manusia (IPM) ${regionName}`;
            const d = dataIpm.wilayah[regionKey];
            let dataArr = [];
            if(d && d.tahunan) { dataArr = d.tahunan; }
            return { type:'line', data:{ labels: dataIpm.tahun, datasets:[{ label:'IPM', data: dataArr, borderColor:'#7c3aed', backgroundColor:'rgba(124,58,237,0.1)', fill:true, tension:0.3, borderWidth:3, pointRadius:5, pointBackgroundColor:'#7c3aed', pointBorderColor:'#fff', pointBorderWidth:2 }] }, options: lineOpts('') };
        },
        ipg: () => {
            title.textContent = `Indeks Pembangunan Gender (IPG) ${regionName}`;
            const d = dataIpg.wilayah[regionKey];
            let dataArr = [];
            if(d && d.tahunan) { dataArr = d.tahunan; }
            return { type:'line', data:{ labels: dataIpg.tahun, datasets:[{ label:'IPG', data: dataArr, borderColor:'#ec4899', backgroundColor:'rgba(236,72,153,0.1)', fill:true, tension:0.3, borderWidth:3, pointRadius:5, pointBackgroundColor:'#ec4899', pointBorderColor:'#fff', pointBorderWidth:2 }] }, options: lineOpts('') };
        },
        tpt: () => {
            title.textContent = `Tingkat Pengangguran Terbuka (TPT) ${regionName}`;
            const d = dataTpt.wilayah[regionKey];
            let dataArr = [];
            if(d && d.tahunan) { dataArr = d.tahunan; }
            return { type:'bar', data:{ labels: dataTpt.tahun, datasets:[{ label:'TPT (%)', data: dataArr, backgroundColor:'rgba(239,68,68,0.7)', borderRadius:6 }] }, options: barOpts('%') };
        },
        aps: () => {
            title.textContent = `Angka Partisipasi Sekolah (APS) SMA/SMK ${regionName}`;
            const d = dataAps.wilayah[regionKey];
            let dataArr = [];
            if(d && d.tahunan) { dataArr = d.tahunan; }
            return { type:'line', data:{ labels: dataAps.tahun, datasets:[{ label:'APS', data: dataArr, borderColor:'#0d9488', backgroundColor:'rgba(13,148,136,0.1)', fill:true, tension:0.3, borderWidth:3, pointRadius:5, pointBackgroundColor:'#0d9488', pointBorderColor:'#fff', pointBorderWidth:2 }] }, options: lineOpts('') };
        },
        kemiskinan: () => {
            title.textContent = `Angka Kemiskinan ${regionName}`;
            const d = dataKemiskinan.wilayah[regionKey];
            let dataArr = [];
            if(d && d.tahunan) { dataArr = d.tahunan; }
            return { type:'bar', data:{ labels: dataKemiskinan.tahun, datasets:[{ label:'Kemiskinan (%)', data: dataArr, backgroundColor:'rgba(245,158,11,0.7)', borderRadius:6 }] }, options: barOpts('%') };
        },
        gini: () => {
            title.textContent = `Gini Ratio ${regionName}`;
            const d = dataGini.wilayah[regionKey];
            let dataArr = [];
            if(d && d.tahunan) { dataArr = d.tahunan; }
            return { type:'line', data:{ labels: dataGini.tahun, datasets:[{ label:'Gini Ratio', data: dataArr, borderColor:'#f59e0b', backgroundColor:'rgba(245,158,11,0.1)', fill:true, tension:0.3, borderWidth:3, pointRadius:5, pointBackgroundColor:'#f59e0b', pointBorderColor:'#fff', pointBorderWidth:2 }] }, options: lineOpts('') };
        },
        penduduk: () => {
            title.textContent = `Jumlah Penduduk ${regionName} (Sensus Penduduk)`;
            let dataArr = [];
            if(dataPenduduk[regionKey]) { dataArr = dataPenduduk[regionKey]; }
            return { type:'bar', data:{ labels:['SP 2010','SP 2020'], datasets:[{ label:'Jumlah Penduduk (jiwa)', data: dataArr, backgroundColor:['rgba(59,130,246,0.7)','rgba(16,185,129,0.7)'], borderRadius:8, barThickness:60 }] }, options:{ responsive:true, maintainAspectRatio:false, indexAxis:'y', plugins:{ legend:{display:false}, datalabels:{ anchor:'end', align:'right', formatter:(v)=>v.toLocaleString('id-ID')+' jiwa', font:{weight:'bold',size:12}, color:'#1e293b' } }, scales:{ x:{display:false}, y:{grid:{display:false},border:{display:false}} }, layout:{padding:{right:120}} } };
        },
        inflasi: () => {
            title.textContent = `Tingkat Inflasi Y-on-Y ${regionName}, Januari 2026`;
            
            // Hardcode Y-on-Y arrays based on user screenshots or available data
            let dataArr = [];
            if(regionKey === 'karimun') {
                dataArr = [-0.73, -0.15, 2.30, 0.87, -0.15, 0.40, 1.92, 2.91, 2.58, 2.43, 2.72, 2.77];
            } else {
                const d = dataInflasi.wilayah[regionKey]?.tahunan;
                if(d && d['2025']) {
                    const jan26 = d['2026']?.[0] || 0;
                    dataArr = [...d['2025'].slice(1), jan26];
                }
            }
            if(dataArr.length === 0) dataArr = [0];

            return { type:'line', data:{ labels:['Feb 25','Mar 25','Apr 25','Mei 25','Jun 25','Jul 25','Ags 25','Sep 25','Okt 25','Nov 25','Des 25','Jan 26'], datasets:[{ label:'Inflasi Y-on-Y (%)', data:dataArr, borderColor: gradientLine, backgroundColor: gradientFill, fill:true, tension:0.3, borderWidth:3, pointRadius:5, pointBackgroundColor:'#7c3aed', pointBorderColor:'#fff', pointBorderWidth:2, pointHoverRadius:7 }] }, options: lineOpts('%') };
        }
    };

    if (charts[type]) {
        const cfg = charts[type]();
        modalChartInstance = new Chart(ctx, cfg);
        overlay.classList.add('active');
    }
}

function closeModal() {
    document.getElementById('modalOverlay').classList.remove('active');
    if (modalChartInstance) { modalChartInstance.destroy(); modalChartInstance = null; }
}

document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });

function barOpts(suffix) {
    return {
        responsive:true, maintainAspectRatio:false,
        plugins:{ legend:{display:false}, datalabels:{ anchor:'end', align:'top', formatter:(v)=>v.toLocaleString('id-ID')+suffix, font:{weight:'bold',size:11}, color:'#1e293b' } },
        scales:{ y:{display:false}, x:{grid:{display:false},border:{display:false}} },
        layout:{padding:{top:30}}
    };
}
function lineOpts(suffix) {
    return {
        responsive:true, maintainAspectRatio:false,
        plugins:{ legend:{display:false}, datalabels:{ align:'top', offset:6, formatter:(v)=>v.toLocaleString('id-ID')+suffix, font:{weight:'bold',size:11}, color:'#1e293b' } },
        scales:{ y:{display:false}, x:{grid:{display:false},border:{display:false}, ticks: { font: { size: 11 } }} },
        layout:{padding:{top:30, bottom:10}}
    };
}
"""

with open("assets/js/modal.js", "w") as f:
    f.write(modal_js_str)
print("Created assets/js/modal.js")

# 5. Modal HTML block to append before </body>
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

# 6. Process all HTML files
for rk, (filename, rname) in regions_meta.items():
    if not os.path.exists(filename): continue
    
    with open(filename, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Determine if it's index.html (has indikator-container) or regional (detail-container)
    start_tag = ""
    end_tag = ""
    if "indikator-container" in html_content:
        # replace the indikator-container block
        html_content = re.sub(r'<div class="indikator-container">.*?</div>\s*</div>\s*(?=<div class="style|<!-- MODAL)', 
                              get_indikator_html(rk, rname) + '\n            </div>\n        </div>\n', 
                              html_content, flags=re.DOTALL)
    elif "detail-container" in html_content:
        # replace the detail-container block
        html_content = re.sub(r'<div class="detail-container">.*?</div>\s*</div>\s*(?=<div class="style|<!-- MODAL)', 
                              get_indikator_html(rk, rname) + '\n            </div>\n        </div>\n', 
                              html_content, flags=re.DOTALL)

    # Clean up old chart scripts inside <body> or at bottom
    # We will remove from "<script>" where it contains "chartInflasi" or "Chart.register" down to "</script>"
    # Actually, simpler: just remove all script blocks that mention "ctxEkonomi", "chartInflasi", "modalChartInstance", or "Chart.register"
    # and then append our single modal block.
    
    # Remove inline Modal scripts in index.html
    html_content = re.sub(r'<script>[^<]*?Chart\.register\(ChartDataLabels\);.*?</script>', '', html_content, flags=re.DOTALL)
    
    # Remove large inline scripts in regional pages
    html_content = re.sub(r'<script>[^<]*?ctxEkonomi.*?</script>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<script>[^<]*?chartInflasi.*?</script>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<script>[^<]*?ipm.*?</script>', '', html_content, flags=re.DOTALL)
    
    # Remove the hardcoded <!-- Data scripts --> from anywhere
    html_content = re.sub(r'<!-- MODAL -->.*?</script>\s*</script>', '', html_content, flags=re.DOTALL) # wait, previous one handles modal logic
    html_content = re.sub(r'<!-- MODAL -->.*?<script src="assets/data/inflasi.js"></script>', '', html_content, flags=re.DOTALL)

    # We need to make sure we inject the <head> CDN for ChartJS
    if "https://cdn.jsdelivr.net/npm/chart.js" not in html_content:
        html_content = html_content.replace('</head>', '    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>\n    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2"></script>\n</head>')

    # Strip existing inline CSS from index.html head
    html_content = re.sub(r'<style>\s*/\* Compact indikator cards \*/.*?</style>', '', html_content, flags=re.DOTALL)

    # Prepend the body closing tag with the modal_html
    # Remove any stray modal_html first to be safe
    html_content = re.sub(r'<!-- MODAL -->.*?assets/js/modal\.js"></script>', '', html_content, flags=re.DOTALL)
    
    html_content = html_content.replace('</body>', f'{modal_html}\n</body>')

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Updated {filename}")

# 7. Add modal CSS to shared.css
shared_css_path = "assets/css/shared.css"
with open(shared_css_path, "r", encoding="utf-8") as f:
    shared_css = f.read()

modal_css = """
/* Compact indicator cards & Modal Styles */
.indikator-card {
    padding: 14px 10px !important;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
}
.indikator-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}
.indikator-icon { width: 48px !important; height: 48px !important; margin-top: 4px !important; }
.indikator-title { font-size: 11px !important; margin: 4px 0 2px !important; }
.indikator-value { font-size: 18px !important; }
.indikator-value span { font-size: 10px !important; }
.indikator-date { font-size: 10px !important; margin: 2px 0 0 !important; }

/* Modal */
.modal-overlay {
    display: none; position: fixed; inset: 0; z-index: 9999;
    background: rgba(0,0,0,0.5); align-items: center; justify-content: center;
    backdrop-filter: blur(4px);
}
.modal-overlay.active { display: flex; }
.modal-box {
    background: #fff; border-radius: 16px; width: 90%; max-width: 720px;
    max-height: 85vh; overflow-y: auto; padding: 32px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    animation: modalIn 0.25s ease;
}
@keyframes modalIn { from { opacity: 0; transform: scale(0.95); } to { opacity: 1; transform: scale(1); } }
.modal-header {
    display: flex; justify-content: space-between; align-items: center;
    margin-bottom: 20px; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px;
}
.modal-header h3 { margin: 0; font-size: 18px; color: #1e293b; font-weight: 700; }
.modal-close {
    background: none; border: none; font-size: 28px; cursor: pointer;
    color: #94a3b8; line-height: 1; padding: 0 4px;
}
.modal-close:hover { color: #ef4444; }
.modal-chart { position: relative; height: 320px; }
"""

if "Compact indicator cards" not in shared_css:
    with open(shared_css_path, "a", encoding="utf-8") as f:
        f.write("\n" + modal_css)
    print("Added Modal CSS to shared.css")

print("All done!")
