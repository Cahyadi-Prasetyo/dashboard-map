import re
import os

filepath = r'd:\Workspace\dashboard-map\batam.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. PE (Pertumbuhan Ekonomi)
pe_start = content.find('<!-- ====== INDIKATOR 1: PERTUMBUHAN EKONOMI ====== -->')
ipm_start = content.find('<!-- ====== INDIKATOR 2: INDEKS PEMBANGUNAN MANUSIA')

pe_content = content[pe_start:ipm_start].strip()
pe_content = pe_content.replace('<!-- ====== INDIKATOR 1: PERTUMBUHAN EKONOMI ====== -->', '')
pe_wrapped = f"""<!-- ====== INDIKATOR 1: PERTUMBUHAN EKONOMI (ORANGE BACKGROUND) ====== -->
    <div style="margin-left: calc(-50vw + 50%); margin-right: calc(-50vw + 50%); padding-left: calc(50vw - 50%); padding-right: calc(50vw - 50%); background: #e37f2a; padding-top: 64px; padding-bottom: 64px;">
        <div style="max-width: 1200px; margin: 0 auto;">
            <div class="eko-section-header">
                <h3 style="color: #ffffff;">Pertumbuhan Ekonomi</h3>
                <p style="color: rgba(255,255,255,0.9);">Mengukur persentase perubahan nilai tambah barang dan jasa riil dari tahun ke tahun.</p>
            </div>
            {pe_content}
        </div>
    </div>
"""

# 2. IPM
ipg_start = content.find('<!-- ====== INDIKATOR 3: INDEKS PEMBANGUNAN GENDER')
ipm_content = content[ipm_start:ipg_start].strip()
ipm_content = ipm_content.replace('<!-- ====== INDIKATOR 2: INDEKS PEMBANGUNAN MANUSIA (IPM) (WHITE BACKGROUND) ====== -->', '')
ipm_content = ipm_content.replace('<div class="eko-section-header">\\n            <h3>Indeks Pembangunan Manusia (IPM)</h3>', '<div class="eko-section-header">\\n                <h3>Indeks Pembangunan Manusia (IPM)</h3>')
ipm_wrapped = f"""<!-- ====== INDIKATOR 2: INDEKS PEMBANGUNAN MANUSIA (IPM) (WHITE BACKGROUND) ====== -->
    <div style="margin-left: calc(-50vw + 50%); margin-right: calc(-50vw + 50%); padding-left: calc(50vw - 50%); padding-right: calc(50vw - 50%); background: #ffffff; padding-top: 64px; padding-bottom: 64px;">
        <div style="max-width: 1200px; margin: 0 auto;">
            <div class="eko-dashboard-section" id="section-ipm">
                {ipm_content}
            </div>
        </div>
    </div>
"""

# 3. IPG
tpt_start = content.find('<!-- ====== INDIKATOR 4 & 5: TPT & APS (PAIRED) ====== -->')
ipg_content = content[ipg_start:tpt_start].strip()
ipg_content = ipg_content.replace('<!-- ====== INDIKATOR 3: INDEKS PEMBANGUNAN GENDER (IPG) ====== -->', '')
ipg_wrapped = f"""<!-- ====== INDIKATOR 3: INDEKS PEMBANGUNAN GENDER (IPG) (CREAM BACKGROUND) ====== -->
    <div style="margin-left: calc(-50vw + 50%); margin-right: calc(-50vw + 50%); padding-left: calc(50vw - 50%); padding-right: calc(50vw - 50%); background: #faf3ec; padding-top: 64px; padding-bottom: 64px;">
        <div style="max-width: 1200px; margin: 0 auto;">
            {ipg_content}
        </div>
    </div>
"""

