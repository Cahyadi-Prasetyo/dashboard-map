import glob
import re

files = glob.glob("*.html")

replacements = [
    # Ekonomi 1
    (
        "Perkembangan produksi barang dan jasa di suatu wilayah perekonomian pada tahun tertentu terhadap nilai tahun sebelumnya yang dihitung berdasarkan PDB/PDRB atas dasar harga konstan.",
        "Perkembangan produksi barang dan jasa suatu wilayah terhadap tahun sebelumnya berdasarkan PDRB konstan."
    ),
    (
        "Pertumbuhan ekonomi dihitung berdasarkan persentase perubahan Produk Domestik Regional Bruto (PDRB) Atas Dasar Harga Konstan (ADHK) dibandingkan dengan periode sebelumnya.",
        "Persentase perubahan PDRB Atas Dasar Harga Konstan (ADHK) dibandingkan dengan periode sebelumnya."
    ),
    # IPM
    (
        "Ukuran ringkas capaian pembangunan manusia yang diukur dari aspek\n                            kesehatan (umur panjang dan sehat), pendidikan (pengetahuan), serta\n                            ekonomi (standar hidup layak).",
        "Ukuran ringkas capaian pembangunan bangsa dari aspek kesehatan, pendidikan, dan standar hidup layak."
    ),
    (
        "Ukuran ringkas capaian pembangunan manusia yang diukur dari aspek kesehatan (umur panjang dan sehat), pendidikan (pengetahuan), serta ekonomi (standar hidup layak).",
        "Ukuran ringkas capaian pembangunan bangsa dari aspek kesehatan, pendidikan, dan standar hidup layak."
    ),
    # IPG
    (
        "Ukuran tingkat peran aktif perempuan dalam kehidupan ekonomi dan politik. Digunakan untuk melihat seberapa besar perempuan berpartisipasi dan mengambil peran sebagai tenaga profesional dan pengambil keputusan.",
        "Ukuran tingkat peran aktif perempuan dalam kegiatan ekonomi dan dalam pengambilan keputusan politik."
    ),
    # TPT
    (
        "Persentase jumlah pengangguran terhadap jumlah angkatan kerja. Indikator ini mengukur seberapa besar penduduk usia kerja yang aktif mencari pekerjaan namun belum mendapatkannya.",
        "Persentase jumlah pengangguran terhadap jumlah angkatan kerja yang mencari pekerjaan namun belum mendapatkannya."
    ),
    # APS
    (
        "Proporsi dari penduduk pada kelompok umur sekolah tertentu yang sedang bersekolah pada tingkat pendidikan yang sesuai dengan usianya. Grafik di bawah memperlihatkan APS untuk kelompok umur 16-18 tahun.",
        "Proporsi penduduk usia 16-18 tahun yang saat ini sedang bersekolah pada tingkat pendidikan sesuai usianya."
    ),
    # Kemiskinan
    (
        "Persentase penduduk yang memiliki rata-rata pengeluaran per kapita per bulan di bawah Garis Kemiskinan. Indikator ini merupakan ukuran kesejahteraan dari sisi pemenuhan kebutuhan dasar (basic needs).",
        "Persentase penduduk daerah yang memiliki rata-rata pengeluaran bulanan di bawah standardisasi Garis Kemiskinan."
    ),
    # Gini
    (
        "Ukuran tingkat ketimpangan/kesenjangan pengeluaran penduduk secara keseluruhan. Nilainya berkisar antara 0 hingga 1. Semakin mendekati angka 1 berarti tingkat ketimpangan semakin tinggi.",
        "Skala ukuran rentang 0-1 untuk menakar tingkat ketimpangan dan kesenjangan distribusi pengeluaran penduduk."
    )
]

row5_addition = """    <!-- ROW 5 -->
    <div class="indikator-wrapper" style="margin-top: 30px;">
        <!-- INDIKATOR 9: INFLASI -->
        <div class="indikator-card">
            <h3>Inflasi Kepulauan Riau</h3>
            <div class="indikator-top">
                <img src="assets/img/potensi.png" alt="Inflasi">
                <div class="indikator-desc">
                    <div class="indikator-info">
                        <div class="indikator-info-header"><div></div><span>Definisi</span></div>
                        <div class="indikator-info-text">Indikator yang mengukur perubahan rata-rata harga sekelompok barang dan jasa yang dikonsumsi masyarakat.</div>
                    </div>
                    <div class="indikator-info">
                        <div class="indikator-info-header"><div></div><span>Metode Perhitungan</span></div>
                        <div class="indikator-info-text">Dihitung dari persentase perubahan Indeks Harga Konsumen (IHK) berjalan terhadap IHK periode sebelumnya.</div>
                    </div>
                </div>
            </div>
            <div class="indikator-chart"><canvas id="chartInflasi"></canvas></div>
            <div class="indikator-insight"><strong>Insight</strong><br>Data inflasi akan segera dialokasikan untuk memonitor stabilitas tingkat harga barang kebutuhan pokok dan daya beli di wilayah Riau.</div>
        </div>
        <!-- INDIKATOR 10: PENDUDUK -->
        <div class="indikator-card">
            <h3>Jumlah Penduduk</h3>
            <div class="indikator-top">
                <img src="assets/img/potensi.png" alt="Demografi">
                <div class="indikator-desc">
                    <div class="indikator-info">
                        <div class="indikator-info-header"><div></div><span>Definisi</span></div>
                        <div class="indikator-info-text">Total populasi individu yang berdomisili secara sah dan mengikat di dalam batas wilayah geografis daerah setempat.</div>
                    </div>
                    <div class="indikator-info">
                        <div class="indikator-info-header"><div></div><span>Metode Perhitungan</span></div>
                        <div class="indikator-info-text">Dihitung berdasarkan hasil proyeksi dari pencatatan registrasi sipil dan pendataan komprehensif sensus penduduk.</div>
                    </div>
                </div>
            </div>
            <div class="indikator-chart"><canvas id="chartPenduduk"></canvas></div>
            <div class="indikator-insight"><strong>Insight</strong><br>Analisis laju pertumbuhan jumlah penduduk dan transisi demografis menjadi fondasi dan baseline bagi strategi kebijakan infrastruktur.</div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Shorten definitions
    for old, new in replacements:
        # Also clean up whitespace variations using regex
        old_regex = re.escape(old).replace(r'\ ', r'\s+').replace(r'\n', r'\s+')
        content = re.sub(old_regex, new, content, flags=re.IGNORECASE)

    # Append new indicators if not already present
    if "Inflasi Kepulauan Riau" not in content:
        content = content.replace("<script src=\"https://cdn.jsdelivr.net/npm/chart.js\"></script>", row5_addition)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML pages updated.")
