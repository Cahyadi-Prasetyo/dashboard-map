document.addEventListener('DOMContentLoaded', () => {
    // Helper to format numbers like 1.845,00
    const formatNum = (num, minFrac = 2, maxFrac = 2) => {
        return num.toLocaleString('id-ID', { minimumFractionDigits: minFrac, maximumFractionDigits: maxFrac });
    };

    // Helper to extract region key from openModal call
    const extractRegion = (onclickAttr) => {
        const match = onclickAttr.match(/openModal\s*\(\s*['"][^'"]+['"]\s*,\s*['"]([^'"]+)['"]/);
        return match ? match[1] : null;
    };

    // Update Pertumbuhan Ekonomi (Laju Pertumbuhan PDRB)
    const updateEkonomi = (card, region) => {
        if (typeof dataEkonomi !== 'undefined' && dataEkonomi.wilayah[region]) {
            const arr = dataEkonomi.wilayah[region].tahunan;
            const tahunArr = dataEkonomi.tahun;
            if (arr && arr.length > 0) {
                const val = arr[arr.length - 1];
                const year = tahunArr[tahunArr.length - 1];
                const valEl = card.querySelector('.indikator-value');
                const dateEl = card.querySelector('.indikator-date');
                if (valEl) valEl.innerHTML = `${formatNum(val)}%`;
                if (dateEl) dateEl.innerText = year;
            }
        }
    };

    // Update PDRB per kapita
    const updatePdrb = (card, region) => {
        if (typeof dataPdrb !== 'undefined' && dataPdrb[region]) {
            const arr = dataPdrb[region];
            if (arr && arr.length > 0) {
                const val = arr[arr.length - 1];
                const valEl = card.querySelector('.indikator-value');
                const dateEl = card.querySelector('.indikator-date');
                if (valEl) valEl.innerHTML = `${formatNum(val, 0, 0)}<br><span>Ribu Rupiah</span>`;
                if (dateEl) dateEl.innerText = '2025'; // PDRB is mapped to 2025 based on the user's data array length
            }
        }
    };

    // Update values for Ekspor and Impor
    const updateTrade = (card, region, type) => {
        const dataObj = type === 'ekspor' ? eksporData : imporData;

        if (typeof dataObj !== 'undefined' && dataObj[region]) {
            const arr = dataObj[region].values;
            const labels = dataObj[region].labels;

            const valEl = card.querySelector('.indikator-value');
            const dateEl = card.querySelector('.indikator-date');

            if (arr && arr.length > 0 && labels && labels.length > 0) {
                const val = arr[arr.length - 1];
                const label = labels[labels.length - 1]; // e.g., 'Jan 26'

                // Convert 'Jan 26' -> 'Januari 2026' manually for cleaner UI if possible, but raw label is fine too
                let niceDate = label;
                if (label === 'Jan 26') niceDate = 'Januari 2026';
                if (label === 'Des 25') niceDate = 'Desember 2025';

                if (valEl) valEl.innerHTML = `${formatNum(val, 2, 2)}<br><span>Juta USD</span>`;
                if (dateEl) dateEl.innerText = niceDate;
            } else {
                if (valEl) valEl.innerHTML = `-`;
                if (dateEl) dateEl.innerText = '-';
            }
        }
    };

    // Main Loop
    const cards = document.querySelectorAll('.indikator-card');
    cards.forEach(card => {
        const onclickAttr = card.getAttribute('onclick');
        if (!onclickAttr) return;

        const region = extractRegion(onclickAttr) || 'kepulauan_riau'; // default to province if missing (index.html)

        if (onclickAttr.includes("'ekonomi'")) updateEkonomi(card, region);
        if (onclickAttr.includes("'pdrb'")) updatePdrb(card, region);

        // Only run trade updates if it's the province (since we hid them for kab/kot)
        if (region === 'kepulauan_riau') {
            if (onclickAttr.includes("'ekspor'")) updateTrade(card, region, 'ekspor');
            if (onclickAttr.includes("'impor'")) updateTrade(card, region, 'impor');
        }
    });
});
