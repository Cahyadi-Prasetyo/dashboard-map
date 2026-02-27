Chart.register(ChartDataLabels);
let modalChartInstance = null;

const indicatorInfo = {
    ekonomi: {
        def: 'Pertumbuhan ekonomi mengukur perubahan persentase Produk Domestik Regional Bruto (PDRB) riil dari suatu periode ke periode berikutnya. Ini mencerminkan laju ekspansi atau penyusutan ekonomi wilayah.',
        metode: 'Pertumbuhan Ekonomi = ((PDRB ADHK Tahun t - PDRB ADHK Tahun t-1) / PDRB ADHK Tahun t-1) × 100%',
        img: 'assets/img/pertumbuhan ekonomi.jpg',
        insight: (rn) => `Pertumbuhan ekonomi di ${rn} dipengaruhi oleh aktivitas industri dan pariwisata yang meningkat.`
    },
    pdrb: {
        def: 'PDRB per Kapita adalah rata-rata nilai tambah bruto yang dihasilkan oleh setiap penduduk di suatu wilayah, dihitung dari total PDRB dibagi dengan jumlah penduduk.',
        metode: 'PDRB per Kapita = Total PDRB / Jumlah Penduduk Pertengahan Tahun',
        img: 'assets/img/PDRB perkapita.jpg',
        insight: (rn) => `Nilai PDRB per kapita ${rn} menunjukkan tren positif, merefleksikan peningkatan kesejahteraan dan produktivitas rata-rata.`
    },
    ipm: {
        def: 'Indeks Pembangunan Manusia (IPM) mengukur capaian pembangunan manusia berbasis tiga dimensi dasar: Umur pajang dan hidup sehat, pengetahuan, dan standar hidup layak.',
        metode: 'Dihitung melalui rata-rata geometrik dari indeks kesehatan, indeks pendidikan, dan indeks pengeluaran riil.',
        img: 'assets/img/IPM.jpg',
        insight: (rn) => `${rn} konsisten berada di kategori 'Tinggi' atau 'Sangat Tinggi' terhadap kualitas hidup masyarakatnya.`
    },
    ipg: {
        def: 'Indeks Pembangunan Gender (IPG) mengukur kesenjangan pencapaian pembangunan manusia antara partisipasi laki-laki dan perempuan.',
        metode: 'IPG = IPM Perempuan / IPM Laki-Laki × 100',
        img: 'assets/img/IPG.jpeg',
        insight: (rn) => `Kesetaraan gender dalam akses pendidikan dan kesehatan di ${rn} semakin baik dari tahun ke tahun.`
    },
    tpt: {
        def: 'Tingkat Pengangguran Terbuka (TPT) adalah persentase angkatan kerja yang tidak memiliki pekerjaan secara aktif mencari, mempersiapkan usaha, atau menunggu keputusan pekerjaan.',
        metode: 'TPT = (Jumlah Pengangguran / Jumlah Angkatan Kerja) × 100%',
        img: 'assets/img/TPT.jpg',
        insight: (rn) => `Fluktuasi TPT di ${rn} selaras dengan dinamisnya serapan tenaga kerja di sektor industri pengolahan.`
    },
    aps: {
        def: 'Angka Partisipasi Sekolah (APS) mengukur proporsi penduduk pada kelompok usia jenjang sekolah tertentu yang sedang bersekolah.',
        metode: 'APS = (Penduduk Usia 16-18 Sekolah / Penduduk Usia 16-18 Tahun) × 100%',
        img: 'assets/img/APS.jpg',
        insight: (rn) => `Kesadaran masyarakat ${rn} untuk menuntaskan wajib belajar 12 tahun terus menunjukkan perkembangan pesat.`
    },
    kemiskinan: {
        def: 'Persentase Penduduk Miskin didefinisikan sebagai rasio jumlah penduduk yang memiliki rata-rata pengeluaran per kapita di bawah Garis Kemiskinan terhadap total penduduk.',
        metode: 'Headcount Index (P0) berdasarkan data Survei Sosial Ekonomi Nasional (Susenas).',
        img: 'assets/img/kemiskinan.jpg',
        insight: (rn) => `Intervensi program bantuan sosial terbukti efektif menekan rasio kemiskinan di ${rn}.`
    },
    gini: {
        def: 'Gini Ratio mengukur seberapa merata pengeluaran/pendapatan di antara penduduk dalam suatu wilayah. Bernilai 0 (pemerataan sempurna) hingga 1 (ketimpangan sempurna).',
        metode: 'Dihitung menggunakan Kurva Lorenz yang membandingkan proporsi pengeluaran kumulatif dan populasi kumulatif.',
        img: 'assets/img/giniratio.jpeg',
        insight: (rn) => `Ketimpangan pengeluaran antar golongan masyarakat di ${rn} relatif rendah dan dalam kondisi stabil.`
    },
    penduduk: {
        def: 'Sensus Penduduk mencatat total populasi seluruh penduduk (WNI & WNA) baik yang menetap maupun yang berpindah sementara waktu di wilayah administratif.',
        metode: 'Pencacahan lengkap lapangan secara de facto dan de jure setiap 10 tahun (SP2020).',
        img: 'assets/img/kepri2.png',
        insight: (rn) => `Konsentrasi penduduk terbesar di ${rn} masih berada di wilayah-wilayah yang dekat dengan kawasan industri.`
    },
    inflasi: {
        def: 'Inflasi adalah tren kenaikan harga barang dan jasa secara umum dan terus menerus dalam waktu tertentu. Y-on-Y membandingkan inflasi bulan ini dengan bulan yang sama tahun sebelumnya.',
        metode: 'Persentase kenaikan Indeks Harga Konsumen (IHK).',
        img: 'assets/img/aset1.png',
        insight: (rn) => `Tingkat inflasi ${rn} terjaga berkat pasokan bahan pangan yang stabil antar pulau.`
    },
    wisman: {
        def: 'Wisatawan Mancanegara (Wisman) mencatat jumlah turis internasional yang masuk ke pintu-pintu kedatangan pelabuhan/bandara internasional di wilayah tersebut.',
        metode: 'Kompilasi dokumen keimigrasian di titik TPI (Tempat Pemeriksaan Imigrasi).',
        img: 'assets/img/wisman.png',
        // untuk wisman, insight kita ambil dari data object karena sudah dibikin di js
        dynamicInsight: true
    },
    ekspor: {
        def: 'Ekspor adalah nilai total arus keluar barang komoditas (migas dan non-migas) yang dijual ke luar negeri.',
        metode: 'Pencatatan dari Dokumen Pemberitahuan Ekspor Barang (PEB) yang disahkan Bea Cukai.',
        img: 'assets/img/import-export.png',
        dynamicInsight: true
    },
    impor: {
        def: 'Impor adalah nilai arus kedatangan barang komoditas dari luar kawasan pabean Indonesia yang dibongkar di pelabuhan terdaftar.',
        metode: 'Pencatatan dari Pemberitahuan Impor Barang (PIB) yang disahkan Bea Cukai.',
        img: 'assets/img/import-export.png',
        dynamicInsight: true
    }
};

