import re
with open('karimun_old.html', 'r', encoding='utf-8') as f:
    old_html = f.read()

# I want to restore karimun_old.html exactly for Karimun, 
# but user specifically said "serta untuk chart" nya juga sama yaitu menggunakan modal untuk tampilannya"

# This means they want the big detail-cards from karimun_old.html 
# BUT they want the charts inside them to BE A MODAL instead of directly rendered?
# OR they want the small indikator-cards on top, AND the big detail-cards below?

# Let me re-read user carefully:
# User Prompt 1: "untuk yang dihalaman karimun dan lain" juga disamakan seperti yang di index untuk strategi indikatornya baik itu dari style nya dan lain". serta untuk chart" nya juga sama yaitu menggunakan modal untuk tampilannya"
# User Prompt 2: "tetapi yang dimana data"nya adalah data kabupaten per page tersebut"
# User Prompt 3: "untuk data layout karimun sebelumnya bisa dijadikan referensi ambil dari github saya di branch feature/karimun, durasi 1 jam lalu"

# OK, it means they DO NOT want the `indikator-container` with 10 small cards directly.
# They want the layout of `karimun` from 1 hour ago (the `detail-wrapper` big cards), 
# BUT THEY WANT THOSE BIG CARDS TO BE CLICKABLE AND OPEN MODALS for the charts, rather than rendering the charts directly inside them?
# Wait... "disamakan seperti yang di index untuk strategi indikatornya baik itu dari style nya". 
# Ah, "strategy indikatornya" = the small 10 cards. They want the small 10 cards to look like index.html.
# BUT then they said "untuk data layout karimun sebelumnya bisa dijadikan referensi" 
# In the karimun_old.html, we had:
# 1. NO small 10 cards. We only had the big `detail-wrapper` cards.
# Let me stop and ask the user to clarify to avoid doing the wrong work.
