const fs = require('fs');

// Read landingpage as base
const landing = fs.readFileSync('d:/Workspace/dashboard-map/landingpage.html', 'utf-8');

// The indicator section to replace is lines containing indikator-container (approx lines 108-172)
// We find: <div class="indikator-container"> ... </div> (closing the container)
// And replace with the new 10-indicator layout

const startMarker = '                <div class="indikator-container">';
const endMarker = '                </div>\n            </div>';

const startIdx = landing.indexOf(startMarker);
// Find the closing </div> of indikator-container, which is followed by </div> of style-69
const containerEnd = landing.indexOf('                </div>\n            </div>\n            \n        </div>');

if (startIdx === -1 || containerEnd === -1) {
    console.log('Markers not found, start:', startIdx, 'end:', containerEnd);
    // Try alternate approach - find by line content
}

// New 10-indicator HTML using same card style but with CSS grid for paired sections
const newIndicatorHTML = `                <div class="indikator-container-v2">
                <!-- Row 1: Solo Cards (4 cards in a grid) -->
                <div class="indikator-solo-grid">
                    <!-- Card 1: Pertumbuhan Ekonomi -->
                    <div class="indikator-card-v2 card-orange">
                        <div class="indikator-icon-v2" style="background-image:url('potensi.png')"></div>
                        <p class="indikator-title">Pertumbuhan Ekonomi</p>
                        <h3 class="indikator-value">6,48<span>%</span></h3>
                        <p class="indikator-date">2024</p>
                    </div>

                    <!-- Card 2: IPM -->
                    <div class="indikator-card-v2 card-white">
                        <div class="indikator-icon-v2" style="mask-image:url('assets/icons/subject/563.svg')"></div>
                        <p class="indikator-title">IPM</p>
                        <h3 class="indikator-value">80,12</h3>
                        <p class="indikator-date">2024</p>
                    </div>

                    <!-- Card 3: IPG -->
                    <div class="indikator-card-v2 card-cream">
                        <div class="indikator-icon-v2" style="mask-image:url('assets/icons/subject/563.svg')"></div>
                        <p class="indikator-title">IPG</p>
                        <h3 class="indikator-value">94,28</h3>
                        <p class="indikator-date">2024</p>
                    </div>

                    <!-- Card 4: Inflasi -->
                    <div class="indikator-card-v2 card-white">
                        <div class="indikator-icon-v2" style="mask-image:url('assets/icons/subject/536.svg')"></div>
                        <p class="indikator-title">Inflasi</p>
                        <h3 class="indikator-value">3,12<span>%</span></h3>
                        <p class="indikator-date">2024</p>
                    </div>
                </div>

                <!-- Row 2: Paired — APS + TPT -->
                <div class="indikator-paired-grid">
                    <div class="indikator-card-v2 card-cream">
                        <div class="indikator-icon-v2" style="mask-image:url('assets/icons/subject/563.svg')"></div>
                        <p class="indikator-title">Angka Partisipasi Sekolah (APS)</p>
                        <h3 class="indikator-value">99,15<span>%</span></h3>
                        <p class="indikator-date">2024</p>
                    </div>
                    <div class="indikator-card-v2 card-orange">
                        <div class="indikator-icon-v2" style="mask-image:url('assets/icons/subject/520.svg')"></div>
                        <p class="indikator-title">Tingkat Pengangguran Terbuka</p>
                        <h3 class="indikator-value">7,25<span>%</span></h3>
                        <p class="indikator-date">2024</p>
                    </div>
                </div>

                <!-- Row 3: Paired — Jumlah Penduduk + PDRB Per Kapita -->
                <div class="indikator-paired-grid">
                    <div class="indikator-card-v2 card-orange">
                        <div class="indikator-icon-v2" style="mask-image:url('assets/icons/subject/519.svg')"></div>
                        <p class="indikator-title">Jumlah Penduduk</p>
                        <h3 class="indikator-value">1,21<span> Juta Jiwa</span></h3>
                        <p class="indikator-date">SP2020</p>
                    </div>
                    <div class="indikator-card-v2 card-white">
                        <div class="indikator-icon-v2" style="mask-image:url('assets/icons/subject/531.svg')"></div>
                        <p class="indikator-title">PDRB Per Kapita</p>
                        <h3 class="indikator-value">185,32<span> Juta Rp</span></h3>
                        <p class="indikator-date">2024</p>
                    </div>
                </div>

                <!-- Row 4: Paired — Kemiskinan + Rasio Gini -->
                <div class="indikator-paired-grid">
                    <div class="indikator-card-v2 card-cream">
                        <div class="indikator-icon-v2" style="mask-image:url('assets/icons/subject/563.svg')"></div>
                        <p class="indikator-title">Persentase Kemiskinan</p>
                        <h3 class="indikator-value">4,85<span>%</span></h3>
                        <p class="indikator-date">2024</p>
                    </div>
                    <div class="indikator-card-v2 card-white">
                        <div class="indikator-icon-v2" style="mask-image:url('assets/icons/subject/563.svg')"></div>
                        <p class="indikator-title">Rasio Gini</p>
                        <h3 class="indikator-value">0,312</h3>
                        <p class="indikator-date">2024</p>
                    </div>
                </div>
                </div>`;

// Build batam.html
let batam = landing;

// Replace title
batam = batam.replace(
    '<title>Landing Page — Sensus Ekonomi 2026</title>',
    '<title>Dashboard — Kota Batam</title>'
);

// Replace heading
batam = batam.replace(
    'Indikator Strategis Kepulauan Riau',
    'Indikator Strategis Kota Batam'
);

// Replace the indicator cards section
// Find the exact boundaries
const cardStart = batam.indexOf('<div class="indikator-container">');
const cardEndStr = '</div>\n            </div>\n            \n        </div>';
const cardEnd = batam.indexOf(cardEndStr, cardStart);

if (cardStart === -1 || cardEnd === -1) {
    console.error('Could not find card boundaries:', cardStart, cardEnd);
    process.exit(1);
}

// Replace between cardStart and the closing tags
batam = batam.substring(0, cardStart) + newIndicatorHTML + '\n            </div>\n            \n        </div>' + batam.substring(cardEnd + cardEndStr.length);

fs.writeFileSync('d:/Workspace/dashboard-map/batam.html', batam, 'utf-8');
console.log('Created batam.html successfully!');
