
Chart.register(ChartDataLabels);
let modalChartInstance = null;

const indicatorInfo = {
    ekonomi: {
        def: 'Indikator ekonomi makro yang menggambarkan seberapa jauh keberhasilan pembangunan suatu daerah dalam periode waktu tertentu',
        img: 'assets/img/pertumbuhan ekonomi.jpg',
        insight: (rn) => `Pertumbuhan ekonomi di ${rn} berfluktuasi dan membaik pasca 2020.`
    },
    tpt: {
        def: 'Persentase jumlah pengangguran terhadap jumlah angkatan kerja',
        img: 'assets/img/TPT.jpg',
        insight: (rn) => `Tingkat pengangguran terbuka di ${rn} menunjukkan tren penurunan yang positif.`
    },
    pdrb: {
        def: 'Nilai PDRB dibagi jumlah penduduk dalam suatu wilayah pada periode tertentu',
        img: 'assets/img/PDRB perkapita.jpg',
        insight: (rn) => `PDRB per kapita ${rn} konsisten meningkat dari tahun ke tahun.`
    },
    ipm: {
        def: 'Indikator yang mengukur kualitas hidup penduduk berdasarkan kesehatan, pendidikan, dan standar hidup layak.',
        img: 'assets/img/IPM.jpg',
        insight: (rn) => `Kualitas hidup di ${rn} selalu mengalami peningkatan yang stabil.`
    },
    aps: {
        def: 'Persentase penduduk usia sekolah SMA/SMK yang sedang menempuh pendidikan per 1,000 jumlah penduduk usia pendidikan menengah.',
        img: 'assets/img/APS.jpg',
        insight: (rn) => `Angka partisipasi sekolah tingkat menengah di ${rn} semakin membaik.`
    },
    ipg: {
        def: 'Indikator yang mengukur kesetaraan capaian pembangunan manusia antara laki-laki dan perempuan.',
        img: 'assets/img/IPG.jpeg',
        insight: (rn) => `Kesetaraan pembangunan gender di ${rn} stabil dan terjaga dengan baik.`
    },
    kemiskinan: {
        def: 'Persentase penduduk yang memiliki pengeluaran per kapita di bawah garis kemiskinan.',
        img: 'assets/img/kemiskinan.jpg',
        insight: (rn) => `Angka kemiskinan di ${rn} terus ditekan dan berangsur turun.`
    },
    gini: {
        def: 'Indikator yang menunjukkan tingkat ketimpangan pengeluaran secara menyeluruh',
        img: 'assets/img/giniratio.jpeg',
        insight: (rn) => `Ketimpangan pengeluaran di ${rn} relatif stabil dan tergolong moderat.`
    },
    inflasi: {
        def: 'Persentase kenaikan harga barang dan jasa secara umum dan terus-menerus dalam periode tertentu.',
        img: 'assets/img/aset1.png',
        insight: (rn) => `Tingkat inflasi di ${rn} cukup dinamis namun tetap terkendali.`
    },
    penduduk: {
        def: 'Total orang yang tinggal dan menetap di suatu wilayah pada waktu tertentu.',
        img: 'assets/img/kepri2.png',
        insight: (rn) => `Jumlah penduduk di ${rn} bertambah secara proporsional berdasar sensus terbaru.`
    },
    wisman: {
        def: 'Jumlah kunjungan wisatawan asing ke suatu wilayah dalam periode tertentu.',
        img: 'assets/img/wisman.png',
        insight: (rn) => `Kunjungan wisman di ${rn} meningkat tajam menandakan pemulihan pariwisata.`
    },
    ekspor: {
        def: 'Nilai atau volume barang dan jasa yang dijual ke luar negeri dalam periode tertentu.',
        img: 'assets/img/import (1).png',
        insight: (rn) => `Aktivitas ekspor ${rn} menunjukkan tren pertumbuhan yang solid.`
    },
    impor: {
        def: 'Nilai atau volume barang dan jasa yang dibeli dari luar negeri dalam periode tertentu.',
        img: 'assets/img/export (2).png',
        insight: (rn) => `Nilai impor di ${rn} meningkat sejalan dengan kebutuhan suplai industri.`
    }
};