# 4. TPT & APS
kem_start = content.find('<!-- ========================================================\\n         SECTION 5: KEMISKINAN')
if kem_start == -1: kem_start = content.find('<!-- ====== INDIKATOR 5:')
if kem_start == -1: kem_start = content.find('<!-- ========================================================\\n         SECTION 5: KEMISKINAN & RASIO GINI (CREAM BACKGROUND)\\n         ======================================================== -->')
tpt_content = content[tpt_start:kem_start].strip()
tpt_content = tpt_content.replace('<!-- ====== INDIKATOR 4 & 5: TPT & APS (PAIRED) ====== -->', '')
tpt_wrapped = f"""<!-- ====== INDIKATOR 4: TPT & APS (PAIRED) (WHITE BACKGROUND) ====== -->
    <div style="margin-left: calc(-50vw + 50%); margin-right: calc(-50vw + 50%); padding-left: calc(50vw - 50%); padding-right: calc(50vw - 50%); background: #ffffff; padding-top: 64px; padding-bottom: 64px;">
        <div style="max-width: 1200px; margin: 0 auto;">
            {tpt_content}
        </div>
    </div>
"""

# 5. Kemiskinan & Gini
end_potensi = content.find('<!-- <div class="style-129">')
if end_potensi == -1: end_potensi = content.find('<div class="style-137">')
kem_content = content[kem_start:end_potensi].strip()
kem_content = re.sub(r'<!-- =+\\n\\s*SECTION 5: KEMISKINAN.*?\\n\\s*=+\\s*-->', '', kem_content, flags=re.DOTALL)
kem_wrapped = f"""<!-- ====== INDIKATOR 5: KEMISKINAN & RASIO GINI (CREAM BACKGROUND) ====== -->
    <div style="margin-left: calc(-50vw + 50%); margin-right: calc(-50vw + 50%); padding-left: calc(50vw - 50%); padding-right: calc(50vw - 50%); background: #faf3ec; padding-top: 64px; padding-bottom: 64px;">
        <div style="max-width: 1200px; margin: 0 auto;">
            {kem_content}
        </div>
    </div>
"""

