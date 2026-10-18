def kotoba(kanji, furigana, arti):
    furigana_html = f"{furigana}" if furigana else "&nbsp;"
    # HAPUS semua enter dan jadikan string satu baris lurus agar tidak dibaca sebagai Markdown Code Block
    return f"<div style='display: inline-flex; flex-direction: column; align-items: center; vertical-align: bottom; margin: 0 2px;'><span style='font-size: 0.6em; line-height: 1.1; color: #666;'>{furigana_html}</span><span style='font-size: 1.2em; line-height: 1.2; font-weight: 500;'>{kanji}</span><span style='font-size: 0.6em; line-height: 1.1; color: #0066cc;'>{arti}</span></div>"

# Diubah menjadi List agar dieksekusi berurutan dari atas ke bawah
data_bab1 = [
    # --- BAGIAN 1 ---
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
        "jp": f"トラックは、{kotoba('身近', 'みぢか', 'dekat/sehari-hari')}な{kotoba('食料品', 'しょくりょうひん', 'bahan makanan')}や{kotoba('衣料', 'いりょう', 'pakaian')}・{kotoba('雑貨', 'ざっか', 'barang kelontong')}をはじめ、{kotoba('工業製品', 'こうぎょうせいひん', 'produk industri')}や{kotoba('部品', 'ぶひん', 'suku cadang')}、{kotoba('建設資材', 'けんせつしざい', 'bahan konstruksi')}のほか、{kotoba('石油', 'せきゆ', 'minyak')}や{kotoba('ガス', '', 'gas')}などの{kotoba('液体', 'えきたい', 'cair')}や{kotoba('気体', 'きたい', 'gas')}も{kotoba('運', 'はこ', 'mengangkut')}びます。",
        "id": "Truk mengangkut kebutuhan sehari-hari seperti bahan makanan, pakaian, dan barang kelontong, produk industri dan suku cadang, bahan konstruksi, serta benda cair dan gas seperti minyak dan gas."
    },
    {
        "is_header": False,
        "jp": f"また、{kotoba('巨大', 'きょだい', 'raksasa')}な{kotoba('橋', 'はし', 'jembatan')}やプラント{kotoba('設備', 'せつび', 'peralatan')}など、{kotoba('特殊', 'とくしゅ', 'khusus')}な{kotoba('物', 'もの', 'barang')}も{kotoba('運', 'はこ', 'mengangkut')}びます。{kotoba('宅配便', 'たくはいびん', 'paket kurir')}やコンビニの{kotoba('荷物', 'にもつ', 'barang/muatan')}を{kotoba('運', 'はこ', 'mengangkut')}んでいるのもトラックです。",
        "id": "Selain itu, truk juga mengangkut barang khusus seperti jembatan raksasa dan peralatan pabrik. Truk pulalah yang mengangkut paket kurir dan barang-barang minimarket."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('鉄道', 'てつどう', 'Kereta api')}、{kotoba('船', 'ふね', 'kapal')}、{kotoba('飛行機', 'ひこうき', 'pesawat')}による{kotoba('輸送', 'ゆそう', 'transportasi')}も{kotoba('行', 'おこな', 'dilakukan')}われていますが、{kotoba('駅', 'えき', 'stasiun')}、{kotoba('港', 'みなと', 'pelabuhan')}、{kotoba('空港', 'くうこう', 'bandara')}の{kotoba('先', 'さき', 'tujuan lanjutan')}の{kotoba('輸送', 'ゆそう', 'transportasi')}はトラックが{kotoba('運', 'はこ', 'mengangkut')}んでいます。",
        "id": "Meskipun transportasi melalui kereta api, kapal laut, dan pesawat terbang juga dilakukan, namun transportasi lanjutan dari stasiun, pelabuhan, dan bandara diangkut oleh truk."
    },
    
    # --- BAGIAN 1.2 ---
    {
        "is_header": True,
        "jp": "１．２ もしもトラック輸送が止まったら",
        "id": "1.2 Jika Transportasi Truk Berhenti"
    },
    {
        "is_header": False,
        "jp": f"トラック{kotoba('輸送', 'ゆそう', 'transportasi')}は、{kotoba('人々', 'ひとびと', 'orang-orang')}が{kotoba('仕事', 'しごと', 'pekerjaan')}をしたり、{kotoba('生活', 'せいかつ', 'kehidupan')}をしたりするためにとても{kotoba('大切', 'たいせつ', 'penting')}です。もしも{kotoba('日本中', 'にほんじゅう', 'seluruh Jepang')}のトラック{kotoba('輸送', 'ゆそう', 'transportasi')}が{kotoba('止', 'と', 'berhenti')}まったら、{kotoba('商品', 'しょうひん', 'barang dagangan')}や{kotoba('部品', 'ぶひん', 'suku cadang')}、{kotoba('薬', 'くすり', 'obat')}などが{kotoba('運', 'はこ', 'diangkut')}べなくなり、{kotoba('日本中', 'にほんじゅう', 'seluruh Jepang')}のお{kotoba('店', 'みせ', 'toko')}や{kotoba('工場', 'こうじょう', 'pabrik')}、{kotoba('病院', 'びょういん', 'rumah sakit')}などで{kotoba('仕事', 'しごと', 'pekerjaan')}ができなくなってしまいます。",
        "id": "Transportasi truk sangat penting agar orang-orang dapat bekerja dan menjalani kehidupan. Jika transportasi truk di seluruh Jepang terhenti, barang dagangan, suku cadang, obat-obatan, dan lainnya tidak akan bisa diangkut, sehingga toko, pabrik, dan rumah sakit di seluruh Jepang tidak akan bisa beroperasi."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('日本', 'にほん', 'Jepang')}でも、２０１１{kotoba('年', 'ねん', 'tahun')}の{kotoba('東日本大震災', 'ひがしにほんだいしんさい', 'Gempa Besar Jepang Timur')}の{kotoba('直後', 'ちょくご', 'sesaat setelah')}には、{kotoba('燃料不足', 'ねんりょうぶそく', 'kekurangan bahan bakar')}により{kotoba('多', 'おお', 'banyak')}くのトラックが{kotoba('走', 'はし', 'berjalan')}ることができなくなり、しばらくの{kotoba('間', 'あいだ', 'waktu')}、コンビニなどで{kotoba('商品', 'しょうひん', 'barang dagangan')}を{kotoba('買', 'か', 'membeli')}えなくなってしまいました。",
        "id": "Di Jepang pun, sesaat setelah Gempa Besar Jepang Timur tahun 2011, banyak truk yang tidak bisa beroperasi karena kekurangan bahan bakar, sehingga untuk sementara waktu barang dagangan tidak bisa dibeli di minimarket dan tempat lainnya."
    },
    
    # Tambahkan sisa materi Bab 1.3 sampai 7.2 di bawah sini mengikuti pola yang sama...
]
