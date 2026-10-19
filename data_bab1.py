def kotoba(kanji, furigana, arti):
    furigana_html = f"{furigana}" if furigana else "&nbsp;"
    return f"<div style='display: inline-flex; flex-direction: column; align-items: center; vertical-align: bottom; margin: 0 2px;'><span style='font-size: 0.6em; line-height: 1.1; color: #e63946; font-weight: bold;'>{furigana_html}</span><span style='font-size: 1.2em; line-height: 1.2; font-weight: 500; color: #0f172a;'>{kanji}</span><span style='font-size: 0.6em; line-height: 1.1; color: #1d3557;'>{arti}</span></div>"

data_bab1 = [
    {
        "is_header": True,
        "jp": f"１ {kotoba('人々', 'ひとびと', 'orang-orang')} の {kotoba('生活', 'せいかつ', 'kehidupan')} や {kotoba('仕事', 'しごと', 'pekerjaan')} を {kotoba('支える', 'ささえる', 'mendukung')} トラック",
        "id": "1. Truk yang Menopang Kehidupan dan Pekerjaan Masyarakat"
    },
    {
        "is_header": True,
        "jp": f"１．１ トラックの {kotoba('役割', 'やくわり', 'peran')}",
        "id": "1.1 Peran Truk"
    },
    {
        "is_header": False,
        "jp": f"みなさんは {kotoba('今', 'いま', 'sekarang')} 、 {kotoba('日本', 'にほん', 'Jepang')} でトラック {kotoba('運転者', 'うんてんしゃ', 'pengemudi')} になるための {kotoba('勉強', 'べんきょう', 'belajar')} を {kotoba('始', 'はじ', 'mulai')} めたところだと {kotoba('思', 'おも', 'berpikir')} います。 {kotoba('では', '', 'kalau begitu')} 、 {kotoba('日本', 'にほん', 'Jepang')} では、トラックはどれだけ {kotoba('活躍', 'かつやく', 'berperan')} しているのでしょうか。",
        "id": "Anda sekalian mungkin sekarang baru saja mulai belajar untuk menjadi pengemudi truk di Jepang. Kalau begitu, seberapa besar peran truk di Jepang saat ini?"
    },
    {
        "is_header": False,
        "jp": f"トラックは、 {kotoba('身近', 'みぢか', 'dekat')} な {kotoba('食料品', 'しょくりょうひん', 'bahan makanan')} や {kotoba('衣料', 'いりょう', 'pakaian')} ・ {kotoba('雑貨', 'ざっか', 'barang kelontong')} をはじめ、 {kotoba('工業製品', 'こうぎょうせいひん', 'produk industri')} や {kotoba('部品', 'ぶひん', 'suku cadang')} 、 {kotoba('建設資材', 'けんせつしざい', 'bahan bangunan')} のほか、 {kotoba('石油', 'せきゆ', 'minyak bumi')} やガスなどの {kotoba('液体', 'えきたい', 'cairan')} や {kotoba('気体', 'きたい', 'gas')} も {kotoba('運びます', 'はこびます', 'membawa')} 。また、 {kotoba('巨大', 'きょだい', 'raksasa')} な {kotoba('橋', 'はし', 'jembatan')} やプラント {kotoba('設備', 'せつび', 'fasilitas')} など、 {kotoba('特殊', 'とくしゅ', 'khusus')} な {kotoba('物', 'もの', 'barang')} も {kotoba('運びます', 'はこびます', 'membawa')} 。 {kotoba('宅配便', 'たくはいびん', 'paket kiriman')} やコンビニの {kotoba('荷物', 'にもつ', 'barang')} を {kotoba('運んでいる', 'haconde iru', 'sedang membawa')} のもトラックです。 {kotoba('鉄道', 'てつどう', 'kereta api')} 、 {kotoba('船', 'ふね', 'kapal')} 、 {kotoba('飛行機', 'ひこうき', 'pesawat')} による {kotoba('輸送', 'ゆそう', 'pengangkutan')} も {kotoba('行われて', 'おこなわれて', 'dilakukan')} いますが、 {kotoba('駅', 'えき', 'stasiun')} 、 {kotoba('港', 'みなと', 'pelabuhan')} 、 {kotoba('空港', 'くうこう', 'bandara')} の {kotoba('先', 'さき', 'setelahnya')} の {kotoba('輸送', 'ゆそう', 'pengangkutan')} はトラックが {kotoba('運んで', 'はこんで', 'membawa')} います。",
        "id": "Truk tidak hanya membawa barang-barang yang dekat dengan kita seperti bahan makanan, pakaian, dan barang kelontong, tetapi juga produk industri, suku cadang, bahan bangunan, serta cairan dan gas seperti minyak bumi dan gas. Selain itu, truk juga mengangkut barang-barang khusus seperti jembatan raksasa dan fasilitas pabrik. Truk pulalah yang mengangkut paket kiriman dan barang-barang minimarket (konbini). Meskipun pengangkutan juga dilakukan oleh kereta api, kapal laut, dan pesawat terbang, transportasi lanjutan dari stasiun, pelabuhan, dan bandara dilakukan oleh truk."
    },
    {
        "is_header": False,
        "jp": f"このように、 {kotoba('日本', 'にほん', 'Jepang')} では、トラックが {kotoba('国内貨物', 'こくないかもつ', 'kargo domestik')} の9 {kotoba('割以上', 'わりいじょう', 'lebih dari 90%')} を {kotoba('運んで', 'はこんで', 'membawa')} おり、 {kotoba('人々', 'ひとびと', 'orang-orang')} の {kotoba('生活', 'せいかつ', 'kehidupan')} や {kotoba('仕事', 'しごと', 'pekerjaan')} を {kotoba('支えて', 'ささえて', 'mendukung')} います。",
        "id": "Dengan demikian, di Jepang, truk mengangkut lebih dari 90% kargo domestik, mendukung kehidupan dan pekerjaan orang-orang."
    },
    {
        "is_header": False,
        "jp": f"トラック {kotoba('運転者', 'うんてんしゃ', 'pengemudi')} は、まさにエッセンシャルワーカー（ {kotoba('社会生活', 'しゃかいせいかつ', 'kehidupan sosial')} を {kotoba('支える', 'ささえる', 'mendukung')} ために {kotoba('欠かすことのできない', 'kakasu koto no dekinai', 'tidak bisa ditinggalkan')} {kotoba('仕事', 'しごと', 'pekerjaan')} についている {kotoba('人', 'ひと', 'orang')} ）だと {kotoba('言えます', 'いえま', 'dapat dikatakan')} 。",
        "id": "Dapat dikatakan bahwa pengemudi truk benar-benar merupakan pekerja esensial (orang-orang yang melakukan pekerjaan yang mutlak diperlukan untuk mendukung kehidupan sosial)."
    },
    {
        "is_header": True,
        "jp": f"１．２ {kotoba('もしも', '', 'seandainya')} トラック {kotoba('輸送', 'ゆそう', 'pengangkutan')} が {kotoba('止まったら', 'とまったら', 'berhenti')}",
        "id": "1.2 Jika Pengangkutan Truk Berhenti"
    },
    {
        "is_header": False,
        "jp": f"トラック {kotoba('輸送', 'ゆそう', 'pengangkutan')} は、 {kotoba('人々', 'ひとびと', 'orang-orang')} が {kotoba('仕事', 'しごと', 'pekerjaan')} をしたり、 {kotoba('生活', 'せいかつ', 'kehidupan')} をするためにとても {kotoba('大切', 'たいせつ', 'penting')} です。もしも {kotoba('日本中', 'にほんじゅう', 'seluruh Jepang')} のトラック {kotoba('輸送', 'ゆそう', 'pengangkutan')} が {kotoba('止まったら', 'とまったら', 'berhenti')} 、 {kotoba('商品', 'しょうひん', 'しょうひん', 'produk')} や {kotoba('部品', 'ぶひん', 'suku cadang')} 、 {kotoba('薬', 'くすり', 'obat')} などが {kotoba('運べなくなり', 'はこべなくなり', 'tidak bisa diangkut')} 、 {kotoba('日本中', 'にほんじゅう', 'seluruh Jepang')} のお {kotoba('店', 'みせ', 'toko')} や {kotoba('工場', 'こうじょう', 'pabrik')} 、 {kotoba('病院', 'びょういん', 'rumah sakit')} などで {kotoba('仕事', 'しごと', 'pekerjaan')} ができなくなってしまいます。",
        "id": "Pengangkutan truk sangat penting bagi orang-orang untuk bekerja dan menjalani kehidupan. Seandainya pengangkutan truk di seluruh Jepang berhenti, produk, suku cadang, obat-obatan, dan lain-lain tidak akan bisa diangkut, sehingga toko, pabrik, dan rumah sakit di seluruh Jepang tidak akan bisa beroperasi."
    }
]