function openModal(type, regionKey = 'kepri', regionName = 'Provinsi Kepulauan Riau') {
    const overlay = document.getElementById('modalOverlay');
    const title = document.getElementById('modalTitle');
    const ctx = document.getElementById('modalChart');

    // Rich content IDs
    const imgEl = document.getElementById('modalImg');
    const defEl = document.getElementById('modalDef');
    const metEl = document.getElementById('modalMetode');
    const insEl = document.getElementById('modalInsight');

    const info = indicatorInfo[type];
    if (info) {
        imgEl.src = info.img || 'assets/img/potensi.png';
        defEl.textContent = info.def || '-';
        metEl.textContent = info.metode || '-';
        insEl.textContent = typeof info.insight === 'function' ? info.insight(regionName) : '-';
    }

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
            let dataArr = d && d.tahunan ? d.tahunan : [];
            return { type: 'bar', data: { labels: dataEkonomi.tahun, datasets: [{ label: 'Pertumbuhan Ekonomi (%)', data: dataArr, backgroundColor: 'rgba(59,130,246,0.7)', borderRadius: 6 }] }, options: barOpts('%') };
        },
        pdrb: () => {
            title.textContent = `PDRB per Kapita ${regionName}`;
            let dataArr = dataPdrb[regionKey] || [];
            return { type: 'bar', data: { labels: [2020, 2021, 2022, 2023, 2024], datasets: [{ label: 'PDRB per Kapita (Ribu Rp)', data: dataArr, backgroundColor: 'rgba(16,185,129,0.7)', borderRadius: 6 }] }, options: barOpts('Rb') };
        },
        ipm: () => {
            title.textContent = `Indeks Pembangunan Manusia (IPM) ${regionName}`;
            const d = dataIpm.wilayah[regionKey];
            let dataArr = d && d.tahunan ? d.tahunan : [];
            return { type: 'line', data: { labels: dataIpm.tahun, datasets: [{ label: 'IPM', data: dataArr, borderColor: '#7c3aed', backgroundColor: 'rgba(124,58,237,0.1)', fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#7c3aed', pointBorderColor: '#fff', pointBorderWidth: 2 }] }, options: lineOpts('') };
        },
        ipg: () => {
            title.textContent = `Indeks Pembangunan Gender (IPG) ${regionName}`;
            const d = dataIpg.wilayah[regionKey];
            let dataArr = d && d.tahunan ? d.tahunan : [];
            return { type: 'line', data: { labels: dataIpg.tahun, datasets: [{ label: 'IPG', data: dataArr, borderColor: '#ec4899', backgroundColor: 'rgba(236,72,153,0.1)', fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#ec4899', pointBorderColor: '#fff', pointBorderWidth: 2 }] }, options: lineOpts('') };
        },
        tpt: () => {
            title.textContent = `Tingkat Pengangguran Terbuka (TPT) ${regionName}`;
            const d = dataTpt.wilayah[regionKey];
            let dataArr = d && d.tahunan ? d.tahunan : [];
            return { type: 'bar', data: { labels: dataTpt.tahun, datasets: [{ label: 'TPT (%)', data: dataArr, backgroundColor: 'rgba(239,68,68,0.7)', borderRadius: 6 }] }, options: barOpts('%') };
        },
        aps: () => {
            title.textContent = `Angka Partisipasi Sekolah (APS) SMA/SMK ${regionName}`;
            const d = dataAps.wilayah[regionKey];
            let dataArr = d && d.tahunan ? d.tahunan : [];
            return { type: 'line', data: { labels: dataAps.tahun, datasets: [{ label: 'APS', data: dataArr, borderColor: '#0d9488', backgroundColor: 'rgba(13,148,136,0.1)', fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#0d9488', pointBorderColor: '#fff', pointBorderWidth: 2 }] }, options: lineOpts('') };
        },
        kemiskinan: () => {
            title.textContent = `Angka Kemiskinan ${regionName}`;
            const d = dataKemiskinan.wilayah[regionKey];
            let dataArr = d && d.tahunan ? d.tahunan : [];
            return { type: 'bar', data: { labels: dataKemiskinan.tahun, datasets: [{ label: 'Kemiskinan (%)', data: dataArr, backgroundColor: 'rgba(245,158,11,0.7)', borderRadius: 6 }] }, options: barOpts('%') };
        },
        gini: () => {
            title.textContent = `Gini Ratio ${regionName}`;
            const d = dataGini.wilayah[regionKey];
            let dataArr = d && d.tahunan ? d.tahunan : [];
            return { type: 'line', data: { labels: dataGini.tahun, datasets: [{ label: 'Gini Ratio', data: dataArr, borderColor: '#f59e0b', backgroundColor: 'rgba(245,158,11,0.1)', fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#f59e0b', pointBorderColor: '#fff', pointBorderWidth: 2 }] }, options: lineOpts('') };
        },
        penduduk: () => {
            title.textContent = `Jumlah Penduduk ${regionName} (Sensus Penduduk)`;
            let dataArr = dataPenduduk[regionKey] || [];
            return { type: 'bar', data: { labels: ['SP 2010', 'SP 2020'], datasets: [{ label: 'Jumlah Penduduk (jiwa)', data: dataArr, backgroundColor: ['rgba(59,130,246,0.7)', 'rgba(16,185,129,0.7)'], borderRadius: 8, barThickness: 40 }] }, options: { responsive: true, maintainAspectRatio: false, indexAxis: 'y', plugins: { legend: { display: false }, datalabels: { anchor: 'end', align: 'right', formatter: (v) => v.toLocaleString('id-ID') + ' jiwa', font: { weight: 'bold', size: 11 }, color: '#1e293b' } }, scales: { x: { display: false }, y: { grid: { display: false }, border: { display: false } } }, layout: { padding: { right: 120 } } } };
        },
        inflasi: () => {
            title.textContent = `Tingkat Inflasi Y-on-Y ${regionName}, Januari 2026`;
            let dataArr = [];
            if (regionKey === 'karimun') dataArr = [-0.73, -0.15, 2.30, 0.87, -0.15, 0.40, 1.92, 2.91, 2.58, 2.43, 2.72, 2.77];
            else {
                const d = dataInflasi.wilayah[regionKey]?.tahunan;
                if (d && d['2025']) {
                    const jan26 = d['2026']?.[0] || 0;
                    dataArr = [...d['2025'].slice(1), jan26];
                }
            }
            if (dataArr.length === 0) dataArr = [0];
            return { type: 'line', data: { labels: ['Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Ags', 'Sep', 'Okt', 'Nov', 'Des', 'Jan 26'], datasets: [{ label: 'Inflasi Y-on-Y (%)', data: dataArr, borderColor: gradientLine, backgroundColor: gradientFill, fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#7c3aed', pointBorderColor: '#fff', pointBorderWidth: 2 }] }, options: lineOpts('%') };
        },
        wisman: () => {
            title.textContent = `Kunjungan Wisman ${regionName}`;
            let dataObj = wismanData[regionKey] || { labels: [], values: [], insight: '-' };
            insEl.textContent = dataObj.insight;
            return { type: 'line', data: { labels: dataObj.labels, datasets: [{ label: 'Kunjungan Wisman', data: dataObj.values, borderColor: '#0ea5e9', backgroundColor: 'rgba(14,165,233,0.1)', fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#0ea5e9', pointBorderColor: '#fff', pointBorderWidth: 2 }] }, options: lineOpts(' kunjungan') };
        },
        ekspor: () => {
            title.textContent = `Nilai Ekspor ${regionName}`;
            let dataObj = eksporData[regionKey] || { labels: [], values: [], insight: '-' };
            insEl.textContent = dataObj.insight;
            return { type: 'bar', data: { labels: dataObj.labels, datasets: [{ label: 'Ekspor (Juta USD)', data: dataObj.values, backgroundColor: 'rgba(16,185,129,0.7)', borderRadius: 6 }] }, options: barOpts(' Juta USD') };
        },
        impor: () => {
            title.textContent = `Nilai Impor ${regionName}`;
            let dataObj = imporData[regionKey] || { labels: [], values: [], insight: '-' };
            insEl.textContent = dataObj.insight;
            return { type: 'bar', data: { labels: dataObj.labels, datasets: [{ label: 'Impor (Juta USD)', data: dataObj.values, backgroundColor: 'rgba(239,68,68,0.7)', borderRadius: 6 }] }, options: barOpts(' Juta USD') };
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
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false }, datalabels: { anchor: 'end', align: 'top', formatter: (v) => v.toLocaleString('id-ID') + suffix, font: { weight: 'bold', size: 11 }, color: '#1e293b' } },
        scales: { y: { display: false }, x: { grid: { display: false }, border: { display: false } } },
        layout: { padding: { top: 30 } }
    };
}
function lineOpts(suffix) {
    return {
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false }, datalabels: { align: 'top', offset: 6, formatter: (v) => v.toLocaleString('id-ID') + suffix, font: { weight: 'bold', size: 11 }, color: '#1e293b' } },
        scales: { y: { display: false }, x: { grid: { display: false }, border: { display: false }, ticks: { font: { size: 10 } } } },
        layout: { padding: { top: 30, bottom: 10 } }
    };
}
