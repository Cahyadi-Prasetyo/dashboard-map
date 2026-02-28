# Kebutuhan Desain Responsif (Responsive Design)

Dokumen ini menguraikan kebutuhan dan strategi untuk menerapkan desain yang responsif di seluruh proyek Dashboard Kepulauan Riau. Tujuannya adalah untuk memastikan dashboard memberikan pengalaman UI/UX yang optimal untuk **setiap ukuran perangkat yang ada di pasaran**.

**Target Proritas Utama:**
1.  **Tablet Layar Besar (khususnya Samsung Galaxy Tab S10 Ultra - 14.6" / Tab S10+)**: Tampilan harus terlihat proporsional, tidak *stretch* berlebihan, dan memanfaatkan ruang layar dengan cerdas (tidak terlalu renggang).
2.  **Layar Sangat Lebar (Smart TV 75" / Resolusi 4K)**: Tampilan tidak boleh rusak atau elemen menjadi terlalu besar/menyimpang. Konteks layar harus terpusat (*center-aligned max-width*) agar tetap elegan.
3.  **Dukungan Penuh Breakpoint Standar**: Mencakup seluruh variasi layar standar modern (Smartphone kecil hingga layar Ultrawide).

### Daftar *Breakpoints* (Titik Henti CSS) yang Akan Digunakan

Kita akan menggunakan pendekatan *Mobile-First* atau sistem *grid* modern dengan dukungan *breakpoints* menyeluruh:
*   **Mobile Small (sm):** Maksimal 480px (iPhone SE, ponsel Android kecil).
*   **Mobile Large / Murni (md):** Maksimal 767px (iPhone Pro Max, kebanyakan ponsel standar).
*   **Tablet Portrait (lg):** 768px hingga 1023px (iPad standar).
*   **Tablet Landscape / Laptop (xl):** 1024px hingga 1365px (Samsung Galaxy Tab S10 biasa, layar laptop kecil 13").
*   **Tablet Jumbo / Desktop Modern (2xl):** 1366px hingga 1919px (Samsung Galaxy Tab S10 Ultra, monitor standar 1080p).
*   **Layar Ultrawide & Smart TV (3xl / 4K):** 1920px ke atas hingga TV 75 Inci (Resolusi 4K atau 8K). Area antarmuka harus dibatasi maksimal lebarnya (misalnya `max-width: 1600px; margin: 0 auto;`) agar elemen tidak renggang menyebar dari ujung ke ujung layar TV raksasa.

## 1. Penyesuaian Grid dan Tata Letak (Layout)

*   **Grid Kartu Indikator (`.indikator-container` / `.style-69` / `.style-60`):**
    *   **TV 75" / Layar Lebar (> 1920px):** Kartu indikator berada dalam *container* tengah (*centered*). Jumlah grid mencapai 4 atau 5 kolom.
    *   **Tablet Jumbo (Tab S10) / Desktop (1366px - 1919px):** Pertahankan tata letak unggulan saat ini, 4 kolom kartu per baris.
    *   **Laptop / Tablet Biasa (1024px - 1365px):** Menampilkan 3 atau 4 kartu per baris.
    *   **Tablet Portrait (768px - 1023px):** Menampilkan 2 atau 3 kartu per baris.
    *   **Mobile (< 768px):** Wajib menggunakan tata letak 1 kolom murni (atau 2 kolom kecil untuk indikator angka utama jika memadai) untuk mencegah *scrolling* horizontal sembarangan.
*   **Bagian Hero / Banner Atas (`.hero-carousel`, `.style-22`):**
    *   **TV 75" / Desktop:** Overlay carousel dan rasio gambar tetap proporsional dan tidak pecah (*pixelated*). Gunakan `object-fit: cover` dan pembatasan lebar maksimum teks.
    *   **Tablet (Tab S10):** Komposisi hero image sangat optimal dan tajam. Teks dan jarak tombol carousel sesuai sentuhan jari besar.
    *   **Mobile:** Teks "Hero" tersusun secara vertikal, rata tengah. Gambar berskala tanpa pembatasan `fixed height` yang merusak estetika.
*   **Bagian "Potensi Strategis" (`.style-145`):**
    *   Harus menyesuaikan sistem *grid responsive* secara *fluid* dari 4 kolom di TV/Desktop menjadi 2 kolom di Tab S10/Tablet, dan 1 kolom di ponsel.
*   **Grid Galeri/Video (`.video-testi-grid`, `.reels-grid`):**
    *   **TV/Desktop (> 1366px):** 4 kolom stabil.
    *   **Tablet (Tab S10):** 3 kolom.
    *   **Tablet Portrait:** 2 baris kolom.
    *   **Mobile:** 1 kolom vertikal.

## 2. Tipografi (Teks) dan Jarak (Spacing)

*   **Ukuran Font (Huruf):**
    *   Gunakan unit relatif (`rem`, `em`, atau `vw`) sebagai pengganti `px` tetap jika memungkinkan, atau gunakan *CSS media queries* untuk mengecilkan ukuran judul (misalnya, `h2`, `h3`) pada perangkat *mobile*.
*   **Padding dan Margin:**
    *   Kurangi *padding* dan *margin* yang terlalu lebar pada perangkat *mobile* untuk memaksimalkan ruang layar yang dapat digunakan, namun tetap perhatikan jarak agar nyaman ditekan (sentuhan jari).

## 3. Navigasi (`nav.style-2`)

*   **Desktop:** Daftar wilayah tersusun horizontal.
*   **Mobile (< 768px):**
    *   Terapkan menu "hamburger" (garis tiga) atau bilah navigasi horizontal yang dapat digeser / di-*scroll* barisannya (`overflow-x: auto; white-space: nowrap;`).
    *   Pastikan kursor penanda halaman aktif (`.active`) terlihat jelas, tanpa mengeblok tombol menu di layar kecil.

## 4. Perbaikan Modal / Kotak Popup (`#modalOverlay`, `.modal-box`)

*   **Desktop:** Tampilan terbagi dua sisi (kiri: gambar/definisi, kanan: grafik/*insight*).
*   **Mobile (< 768px):**
    *   Ubah tampilan terbagi dua tersebut (`.modal-body-split`) dari menyamping (`flex-direction: row`) menjadi tersusun atas-bawah (`flex-direction: column`).
    *   Pastikan elemen grafik `<canvas>` dapat diubah ukurannya dengan benar (gunakan `maintainAspectRatio: false` pada opsi *Chart.js*, meski ini sebagian besar sudah diterapkan, namun pastikan *container* / wadah induknya memiliki tinggi yang terdefinisi).
    *   Buat kotak modal membentang menghabiskan hampir 100% lebar layar dengan *padding* yang sedikit di bagian ujungnya.
    *   Sesuaikan ukuran gambar di dalam modal agar tidak menyita terlalu banyak ruang vertikal di layar ponsel, menggeser / mendorong grafiknya menjadi terlalu di bawah.
    *   Buat isi di dalam modal dapat di-*scroll* (gulir) jika melebihi panjang layar/viewport pengguna.

## 5. Strategi Implementasi / Pelaksanaan

1.  **CSS Media Queries:** Tambahkan kode kueri di berkas `shared.css` dan di berkas CSS spesifik halaman untuk menangani perubahan titik layar (*breakpoints*), misalnya dengan menambahkan `@media (max-width: 768px)`.
2.  **Flexbox / CSS Grid:** Maksimalkan kemudahan alat *Flexbox* dan properti *CSS Grid* untuk secara otomatis menangani pembungkusan baris baru (`wrapping`) dan perataan (`alignment`).
3.  **Pengujian (Testing):** Lakukan proses Verifikasi (*Testing*) kerangka *responsive* dengan menggunakan emulator *Developer Tools* pada peramban Chrome, dan pada perangkat nyata (seperti ponsel pengguna).

## Langkah Selanjutnya

1.  Menyepakati dan menyetujui dokumen ini.
2.  Menerapkan perubahan utama pada berkas CSS utama `shared.css`.
3.  Menerapkan perbaikan di berkas CSS spesifik di masing-masing halaman jika diperlukan.
4.  Menguji fitur Navigasi dan Kotak *Modal* di ukuran ponsel (*small screen*).