# 6. PDRB
pdrb_wrapped = """
    <!-- ====== INDIKATOR 6: PENDUDUK & PDRB (ORANGE BACKGROUND) ====== -->
    <div style="margin-left: calc(-50vw + 50%); margin-right: calc(-50vw + 50%); padding-left: calc(50vw - 50%); padding-right: calc(50vw - 50%); background: #e37f2a; padding-top: 64px; padding-bottom: 64px;">
        <div style="max-width: 1200px; margin: 0 auto;">
            <div class="eko-section-header">
                <h3 style="color: #ffffff;">Jumlah Penduduk & PDRB per Kapita</h3>
                <p style="color: rgba(255,255,255,0.9);">Perkembangan demografi dan kesejahteraan rata-rata penduduk Kota Batam.</p>
            </div>

            <div class="eko-paired-grid" style="grid-template-columns: 1fr 1fr; gap: 24px;">
                <!-- LEFT: PENDUDUK -->
                <div class="eko-paired-card" style="background: #ffffff; box-shadow: 0 4px 20px rgba(0,0,0,0.05); border-radius: 16px; padding: 24px; border: 1px solid #eaeaea;">
                    <div class="eko-paired-card-header">
                        <h4 class="eko-paired-card-title" style="color: #1a1a2e; font-size: 18px; margin-bottom: 4px;"><i class="bi bi-people-fill" style="color: #e37f2a; margin-right: 8px;"></i> Jumlah Penduduk</h4>
                        <p class="eko-paired-card-subtitle" style="color: #666; font-size: 13px;">Sensus Penduduk (Jiwa)</p>
                    </div>
                    <div class="eko-paired-highlight">
                        <span class="eko-paired-highlight-val" style="color: #e37f2a; font-size: 36px; font-weight: 700; line-height: 1;">1.196.396</span>
                        <span class="eko-paired-highlight-desc" style="color: #888; font-size: 14px; margin-top: 4px;">Tahun 2020</span>
                    </div>
                    
                    <table class="eko-table" style="width: 100%; margin-top: 32px; border-radius: 8px; overflow: hidden;">
                        <thead>
                            <tr class="eko-thead-title">
                                <th colspan="2" style="background: #f8f9fa; color: #1a1a2e; padding: 12px; font-size: 14px; border-bottom: 1px solid #ddd;">Hasil Sensus Penduduk (SP)</th>
                            </tr>
                            <tr class="eko-thead-cols">
                                <th style="background: #ffffff; padding: 10px; border-bottom: 1px solid #eee;">Tahun 2010</th>
                                <th style="background: #ffffff; padding: 10px; border-bottom: 1px solid #eee;">Tahun 2020</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="text-align: center; font-weight: 600; color: #444; font-size: 16px; padding: 16px; border-right: 1px solid #eee;">944.285</td>
                                <td style="text-align: center; font-weight: 700; color: #e37f2a; font-size: 18px; padding: 16px;">1.196.396</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- RIGHT: PDRB -->
                <div class="eko-paired-card" style="background: #ffffff; box-shadow: 0 4px 20px rgba(0,0,0,0.05); border-radius: 16px; padding: 24px; border: 1px solid #eaeaea;">
                    <div class="eko-paired-card-header">
                        <h4 class="eko-paired-card-title" style="color: #1a1a2e; font-size: 18px; margin-bottom: 4px;"><i class="bi bi-wallet2" style="color: #27ae60; margin-right: 8px;"></i> PDRB per Kapita</h4>
                        <p class="eko-paired-card-subtitle" style="color: #666; font-size: 13px;">Atas Dasar Harga Berlaku (Ribu Rp)</p>
                    </div>
                    <div class="eko-paired-highlight">
                        <span class="eko-paired-highlight-val" style="color: #27ae60; font-size: 36px; font-weight: 700; line-height: 1;">182.507</span>
                        <span class="eko-paired-highlight-desc" style="color: #888; font-size: 14px; margin-top: 4px;">Tahun 2024</span>
                    </div>
                    
                    <div class="eko-histogram" id="pdrbHistogramContainer" style="height: 150px; margin-top: 24px; position: relative;">
                    </div>
                </div>
            </div>

            <script>
            (function() {
                const years = [2020, 2021, 2022, 2023, 2024];
                const vals = [135402, 142243, 157633, 171968, 182507];
                setTimeout(() => {
                    const ctx = document.getElementById('pdrbHistogramContainer');
                    if (!ctx) return;
                    const minVal = 120000;
                    const maxVal = 190000;
                    const range = maxVal - minVal;
                    ctx.innerHTML = '';
                    const yAxis = document.createElement('div');
                    yAxis.className = 'eko-y-axis';
                    const steps = 3;
                    for (let i = steps; i >= 0; i--) {
                        const label = document.createElement('span');
                        const val = Math.round(minVal + (range / steps) * i);
                        label.textContent = val.toLocaleString('id-ID');
                        yAxis.appendChild(label);
                    }
                    ctx.appendChild(yAxis);
                    const barsArea = document.createElement('div');
                    barsArea.className = 'eko-bars-area';
                    years.forEach((yr, i) => {
                        const val = vals[i];
                        const barGroup = document.createElement('div');
                        barGroup.className = 'eko-bar-group';
                        const bar = document.createElement('div');
                        bar.className = 'eko-bar';
                        bar.style.background = 'linear-gradient(180deg, #27ae60 0%, #2ecc71 100%)';
                        bar.style.boxShadow = '0 -2px 8px rgba(39, 174, 96, 0.2)';
                        const heightPct = Math.max(5, ((val - minVal) / range) * 100);
                        bar.style.height = '0%';
                        bar.style.bottom = '0';
                        bar.style.position = 'absolute';
                        bar.style.left = '0';
                        bar.style.right = '0';
                        setTimeout(() => { bar.style.height = heightPct + '%'; }, 100 + i * 120);
                        const valLabel = document.createElement('span');
                        valLabel.className = 'eko-bar-value';
                        valLabel.textContent = val.toLocaleString('id-ID');
                        valLabel.style.fontSize = '11px';
                        bar.appendChild(valLabel);
                        const yrLabel = document.createElement('span');
                        yrLabel.className = 'eko-bar-year';
                        yrLabel.textContent = yr;
                        barGroup.appendChild(bar);
                        barGroup.appendChild(yrLabel);
                        barsArea.appendChild(barGroup);
                    });
                    ctx.appendChild(barsArea);
                }, 100);
            })();
            </script>
        </div>
    </div>
"""

