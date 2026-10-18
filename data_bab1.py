# Fungsi 3 susun (Furigana - Kanji - Arti)
def kotoba(kanji, furigana, arti):
    # Jika tidak ada furigana, biarkan kosong agar tingginya tetap rata
    furigana_html = f"{furigana}" if furigana else "&nbsp;"
    
    return f"""
    <div style="display: inline-flex; flex-direction: column; align-items: center; vertical-align: bottom; margin: 0 2px;">
        <span style="font-size: 0.6em; line-height: 1.1; color: #666;">{furigana_html}</span>
        <span style="font-size: 1.2em; line-height: 1.2; font-weight: 500;">{kanji}</span>
        <span style="font-size: 0.6em; line-height: 1.1; color: #0066cc;">{arti}</span>
    </div>
    """

# Data Dictionary
data_bab1 = {
    "1.1": [
        {
            "is_header": True,
            "jp": "トラックの役割",
            "id": "Peran Truk"
        },
        {
            "is_header": False,
            # Gunakan f"" di depan string agar fungsi kotoba() bisa dipanggil di dalamnya
            "jp": f"みなさんは{kotoba('今', 'いま', 'sekarang')}、{kotoba('日本', 'にほん', 'Jepang')}でトラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}になるための{kotoba('勉強', 'べんきょう', 'belajar')}を{kotoba('始', 'はじ', 'mulai')}めたところだと{kotoba('思', 'おも', 'berpikir')}います。",
            "id": "Anda sekalian saat ini mungkin baru saja mulai belajar untuk menjadi pengemudi truk di Jepang."
        },
        {
            "is_header": False,
            "jp": f"「{kotoba('整理', 'せいり', 'Ringkas')}」とは、「{kotoba('乱れた', 'みだれた', 'berantakan')}{kotoba('状態に', 'じょうたいに', 'kondisi')}あるものを{kotoba('整える', 'ととのえる', 'menata')}ことであり、{kotoba('必要な', 'ひつような', 'perlu')}ものとそうでないものを{kotoba('区別', 'くべつ', 'membedakan')}し、{kotoba('必要ない', 'ひつようない', 'tak perlu')}ものを{kotoba('処分する', 'しょぶんする', 'membuang')}ことです」",
            "id": '"Seiri (Ringkas)" berarti "menata barang-barang yang berantakan, membedakan antara barang yang diperlukan dan yang tidak diperlukan, serta membuang barang yang tidak diperlukan".'
        }
    ],
    "1.2": [
        {
            "is_header": True,
            "jp": "トラック運転者の心構え",
            "id": "Sikap Mental Pengemudi Truk"
        },
        {
            "is_header": False,
            "jp": f"トラックは{kotoba('他', 'ほか', 'lain')}の{kotoba('車', 'くるま', 'mobil')}とは{kotoba('違', 'ちが', 'beda')}う{kotoba('特性', 'とくせい', 'karakteristik')}があります。",
            "id": "Truk memiliki karakteristik yang berbeda dengan kendaraan lain."
        }
    ]
}
