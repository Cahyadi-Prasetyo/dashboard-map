
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
        insight: (rn) => `TPT menunjukkan tren menurun dari 2021 hingga 2025, mencerminkan perbaikan kondisi ketenagakerjaan di ${rn}.`
    },
    pdrb: {
        def: 'Nilai PDRB dibagi jumlah penduduk dalam suatu wilayah pada periode tertentu',
        img: 'assets/img/PDRB perkapita.jpg',
        insight: (rn) => `PDRB per kapita ${rn} konsisten meningkat dari tahun ke tahun.`
    },
    ipm: {
        def: 'Indikator yang mengukur kualitas hidup penduduk berdasarkan kesehatan, pendidikan, dan standar hidup layak.',
        img: 'assets/img/IPM.jpg',
        insight: (rn) => `IPM di ${rn} meningkat secara konsisten dari tahun ke tahun yang menunjukkan perbaikan berkelanjutan dalam kualitas hidup masyarakat.`
    },
    aps: {
        def: 'Persentase penduduk usia sekolah SMA/SMK yang sedang menempuh pendidikan per 1,000 jumlah penduduk usia pendidikan menengah.',
        img: 'assets/img/APS.jpg',
        insight: (rn) => `Angka partisipasi sekolah tingkat menengah di ${rn} semakin membaik.`
    },
    ipg: {
        def: 'Indikator yang mengukur kesetaraan capaian pembangunan manusia antara laki-laki dan perempuan.',
        img: 'assets/img/IPG.jpeg',
        insight: (rn) => `IPG di ${rn} menunjukkan tren meningkat dari yang menunjukkan kesetaraan capaian pembangunan antara laki-laki dan perempuan semakin membaik`
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
        def: '-',
        img: 'assets/img/inflasi.jpeg',
        insight: (rn) => `Data inflasi belum ditemukan`
    },
    penduduk: {
        def: 'Total orang yang tinggal dan menetap di suatu wilayah pada waktu tertentu.',
        img: 'assets/img/penduduk.jpeg',
        insight: (rn) => `Jumlah penduduk di ${rn} bertambah secara proporsional berdasar sensus terbaru.`
    },
    wisman: {
        def: '-',
        img: 'assets/img/wisata.jpeg',
        insight: (rn) => `Data kunjungan wisman belum ditemukan`
    },
    ekspor: {
        def: '-',
        img: 'assets/img/ekspor.png',
        insight: (rn) => `Data ekspor belum ditemukan`
    },
    impor: {
        def: '-',
        img: 'assets/img/impor.jpeg',
        insight: (rn) => `Data impor belum ditemukan`
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
            title.textContent = `Pertumbuhan Ekonomi ${regionName} 2020–2024`;
            let dataArr = [];
            let labelsArr = dataEkonomi.tahun;

            if (dataEkonomi.triwulanan && dataEkonomi.triwulanan[regionKey]) {
                dataArr = dataEkonomi.triwulanan[regionKey].y_on_y || [];
                labelsArr = ['Triwulan I', 'Triwulan II', 'Triwulan III', 'Triwulan IV'];
            } else {
                const d = dataEkonomi.wilayah[regionKey];
                if (d && d.tahunan) { dataArr = d.tahunan; }
            }

            return { type: 'bar', data: { labels: labelsArr, datasets: [{ label: 'Pertumbuhan Ekonomi (%)', data: dataArr, backgroundColor: 'rgba(59,130,246,0.7)', borderRadius: 6 }] }, options: barOptsDecimal('%') };
        },
        pdrb: () => {
            title.textContent = `PDRB per Kapita ${regionName} (Ribu Rupiah)`;
            let dataArr = [];
            if (dataPdrb[regionKey]) { dataArr = dataPdrb[regionKey]; }
            return {
                type: 'line',
                data: {
                    labels: [2020, 2021, 2022, 2023, 2024, 2025],
                    datasets: [{
                        label: 'PDRB per Kapita',
                        data: dataArr,
                        borderColor: '#10b981',
                        backgroundColor: 'rgba(16,185,129,0.1)',
                        fill: true,
                        tension: 0.3,
                        borderWidth: 3,
                        pointRadius: 5,
                        pointBackgroundColor: '#10b981',
                        pointBorderColor: '#fff',
                        pointBorderWidth: 2
                    }]
                },
                options: {
                    responsive: true, maintainAspectRatio: false,
                    plugins: { legend: { display: false }, datalabels: { align: 'top', offset: 6, formatter: (v) => v.toLocaleString('id-ID'), font: { weight: 'bold', size: 11 }, color: '#1e293b' } },
                    scales: { y: { display: false }, x: { grid: { display: false }, border: { display: false }, ticks: { font: { size: 11 } } } },
                    layout: { padding: { top: 30, bottom: 10, left: 40, right: 20 } }
                }
            };
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
            if (regionKey === 'kepulauan_riau') {
                const labels = ['Feb 2021', 'Ags 2021', 'Feb 2022', 'Ags 2022', 'Feb 2023', 'Ags 2023', 'Feb 2024', 'Ags 2024', 'Feb 2025', 'Ags 2025', 'Nov 2025'];
                const barData = [116.75, 119.60, 84.79, 103.72, 84.23, 74.33, 74.78, 71.57, 75.21, 72.56, 71.84];
                const lineData = [10.12, 9.91, 8.02, 8.23, 7.61, 6.80, 6.94, 6.39, 6.89, 6.45, 6.35];

                return {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [
                            {
                                type: 'line',
                                label: 'TPT (%)',
                                data: lineData,
                                borderColor: '#1e293b',
                                backgroundColor: '#1e293b',
                                borderWidth: 3,
                                pointBackgroundColor: '#fff',
                                pointBorderColor: '#1e293b',
                                pointBorderWidth: 3,
                                pointRadius: 5,
                                yAxisID: 'y',
                                datalabels: {
                                    align: 'bottom',
                                    anchor: 'start',
                                    offset: 2,
                                    formatter: (v) => v.toLocaleString('id-ID', { minimumFractionDigits: 2 }),
                                    color: '#1e293b',
                                    font: { weight: 'bold', size: 12 }
                                }
                            },
                            {
                                type: 'bar',
                                label: 'Pengangguran (Ribu Orang)',
                                data: barData,
                                backgroundColor: 'rgba(245, 158, 11, 0.85)',
                                borderRadius: 4,
                                yAxisID: 'y',
                                datalabels: {
                                    align: 'top',
                                    anchor: 'end',
                                    offset: 2,
                                    formatter: (v) => v.toLocaleString('id-ID', { minimumFractionDigits: 2 }),
                                    color: '#1e293b',
                                    font: { weight: '600', size: 11 }
                                }
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { display: true, position: 'bottom' }
                        },
                        scales: {
                            x: { grid: { display: false } },
                            y: { display: false }
                        },
                        layout: { padding: { top: 30, bottom: 20 } }
                    }
                };
            }

            const d = dataTpt.wilayah[regionKey];
            let dataArr = [];
            if (d && d.tahunan) { dataArr = d.tahunan; }
            return { type: 'bar', data: { labels: dataTpt.tahun, datasets: [{ label: 'TPT (%)', data: dataArr, backgroundColor: 'rgba(239,68,68,0.7)', borderRadius: 6 }] }, options: barOpts('%') };
        },
        aps: () => {
            title.textContent = `Angka Partisipasi Sekolah (APS) SMA/SMK ${regionName} (%)`;
            const d = dataAps.wilayah[regionKey];
            let dataArr = [];
            let labelsArr = dataAps.tahun;

            if (d && d.tahunan) {
                dataArr = [...d.tahunan];
            }

            // Inject 2025 data (16-18) specifically for Provinsi Kepri
            if (regionKey === 'kepulauan_riau') {
                labelsArr = [...dataAps.tahun, 2025];
                dataArr.push(88.24); // append 2025 value
            }

            return {
                type: 'line',
                data: {
                    labels: labelsArr,
                    datasets: [{
                        label: 'APS',
                        data: dataArr,
                        borderColor: '#0d9488',
                        backgroundColor: 'rgba(13,148,136,0.1)',
                        fill: true,
                        tension: 0.3,
                        borderWidth: 3,
                        pointRadius: 5,
                        pointBackgroundColor: '#0d9488',
                        pointBorderColor: '#fff',
                        pointBorderWidth: 2,
                        spanGaps: true
                    }]
                },
                options: lineOpts('')
            };
        },
        kemiskinan: () => {
            title.textContent = `Angka Kemiskinan ${regionName} (%)`;
            const d = dataKemiskinan.wilayah[regionKey];
            let dataArr = [];
            if (d && d.tahunan) { dataArr = d.tahunan; }
            return { type: 'bar', data: { labels: dataKemiskinan.tahun, datasets: [{ label: 'Kemiskinan', data: dataArr, backgroundColor: 'rgba(245,158,11,0.7)', borderRadius: 6 }] }, options: barOpts('') };
        },
        gini: () => {
            title.textContent = `Gini Ratio ${regionName} (Indeks)`;
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
            title.textContent = `Tingkat Inflasi Year-on-Year (Y-on-Y) `;

            let dataArr = [];
            let labelsArr = ['Jan 25', 'Feb 25', 'Mar 25', 'Apr 25', 'Mei 25', 'Jun 25', 'Jul 25', 'Ags 25', 'Sep 25', 'Okt 25', 'Nov 25', 'Des 25', 'Jan 26'];

            if (regionKey === 'anambas') {
                return { type: 'bar', data: { labels: ['Data Belum Ditemukan'], datasets: [{ label: 'Inflasi Y-on-Y (%)', data: [0], backgroundColor: 'rgba(200,200,200,0.5)' }] }, options: barOptsDecimal('') };
            } else if (regionKey === 'kepulauan_riau') {
                dataArr = [2.01, 2.09, 2.01, 2.56, 1.73, 1.32, 1.97, 2.19, 2.70, 3.01, 3.00, 3.47, 2.94];
            } else if (regionKey === 'karimun') {
                dataArr = [0, -0.73, -0.15, 2.30, 0.87, -0.15, 0.40, 1.92, 2.91, 2.58, 2.43, 2.70, 2.77];
            } else {
                dataArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
            }

            return { type: 'line', data: { labels: labelsArr, datasets: [{ label: 'Inflasi Y-on-Y (%)', data: dataArr, borderColor: gradientLine, backgroundColor: gradientFill, fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#7c3aed', pointBorderColor: '#fff', pointBorderWidth: 2, pointHoverRadius: 7 }] }, options: lineOpts('%') };
        },
        wisman: () => {
            title.textContent = `Jumlah Kunjungan Wisatawan ${regionName}`;
            let labelsArr = [];
            let barData = [];

            // Read dynamically from wismanData (wisman.js)
            if (typeof wismanData !== 'undefined' && wismanData[regionKey]) {
                labelsArr = wismanData[regionKey].labels || [];
                barData = wismanData[regionKey].values || [];
            }

            return {
                type: 'bar',
                data: {
                    labels: labelsArr,
                    datasets: [
                        {
                            label: 'Kunjungan Wisman',
                            data: barData,
                            backgroundColor: 'rgba(22, 163, 74, 0.75)',
                            borderRadius: 4,
                            datalabels: {
                                align: 'top',
                                anchor: 'end',
                                offset: 2,
                                formatter: (v) => v.toLocaleString('id-ID'),
                                color: '#1e293b',
                                font: { weight: '600', size: 10 }
                            }
                        },
                        {
                            type: 'line',
                            label: 'Trend',
                            data: barData,
                            borderColor: '#166534',
                            backgroundColor: '#166534',
                            borderWidth: 2,
                            pointRadius: 0,
                            datalabels: { display: false }
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: true, position: 'bottom' } },
                    scales: {
                        x: { grid: { display: false } },
                        y: { display: false }
                    },
                    layout: { padding: { top: 30, bottom: 20 } }
                }
            };
        },
        ekspor: () => {
            title.textContent = `Nilai Ekspor ${regionName} (Juta USD)`;
            let labelsArr = ["Des'24", "Jan'25", "Feb'25", "Mar'25", "Apr'25", "Mei'25", "Jun'25", "Jul'25", "Ags'25", "Sep'25", "Okt'25", "Nov'25", "Des'25"];
            let dataArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

            if (regionKey === 'kepulauan_riau') {
                dataArr = [1839.28, 2177.29, 1796.50, 2052.49, 2003.39, 2386.35, 1902.37, 2001.78, 1883.21, 1935.44, 2134.77, 1850.18, 2071.02];
            } else if (regionKey === 'kepulauan_anambas') {
                return { type: 'bar', data: { labels: ['Data Belum Ditemukan'], datasets: [{ label: 'Ekspor (Juta USD)', data: [0], backgroundColor: 'rgba(200,200,200,0.5)' }] }, options: barOptsDecimal('') };
            }

            return { type: 'line', data: { labels: labelsArr, datasets: [{ label: 'Ekspor (Juta USD)', data: dataArr, borderColor: '#58508d', backgroundColor: 'rgba(88,80,141,0.1)', fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#58508d', pointBorderColor: '#fff', pointBorderWidth: 2 }] }, options: lineOpts('') };
        },
        impor: () => {
            title.textContent = `Nilai Impor ${regionName}, Desember 2024–Desember 2025 (Juta USD)`;
            let labelsArr = ["Des'24", "Jan'25", "Feb'25", "Mar'25", "Apr'25", "Mei'25", "Jun'25", "Jul'25", "Ags'25", "Sep'25", "Okt'25", "Nov'25", "Des'25"];
            let dataArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

            if (regionKey === 'kepulauan_riau') {
                dataArr = [1607.57, 1749.79, 1686.27, 1920.16, 1926.94, 2273.53, 1872.70, 1680.45, 1784.58, 1783.55, 1866.03, 1755.49, 1908.61];
            } else if (regionKey === 'kepulauan_anambas') {
                return { type: 'bar', data: { labels: ['Data Belum Ditemukan'], datasets: [{ label: 'Impor (Juta USD)', data: [0], backgroundColor: 'rgba(200,200,200,0.5)' }] }, options: barOptsDecimal('') };
            }

            return { type: 'line', data: { labels: labelsArr, datasets: [{ label: 'Impor (Juta USD)', data: dataArr, borderColor: '#ff6361', backgroundColor: 'rgba(255,99,97,0.1)', fill: true, tension: 0.3, borderWidth: 3, pointRadius: 5, pointBackgroundColor: '#ff6361', pointBorderColor: '#fff', pointBorderWidth: 2 }] }, options: lineOpts('') };
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
        layout: { padding: { top: 30, right: 30 } }
    };
}
function barOptsDecimal(suffix) {
    return {
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false }, datalabels: { anchor: 'end', align: 'top', formatter: (v) => v.toLocaleString('id-ID', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + suffix, font: { weight: 'bold', size: 14 }, color: '#1e293b' } },
        scales: { y: { display: false }, x: { grid: { display: false }, border: { display: false } } },
        layout: { padding: { top: 30, right: 30 } }
    };
}
function lineOpts(suffix) {
    return {
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false }, datalabels: { align: 'top', offset: 6, formatter: (v) => v.toLocaleString('id-ID') + suffix, font: { weight: 'bold', size: 11 }, color: '#1e293b' } },
        scales: { y: { display: false }, x: { grid: { display: false }, border: { display: false }, ticks: { font: { size: 11 } } } },
        layout: { padding: { top: 30, bottom: 10, right: 30 } }
    };
}