# 7. Inflasi
inflasi_wrapped = """
    <!-- ====== INDIKATOR 7: INFLASI (WHITE BACKGROUND) ====== -->
    <div style="margin-left: calc(-50vw + 50%); margin-right: calc(-50vw + 50%); padding-left: calc(50vw - 50%); padding-right: calc(50vw - 50%); background: #ffffff; padding-top: 64px; padding-bottom: 64px;">
        <div style="max-width: 1200px; margin: 0 auto;">
            <div class="eko-inflasi-section" id="section-inflasi">
                <div class="eko-ipg-container">
                    <div class="eko-ipg-header">
                        <h3 style="color: #1a1a2e;">Tingkat Inflasi (m-to-m)</h3>
                        <p style="color: #444;">Perkembangan inflasi bulanan menunjukkan tingkat perubahan harga.</p>
                    </div>

                    <div class="eko-ipg-grid">
                        <!-- Main IPG Card -->
                        <div class="eko-ipg-main" style="background: #faf3ec;">
                            <span class="badge" style="background: rgba(227, 127, 42, 0.1); color: #e37f2a;">Inflasi Terbaru</span>
                            <div class="eko-ipg-value" id="inflasi-main-val" style="color: #e37f2a; font-size: 56px;">-</div>
                            <div class="eko-ipg-growth" id="inflasi-main-desc">Bulan -</div>
                        </div>

                        <!-- Histogram Chart Area -->
                        <div class="eko-ipg-chart-box" style="background: #faf3ec;">
                            <div class="eko-chart-header" style="margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <h4 class="eko-chart-title" style="font-size: 16px;">Grafik Inflasi Bulanan</h4>
                                    <span class="eko-chart-subtitle" id="inflasi-chart-subtitle">Kota Batam (Persen)</span>
                                </div>
                                <select id="inflasi-year-select" class="form-select form-select-sm" style="width: auto; background-color: #ffffff; border: 1px solid #dee2e6; color: #333; font-weight: 600; cursor: pointer; border-radius: 6px; padding: 4px 28px 4px 12px; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
                                    <option value="2026" selected>2026</option>
                                    <option value="2025">2025</option>
                                    <option value="2024">2024</option>
                                    <option value="2023">2023</option>
                                    <option value="2022">2022</option>
                                    <option value="2021">2021</option>
                                    <option value="2020">2020</option>
                                </select>
                            </div>
                            <div class="eko-histogram" id="inflasiHistogram" style="height: 180px;">
                            </div>
                        </div>
                    </div>
                    
                    <div class="eko-description" style="margin-top: 24px; background: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #eaeaea; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
                        <p style="color: #444; margin: 0;">Inflasi bulan ke bulan (m-to-m) membandingkan indeks harga konsumen bulan berjalan dengan bulan sebelumnya. Angka yang positif menunjukkan inflasi (kenaikan harga), sedangkan angka negatif menunjukkan deflasi (penurunan harga).</p>
                    </div>
                </div>
            </div>
        </div>
        
        <script src="assets/data/inflasi.js"></script>
        <script>
        (function() {
            const WILAYAH_KEY = 'batam';
            const yearSelect = document.getElementById('inflasi-year-select');
            
            function updateInflasi() {
                if (typeof dataInflasi === 'undefined') return;
                const wData = dataInflasi.wilayah[WILAYAH_KEY];
                if(!wData) return;
                
                const selectedYear = yearSelect.value;
                const vals = wData.tahunan[selectedYear] || Array(12).fill(null);
                
                let latestVal = null;
                let latestMonthIdx = -1;
                for(let i = 11; i >= 0; i--) {
                   if(vals[i] !== null && vals[i] !== undefined) {
                      latestVal = vals[i];
                      latestMonthIdx = i;
                      break;
                   }
                }
                
                if (latestVal !== null) {
                    document.getElementById('inflasi-main-val').textContent = latestVal.toString().replace('.', ',') + '%';
                    document.getElementById('inflasi-main-desc').textContent = dataInflasi.bulan[latestMonthIdx] + ' ' + selectedYear;
                } else {
                    document.getElementById('inflasi-main-val').textContent = '-';
                    document.getElementById('inflasi-main-desc').textContent = 'Belum Ada Data';
                }
                
                document.getElementById('inflasi-chart-subtitle').textContent = 'Tahun ' + selectedYear + ' (Persen)';
                
                document.getElementById('inflasiHistogram').innerHTML = '';
                renderHistogramInflasi('inflasiHistogram', dataInflasi.bulan, vals, '#e37f2a');
            }

            if (yearSelect) {
                yearSelect.addEventListener('change', updateInflasi);
            }
            
            setTimeout(updateInflasi, 100);

            function renderHistogramInflasi(ctxId, years, vals, colorHex) {
                const ctx = document.getElementById(ctxId);
                if (!ctx) return;
                
                const validVals = vals.filter(v => v !== null && v !== undefined);
                if (validVals.length === 0) {
                    ctx.innerHTML = '<div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; color:#999; font-size:14px; font-style:italic;">Belum ada rilis data untuk tahun ini.</div>';
                    return;
                }
                
                const valRange = Math.max(...validVals) - Math.min(...validVals);
                const padding = Math.max(0.2, valRange * 0.2); 
                const minVal = Math.min(...validVals) - padding;
                const maxVal = Math.max(...validVals) + padding;
                const range = maxVal - minVal;

                const yAxis = document.createElement('div');
                yAxis.className = 'eko-y-axis';
                const steps = 3;
                for (let i = steps; i >= 0; i--) {
                    const label = document.createElement('span');
                    const val = (minVal + (range / steps) * i).toFixed(1).replace('.', ',');
                    label.textContent = val;
                    yAxis.appendChild(label);
                }
                ctx.appendChild(yAxis);

                const barsArea = document.createElement('div');
                barsArea.className = 'eko-bars-area';

                const zeroFromTop = (maxVal / range) * 100;
                const zeroLine = document.createElement('div');
                zeroLine.className = 'eko-zero-line';
                zeroLine.style.top = zeroFromTop + '%';
                zeroLine.style.position = 'absolute';
                zeroLine.style.left = '0';
                zeroLine.style.right = '0';
                zeroLine.style.height = '1px';
                zeroLine.style.background = '#e0e0e0';
                zeroLine.style.zIndex = '1';
                barsArea.appendChild(zeroLine);

                years.forEach((yr, i) => {
                    const val = vals[i];
                    const barGroup = document.createElement('div');
                    barGroup.className = 'eko-bar-group';

                    if (val !== null && val !== undefined) {
                        const bar = document.createElement('div');
                        bar.className = 'eko-bar' + (val < 0 ? ' eko-bar-negative' : '');
                        
                        bar.style.background = `linear-gradient(180deg, ${colorHex} 0%, ${colorHex}dd 100%)`;
                        bar.style.boxShadow = `0 -2px 8px ${colorHex}33`;

                        const heightPct = (Math.abs(val) / range) * 100;

                        if (val >= 0) {
                            bar.style.height = '0%';
                            bar.style.bottom = (100 - zeroFromTop) + '%';
                            bar.style.position = 'absolute';
                            bar.style.left = '0';
                            bar.style.right = '0';
                            setTimeout(() => { bar.style.height = heightPct + '%'; }, 10 + i * 80);
                        } else {
                            bar.style.height = '0%';
                            bar.style.top = zeroFromTop + '%';
                            bar.style.position = 'absolute';
                            bar.style.left = '0';
                            bar.style.right = '0';
                            setTimeout(() => { bar.style.height = heightPct + '%'; }, 10 + i * 80);
                        }

                        const valLabel = document.createElement('span');
                        valLabel.className = 'eko-bar-value';
                        valLabel.textContent = val.toFixed(2).replace('.', ',');
                        bar.appendChild(valLabel);
                        
                        const yrLabel = document.createElement('span');
                        yrLabel.className = 'eko-bar-year';
                        yrLabel.textContent = yr;
                        barGroup.appendChild(bar);
                        barGroup.appendChild(yrLabel);
                        barsArea.appendChild(barGroup);
                    }
                });
                ctx.appendChild(barsArea);
            }
        })();
        </script>
    </div>
"""

new_sections = pe_wrapped + ipm_wrapped + ipg_wrapped + tpt_wrapped + kem_wrapped + pdrb_wrapped + inflasi_wrapped

head = content[:pe_start]
tail = content[end_potensi:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(head + '\n        <div class="style-69">\n' + new_sections + '\n        </div>\n' + tail)

print("Recovered successfully!")
