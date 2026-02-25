<p align="center">
  <img src="assets/images/logo-bps.png" alt="BPS Logo" width="80"/>
</p>

<h1 align="center">Dashboard Indikator Strategis<br/>Kepulauan Riau</h1>

<p align="center">
  <strong>Visualisasi Data Statistik 9 Indikator Daerah Kabupaten/Kota Kepulauan Riau</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
</p>

---

## 📖 Tentang Project

Dashboard Map Kepulauan Riau adalah web dashboard interaktif yang menyajikan **9 indikator strategis daerah** untuk seluruh Kabupaten/Kota di Provinsi Kepulauan Riau. Dashboard ini menampilkan data statistik dalam bentuk visualisasi yang mudah dipahami, dengan referensi desain dari [Sensus Ekonomi 2026 - BPS](https://sensus.bps.go.id/se2026/).

Setiap halaman indikator memiliki **desain yang konsisten**, dengan **dropdown** sebagai pembeda untuk memilih Kabupaten/Kota yang ingin ditampilkan datanya.

---

## 📊 Indikator

Dashboard ini menampilkan **9 indikator strategis** yang dikelompokkan berpasangan:

| Pasangan | Indikator 1 | Indikator 2 |
|:--------:|-------------|-------------|
| 1 | 📈 Pertumbuhan Ekonomi (%) | 💰 PDRB Per Kapita (Juta Rupiah/Tahun) |
| 2 | 👷 Tingkat Pengangguran Terbuka / TPT (%) | 📉 Persentase Kemiskinan (%) |
| 3 | 🎓 Indeks Pembangunan Manusia / IPM (0-100) | ⚖️ Indeks Pembangunan Gender / IPG (0-100) |
| 4 | 📚 Angka Partisipasi Sekolah / APS (%) | - |
| 5 | 📏 Rasio Gini (0-1) | - |
| 6 | 🏷️ Inflasi | - |

> **Catatan:** Pasangan untuk indikator Inflasi masih dalam tahap perencanaan.

---

## 🗺️ Cakupan Wilayah

Data mencakup seluruh **Kabupaten/Kota di Provinsi Kepulauan Riau**:

| No | Kabupaten/Kota |
|:--:|----------------|
| 1 | Kota Batam |
| 2 | Kota Tanjungpinang |
| 3 | Kabupaten Bintan |
| 4 | Kabupaten Karimun |
| 5 | Kabupaten Kepulauan Anambas |
| 6 | Kabupaten Lingga |
| 7 | Kabupaten Natuna |

---

## 🛠️ Tech Stack

| Teknologi | Kegunaan |
|-----------|----------|
| **HTML5** | Struktur halaman & layout |
| **CSS3** | Styling, animasi, & responsive design |
| **JavaScript** | Interaktivitas, chart, dan data handling |

---

## 📁 Struktur Project

```
dashboard-map/
├── index.html              # Halaman utama
├── assets/
│   ├── css/
│   │   └── style.css       # Stylesheet utama
│   ├── js/
│   │   └── main.js         # Script utama
│   ├── images/              # Gambar & icon
│   └── data/                # Data JSON indikator
├── pages/                   # Halaman per indikator
├── .gitignore
└── README.md
```

---

## 🚀 Cara Menjalankan

1. **Clone repository**
   ```bash
   git clone https://github.com/Cahyadi-Prasetyo/dashboard-map.git
   cd dashboard-map
   ```

2. **Checkout ke branch develop**
   ```bash
   git checkout develop
   ```

3. **Jalankan secara lokal**

   Buka file `index.html` langsung di browser, atau gunakan Live Server:
   ```bash
   # Menggunakan VS Code Live Server Extension
   # Klik kanan index.html → "Open with Live Server"

   # Atau menggunakan npx
   npx serve .
   ```

---

## 🌿 Branch Strategy

| Branch | Keterangan |
|--------|------------|
| `develop` | Branch utama untuk development (default) |
| `main` | Branch untuk production / release |

**Alur Kerja:**
```
feature-branch → develop → main
```

---

## 🎨 Referensi Desain

Desain dashboard ini mengambil inspirasi dari:
- [Sensus Ekonomi 2026 - BPS](https://sensus.bps.go.id/se2026/)

Dengan penyesuaian dan identitas visual tersendiri untuk kebutuhan dashboard indikator Kepulauan Riau.

---

## 📄 Lisensi

© 2026 - Dashboard Indikator Strategis Kepulauan Riau

---

<p align="center">
  <sub>Dibuat dengan ❤️ untuk Kepulauan Riau</sub>
</p>
