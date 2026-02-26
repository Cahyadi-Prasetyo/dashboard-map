import json

# Population data
penduduk = {
    "karimun": {"2010": 212561, "2020": 253457},
    "bintan": {"2010": 142300, "2020": 159518},
    "natuna": {"2010": 69003, "2020": 81495},
    "lingga": {"2010": 86244, "2020": 98633},
    "anambas": {"2010": 37411, "2020": 47402},
    "batam": {"2010": 944285, "2020": 1196396},
    "tanjungpinang": {"2010": 187359, "2020": 227663}
}

# Inflasi data (latest full year = 2025)
inflasi_data = {
    "batam": [0.87, 0.03, 0.11, 0.38, -0.38, -0.06, 0.15, 0.08, 0.62, 0.43, 0.25, 1.14],
    "tanjungpinang": [-1.57, -0.45, 1.4, 1.09, -0.42, -0.13, 0.19, 0.26, 0.54, 0.35, 0.23, 1.28],
    "karimun": [-0.72, -1.3, 1.43, 1.97, -1.08, -0.71, 0.46, 1.03, 0.99, -0.31, 0.07, 0.92],
}
# For regions without specific data, use provinsi data
prov_inflasi = [0.43, -0.14, 0.38, 0.59, -0.44, -0.12, 0.19, 0.18, 0.64, 0.36, 0.23, 1.14]

files_map = {
    "karimun.html": "karimun",
    "bintan.html": "bintan",
    "natuna.html": "natuna",
    "lingga.html": "lingga",
    "anambas.html": "anambas",
    "batam.html": "batam",
    "tanjungpinang.html": "tanjungpinang"
}

for filename, region in files_map.items():
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    pop = penduduk[region]
    inf = inflasi_data.get(region, prov_inflasi)
    inf_label = f"Kab. {region.capitalize()}" if region in inflasi_data else "Prov. Kepulauan Riau"
    growth = round((pop["2020"] - pop["2010"]) / pop["2010"] * 100, 1)

    chart_code = f"""
    // --- INFLASI ---
    const ctxInflasi = document.getElementById('chartInflasi');
    if (ctxInflasi) {{
        new Chart(ctxInflasi, {{
            type: 'bar',
            data: {{
                labels: ['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Ags','Sep','Okt','Nov','Des'],
                datasets: [{{
                    label: 'Inflasi m-to-m 2025 ({inf_label})',
                    data: {inf},
                    backgroundColor: {inf}.map(v => v >= 0 ? 'rgba(239,68,68,0.7)' : 'rgba(34,197,94,0.7)'),
                    borderRadius: 4
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: true, position: 'top' }},
                    title: {{
                        display: true,
                        text: 'Inflasi Bulanan (m-to-m) Tahun 2025',
                        font: {{ size: 16, weight: 'bold', family: 'Inter' }},
                        padding: {{ bottom: 20 }},
                        align: 'start'
                    }},
                    datalabels: {{
                        anchor: function(ctx) {{ return ctx.dataset.data[ctx.dataIndex] >= 0 ? 'end' : 'start'; }},
                        align: function(ctx) {{ return ctx.dataset.data[ctx.dataIndex] >= 0 ? 'top' : 'bottom'; }},
                        formatter: (v) => v.toFixed(2) + '%',
                        font: {{ weight: 'bold', size: 10 }},
                        color: '#1a1a2e'
                    }}
                }},
                scales: {{
                    y: {{ display: false }},
                    x: {{ grid: {{ display: false }}, border: {{ display: false }} }}
                }},
                layout: {{ padding: {{ top: 30, bottom: 10 }} }}
            }}
        }});
    }}

    // --- JUMLAH PENDUDUK ---
    const ctxPenduduk = document.getElementById('chartPenduduk');
    if (ctxPenduduk) {{
        new Chart(ctxPenduduk, {{
            type: 'bar',
            data: {{
                labels: ['SP 2010', 'SP 2020'],
                datasets: [{{
                    label: 'Jumlah Penduduk (jiwa)',
                    data: [{pop["2010"]}, {pop["2020"]}],
                    backgroundColor: ['rgba(59,130,246,0.7)', 'rgba(16,185,129,0.7)'],
                    borderRadius: 8,
                    barThickness: 60
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: 'y',
                plugins: {{
                    legend: {{ display: false }},
                    title: {{
                        display: true,
                        text: 'Jumlah Penduduk Hasil Sensus Penduduk',
                        font: {{ size: 16, weight: 'bold', family: 'Inter' }},
                        padding: {{ bottom: 20 }},
                        align: 'start'
                    }},
                    subtitle: {{
                        display: true,
                        text: 'Pertumbuhan: +{growth}% (2010 → 2020)',
                        font: {{ size: 13, style: 'italic' }},
                        padding: {{ bottom: 10 }},
                        align: 'start',
                        color: '#64748b'
                    }},
                    datalabels: {{
                        anchor: 'end',
                        align: 'right',
                        formatter: (v) => v.toLocaleString('id-ID') + ' jiwa',
                        font: {{ weight: 'bold', size: 12 }},
                        color: '#1a1a2e'
                    }}
                }},
                scales: {{
                    x: {{ display: false }},
                    y: {{ grid: {{ display: false }}, border: {{ display: false }} }}
                }},
                layout: {{ padding: {{ right: 120 }} }}
            }}
        }});
    }}
"""

    # Insert chart code before the closing </script> of the main chart script block
    # Find the last occurrence of "});\n    </script>" which is the end of the main chart DOMContentLoaded block
    marker = "});\n    </script>"
    idx = content.find(marker)
    if idx == -1:
        marker = "});\r\n    </script>"
        idx = content.find(marker)

    if idx != -1:
        content = content[:idx] + chart_code + "\n    " + content[idx:]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added charts to {filename}")
    else:
        print(f"WARNING: Could not find insertion point in {filename}")

print("Done!")
