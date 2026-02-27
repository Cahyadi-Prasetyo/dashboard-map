import re

html_cards = """    <div class="style-129" style="background-color: transparent;">
        <div class="style-130">
            <div class="style-131">
                <div class="style-132">
                    <div class="style-133">
                        <br><br><br>
                        <h4 class="style-134" style="text-align: center; font-size: 28px; font-weight: bold; color: #1e293b;">Indikator Strategis</h4>
                        <p class="style-135" style="text-align: center; font-size: 16px; color: #475569; max-width: 800px; margin: 0 auto 30px;">Indikator strategis ini digunakan untuk memantau kinerja pembangunan Kabupaten Karimun meliputi pertumbuhan ekonomi, kemiskinan, ketenagakerjaan, dan kualitas pembangunan manusia sebagai dasar perencanaan dan evaluasi kebijakan daerah.</p>
                        <!----><i class="bi bi-eye-fill"></i>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="indikator-container">
            <div class="indikator-card" onclick="openModal('ekonomi', 'karimun', 'Kabupaten Karimun')">
                <div class="indikator-icon" style="background-image:url('assets/img/in1.png')"></div>
                <p class="indikator-title">Pertumbuhan Ekonomi (y-on-y)</p>
                <h3 class="indikator-value">7,89<br><span>persen</span></h3>
                <p class="indikator-date">Triwulan IV 2024</p>
            </div>

            <!-- Card 2 -->
             <div class="indikator-card" onclick="openModal('pdrb', 'karimun', 'Kabupaten Karimun')">
                <div class="indikator-icon" style="background-image:url('assets/img/in2.png')"></div>
                <p class="indikator-title">PDRB per Kapita</p>
                <h3 class="indikator-value">161.424<br><span>ribu rupiah</span></h3>
                <p class="indikator-date">2024</p>
            </div>

            <!-- Card 3 -->
            <div class="indikator-card" onclick="openModal('ipm', 'karimun', 'Kabupaten Karimun')">
                <div class="indikator-icon" style="background-image:url('assets/img/healthy.png')"></div>
                <p class="indikator-title">IPM</p>
                <h3 class="indikator-value">80,53<br><span>persen</span></h3>
                <p class="indikator-date">2025</p>
            </div>

            <!-- Card 4 -->
            <div class="indikator-card" onclick="openModal('ipg', 'karimun', 'Kabupaten Karimun')">
                <div class="indikator-icon" style="background-image:url('assets/img/IPG.png')"></div>
                <p class="indikator-title">IPG</p>
                <h3 class="indikator-value">94,2<br><span> </span></h3>
                <p class="indikator-date">2024</p>
            </div>

            <!-- Card 5 -->
            <div class="indikator-card" onclick="openModal('tpt', 'karimun', 'Kabupaten Karimun')">
                <div class="indikator-icon" style="background-image:url('assets/img/TPT.png')"></div>
                <p class="indikator-title">TPT</p>
                <h3 class="indikator-value">6,35<br><span>persen</span></h3>
                <p class="indikator-date">November 2025</p>
            </div>

            <!-- Card 6 -->
            <div class="indikator-card" onclick="openModal('aps', 'karimun', 'Kabupaten Karimun')">
                <div class="indikator-icon" style="background-image:url('assets/img/APS.png')"></div>
                <p class="indikator-title">APS SMA/SMK</p>
                <h3 class="indikator-value">88,24<br><span></span></h3>
                <p class="indikator-date">2025</p>
            </div>

            <!-- Card 7 -->
            <div class="indikator-card" onclick="openModal('kemiskinan', 'karimun', 'Kabupaten Karimun')">
                <div class="indikator-icon" style="background-image:url('assets/img/poverty.png')"></div>
                <p class="indikator-title">Kemiskinan</p>
                <h3 class="indikator-value">4,44<br><span>persen</span></h3>
                <p class="indikator-date">Maret 2025</p>
            </div>

            <!-- Card 8 -->
            <div class="indikator-card" onclick="openModal('gini', 'karimun', 'Kabupaten Karimun')">
                <div class="indikator-icon" style="background-image:url('assets/img/IPM.png')"></div>
                <p class="indikator-title">Gini Ratio</p>
                <h3 class="indikator-value">0,385<br><span>persen</span></h3>
                <p class="indikator-date">September 2025</p>
            </div>

            <div class="indikator-card" onclick="openModal('penduduk', 'karimun', 'Kabupaten Karimun')">
                <div class="indikator-icon" style="background-image:url('assets/img/output-onlinepngtools.png'); filter: invert(1);"></div>
                <p class="indikator-title">Penduduk</p>
                <h3 class="indikator-value">2.064.564<br><span>jiwa</span></h3>
                <p class="indikator-date">Hasil SP2020</p>
            </div>

            <div class="indikator-card" onclick="openModal('inflasi', 'karimun', 'Kabupaten Karimun')">
                <div class="indikator-icon" style="background-image:url('assets/img/indonesian-rupiah.png'); filter: invert(1);"></div>
                <p class="indikator-title">Inflasi (Y-on-Y)</p>
                <h3 class="indikator-value">2,94<br><span>persen</span></h3>
                <p class="indikator-date">Januari 2026</p>
            </div>
        </div>
    </div>
"""

with open('karimun.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the start and end of the block to be replaced 
# (From "<div class="style-129">" which is the Indikator Strategis title banner equivalent down to before the MODAL part)
# Actually in karimun.html the big detail-wrapper grid starts right after the hero carousel ends
# In karimun.html, we find:
# <div class="detail-wrapper">
# ...
# </div> (multiple wrappers)
# down to the start of <!-- MODAL -->

# Let's replace everything from the first `<div class="detail-wrapper">` up to `<!-- MODAL -->`
pattern = re.compile(r'<div class="detail-wrapper">.*?<!-- MODAL -->', re.DOTALL)
new_content = pattern.sub(html_cards + '\n\n    <!-- MODAL -->', content)

with open('karimun.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Karimun big cards replaced with small index grid.")