function openModal(type, regionKey = 'kepulauan_riau', regionName = 'Kepulauan Riau') {
    const overlay = document.getElementById('modalOverlay');
    const title = document.getElementById('modalTitle');
    const ctx = document.getElementById('modalChart');

    const imgEl = document.getElementById('modalImg');
    const defEl = document.getElementById('modalDef');
    const insEl = document.getElementById('modalInsight');

    const info = indicatorInfo[type];
    if (info && imgEl && defEl && insEl) {
        imgEl.src = info.img || 'assets/img/potensi.png';
        defEl.textContent = info.def || '-';
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
            title.textContent = `Pertumbuhan Ekonomi (y-on-y) ${regionName}`;
            let dataArr = [];
            let labelsArr = dataEkonomi.tahun;

            if (dataEkonomi.triwulanan && dataEkonomi.triwulanan[regionKey]) {
                dataArr = dataEkonomi.triwulanan[regionKey].y_on_y || [];
                labelsArr = ['Triwulan I', 'Triwulan II', 'Triwulan III', 'Triwulan IV'];
            } else {
                const d = dataEkonomi.wilayah[regionKey];
                if (d && d.tahunan) { dataArr = d.tahunan; }
            }

            return { type: 'bar', data: { labels: labelsArr, datasets: [{ label: 'Pertumbuhan Ekonomi (%)', data: dataArr, backgroundColor: 'rgba(59,130,246,0.7)', borderRadius: 6 }] }, options: barOpts('%') };
        },
        pdrb: () => {
            title.textContent = `PDRB per Kapita ${regionName}`;
            let dataArr = [];
            if (dataPdrb[regionKey]) { dataArr = dataPdrb[regionKey]; }
            return { type: 'bar', data: { labels: [2020, 2021, 2022, 2023, 2024], datasets: [{ label: 'PDRB per Kapita (Ribu Rp)', data: dataArr, backgroundColor: 'rgba(16,185,129,0.7)', borderRadius: 6 }] }, options: barOpts('Rb') };
        },
        ipm: () => {
            title.textContent = `Indeks Pembangunan Manusia (IPM) ${regionName}`;
            const d = dataIpm.wilayah[regionKey];
            let dataArr = [];
            if (d && d.tahunan) { dataArr = d.tahunan; }
            return { type: 'line', data: { labels: dataIpm.tahun, datasets: [{ label: 'IPM', data: dataArr, borderColor: '#7c3aed', backgroundColor: 'rgba(124,58,237,0.1)', fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#7c3aed', pointBorderColor: '#fff', pointBorderWidth: 2 }] }, options: lineOpts('') };
        },
        ipg: () => {
            title.textContent = `Indeks Pembangunan Gender (IPG) ${regionName}`;
            const d = dataIpg.wilayah[regionKey];
            let dataArr = [];
            if (d && d.tahunan) { dataArr = d.tahunan; }
            return { type: 'line', data: { labels: dataIpg.tahun, datasets: [{ label: 'IPG', data: dataArr, borderColor: '#ec4899', backgroundColor: 'rgba(236,72,153,0.1)', fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#ec4899', pointBorderColor: '#fff', pointBorderWidth: 2 }] }, options: lineOpts('') };
        },
        tpt: () => {
            title.textContent = `Tingkat Pengangguran Terbuka (TPT) ${regionName}`;
            const d = dataTpt.wilayah[regionKey];
            let dataArr = [];
            if (d && d.tahunan) { dataArr = d.tahunan; }
            return { type: 'bar', data: { labels: dataTpt.tahun, datasets: [{ label: 'TPT (%)', data: dataArr, backgroundColor: 'rgba(239,68,68,0.7)', borderRadius: 6 }] }, options: barOpts('%') };
        },
        aps: () => {
            title.textContent = `Angka Partisipasi Sekolah (APS) SMA/SMK ${regionName}`;
            const d = dataAps.wilayah[regionKey];
            let dataArr = [];
            if (d && d.tahunan) { dataArr = d.tahunan; }
            return { type: 'line', data: { labels: dataAps.tahun, datasets: [{ label: 'APS', data: dataArr, borderColor: '#0d9488', backgroundColor: 'rgba(13,148,136,0.1)', fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#0d9488', pointBorderColor: '#fff', pointBorderWidth: 2 }] }, options: lineOpts('') };
        },
        kemiskinan: () => {
            title.textContent = `Angka Kemiskinan ${regionName}`;
            const d = dataKemiskinan.wilayah[regionKey];
            let dataArr = [];
            if (d && d.tahunan) { dataArr = d.tahunan; }
            return { type: 'bar', data: { labels: dataKemiskinan.tahun, datasets: [{ label: 'Kemiskinan (%)', data: dataArr, backgroundColor: 'rgba(245,158,11,0.7)', borderRadius: 6 }] }, options: barOpts('%') };
        },
        gini: () => {
            title.textContent = `Gini Ratio ${regionName}`;
            const d = dataGini.wilayah[regionKey];
            let dataArr = [];
            if (d && d.tahunan) { dataArr = d.tahunan; }
            return { type: 'line', data: { labels: dataGini.tahun, datasets: [{ label: 'Gini Ratio', data: dataArr, borderColor: '#f59e0b', backgroundColor: 'rgba(245,158,11,0.1)', fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#f59e0b', pointBorderColor: '#fff', pointBorderWidth: 2 }] }, options: lineOpts('') };
        },
        penduduk: () => {
            title.textContent = `Jumlah Penduduk ${regionName} (Sensus Penduduk)`;
            let dataArr = [];
            if (dataPenduduk[regionKey]) { dataArr = dataPenduduk[regionKey]; }
            return { type: 'bar', data: { labels: ['SP 2010', 'SP 2020'], datasets: [{ label: 'Jumlah Penduduk (jiwa)', data: dataArr, backgroundColor: ['rgba(59,130,246,0.7)', 'rgba(16,185,129,0.7)'], borderRadius: 8, barThickness: 60 }] }, options: { responsive: true, maintainAspectRatio: false, indexAxis: 'y', plugins: { legend: { display: false }, datalabels: { anchor: 'end', align: 'right', formatter: (v) => v.toLocaleString('id-ID') + ' jiwa', font: { weight: 'bold', size: 12 }, color: '#1e293b' } }, scales: { x: { display: false }, y: { grid: { display: false }, border: { display: false } } }, layout: { padding: { right: 120 } } } };
        },
        inflasi: () => {
            title.textContent = `Tingkat Inflasi Y-on-Y ${regionName}, Januari 2026`;

            // Hardcode Y-on-Y arrays based on user screenshots or available data
            let dataArr = [];
            if (regionKey === 'karimun') {
                dataArr = [-0.73, -0.15, 2.30, 0.87, -0.15, 0.40, 1.92, 2.91, 2.58, 2.43, 2.72, 2.77];
            } else {
                const d = dataInflasi.wilayah[regionKey]?.tahunan;
                if (d && d['2025']) {
                    const jan26 = d['2026']?.[0] || 0;
                    dataArr = [...d['2025'].slice(1), jan26];
                }
            }
            if (dataArr.length === 0) dataArr = [0];

            return { type: 'line', data: { labels: ['Feb 25', 'Mar 25', 'Apr 25', 'Mei 25', 'Jun 25', 'Jul 25', 'Ags 25', 'Sep 25', 'Okt 25', 'Nov 25', 'Des 25', 'Jan 26'], datasets: [{ label: 'Inflasi Y-on-Y (%)', data: dataArr, borderColor: gradientLine, backgroundColor: gradientFill, fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#7c3aed', pointBorderColor: '#fff', pointBorderWidth: 2, pointHoverRadius: 7 }] }, options: lineOpts('%') };
        },
        wisman: () => {
            title.textContent = `Kunjungan Wisman ${regionName}`;
            return { type: 'line', data: { labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul'], datasets: [{ label: 'Kunjungan Wisman', data: [120000, 150000, 180000, 195000, 205000, 215000, 223456], borderColor: '#0ea5e9', backgroundColor: 'rgba(14,165,233,0.1)', fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#0ea5e9', pointBorderColor: '#fff', pointBorderWidth: 2 }] }, options: lineOpts(' kunjungan') };
        },
        ekspor: () => {
            title.textContent = `Nilai Ekspor ${regionName}`;
            return { type: 'bar', data: { labels: ['2020', '2021', '2022', '2023', '2024'], datasets: [{ label: 'Ekspor (Juta USD)', data: [1500, 1650, 1800, 2000, 2145], backgroundColor: 'rgba(16,185,129,0.7)', borderRadius: 6 }] }, options: barOpts(' Juta USD') };
        },
        impor: () => {
            title.textContent = `Nilai Impor ${regionName}`;
            return { type: 'bar', data: { labels: ['2020', '2021', '2022', '2023', '2024'], datasets: [{ label: 'Impor (Juta USD)', data: [1200, 1300, 1450, 1600, 1845], backgroundColor: 'rgba(239,68,68,0.7)', borderRadius: 6 }] }, options: barOpts(' Juta USD') };
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
        scales: { y: { display: false }, x: { grid: { display: false }, border: { display: false }, ticks: { font: { size: 11 } } } },
        layout: { padding: { top: 30, bottom: 10 } }
    };
}
