document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.indikator-card');
    cards.forEach(card => {
        const onclickAttr = card.getAttribute('onclick');
        if (onclickAttr && onclickAttr.includes("openModal('pdrb'")) {
            const match = onclickAttr.match(/openModal\('pdrb',\s*'([^']+)'/);
            if (match && match[1]) {
                const region = match[1];
                if (typeof dataPdrb !== 'undefined' && dataPdrb[region]) {
                    // Ambil nilai data terbaru (index terakhir dari array)
                    const latestValue = dataPdrb[region][dataPdrb[region].length - 1];
                    // Format number to 'id-ID' format without fractions
                    const formattedValue = latestValue.toLocaleString('id-ID');

                    const valueEl = card.querySelector('h3.indikator-value');
                    const dateEl = card.querySelector('p.indikator-date');

                    if (valueEl) {
                        valueEl.innerHTML = `${formattedValue}<br><span>ribu rupiah</span>`;
                    }
                    if (dateEl) {
                        // Tahun terbaru untuk PDRB saat ini
                        dateEl.innerText = '2025';
                    }
                }
            }
        }
    });
});
