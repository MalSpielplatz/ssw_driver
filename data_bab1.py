# Fungsi sederhana pembuat tag ruby HTML
def ruby(kanji, furigana):
    return f"<ruby>{kanji}<rt>{furigana}</rt></ruby>"

# Format Dictionary kembali agar cocok dengan Selectbox Navigasi
data_bab1 = {
    "1.1": [
        {
            "is_header": True,
            "jp": f"1.1 トラックの{ruby('役割', 'やくわり')}",
            "id": "1.1 Peran Truk"
        },
        {
            "is_header": False,
            # Teks disesuaikan persis seperti di screenshot merah'.png
            "jp": f"{ruby('皆', 'みな')}さんは{ruby('今', 'いま')}、{ruby('日本', 'にほん')}でトラック{ruby('運転者', 'うんてんしゃ')}になるための{ruby('勉強', 'べんきょう')}を{ruby('始', 'はじ')}めたところだと{ruby('思', 'おも')}います。",
            "id": "Saat ini, Anda sekalian mungkin baru saja mulai belajar untuk menjadi pengemudi truk di Jepang."
        },
        {
            "is_header": False,
            "jp": f"では、{ruby('日本', 'にほん')}では、トラックはどれだけ{ruby('活躍', 'かつやく')}しているのでしょうか。",
            "id": "Lalu, seberapa besarkah peran truk di Jepang?"
        },
        {
            "is_header": False,
            "jp": f"トラックは、{ruby('身近', 'みぢか')}な{ruby('食料品', 'しょくりょうひん')}や{ruby('衣料', 'いりょう')}品や{ruby('雑貨', 'ざっか')}をはじめ、{ruby('工業製品', 'こうぎょうせいひん')}や{ruby('部品', 'ぶひん')}、{ruby('建設資材', 'けんせつしざい')}のほか、{ruby('石油', 'せきゆ')}やガスなどの{ruby('液体', 'えきたい')}や{ruby('気体', 'きたい')}も{ruby('運', 'はこ')}びます。",
            "id": "Truk mengangkut barang-barang kebutuhan sehari-hari seperti bahan makanan, pakaian, dan barang kebutuhan harian, hingga produk industri, suku cadang, dan bahan bangunan, serta cairan dan gas seperti minyak bumi dan gas."
        }
    ]
}
