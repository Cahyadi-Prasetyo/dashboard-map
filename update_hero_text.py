import re
import os

descriptions = {
    "tanjungpinang": "Kota Tanjungpinang merupakan ibu kota Provinsi Kepulauan Riau yang berperan sebagai pusat pemerintahan, perdagangan, dan jasa. Didukung oleh sektor perdagangan, pariwisata, serta aktivitas ekonomi maritim, Tanjungpinang menjadi simpul penting dalam mendorong pertumbuhan ekonomi regional di wilayah kepulauan.",
    "batam": "Kota Batam merupakan pusat industri dan perdagangan internasional yang strategis karena berbatasan langsung dengan Singapura dan Malaysia. Dengan kawasan industri, pelabuhan internasional, serta infrastruktur modern, Batam menjadi motor utama pertumbuhan ekonomi dan investasi di Provinsi Kepulauan Riau.",
    "bintan": "Kabupaten Bintan dikenal sebagai kawasan unggulan pariwisata dan industri yang didukung oleh kawasan ekonomi khusus dan destinasi wisata kelas internasional. Potensi sektor pariwisata, perikanan, dan industri pengolahan menjadikan Bintan sebagai salah satu pilar penting pembangunan ekonomi daerah.",
    "karimun": "Kabupaten Karimun memiliki posisi strategis di jalur perdagangan internasional dan didukung oleh sektor pertambangan, industri galangan kapal, serta transportasi laut. Keunggulan geografis dan potensi sumber daya alam menjadikan Karimun sebagai pusat kegiatan ekonomi maritim yang berperan penting dalam pertumbuhan wilayah.",
    "natuna": "Kabupaten Natuna merupakan wilayah perbatasan yang memiliki potensi besar di sektor perikanan, energi, dan sumber daya alam. Letaknya yang strategis di Laut Natuna Utara menjadikan wilayah ini penting dalam mendukung ketahanan ekonomi, kedaulatan, dan pengembangan ekonomi maritim nasional.",
    "lingga": "Kabupaten Lingga memiliki potensi ekonomi yang didukung oleh sektor perikanan, pertanian, dan pariwisata bahari. Dengan kekayaan sumber daya alam dan budaya, Lingga terus berkembang sebagai wilayah yang berkontribusi terhadap penguatan ekonomi berbasis sumber daya lokal.",
    "anambas": "Kabupaten Kepulauan Anambas merupakan wilayah kepulauan dengan potensi unggulan di sektor perikanan, migas, dan pariwisata bahari. Keindahan alam serta letak strategisnya menjadikan Anambas memiliki peran penting dalam pengembangan ekonomi maritim dan pariwisata berkelanjutan."
}

for region, text in descriptions.items():
    filename = f"{region}.html"
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        continue
        
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Look for the h2 with style-24 and the following header/paragraph
    # Usually it's <h6 class="style-43">...</h6> or <p class="style-43"...>
    pattern = r'(<h2 class="style-24">.*?</h2>\s*)<(?:h6|p)\s+class="style-43".*?>.*?</(?:h6|p)>'
    replacement = r'\1<p class="style-43" style="line-height: 1.6; font-weight: 500; font-size: 15px; color: #475569; margin-top: 12px; text-align: justify;">' + text + '</p>'
    
    new_content, count = re.subn(pattern, replacement, content, count=1, flags=re.DOTALL)
    
    if count > 0:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Could not find matching pattern in {filename}")

