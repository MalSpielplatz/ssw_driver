# Fungsi 3 susun dengan warna yang lebih bersih dan profesional
def kotoba(kanji, furigana, arti):
    furigana_html = f"{furigana}" if furigana else "&nbsp;"
    return f"<div style='display: inline-flex; flex-direction: column; align-items: center; vertical-align: bottom; margin: 0 2px;'><span style='font-size: 0.6em; line-height: 1.1; color: #64748b;'>{furigana_html}</span><span style='font-size: 1.2em; line-height: 1.2; font-weight: 500; color: #0f172a;'>{kanji}</span><span style='font-size: 0.6em; line-height: 1.1; color: #0284c7;'>{arti}</span></div>"

# Data berurutan ke bawah
data_bab1 = [
    {
        "is_header": True,
        "jp": "１ 人々の生活や仕事を支えるトラック",
        "id": "1. Truk yang Menopang Kehidupan dan Pekerjaan Masyarakat"
    },
    {
        "is_header": True,
        "jp": "１．１ トラックの役割",
        "id": "1.1 Peran Truk"
    },
    {
        "is_header": False,
        "jp": f"みなさんは{kotoba('今', 'いま', 'sekarang')}、{kotoba('日本', 'にほん', 'Jepang')}でトラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}になるための{kotoba('勉強', 'べんきょう', 'belajar')}を{kotoba('始', 'はじ', 'mulai')}めたところだと{kotoba('思', 'おも', 'berpikir')}います。では、{kotoba('日本', 'にほん', 'Jepang')}では、トラックはどれだけ{kotoba('活躍', 'かつやく', 'berperan')}しているのでしょうか。",
        "id": "Anda sekalian saat ini mungkin baru saja mulai belajar untuk menjadi pengemudi truk di Jepang. Lalu, seberapa besar peran truk di Jepang?"
    },
    {
        "is_header": False,
        "jp": f"トラックは、{kotoba('身近', 'みぢか', 'dekat')}な{kotoba('食料品', 'しょくりょうひん', 'bahan makanan')}や{kotoba('衣料', 'いりょう', 'pakaian')}・{kotoba('雑貨', 'ざっか', 'barang')}をはじめ、{kotoba('工業製品', 'こうぎょうせいひん', 'produk industri')}や{kotoba('部品', 'ぶひん', 'suku cadang')}、{kotoba('建設資材', 'けんせつしざい', 'bahan bangunan')}のほか、{kotoba('石油', 'せきゆ', 'minyak')}やガスなどの{kotoba('液体', 'えきたい', 'cair')}や{kotoba('気体', 'きたい', 'gas')}も{kotoba('運', 'はこ', 'mengangkut')}びます。",
        "id": "Truk mengangkut kebutuhan sehari-hari seperti bahan makanan, pakaian, dan barang kelontong, produk industri dan suku cadang, bahan bangunan, serta benda cair dan gas seperti minyak dan gas."
    }
]
