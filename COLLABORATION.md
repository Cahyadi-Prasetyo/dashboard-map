# 📊 Dashboard Map — Task Board Kolaborasi

## 📋 Panduan Singkat

Repository: `https://github.com/Cahyadi-Prasetyo/dashboard-map`
Branch default: `develop`

**Cara mulai:**
1. Clone repo
2. `git checkout feature/[nama-kabkot-kamu]`
3. Buka file `.html` sesuai kab/kota kamu
4. Edit konten (data, insight, grafik) → commit → push
5. Buat Pull Request ke `develop`

---

## 🔖 Status Branch per Kabupaten/Kota

> Centang (☑) jika sudah diambil, lalu isi nama penanggung jawab.

- [ ] **Kab. Karimun (2101)** — Branch: `feature/karimun` — File: `karimun.html` — PIC: ____________
- [ ] **Kab. Bintan (2102)** — Branch: `feature/bintan` — File: `bintan.html` — PIC: ____________
- [ ] **Kab. Natuna (2103)** — Branch: `feature/natuna` — File: `natuna.html` — PIC: ____________
- [ ] **Kab. Lingga (2104)** — Branch: `feature/lingga` — File: `lingga.html` — PIC: ____________
- [ ] **Kab. Kepulauan Anambas (2105)** — Branch: `feature/anambas` — File: `anambas.html` — PIC: ____________
- [ ] **Kota Batam (2171)** — Branch: `feature/batam` — File: `batam.html` — PIC: ____________
- [ ] **Kota Tanjung Pinang (2172)** — Branch: `feature/tanjungpinang` — File: `tanjungpinang.html` — PIC: ____________

---

## 📐 Struktur Indikator per Halaman

Setiap halaman kab/kota memiliki **5 section indikator** dengan layout berikut:

### Section 1 — Pertumbuhan Ekonomi *(full-width, background oranye)*
- [ ] Card utama: Nilai pertumbuhan ekonomi tahunan
- [ ] Histogram: Perbandingan 5 tahun terakhir
- [ ] Deskripsi / insight

### Section 2 — Indeks Pembangunan Manusia / IPM *(full-width, background putih)*
- [ ] Card utama: Nilai IPM + pertumbuhan dari tahun sebelumnya
- [ ] 3 card metadata: Umur Harapan Hidup, Pengetahuan (Sekolah), Standar Hidup Layak
- [ ] Histogram: Perkembangan IPM 2020–2025
- [ ] Deskripsi / insight

### Section 3 — Indeks Pembangunan Gender / IPG *(full-width, background krem)*
- [ ] Card utama: Nilai IPG + pertumbuhan dari tahun sebelumnya
- [ ] Histogram: Perkembangan IPG 2020–2024
- [ ] Deskripsi / insight

### Section 4 — TPT + APS *(dibagi 2 kolom, background putih)*

**Kolom kiri: Tingkat Pengangguran Terbuka (TPT)**
- [ ] Nilai highlight TPT terbaru
- [ ] Histogram tren TPT
- [ ] Deskripsi tren penurunan TPT

**Kolom kanan: Angka Partisipasi Sekolah (APS)**
- [ ] Nilai highlight APS terbaru
- [ ] Histogram tren APS
- [ ] Deskripsi partisipasi pendidikan menengah

### Section 5 — Kemiskinan + Gini Ratio *(dibagi 2 kolom, background krem)*

**Kolom kiri: Persentase Penduduk Miskin**
- [ ] Nilai highlight kemiskinan terbaru
- [ ] Histogram tren kemiskinan
- [ ] Deskripsi penurunan angka kemiskinan

**Kolom kanan: Rasio Gini**
- [ ] Nilai highlight rasio gini terbaru
- [ ] Histogram tren rasio gini
- [ ] Deskripsi ketimpangan pendapatan

---

## 📊 Progress Keseluruhan

- [ ] Landing page (`landingpage.html`) — selesai
- [ ] Karimun — selesai
- [ ] Bintan — selesai
- [ ] Natuna — selesai
- [ ] Lingga — selesai
- [ ] Anambas — selesai
- [ ] Batam — selesai
- [ ] Tanjung Pinang — selesai
- [ ] Semua branch di-merge ke `develop`
- [ ] Review final di `develop`
- [ ] Merge `develop` ke `main` → siap presentasi 🎉

---

## ⚠️ Catatan Penting

- Jangan push langsung ke `main` atau `develop`
- Selalu buat Pull Request dari branch kab/kota ke `develop`
- Data di-hardcode langsung di HTML (bukan dari JSON/JS)
- **Hindari penggunaan tabel** untuk tampilan data — gunakan card dan grafik
- Referensi data ada di folder `assets/data/` dan halaman backup di `backup/`
- CSS masing-masing halaman ada di `assets/css/[nama-kabkot].css`
- Contoh halaman lengkap ada di `backup/karimun.html` (referensi layout & data)
