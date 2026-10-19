# Fungsi 3 susun: Furigana merah di atas, Kanji di tengah, Arti di bawah
def kotoba(kanji, furigana, arti):
    furigana_html = f"{furigana}" if furigana else "&nbsp;"
    return f"<div style='display: inline-flex; flex-direction: column; align-items: center; vertical-align: bottom; margin: 0 2px;'><span style='font-size: 0.6em; line-height: 1.1; color: #e63946; font-weight: bold;'>{furigana_html}</span><span style='font-size: 1.2em; line-height: 1.2; font-weight: 500; color: #0f172a;'>{kanji}</span><span style='font-size: 0.6em; line-height: 1.1; color: #1d3557;'>{arti}</span></div>"

# Data berurutan ke bawah untuk scroll panjang
data_bab1 = [
    {
        "is_header": True,
        "jp": f"１ {kotoba('人々', 'ひとびと', 'orang-orang')}の{kotoba('生活', 'せいかつ', 'kehidupan')}や{kotoba('仕事', 'しごと', 'pekerjaan')}を{kotoba('支える', 'ささえる', 'mendukung')}トラック",
        "id": "1. Truk yang Menopang Kehidupan dan Pekerjaan Masyarakat"
    },
    {
        "is_header": True,
        "jp": f"１．１ トラックの{kotoba('役割', 'やくわり', 'peran')}",
        "id": "1.1 Peran Truk"
    },
    {
        "is_header": False,
        "jp": f"みなさんは{kotoba('今', 'いま', 'sekarang')}、{kotoba('日本', 'にほん', 'Jepang')}でトラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}になるための{kotoba('勉強', 'べんきょう', 'belajar')}を{kotoba('始', 'はじ', 'mulai')}めたところだと{kotoba('思', 'おも', 'berpikir')}います。{kotoba('では', '', 'kalau begitu')}、{kotoba('日本', 'にほん', 'Jepang')}では、トラックはどれだけ{kotoba('活躍', 'かつやく', 'berperan')}しているのでしょうか。",
        "id": "Anda sekalian mungkin sekarang baru saja mulai belajar untuk menjadi pengemudi truk di Jepang. Kalau begitu, seberapa besar peran truk di Jepang saat ini?"
    },
    {
        "is_header": False,
        "jp": f"トラックは、{kotoba('身近', 'みぢか', 'dekat')}な{kotoba('食料品', 'しょくりょうひん', 'bahan makanan')}や{kotoba('衣料', 'いりょう', 'pakaian')}・{kotoba('雑貨', 'ざっか', 'barang kelontong')}をはじめ、{kotoba('工業製品', 'こうぎょうせいひん', 'produk industri')}や{kotoba('部品', 'ぶひん', 'suku cadang')}、{kotoba('建設資材', 'けんせつしざい', 'bahan bangunan')}のほか、{kotoba('石油', 'せきゆ', 'minyak bumi')}やガスなどの{kotoba('液体', 'えきたい', 'cairan')}や{kotoba('気体', 'きたい', 'gas')}も{kotoba('運びます', 'はこびます', 'membawa')}。また、{kotoba('巨大', 'きょだい', 'raksasa')}な{kotoba('橋', 'はし', 'jembatan')}やプラント{kotoba('設備', 'せつび', 'fasilitas')}など、{kotoba('特殊', 'とくしゅ', 'khusus')}な{kotoba('物', 'もの', 'barang')}も{kotoba('運びます', 'はこびます', 'membawa')}。{kotoba('宅配便', 'たくはいびん', 'paket kiriman')}やコンビニの{kotoba('荷物', 'にもつ', 'barang')}を{kotoba('運んでいる', 'はこんでいる', 'sedang membawa')}のもトラックです。{kotoba('鉄道', 'てつどう', 'kereta api')}、{kotoba('船', 'ふね', 'kapal')}、{kotoba('飛行機', 'ひこうき', 'pesawat')}による{kotoba('輸送', 'ゆそう', 'pengangkutan')}も{kotoba('行われて', 'おこなわれて', 'dilakukan')}いますが、{kotoba('駅', 'えき', 'stasiun')}、{kotoba('港', 'みなと', 'pelabuhan')}、{kotoba('空港', 'くうこう', 'bandara')}の{kotoba('先', 'さき', 'setelahnya')}の{kotoba('輸送', 'ゆそう', 'pengangkutan')}はトラックが{kotoba('運んで', 'はこんで', 'membawa')}います。",
        "id": "Truk tidak hanya membawa barang-barang yang dekat dengan kita seperti bahan makanan, pakaian, dan barang kelontong, tetapi juga produk industri, suku cadang, bahan bangunan, serta cairan dan gas seperti minyak bumi dan gas. Selain itu, truk juga mengangkut barang-barang khusus seperti jembatan raksasa dan fasilitas pabrik. Truk pulalah yang mengangkut paket kiriman dan barang-barang minimarket (konbini). Meskipun pengangkutan juga dilakukan oleh kereta api, kapal laut, dan pesawat terbang, transportasi lanjutan dari stasiun, pelabuhan, dan bandara dilakukan oleh truk."
    },
    {
        "is_header": False,
        "jp": f"このように、{kotoba('日本', 'にほん', 'Jepang')}では、トラックが{kotoba('国内貨物', 'こくないかもつ', 'kargo domestik')}の9{kotoba('割以上', 'わりいじょう', 'lebih dari 90%')}を{kotoba('運んで', 'はこんで', 'membawa')}おり、{kotoba('人々', 'ひとびと', 'orang-orang')}の{kotoba('生活', 'せいかつ', 'kehidupan')}や{kotoba('仕事', 'しごと', 'pekerjaan')}を{kotoba('支えて', 'ささえて', 'mendukung')}います。",
        "id": "Dengan demikian, di Jepang, truk mengangkut lebih dari 90% kargo domestik, mendukung kehidupan dan pekerjaan orang-orang."
    },
    {
        "is_header": False,
        "jp": f"トラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}は、まさにエッセンシャルワーカー（{kotoba('社会生活', 'しゃかいせいかつ', 'kehidupan sosial')}を{kotoba('支える', 'ささえる', 'mendukung')}ために{kotoba('欠かすことのできない', 'かかすことのできない', 'tidak bisa ditinggalkan')}{kotoba('仕事', 'しごと', 'pekerjaan')}についている{kotoba('人', 'ひと', 'orang')}）だと{kotoba('言えます', 'いえま', 'dapat dikatakan')}。",
        "id": "Dapat dikatakan bahwa pengemudi truk benar-benar merupakan pekerja esensial (orang-orang yang melakukan pekerjaan yang mutlak diperlukan untuk mendukung kehidupan sosial)."
    },
    {
        "is_header": True,
        "jp": f"１．２ {kotoba('もしも', '', 'seandainya')}トラック{kotoba('輸送', 'ゆそう', 'pengangkutan')}が{kotoba('止まったら', 'とまったら', 'berhenti')}",
        "id": "1.2 Jika Pengangkutan Truk Berhenti"
    },
    {
        "is_header": False,
        "jp": f"トラック{kotoba('輸送', 'ゆそう', 'pengangkutan')}は、{kotoba('人々', 'ひとびと', 'orang-orang')}が{kotoba('仕事', 'しごと', 'pekerjaan')}をしたり、{kotoba('生活', 'せいかつ', 'kehidupan')}をするためにとても{kotoba('大切', 'たいせつ', 'penting')}です。もしも{kotoba('日本中', 'にほんじゅう', 'seluruh Jepang')}のトラック{kotoba('輸送', 'ゆそう', 'pengangkutan')}が{kotoba('止まったら', 'とまったら', 'berhenti')}、{kotoba('商品', 'しょうひん', 'produk')}や{kotoba('部品', 'ぶひん', 'suku cadang')}、{kotoba('薬', 'くすり', 'obat')}などが{kotoba('運べなくなり', 'はこべなくなり', 'tidak bisa diangkut')}、{kotoba('日本中', 'にほんじゅう', 'seluruh Jepang')}のお{kotoba('店', 'みせ', 'toko')}や{kotoba('工場', 'こうじょう', 'pabrik')}、{kotoba('病院', 'びょういん', 'rumah sakit')}などで{kotoba('仕事', 'しごと', 'pekerjaan')}ができなくなってしまいます。",
        "id": "Pengangkutan truk sangat penting bagi orang-orang untuk bekerja dan menjalani kehidupan. Seandainya pengangkutan truk di seluruh Jepang berhenti, produk, suku cadang, obat-obatan, dan lain-lain tidak akan bisa diangkut, sehingga toko, pabrik, dan rumah sakit di seluruh Jepang tidak akan bisa beroperasi."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('日本', 'にほん', 'Jepang')}でも、2011{kotoba('年', 'ねん', 'tahun')}の{kotoba('東日本大震災', 'ひがしにほんだいしんさい', 'Gempa Besar Jepang Timur')}の{kotoba('直後', 'ちょくご', 'tepat setelah')}には、{kotoba('燃料不足', 'ねんりょうぶそく', 'kekurangan bahan bakar')}により{kotoba('多く', 'おおく', 'banyak')}のトラックが{kotoba('走る', 'はしる', 'berjalan')}{kotoba('こと', '', 'hal')}ができなくなり、しばらくの{kotoba('間', 'あいだ', 'selama')}、コンビニなどで{kotoba('商品', 'しょうひん', 'produk')}を{kotoba('買えなく', 'かえなく', 'tidak bisa dibeli')}なってしまいました。",
        "id": "Di Jepang sekalipun, tepat setelah Gempa Bumi Besar Jepang Timur tahun 2011, kekurangan bahan bakar menyebabkan banyak truk tidak bisa beroperasi, sehingga untuk sementara waktu barang tidak bisa dibeli di minimarket dan tempat lainnya."
    },
    {
        "is_header": False,
        "jp": f"ヨーロッパやアジアなどでは、ストライキでトラックがときどき{kotoba('止まります', 'とまります', 'berhenti')}。あるとき、スペインではストライキでタンクローリーが{kotoba('止まり', 'とまり', 'berhenti')}、{kotoba('燃料', 'ねんりょう', 'bahan bakar')}スタンドにガソリンを{kotoba('運べなかった', 'はこべなかった', 'tidak bisa membawa')}ためガソリンが{kotoba('不足', 'ふそく', 'kurang')}しました。そのため{kotoba('市民', 'しみん', 'warga')}が{kotoba('買い物', 'かいもの', 'belanja')}や{kotoba('病院', 'びょういん', 'rumah sakit')}に{kotoba('行けない', 'いけない', 'tidak bisa pergi')}などの{kotoba('困った', 'こまった', 'menyusahkan')}{kotoba('事態', 'じたい', 'situasi')}が{kotoba('起こりました', 'おこりました', 'terjadi')}。",
        "id": "Di Eropa dan Asia, pemogokan terkadang membuat truk berhenti. Suatu ketika di Spanyol, truk tangki berhenti akibat pemogokan dan tidak dapat mengirimkan bensin ke pom bensin, yang menyebabkan kelangkaan bensin. Akibatnya, terjadi situasi yang menyulitkan di mana warga tidak bisa berbelanja atau pergi ke rumah sakit."
    },
    {
        "is_header": False,
        "jp": f"トラックが{kotoba('物', 'もの', 'barang')}を{kotoba('運ばなければ', 'はこばなければ', 'jika tidak diangkut')}、{kotoba('同じ', 'おなじ', 'sama')}{kotoba('こと', '', 'hal')}が{kotoba('工場', 'こうじょう', 'pabrik')}の{kotoba('生産活動', 'せいさんかつどう', 'kegiatan生産')}をはじめ{kotoba('市場', 'しじょう', 'pasar')}や{kotoba('建設現場', 'けんせつげんば', 'lokasi konstruksi')}などでも{kotoba('起こる', 'おこる', 'terjadi')}{kotoba('可能性', 'かのうせい', 'kemungkinan')}があります。",
        "id": "Jika truk tidak mengangkut barang, hal yang sama juga bisa terjadi pada kegiatan produksi pabrik, pasar, dan lokasi konstruksi."
    },
    {
        "is_header": False,
        "jp": f"このように、トラック{kotoba('輸送', 'ゆそう', 'pengangkutan')}が、{kotoba('経済活動', 'けいざいかつどう', 'kegiatan ekonomi')}や{kotoba('生活', 'せいかつ', 'kehidupan')}のためにとても{kotoba('大切', 'たいせつ', 'penting')}であることを、{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}のみなさんも{kotoba('知って', 'しって', 'mengetahui')}おいてください。",
        "id": "Oleh karena itu, Anda sekalian para pengemudi juga harus mengetahui bahwa pengangkutan truk sangatlah penting bagi kegiatan ekonomi dan kehidupan."
    },
    {
        "is_header": True,
        "jp": f"１．３ {kotoba('運転免許', 'うんてんめんきょ', 'SIM')}のしくみと{kotoba('事業用', 'じぎょうよう', 'untuk bisnis')}トラックと{kotoba('自家用', 'じかよう', 'untuk pribadi')}トラックの{kotoba('違い', 'ちがい', 'perbedaan')}",
        "id": "1.3 Sistem SIM dan Perbedaan Truk Bisnis & Truk Pribadi"
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('運転免許', 'うんてんめんきょ', 'SIM')}のしくみ",
        "id": "・Sistem Surat Izin Mengemudi (SIM)"
    },
    {
        "is_header": False,
        "jp": f"トラックを{kotoba('運転', 'うんてん', 'mengemudi')}するためには、そのトラックの{kotoba('大きさ', 'おおきさ', 'ukuran')}に{kotoba('応じた', 'おうじた', 'sesuai')}{kotoba('運転免許', 'うんてんめんきょ', 'SIM')}が{kotoba('必要', 'ひつよう', 'perlu')}です。{kotoba('運転免許', 'うんてんめんきょ', 'SIM')}の{kotoba('種類', 'しゅるい', 'jenis')}に{kotoba('応じて', 'おうじて', 'sesuai')}{kotoba('運転', 'うんてん', 'mengemudi')}できる{kotoba('車', 'くるま', 'kendaraan')}は{kotoba('次', 'つぎ', 'berikut')}のとおりです。",
        "id": "Untuk mengemudikan truk, diperlukan SIM yang sesuai dengan ukuran truk tersebut. Kendaraan yang dapat dikemudikan berdasarkan jenis SIM adalah sebagai berikut:"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('大型免許', 'おおがためんきょ', 'SIM besar')}: {kotoba('大型自動車', 'おおがたじどうしゃ', 'kend. besar')}、{kotoba('中型自動車', 'ちゅうがたじどうしゃ', 'kend. menengah')}、{kotoba('準中型自動車', 'じゅんちゅうがたじどうしゃ', 'kend. semi-menengah')}、{kotoba('普通自動車', 'ふつうじどうしゃ', 'kend. biasa')}、{kotoba('小型特殊自動車', 'こがたとくしゅじどうしゃ', 'kend. khusus kecil')}",
        "id": "SIM Besar: Kendaraan besar, kendaraan menengah, kendaraan semi-menengah, kendaraan biasa, kendaraan khusus kecil."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('中型免許', 'ちゅうがためんきょ', 'SIM menengah')}: {kotoba('中型自動車', 'ちゅうがたじどうしゃ', 'kend. menengah')}、{kotoba('準中型自動車', 'じゅんちゅうがたじどうしゃ', 'kend. semi-menengah')}、{kotoba('普通自動車', 'ふつうじどうしゃ', 'kend. biasa')}、{kotoba('小型特殊自動車', 'こがたとくしゅじどうしゃ', 'kend. khusus kecil')}",
        "id": "SIM Menengah: Kendaraan menengah, kendaraan semi-menengah, kendaraan biasa, kendaraan khusus kecil."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('準中型免許', 'じゅんちゅうがためんきょ', 'SIM semi-menengah')}: {kotoba('準中型自動車', 'じゅんちゅうがたじどうしゃ', 'kend. semi-menengah')}、{kotoba('普通自動車', 'ふつうじどうしゃ', 'kend. biasa')}、{kotoba('小型特殊自動車', 'こがたとくしゅじどうしゃ', 'kend. khusus kecil')}",
        "id": "SIM Semi-Menengah: Kendaraan semi-menengah, kendaraan biasa, kendaraan khusus kecil."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('普通免許', 'ふつうめんきょ', 'SIM biasa')}: {kotoba('普通自動車', 'ふつうじどうしゃ', 'kend. biasa')}、{kotoba('小型特殊自動車', 'こがたとくしゅじどうしゃ', 'kend.特別')} ",
        "id": "SIM Biasa: Kendaraan biasa, kendaraan khusus kecil."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('事業用', 'じぎょうよう', 'untuk bisnis')}トラックと{kotoba('自家用', 'じかよう', 'untuk pribadi')}トラックの{kotoba('違い', 'ちがい', 'perbedaan')}",
        "id": "・Perbedaan Truk untuk Bisnis dan Truk Pribadi"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('日本', 'にほん', 'Jepang')}には、「{kotoba('事業用', 'じぎょうよう', 'untuk bisnis')}トラック」と「{kotoba('自家用', 'じかよう', 'untuk pribadi')}トラック」の2{kotoba('種類', 'しゅるい', 'jenis')}のトラックがあります。",
        "id": "Di Jepang, terdapat dua jenis truk: \"Truk untuk Bisnis\" dan \"Truk untuk Pribadi\"."
    },
    {
        "is_header": False,
        "jp": f"「{kotoba('事業用', 'じぎょうよう', 'untuk bisnis')}トラック」は、{kotoba('国土交通大臣', 'こくどこうつうだいじん', 'Menteri Transportasi')}から{kotoba('営業', 'えいぎょう', 'bisnis')}を{kotoba('許可', 'きょか', 'izin')}されたトラック{kotoba('運送事業者', 'うんそうじぎょうしゃ', 'perusahaan angkutan')}（{kotoba('運送会社', 'うんそうがいしゃ', 'perusahaan angkutan')}）のトラックです。{kotoba('日本', 'にほん', 'Jepang')}では、お{kotoba('客様', 'きゃくさま', 'pelanggan')}から{kotoba('有償', 'ゆうしょう', 'berbayar')}でお{kotoba('客様', 'きゃくさま', 'pelanggan')}の{kotoba('荷物', 'にもつ', 'barang')}を{kotoba('運ぶ', 'はこぶ', 'mengangkut')}ことができるのは、{kotoba('事業用', 'じぎょうよう', 'untuk bisnis')}トラックだけです。{kotoba('事業用', 'じぎょうよう', 'untuk bisnis')}トラックのナンバープレートは「{kotoba('緑地', 'みどりじ', 'latar hijau')}に{kotoba('白い', 'しろい', 'putih')}{kotoba('文字', 'もじ', 'huruf')}」であり、「{kotoba('緑', 'みどり', 'hijau')}ナンバー」などとも{kotoba('呼ばれて', 'よばれて', 'disebut')}います。",
        "id": "\"Truk untuk Bisnis\" adalah truk milik perusahaan angkutan yang telah mendapatkan izin operasional dari Menteri Pertanahan, Infrastruktur, Transportasi, dan Pariwisata. Di Jepang, hanya truk untuk bisnis yang diizinkan mengangkut barang pelanggan dengan kompensasi (bayaran). Plat nomor truk untuk bisnis memiliki \"latar belakang hijau dengan huruf putih\", dan sering disebut juga \"Plat Hijau\"."
    },
    {
        "is_header": False,
        "jp": f"「{kotoba('自家用', 'じかよう', 'untuk pribadi')}トラック」は、{kotoba('会社', 'かいしゃ', 'perusahaan')}やお{kotoba('店', 'みせ', 'toko')}、{kotoba('個人', 'こじん', 'individu')}が、{kotoba('自分', 'じぶん', 'sendiri')}の{kotoba('荷物', 'にもつ', 'barang')}を{kotoba('運ぶ', 'はこぶ', 'mengangkut')}ためのトラックです。{kotoba('自家用', 'じかよう', 'untuk pribadi')}トラックは、{kotoba('有償', 'ゆうしょう', 'berbayar')}でお{kotoba('客様', 'きゃくさま', 'pelanggan')}の{kotoba('荷物', 'にもつ', 'barang')}を{kotoba('運ぶ', 'はこぶ', 'mengangkut')}ことはできません。{kotoba('自家用', 'じかよう', 'untuk pribadi')}トラックのナンバープレートは「{kotoba('白地', 'しろじ', 'latar putih')}に{kotoba('緑', 'みどり', 'hijau')}の{kotoba('文字', 'もじ', 'huruf')}」であり、「{kotoba('白', 'しろ', 'putih')}ナンバー」とも{kotoba('呼ばれて', 'よばれて', 'disebut')}います。",
        "id": "\"Truk Pribadi\" adalah truk yang digunakan oleh perusahaan, toko, atau individu untuk mengangkut barang mereka sendiri. Truk pribadi tidak diizinkan untuk mengangkut barang pelanggan dengan bayaran. Plat nomor truk pribadi memiliki \"latar belakang putih dengan huruf hijau\", dan disebut juga \"Plat Putih\"."
    },
    {
        "is_header": True,
        "jp": f"２ トラック{kotoba('事故', 'じこ', 'kecelakaan')}の{kotoba('社会的影響', 'しゃかいてきえいきょう', 'dampak sosial')}",
        "id": "2 Dampak Sosial Kecelakaan Truk"
    },
    {
        "is_header": True,
        "jp": f"２．１ {kotoba('社会的', 'しゃかいてき', 'secara sosial')}に{kotoba('影響', 'えいきょう', 'dampak')}の{kotoba('大きい', 'おおきい', 'besar')}トラック{kotoba('事故', 'じこ', 'kecelakaan')}",
        "id": "2.1 Kecelakaan Truk Berdampak Besar Secara Sosial"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('荷物', 'にもつ', 'barang')}を{kotoba('安全', 'あんぜん', 'aman')}・{kotoba('安心', 'あんしん', 'tenang')}・{kotoba('確実', 'かくじつ', 'pasti')}に{kotoba('輸送', 'ゆそう', 'transportasi')}していくためには、いつも{kotoba('安全', 'あんぜん', 'keselamatan')}を{kotoba('最優先', 'さいゆうせん', 'prioritas utama')}させなければいけません。",
        "id": "Untuk mengangkut barang dengan aman, tenang, dan pasti, keselamatan harus selalu menjadi prioritas utama."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('とくに', '', 'terutama')}{kotoba('交通事故', 'こうつうじこ', 'kecelakaan lalu lintas')}は、{kotoba('人', 'ひと', 'orang')}の{kotoba('命', 'いのち', 'nyawa')}を{kotoba('奪ったり', 'うばったり', 'merenggut')}{kotoba('傷つけたり', 'きずつけたり', 'melukai')}するだけでなく、{kotoba('会社', 'かいしゃ', 'perusahaan')}の{kotoba('経営', 'けいえい', 'manajemen')}にも{kotoba('影響', 'えいきょう', 'dampak')}を{kotoba('与えます', 'あたえます', 'memberikan')}。",
        "id": "Terutama kecelakaan lalu lintas, tidak hanya merenggut atau melukai nyawa manusia, tetapi juga berdampak pada manajemen perusahaan."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('他', 'ほか', 'lain')}の{kotoba('車', 'くるま', 'kendaraan')}に{kotoba('比べて', 'くらべて', 'dibandingkan')}{kotoba('車体', 'しゃたい', 'bodi kendaraan')}が{kotoba('大きく', 'おおきく', 'besar')}{kotoba('重い', 'おもい', 'berat')}トラックは、{kotoba('いったん', '', 'sekali')}{kotoba('事故', 'じこ', 'kecelakaan')}を{kotoba('起こす', 'おこす', 'menyebabkan')}と、{kotoba('重大事故', 'じゅうだいじこ', 'kecelakaan fatal')}に{kotoba('つながります', '', 'berujung pada')}。{kotoba('そのため', '', 'oleh karena itu')}、{kotoba('被害者', 'ひがいしゃ', 'korban')}だけでなく、その{kotoba('家族', 'かぞく', 'keluarga')}の{kotoba('生活', 'せいかつ', 'kehidupan')}にも{kotoba('影響', 'えいきょう', 'berdampak')}します。",
        "id": "Truk, yang bodinya lebih besar dan berat dibandingkan kendaraan lain, akan berujung pada kecelakaan fatal sekali kecelakaan itu terjadi. Oleh karena itu, hal ini berdampak tidak hanya pada korban, tetapi juga pada kehidupan keluarga mereka."
    },
    {
        "is_header": False,
        "jp": f"また、トラック{kotoba('運送業界', 'うんそうぎょうかい', 'industri angkutan')}や{kotoba('社会全体', 'しゃかいぜんたい', 'masyarakat keseluruhan')}にも{kotoba('大きな', 'おおきな', 'besar')}{kotoba('損失', 'そんしつ', 'kerugian')}を{kotoba('与えます', 'あたえます', 'memberikan')}。{kotoba('ひとり', '', 'satu orang')}のトラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}の{kotoba('事故', 'じこ', 'kecelakaan')}によって、{kotoba('多く', 'おおく', 'banyak')}の{kotoba('運送会社', 'うんそうがいしゃ', 'perusahaan angkutan')}のトラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}が{kotoba('影響', 'えいきょう', 'dampak')}を{kotoba('受ける', 'うける', 'menerima')}ということを{kotoba('忘れてはいけません', 'わすれてはいけません', 'tidak boleh lupa')}。",
        "id": "Selain itu, hal ini juga memberikan kerugian besar pada industri angkutan truk dan masyarakat secara keseluruhan. Tidak boleh dilupakan bahwa kecelakaan yang disebabkan oleh satu orang pengemudi truk akan memengaruhi pengemudi truk dari banyak perusahaan angkutan."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('事業用', 'じぎょうよう', 'untuk bisnis')}トラックの{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}は、{kotoba('一般', 'いっぱん', 'umum')}の{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}とはまったく{kotoba('違う', 'ちがう', 'berbeda')}「プロ{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}」です。{kotoba('職業', 'しょくぎょう', 'profesi')}としてトラックを{kotoba('運転', 'うんてん', 'mengemudi')}しているというプロ{kotoba('意識', 'いしき', 'kesadaran')}と、{kotoba('絶対', 'ぜったい', 'pasti')}に{kotoba('事故', 'じこ', 'kecelakaan')}を{kotoba('起こしてはいけない', 'おこしてはいけない', 'tidak boleh menyebabkan')}という{kotoba('強い', 'つよい', 'kuat')}{kotoba('信念', 'しんねん', 'keyakinan')}を{kotoba('持ちましょう', 'もちましょう', 'mari miliki')}。",
        "id": "Pengemudi truk untuk bisnis adalah \"pengemudi profesional\" yang sama sekali berbeda dengan pengemudi umum. Mari miliki kesadaran profesional bahwa Anda mengemudikan truk sebagai sebuah profesi, dan keyakinan kuat bahwa Anda mutlak tidak boleh menyebabkan kecelakaan."
    },
    {
        "is_header": True,
        "jp": f"２．２ {kotoba('追突事故', 'ついとつじこ', 'kecelakaan tabrak belakang')}の{kotoba('発生状況', 'はっせいじょうきょう', 'situasi terjadinya')}",
        "id": "2.2 Situasi Terjadinya Kecelakaan Tabrak Belakang"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('事業用', 'じぎょうよう', 'untuk bisnis')}トラックの{kotoba('交通事故', 'こうつうじこ', 'kecelakaan lalu lintas')}のうち、およそ{kotoba('半分', 'はんぶん', 'setengah')}が{kotoba('追突事故', 'ついとつじこ', 'kecelakaan tabrak belakang')}です。",
        "id": "Dari kecelakaan lalu lintas yang melibatkan truk bisnis, sekitar setengahnya adalah kecelakaan tabrak belakang."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('追突事故', 'ついとつじこ', 'kecelakaan tabrak belakang')}の{kotoba('多く', 'おおく', 'kebanyakan')}は、{kotoba('漫然運転', 'まんぜんうんてん', 'mengemudi tanpa konsentrasi')}（{kotoba('十分', 'じゅうぶん', 'cukup')}な{kotoba('注意', 'ちゅうい', 'perhatian')}をしないで{kotoba('運転', 'うんてん', 'mengemudi')}すること）や{kotoba('脇見運転', 'わきみうんてん', 'mengemudi sambil menoleh')}によるものですが、その{kotoba('中', 'なか', 'dalam')}には{kotoba('居眠り運転', 'いねむりうんてん', 'mengemudi sambil kantuk')}や{kotoba('過労運転', 'かろううんてん', 'mengemudi karena lelah')}なども{kotoba('含まれて', 'ふくまれて', 'termasuk')}います。また、{kotoba('一般道路', 'いっぱんどうろ', 'jalan umum')}では{kotoba('渋滞', 'じゅうたい', 'macet')}している{kotoba('車', 'くるま', 'kendaraan')}に{kotoba('遅い', 'おそい', 'lambat')}{kotoba('速度', 'そくど', 'kecepatan')}で{kotoba('追突', 'ついとつ', 'menabrak dr belakang')}するケースが{kotoba('多く', 'おおく', 'banyak')}、{kotoba('高速道路', 'こうそくどうろ', 'jalan tol')}では、{kotoba('渋滞', 'じゅうたい', 'macet')}の{kotoba('最後', 'さいご', 'akhir')}に{kotoba('停止', 'ていし', 'berhenti')}している{kotoba('車', 'くるま', 'kendaraan')}に{kotoba('速い', 'はやい', 'cepat')}{kotoba('速度', 'そくど', 'kecepatan')}で{kotoba('追突', 'ついとつ', 'menabrak dr belakang')}するケースが{kotoba('目立って', 'めだって', 'menonjol')}います。",
        "id": "Banyak kecelakaan tabrak belakang disebabkan oleh mengemudi tanpa konsentrasi (mengemudi tanpa cukup perhatian) dan mengemudi sambil melihat ke arah lain, tetapi hal ini juga mencakup mengemudi karena mengantuk dan mengemudi karena kelelahan. Selain itu, di jalan umum, banyak kasus menabrak kendaraan yang sedang macet dari belakang dengan kecepatan lambat, dan di jalan tol, kasus menabrak kendaraan yang berhenti di akhir kemacetan dari belakang dengan kecepatan tinggi sangatlah menonjol."
    },
    {
        "is_header": True,
        "jp": f"２．３ {kotoba('交差点事故', 'こうさてんじこ', 'kecelakaan di persimpangan')}の{kotoba('発生状況', 'はっせいじょうきょう', 'situasi terjadinya')}",
        "id": "2.3 Situasi Terjadinya Kecelakaan di Persimpangan"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('事業用', 'じぎょうよう', 'untuk bisnis')}トラックの{kotoba('交通事故', 'こうつうじこ', 'kecelakaan lalu lintas')}のうち、{kotoba('交差点', 'こうさてん', 'persimpangan')}での{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}や{kotoba('自転車', 'じてんしゃ', 'sepeda')}との{kotoba('死亡事故', 'しぼうじこ', 'kecelakaan fatal')}が、{kotoba('全体', 'ぜんたい', 'keseluruhan')}の3{kotoba('割近く', 'わりちかく', 'hampir 30%')}を{kotoba('占め', 'しめ', 'mendominasi')}、{kotoba('交差点', 'こうさてん', 'persimpangan')}{kotoba('左折時', 'させつじ', 'saat belok kiri')}では{kotoba('自転車', 'じてんしゃ', 'sepeda')}との{kotoba('事故', 'じこ', 'kecelakaan')}、{kotoba('右折時', 'うせつじ', 'saat belok kanan')}では{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}との{kotoba('事故', 'じこ', 'kecelakaan')}が{kotoba('多く', 'おおく', 'banyak')}を{kotoba('占めて', 'しめて', 'mendominasi')}います。",
        "id": "Dari kecelakaan lalu lintas truk bisnis, kecelakaan fatal/kematian yang melibatkan pejalan kaki dan sepeda di persimpangan mendominasi hampir 30% dari keseluruhan, di mana kecelakaan yang melibatkan sepeda banyak mendominasi saat berbelok kiri di persimpangan, dan kecelakaan yang melibatkan pejalan kaki banyak terjadi saat belok kanan."
    },
    {
        "is_header": True,
        "jp": f"２．４ {kotoba('健康起因事故', 'けんこうきいんじこ', 'kecelakaan akibat kesehatan')}の{kotoba('防止', 'ぼうし', 'pencegahan')}",
        "id": "2.4 Pencegahan Kecelakaan Akibat Kesehatan"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('健康起因事故', 'けんこうきいんじこ', 'kecelakaan akibat kesehatan')}とは、{kotoba('運転者', 'うんてんしゃ', '描く')}の{kotoba('疾病', 'しっぺい', 'penyakit')}（{kotoba('病気', 'びょうき', 'penyakit')}）により、{kotoba('車', 'くるま', 'kendaraan')}の{kotoba('運転', 'うんてん', 'mengemudi')}を{kotoba('続ける', 'つづける', 'melanjutkan')}ことができなくなったものを{kotoba('いいます', '', 'disebut')}。",
        "id": "Kecelakaan akibat kesehatan disebut sebagai keadaan di mana pengemudi tidak dapat melanjutkan mengemudikan kendaraan karena penyakit."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('長時間', 'ちょうじかん', 'waktu lama')}の{kotoba('運転', 'うんてん', 'mengemudi')}をするトラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}にとって、{kotoba('健康', 'けんこう', 'sehat')}であることはたいへん{kotoba('重要', 'じゅうよう', 'penting')}な{kotoba('条件', 'じょうけん', 'syarat')}です。{kotoba('体調', 'たいちょう', 'kondisi tubuh')}が{kotoba('悪い', 'わるい', 'buruk')}と{kotoba('注意力', 'ちゅういりょく', 'daya perhatikan')}や{kotoba('集中力', 'しゅうちゅうりょく', 'konsentrasi')}などが{kotoba('低下', 'ていか', 'menurun')}して、{kotoba('事故', 'じこ', 'kecelakaan')}に{kotoba('つながります', '', 'berujung pada')}。",
        "id": "Bagi pengemudi truk yang mengemudi dalam waktu lama, menjadi sehat adalah syarat yang sangat penting. Kondisi tubuh yang buruk akan menurunkan daya perhatian dan konsentrasi, yang berujung pada kecelakaan."
    },
    {
        "is_header": False,
        "jp": f"また、{kotoba('高血圧', 'こうけつあつ', 'darah tinggi')}や{kotoba('糖尿病', 'とうにょうびょう', 'diabetes')}、{kotoba('肥満', 'ひまん', 'obesitas')}などの{kotoba('生活習慣病', 'せいかつしゅうかんびょう', 'penyakit gaya hidup')}は、そのままにしておくと{kotoba('運転中', 'うんてんちゅう', 'saat mengemudi')}に{kotoba('脳卒中', 'のうそっちゅう', 'stroke')}や{kotoba('心臓発作', 'しんぞうほっさ', 'serangan jantung')}などを{kotoba('起こして', 'おこして', 'menyebabkan')}{kotoba('重大事故', 'じゅうだいじこ', 'kecelakaan fatal')}に{kotoba('つながります', '', 'berujung pada')}。",
        "id": "Selain itu, penyakit gaya hidup seperti darah tinggi, diabetes, dan obesitas, jika dibiarkan, akan memicu stroke atau serangan jantung saat mengemudi dan berujung pada kecelakaan fatal."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('定期健康診断', 'ていきけんこうしんだん', 'cek kesehatan rutin')}を{kotoba('必ず', 'かならず', 'pasti/selalu')}{kotoba('受ける', 'うける', 'menerima')}とともに、{kotoba('日頃', 'ひごろ', 'sehari-hari')}から{kotoba('十分', 'じゅうぶん', 'cukup')}な{kotoba('睡眠', 'すいみん', 'tidur')}をとる、{kotoba('適度', 'てきど', 'cukup/sesuai')}な{kotoba('運動', 'うんどう', 'olahraga')}をする、{kotoba('飲み過ぎない', 'のみすぎない', 'tidak minum berlebihan')}などの{kotoba('体調管理', 'たいちょうかんり', 'manajemen kondisi tubuh')}をしっかり{kotoba('行って', 'おこなって', 'melakukan')}、{kotoba('健康起因事故', 'けんこうきいんじこ', 'kecelakaan akibat kesehatan')}の{kotoba('防止', 'ぼうし', 'pencegahan')}に{kotoba('努めましょう', 'つとめましょう', 'mari berusaha')}。",
        "id": "Selain memastikan diri menerima pemeriksaan kesehatan rutin, mari berusaha mencegah kecelakaan akibat kesehatan dengan melakukan manajemen kondisi tubuh secara ketat sehari-hari seperti tidur yang cukup, olahraga yang memadai, dan tidak mengonsumsi alkohol secara berlebihan."
    },
    {
        "is_header": True,
        "jp": f"２．５ {kotoba('安全管理機器', 'あんぜんかんりきき', 'perangkat manajemen keamanan')}（デジタコとドラレコ）の{kotoba('活用', 'かつよう', 'pemanfaatan')}",
        "id": "2.5 Pemanfaatan Perangkat Manajemen Keamanan (Digi-Tacho & Dora-Reko)"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('交通事故', 'こうつうじこ', 'kecelakaan lalu lintas')}をなくすために、さまざまな{kotoba('安全管理機器', 'あんぜんかんりきき', 'perangkat manajemen keamanan')}が{kotoba('活用', 'かつよう', 'dimanfaatkan')}されています。",
        "id": "Untuk menghilangkan kecelakaan lalu lintas, berbagai perangkat manajemen keamanan dimanfaatkan."
    },
    {
        "is_header": False,
        "jp": f"このうち、デジタル{kotoba('式', 'しき', 'sistem')}{kotoba('運行記録計', 'うんこうきろくけい', 'alat rekam perjalanan')}（デジタコ）は、{kotoba('車', 'くるま', 'kendaraan')}の{kotoba('運行', 'うんこう', 'perjalanan')}にかかる{kotoba('速度', 'そくど', 'kecepatan')}や{kotoba('時間', 'じかん', 'waktu')}などを{kotoba('記録', 'きろく', 'merekam')}する{kotoba('装置', 'そうち', 'perangkat')}です。{kotoba('機種', 'きしゅ', 'model')}によっては、{kotoba('急制動', 'きゅうせいどう', 'pengereman mendadak')}、{kotoba('急発進', 'きゅうはっしん', 'akselerasi mendadak')}、{kotoba('燃料消費量', 'ねんりょうしょうひりょう', 'konsumsi bahan bakar')}などの{kotoba('走行', 'そうこう', 'berjalan/melaju')}データを{kotoba('記録', 'きろく', 'merekam')}することができます。また、{kotoba('記録', 'きろく', 'rekaman')}を{kotoba('詳しく', 'くわしく', 'secara detail')}{kotoba('分析', 'ぶんせき', 'analisis')}することで、{kotoba('安全運転', 'あんぜんうんてん', 'berkendara aman')}やエコドライブの{kotoba('指導', 'しどう', 'bimbingan')}が{kotoba('容易', 'ようい', 'mudah')}となります。",
        "id": "Di antaranya, alat rekam perjalanan sistem digital (Digi-Tacho) adalah perangkat yang merekam kecepatan dan waktu terkait operasi kendaraan. Tergantung modelnya, perangkat ini dapat merekam data perjalanan seperti pengereman mendadak, akselerasi mendadak, dan konsumsi bahan bakar. Selain itu, dengan menganalisis rekaman secara rinci, bimbingan berkendara aman dan eco-drive menjadi lebih mudah dilakukan."
    },
    {
        "is_header": False,
        "jp": f"ドライブレコーダ（ドラレコ）は、{kotoba('走行中', 'そうこうちゅう', 'saat melaju')}の{kotoba('映像', 'えいぞう', 'video/gambar')}を{kotoba('記録', 'きろく', 'merekam')}する{kotoba('装置', 'そうち', 'perangkat')}です。{kotoba('急', 'きゅう', 'mendadak')}ブレーキや{kotoba('衝突', 'しょうとつ', 'tabrakan')}などの{kotoba('衝撃', 'しょうげき', 'benturan')}を{kotoba('受ける', 'うける', 'menerima')}と、その{kotoba('前後', 'ぜんご', 'sebelum dan sesudah')}の{kotoba('映像', 'えいぞう', 'video/gambar')}を{kotoba('記録', 'きろく', 'merekam')}します。{kotoba('機種', 'きしゅ', 'model')}によっては{kotoba('映像', 'えいぞう', 'video/gambar')}をいつも{kotoba('記録', 'きろく', 'merekam')}しておくことも{kotoba('可能', 'かのう', 'mungkin')}です。",
        "id": "Drive recorder (Dora-reko) adalah perangkat yang merekam video saat melaju. Saat menerima benturan seperti pengereman mendadak atau tabrakan, perangkat ini merekam video sebelum dan sesudahnya. Bergantung pada modelnya, mungkin juga untuk merekam video secara terus menerus."
    }
    # Data Bab 3 & Bab 4 (4.1 - 4.4) Lengkap
    # --- BAB 3 ---
    {
        "is_header": True,
        "jp": f"３ トラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}としての{kotoba('心構え', 'こころがまえ', 'kesiapan mental/sikap')}",
        "id": "3 Kesiapan Mental/Sikap sebagai Pengemudi Truk"
    },
    {
        "is_header": True,
        "jp": f"３．１ {kotoba('社内', 'しゃない', 'dalam perusahaan')}でのあいさつ",
        "id": "3.1 Salam di Dalam Perusahaan"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('人', 'ひと', 'orang')}との{kotoba('かかわり', '', 'hubungan')}は、あいさつからはじまります。{kotoba('社内', 'しゃない', 'dalam perusahaan')}での{kotoba('良い', 'よい', 'baik')}{kotoba('人間関係', 'にんげんかんけい', 'hubungan antar manusia')}をつくるためには、{kotoba('次', 'つぎ', 'berikut')}のことに{kotoba('気', 'き', 'perhatian')}をつけましょう。",
        "id": "Hubungan dengan orang lain dimulai dari salam. Untuk membangun hubungan antar manusia yang baik di dalam perusahaan, mari perhatikan hal-hal berikut."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('笑顔', 'えがお', 'wajah tersenyum')}であいさつする",
        "id": "・Memberi salam dengan wajah tersenyum"
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('明るい', 'あかるい', 'terang/ceria')}{kotoba('声', 'こえ', 'suara')}であいさつする",
        "id": "・Memberi salam dengan suara yang ceria"
    },
    {
        "is_header": False,
        "jp": f"・あいさつするときは、{kotoba('相手', 'あいて', 'lawan bicara')}の{kotoba('目', 'め', 'mata')}を{kotoba('見る', 'みる', 'melihat')}",
        "id": "・Saat memberi salam, menatap mata lawan bicara"
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('自分', 'じぶん', 'diri sendiri')}からあいさつをする",
        "id": "・Memberi salam lebih dulu dari diri sendiri"
    },
    {
        "is_header": True,
        "jp": f"３．２ {kotoba('社外', 'しゃがい', 'luar perusahaan')}でのあいさつ",
        "id": "3.2 Salam di Luar Perusahaan"
    },
    {
        "is_header": False,
        "jp": f"お{kotoba('客様', 'きゃくさま', 'pelanggan')}がトラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}に{kotoba('望んで', 'のぞんで', 'mengharapkan')}いることとして、{kotoba('荷物', 'にもつ', 'barang')}の{kotoba('丁寧', 'ていねい', 'sopan/hati-hati')}な{kotoba('扱い', 'あつかい', 'penanganan')}や{kotoba('時間', 'じかん', 'waktu')}を{kotoba('守る', 'まもる', 'menjaga/menepati')}ことに{kotoba('加えて', 'くわえて', 'ditambah')}、{kotoba('服装', 'ふくそう', 'pakaian')}・{kotoba('身なり', 'みなり', 'penampilan')}、{kotoba('言葉づかい', 'ことばづかい', 'cara bicara')}や{kotoba('態度', 'たいど', 'sikap')}などのマナーがあげられます。",
        "id": "Hal-hal yang diharapkan pelanggan dari pengemudi truk, selain penanganan barang yang hati-hati dan ketepatan waktu, juga mencakup etika seperti pakaian/penampilan, cara berbicara, dan sikap."
    },
    {
        "is_header": False,
        "jp": f"トラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}は{kotoba('会社', 'かいしゃ', 'perusahaan')}を{kotoba('代表', 'だいひょう', 'mewakili')}する{kotoba('顔', 'かお', 'wajah')}ですから、しっかりあいさつできなければ、{kotoba('会社', 'かいしゃ', 'perusahaan')}のイメージが{kotoba('悪く', 'わるく', 'buruk')}なります。このことをよく{kotoba('理解', 'りかい', 'pahami')}して、お{kotoba('客様', 'きゃくさま', 'pelanggan')}には{kotoba('笑顔', 'えがお', 'wajah tersenyum')}で{kotoba('明るく', 'あかるく', 'dengan ceria')}あいさつしましょう。",
        "id": "Karena pengemudi truk adalah wajah yang mewakili perusahaan, jika tidak bisa memberikan salam dengan baik, citra perusahaan akan menjadi buruk. Pahami hal ini dengan baik, dan berikanlah salam kepada pelanggan dengan wajah tersenyum dan ceria."
    },
    {
        "is_header": True,
        "jp": f"３．３ {kotoba('身だしなみ', 'みだしなみ', 'penampilan diri')}",
        "id": "3.3 Penampilan Diri"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('身だしなみ', 'みだしなみ', 'penampilan diri')}とは、{kotoba('人', 'ひと', 'orang')}に{kotoba('不快感', 'ふかいかん', 'rasa tidak nyaman')}を{kotoba('与えない', 'あたえない', 'tidak memberikan')}{kotoba('服装', 'ふくそう', 'pakaian')}やふるまいなどを{kotoba('いいます', '', 'disebut')}。{kotoba('身だしなみ', 'みだしなみ', 'penampilan diri')}には、その{kotoba('人', 'ひと', 'orang')}の{kotoba('人柄', 'ひとがら', 'kepribadian')}や{kotoba('仕事', 'しごと', 'pekerjaan')}に{kotoba('対する', 'たいする', 'terhadap')}{kotoba('心構え', 'こころがまえ', 'kesiapan mental/sikap')}などがあらわれます。",
        "id": "Penampilan diri adalah pakaian atau perilaku yang tidak memberikan rasa tidak nyaman kepada orang lain. Penampilan diri menunjukkan kepribadian dan sikap seseorang terhadap pekerjaannya."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('身だしなみ', 'みだしなみ', 'penampilan diri')}が{kotoba('悪い', 'わるい', 'buruk')}と、お{kotoba('客様', 'きゃくさま', 'pelanggan')}に{kotoba('悪い', 'わるい', 'buruk')}{kotoba('印象', 'いんしょう', 'kesan')}を{kotoba('与えたり', 'あたえたり', 'memberikan')}、{kotoba('不安感', 'ふあんかん', 'rasa cemas')}を{kotoba('与えます', 'あたえます', 'memberikan')}。これは、トラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}{kotoba('本人', 'ほんにん', 'diri sendiri')}だけでなく、{kotoba('会社', 'かいしゃ', 'perusahaan')}としても{kotoba('大きな', 'おおきな', 'besar')}マイナスとなりますから、いつも{kotoba('清潔感', 'せいけつかん', 'kesan bersih')}のあるきちんとした{kotoba('身だしなみ', 'みだしなみ', 'penampilan diri')}を{kotoba('心掛けましょう', 'こころがけましょう', 'mari usahakan')}。",
        "id": "Jika penampilan diri buruk, hal itu akan memberikan kesan buruk atau rasa cemas kepada pelanggan. Hal ini akan menjadi nilai minus yang besar, tidak hanya bagi pengemudi truk itu sendiri, tetapi juga bagi perusahaan. Oleh karena itu, mari selalu usahakan penampilan diri yang rapi dan memberikan kesan bersih."
    },
    {
        "is_header": False,
        "jp": f"また、きちんとしていた{kotoba('服装', 'ふくそう', 'pakaian')}が{kotoba('運転中', 'うんてんちゅう', 'saat mengemudi')}に{kotoba('乱れてくる', 'みだれてくる', 'menjadi berantakan')}ことがあります。{kotoba('休憩', 'きゅうけい', 'istirahat')}のときなどには、{kotoba('服装', 'ふくそう', 'pakaian')}が{kotoba('乱れて', 'みだれて', 'berantakan')}いないか、{kotoba('名札', 'なふだ', 'papan nama')}は{kotoba('正しく', 'ただしく', 'dengan benar')}つけているか、{kotoba('手', 'て', 'tangan')}や{kotoba('爪', 'つめ', 'kuku')}が{kotoba('汚れて', 'よごれて', 'kotor')}いないかなどをチェックしましょう。",
        "id": "Selain itu, pakaian yang tadinya rapi bisa menjadi berantakan saat mengemudi. Pada saat istirahat dan lain-lain, mari periksa apakah pakaian tidak berantakan, apakah papan nama terpasang dengan benar, dan apakah tangan atau kuku tidak kotor."
    },
    {
        "is_header": True,
        "jp": f"３．４ {kotoba('職場', 'しょくば', 'tempat kerja')}での{kotoba('心構え', 'こころがまえ', 'kesiapan mental/sikap')}",
        "id": "3.4 Sikap Mental di Tempat Kerja"
    },
    {
        "is_header": True,
        "jp": f"◆{kotoba('協調性', 'きょうちょうせい', 'sikap kooperatif')}をもつ",
        "id": "◆ Memiliki Sikap Kooperatif"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('会社', 'かいしゃ', 'perusahaan')}は{kotoba('人', 'ひと', 'orang')}と{kotoba('人', 'ひと', 'orang')}の{kotoba('集まり', 'あつまり', 'kumpulan')}ですから、そこで{kotoba('働いている', 'はたらいている', 'bekerja')}すべての{kotoba('人', 'ひと', 'orang')}が{kotoba('協調性', 'きょうちょうせい', 'sikap kooperatif')}をもつことが{kotoba('大切', 'たいせつ', 'penting')}です。{kotoba('運転', 'うんてん', 'mengemudi')}の{kotoba('仕事', 'しごと', 'pekerjaan')}はトラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}がおこないますが、{kotoba('会社全体', 'かいしゃぜんたい', 'perusahaan keseluruhan')}の{kotoba('仕事', 'しごと', 'pekerjaan')}は、{kotoba('全員', 'ぜんいん', 'semua orang')}がおこなうものであり、チームワークで{kotoba('進めていく', 'すすめていく', 'menjalankan')}ものです。{kotoba('会社', 'かいしゃ', 'perusahaan')}の{kotoba('中', 'なか', 'dalam')}での{kotoba('自分', 'じぶん', 'sendiri')}の{kotoba('役割', 'やくわり', 'peran')}を{kotoba('自覚', 'じかく', 'sadari')}し、みんなと{kotoba('協調', 'きょうちょう', 'bekerja sama')}して{kotoba('仕事', 'しごと', 'pekerjaan')}を{kotoba('進め', 'すすめ', 'memajukan')}、{kotoba('責任', 'せきにん', 'tanggung jawab')}を{kotoba('果たしていく', 'はたしていく', 'menjalankan')}ことで、{kotoba('会社', 'かいしゃ', 'perusahaan')}の{kotoba('発展', 'はってん', 'perkembangan')}や{kotoba('成長', 'せいちょう', 'pertumbuhan')}、{kotoba('従業員', 'じゅうぎょういん', 'karyawan')}の{kotoba('幸福', 'こうふく', 'kebahagiaan')}が{kotoba('生まれる', 'うまれる', 'lahir')}のです。",
        "id": "Karena perusahaan adalah kumpulan orang-orang, sangatlah penting bagi semua orang yang bekerja di sana untuk memiliki sikap kooperatif. Pekerjaan mengemudi memang dilakukan oleh pengemudi truk, tetapi pekerjaan perusahaan secara keseluruhan dilakukan oleh semua orang dan dijalankan melalui kerja sama tim. Dengan menyadari peran diri sendiri di dalam perusahaan, memajukan pekerjaan dengan bekerja sama bersama yang lain, dan memenuhi tanggung jawab, akan melahirkan perkembangan dan pertumbuhan perusahaan, serta kebahagiaan karyawan."
    },
    {
        "is_header": True,
        "jp": f"◆コミュニケーションをとる",
        "id": "◆ Menjalin Komunikasi"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('運転', 'うんてん', 'mengemudi')}という{kotoba('仕事', 'しごと', 'pekerjaan')}は、{kotoba('会社', 'かいしゃ', 'perusahaan')}の{kotoba('外', 'そと', 'luar')}でおこなう{kotoba('単独', 'たんどく', 'sendiri')}{kotoba('の', '', 'partikel')} {kotoba('仕事', 'しごと', 'pekerjaan')}です。だからこそ、{kotoba('点呼時', 'てんこじ', 'saat absen')}など{kotoba('会社', 'かいしゃ', 'perusahaan')}にいる{kotoba('数少ない', 'かずすくない', 'sedikit')}{kotoba('時間', 'じかん', 'waktu')}に、{kotoba('管理者', 'かんりしゃ', 'pengelola/manajer')}や{kotoba('他', 'ほか', 'lain')}のトラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}とのコミュニケーションをとることが{kotoba('大切', 'たいせつ', 'penting')}です。コミュニケーションをとることで、{kotoba('人間関係', 'にんげんかんけい', 'hubungan antar manusia')}がよくなれば、{kotoba('相談', 'そうだん', 'konsultasi')}ごとも{kotoba('気軽', 'きがる', 'tanpa sungkan')}に{kotoba('行える', 'おこなえる', 'bisa dilakukan')}ようになり、ストレスも{kotoba('軽く', 'かるく', 'ringan')}なって{kotoba('仕事', 'しごと', 'pekerjaan')}の{kotoba('能率', 'のうりつ', 'efisiensi')}もアップします。",
        "id": "Pekerjaan mengemudi adalah pekerjaan yang dilakukan sendiri di luar perusahaan. Oleh karena itulah, sangat penting untuk menjalin komunikasi dengan manajer dan pengemudi truk lain pada sedikit waktu saat Anda berada di perusahaan, seperti saat absen. Jika hubungan antar manusia membaik karena menjalin komunikasi, konsultasi pun akan dapat dilakukan tanpa sungkan, stres menjadi ringan, dan efisiensi kerja pun akan meningkat."
    },
    {
        "is_header": True,
        "jp": f"３．５ {kotoba('言葉づかい', 'ことばづかい', 'cara bicara')}の{kotoba('基本', 'きほん', 'dasar')}",
        "id": "3.5 Dasar Cara Berbicara"
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('言葉づかい', 'ことばづかい', 'cara bicara')}は{kotoba('人間関係', 'にんげんかんけい', 'hubungan antar manusia')}の{kotoba('基本', 'きほん', 'dasar')}",
        "id": "・Cara Berbicara adalah Dasar Hubungan Antar Manusia"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('言葉づかい', 'ことばづかい', 'cara bicara')}は{kotoba('人間関係', 'にんげんかんけい', 'hubungan antar manusia')}の{kotoba('基本', 'きほん', 'dasar')}です。{kotoba('話', 'はなし', 'bicara')}をする{kotoba('相手', 'あいて', 'lawan bicara')}に{kotoba('応じて', 'おうじて', 'sesuai')}{kotoba('正しい', 'ただしい', 'benar')}{kotoba('使い方', 'つかいかた', 'cara penggunaan')}ができると{kotoba('人間関係', 'にんげんかんけい', 'hubungan antar manusia')}も{kotoba('良好', 'りょうこう', 'baik')}になります。",
        "id": "Cara berbicara adalah dasar dari hubungan antar manusia. Jika Anda dapat menggunakan cara berbicara yang benar dan sesuai dengan lawan bicara, hubungan antar manusia pun akan menjadi baik."
    },
    {
        "is_header": False,
        "jp": f"また、{kotoba('相手', 'あいて', 'lawan bicara')}に{kotoba('対して', 'たいして', 'terhadap')}{kotoba('正しく', 'ただしく', 'dengan benar')}{kotoba('伝える', 'つたえる', 'menyampaikan')}ことが{kotoba('大切', 'たいせつ', 'penting')}です。{kotoba('早く', 'はやく', 'cepat')}{kotoba('話したり', 'はなしたり', 'berbicara')}、{kotoba('声', 'こえ', 'suara')}が{kotoba('小さい', 'ちいさい', 'kecil')}、{kotoba('言葉', 'ことば', 'kata-kata')}の{kotoba('最後', 'さいご', 'akhir')}がはっきりしないなどは、{kotoba('相手', 'あいて', 'lawan bicara')}に{kotoba('正しく', 'ただしく', 'dengan benar')}{kotoba('伝わらない', 'つたわらない', 'tidak tersampaikan')}{kotoba('おそれ', '', 'kekhawatiran')}がありますから、{kotoba('注意', 'ちゅうい', 'perhatian')}しましょう。",
        "id": "Selain itu, penting untuk menyampaikannya kepada lawan bicara dengan benar. Berbicara terlalu cepat, suara kecil, atau akhir kata yang tidak jelas dikhawatirkan dapat membuat pesan tidak tersampaikan dengan benar kepada lawan bicara, jadi harap berhati-hati."
    },
    {
        "is_header": True,
        "jp": f"◆お{kotoba('客様', 'きゃくさま', 'pelanggan')}に{kotoba('対する', 'たいする', 'terhadap')}{kotoba('言葉づかい', 'ことばづかい', 'cara bicara')}",
        "id": "◆ Cara Berbicara Terhadap Pelanggan"
    },
    {
        "is_header": False,
        "jp": f"お{kotoba('客様', 'きゃくさま', 'pelanggan')}に{kotoba('好感', 'こうかん', 'kesan baik')}をもたれる{kotoba('言葉づかい', 'ことばづかい', 'cara bicara')}は、{kotoba('明るさ', 'あかるさ', 'kecerian')}を{kotoba('第一', 'だいいち', 'pertama/utama')}に、{kotoba('誠実', 'せいじつ', 'tulus')}{kotoba('な', '', 'partikel')} {kotoba('言葉づかい', 'ことばづかい', 'cara bicara')}をするということです。",
        "id": "Cara berbicara yang memberikan kesan baik kepada pelanggan, pertama-tama adalah keceriaan, yakni berbicara dengan tulus."
    },
    {
        "is_header": False,
        "jp": f"それにより、{kotoba('多少', 'たしょう', 'sedikit')}{kotoba('言葉づかい', 'ことばづかい', 'cara bicara')}を{kotoba('間違えた', 'まちがえた', 'salah')}としても、お{kotoba('客様', 'きゃくさま', 'pelanggan')}に{kotoba('理解', 'りかい', 'pahami')}されやすくなります。そのためには、とくに{kotoba('次', 'つぎ', 'berikut')}の{kotoba('点', 'てん', 'poin')}を{kotoba('心掛けましょう', 'こころがけましょう', 'mari usahakan')}。",
        "id": "Dengan demikian, meskipun ada sedikit kesalahan dalam cara berbicara, pelanggan akan lebih mudah memaklumi/memahaminya. Oleh karena itu, mari usahakan poin-poin berikut khususnya:"
    },
    {
        "is_header": False,
        "jp": "・明るく話す",
        "id": "・Berbicara dengan ceria"
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('相手', 'あいて', 'lawan bicara')}の{kotoba('顔', 'かお', 'wajah')}を{kotoba('見て', 'みて', 'melihat')}{kotoba('話す', 'はなす', 'berbicara')}",
        "id": "・Berbicara sambil menatap wajah lawan bicara"
    },
    {
        "is_header": False,
        "jp": f"・はっきり{kotoba('話す', 'はなす', 'berbicara')}",
        "id": "・Berbicara dengan jelas"
    },
    {
        "is_header": False,
        "jp": f"・あいまいな{kotoba('表現', 'ひょうげん', 'ungkapan')}を{kotoba('使わない', 'つかわない', 'tidak menggunakan')}",
        "id": "・Tidak menggunakan ungkapan yang ambigu (tidak jelas)"
    },
    {
        "is_header": True,
        "jp": f"３．６ {kotoba('車', 'くるま', 'kendaraan')}の{kotoba('整理整頓', 'せいりせいとん', 'beres-beres')}",
        "id": "3.6 Beres-Beres Kendaraan"
    },
    {
        "is_header": True,
        "jp": f"◆4Sの{kotoba('大切さ', 'たいせつさ', 'pentingnya')}",
        "id": "◆ Pentingnya 4S"
    },
    {
        "is_header": False,
        "jp": f"4Sとは「{kotoba('整理', 'せいり', 'Seiri')}」「{kotoba('整頓', 'せいとん', 'Seiton')}」「{kotoba('清掃', 'せいそう', 'Seisou')}」「{kotoba('清潔', 'せいけつ', 'Seiketsu')}」のそれぞれの{kotoba('頭文字', 'かしらもじ', 'huruf awal')}の「S」をとったものです。4Sを{kotoba('実行', 'じっこう', 'melaksanakan')}することは、{kotoba('脇見運転', 'わきみうんてん', 'mengemudi sambil menoleh')}の{kotoba('防止', 'ぼうし', 'pencegahan')}や{kotoba('視界', 'しかい', 'jarak pandang')}の{kotoba('保つ', 'たもつ', 'menjaga')}ことで、{kotoba('事故防止', 'じこぼうし', 'pencegahan kecelakaan')}にもつながります。",
        "id": "4S adalah singkatan dari huruf awal \"S\" pada kata \"Seiri (Ringkas)\", \"Seiton (Rapi)\", \"Seisou (Resik)\", dan \"Seiketsu (Rawat)\". Melaksanakan 4S berarti mencegah mengemudi sambil menoleh ke arah lain dan menjaga jarak pandang, yang juga berujung pada pencegahan kecelakaan."
    },
    {
        "is_header": True,
        "jp": f"▶{kotoba('整理', 'せいり', 'Seiri (Ringkas)')}",
        "id": "▶ Seiri (Ringkas)"
    },
    {
        "is_header": False,
        "jp": f"「{kotoba('整理', 'せいり', 'seiri')}」とは、「{kotoba('乱れた', 'みだれた', 'berantakan')}{kotoba('状態', 'じょうたい', 'kondisi')}にあるものを{kotoba('整える', 'ととのえる', 'merapikan')}ことであり、{kotoba('必要な', 'ひつような', 'yang dibutuhkan')}ものとそうでないものを{kotoba('区別', 'くべつ', 'membedakan')}し、{kotoba('必要ない', 'ひつようない', 'tidak diperlukan')}ものを{kotoba('処分', 'しょぶん', 'membuang')}すること」です。",
        "id": "\"Seiri\" berarti \"merapikan kondisi yang berantakan, membedakan antara barang yang dibutuhkan dan yang tidak, serta membuang barang yang tidak diperlukan\"."
    },
    {
        "is_header": False,
        "jp": f"たとえば、{kotoba('助手席側', 'じょしゅせきがわ', 'sisi kursi penumpang')}のドアの{kotoba('安全窓付近', 'あんぜんまどふきん', 'sekitar jendela aman')}に{kotoba('伝票', 'でんぴょう', 'slip')}や{kotoba('地図', 'ちず', 'peta')}、ヘルメット、ダンボール{kotoba('箱', 'はこ', 'kotak')}などを{kotoba('置いている', 'おいている', 'meletakkan')}と、{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}などを{kotoba('見落とす', 'みおとす', 'terlewatkan')}{kotoba('おそれ', '', 'kekhawatiran')}があります。このようなことが{kotoba('起こらない', 'おこらない', 'tidak terjadi')}ようにいらない{kotoba('物', 'もの', 'barang')}を{kotoba('片付けて', 'かたづけて', 'membereskan')}おくようにしましょう。",
        "id": "Misalnya, jika Anda meletakkan slip, peta, helm, kardus, dan lain-lain di sekitar jendela keselamatan pintu sisi kursi penumpang, dikhawatirkan dapat membuat Anda tidak melihat pejalan kaki. Agar hal seperti ini tidak terjadi, bereskanlah barang-barang yang tidak diperlukan."
    },
    {
        "is_header": True,
        "jp": f"▶{kotoba('整頓', 'せいとん', 'Seiton (Rapi)')}",
        "id": "▶ Seiton (Rapi)"
    },
    {
        "is_header": False,
        "jp": f"「{kotoba('整頓', 'せいとん', 'seiton')}」は「{kotoba('必要な', 'ひつような', 'yang dibutuhkan')}ものを{kotoba('使いやすい', 'つかいやすい', 'mudah digunakan')}{kotoba('場所', 'ばしょ', 'tempat')}にきちんと{kotoba('置く', 'おく', 'meletakkan')}こと」です。",
        "id": "\"Seiton\" berarti \"meletakkan barang-barang yang dibutuhkan dengan rapi di tempat yang mudah digunakan\"."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('整頓', 'せいとん', 'seiton')}するときは、{kotoba('運転', 'うんてん', 'mengemudi')}の{kotoba('妨げ', 'さまたげ', 'hambatan')}にならない{kotoba('置き場所', 'おきばしょ', 'tempat meletakkan')}や{kotoba('置き方', 'おきかた', 'cara meletakkan')}をよく{kotoba('考えましょう', 'かんがえましょう', 'mari pikirkan')}。たとえば、{kotoba('書類', 'しょるい', 'dokumen')}などをダッシュボードに{kotoba('置く', 'おく', 'meletakkan')}と、{kotoba('運転中', 'うんてんちゅう', 'saat mengemudi')}に{kotoba('書類', 'しょるい', 'dokumen')}がフロントガラスに{kotoba('映って', 'うつって', 'terpantul')}、{kotoba('視界', 'しかい', 'jarak pandang')}を{kotoba('悪く', 'わるく', 'buruk')}させます。また、{kotoba('書類', 'しょるい', 'dokumen')}などに{kotoba('気', 'き', 'perhatian')}をとられ、{kotoba('脇見運転', 'わきみうんてん', 'mengemudi sambil menoleh')}になる{kotoba('おそれ', '', 'kekhawatiran')}もありますから{kotoba('注意', 'ちゅうい', 'perhatian')}しましょう。",
        "id": "Saat merapikan, pikirkan baik-baik tempat dan cara meletakkan barang agar tidak mengganggu saat mengemudi. Misalnya, jika Anda meletakkan dokumen di dasbor, dokumen tersebut akan terpantul di kaca depan saat mengemudi dan memperburuk jarak pandang. Selain itu, perhatikan karena dikhawatirkan perhatian Anda akan teralihkan oleh dokumen sehingga mengemudi sambil menoleh."
    },
    {
        "is_header": True,
        "jp": f"▶{kotoba('清掃', 'せいそう', 'Seisou (Resik)')}",
        "id": "▶ Seisou (Resik)"
    },
    {
        "is_header": False,
        "jp": f"「{kotoba('清掃', 'せいそう', 'seisou')}」とは、「{kotoba('車内', 'しゃない', 'dalam mobil')}をきれいにして、{kotoba('使いやすい', 'つかいやすい', 'mudah digunakan')}ようにしておくこと」です。",
        "id": "\"Seisou\" berarti \"membersihkan bagian dalam kendaraan dan membuatnya mudah digunakan\"."
    },
    {
        "is_header": False,
        "jp": f"たとえば、{kotoba('空缶', 'あきかん', 'kaleng kosong')}が{kotoba('床', 'ゆか', 'lantai')}に{kotoba('落ちていた', 'おちていた', 'jatuh')}{kotoba('場合', 'ばあい', 'kasus')}、それがブレーキペダルに{kotoba('はまって', '', 'tersangkut')}しまうと、ブレーキが{kotoba('踏めず', 'ふめず', 'tidak bisa diinjak')}、{kotoba('重大な', 'じゅうだいな', 'fatal')}{kotoba('事故', 'じこ', 'kecelakaan')}につながることもあります。また、{kotoba('出発', 'しゅっぱつ', 'keberangkatan')}するときに{kotoba('車内', 'しゃない', 'dalam mobil')}が{kotoba('散らかっている', 'ちらかっている', 'berantakan')}と、それを{kotoba('片付ける', 'かたづける', 'membereskan')}のにも{kotoba('手間', 'てま', 'repot/waktu')}がかかり、{kotoba('時間', 'じかん', 'waktu')}の{kotoba('無駄づかい', 'むだづかい', 'buang-buang')}になります。{kotoba('運転', 'うんてん', 'mengemudi')}の{kotoba('仕事', 'しごと', 'pekerjaan')}が{kotoba('終わった', 'おわった', 'selesai')}ときは、{kotoba('車内', 'しゃない', 'dalam mobil')}を{kotoba('清掃', 'せいそう', 'membersihkan')}する{kotoba('習慣', 'しゅうかん', 'kebiasaan')}をつけておきましょう。",
        "id": "Misalnya, jika kaleng kosong jatuh di lantai dan tersangkut di pedal rem, rem tidak akan bisa diinjak dan dapat menyebabkan kecelakaan fatal. Selain itu, jika bagian dalam kendaraan berantakan saat akan berangkat, akan memakan waktu untuk membereskannya sehingga membuang-buang waktu. Biasakanlah untuk membersihkan kendaraan saat pekerjaan mengemudi telah selesai."
    },
    {
        "is_header": True,
        "jp": f"▶{kotoba('清潔', 'せいけつ', 'Seiketsu (Rawat)')}",
        "id": "▶ Seiketsu (Rawat)"
    },
    {
        "is_header": False,
        "jp": f"「{kotoba('清潔', 'せいけつ', 'seiketsu')}」とは、「{kotoba('整理', 'せいり', 'seiri')}、{kotoba('整頓', 'せいとん', 'seiton')}、{kotoba('清掃', 'せいそう', 'seisou')}」を{kotoba('保つ', 'たもつ', 'menjaga')}{kotoba('活動', 'かつどう', 'kegiatan')}のことです。",
        "id": "\"Seiketsu\" adalah kegiatan untuk menjaga \"seiri, seiton, seisou\"."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('整理', 'せいり', 'seiri')}・{kotoba('整頓', 'せいとん', 'seiton')}・{kotoba('清掃', 'せいそう', 'seisou')}がおこなわれていないと、{kotoba('車', 'くるま', 'kendaraan')}を{kotoba('大切', 'たいせつ', 'menghargai/menyayangi')}にする{kotoba('気持ち', 'きもち', 'perasaan')}が{kotoba('薄れて', 'うすれて', 'memudar')}、{kotoba('運転', 'うんてん', 'mengemudi')}も{kotoba('乱暴', 'らんぼう', 'kasar')}になりがちです。",
        "id": "Jika seiri, seiton, dan seisou tidak dilakukan, rasa menyayangi kendaraan akan memudar, dan cara mengemudi pun cenderung menjadi kasar."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('整理', 'せいり', 'seiri')}・{kotoba('整頓', 'せいとん', 'seiton')}・{kotoba('清掃', 'せいそう', 'seisou')}が{kotoba('行われて', 'おこなわれて', 'dilakukan')}いれば、プロ{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}としての{kotoba('意識', 'いしき', 'kesadaran')}や、{kotoba('走る', 'はしる', 'berjalan')}{kotoba('広告塔', 'こうこくとう', 'papan iklan')}（{kotoba('会社', 'かいしゃ', 'perusahaan')}の{kotoba('名前', 'なまえ', 'nama')}が{kotoba('書かれた', 'かかれた', 'tertulis')}トラックは、{kotoba('走り', 'はしり', 'berjalan')}ながら{kotoba('会社', 'かいしゃ', 'perusahaan')}を{kotoba('宣伝', 'せんでん', 'mengiklankan')}する{kotoba('広告', 'こうこく', 'iklan')}の{kotoba('役割', 'やくわり', 'peran')}を{kotoba('はたして', '', 'menjalankan')}います。）としての{kotoba('意識', 'いしき', 'kesadaran')}も{kotoba('強まります', 'つよまります', 'menguat')}から、マナーの{kotoba('良い', 'よい', 'baik')}{kotoba('安全な', 'あんぜんな', 'aman')}{kotoba('運転', 'うんてん', 'mengemudi')}につながります。",
        "id": "Jika seiri, seiton, dan seisou dilakukan dengan baik, kesadaran sebagai pengemudi profesional dan kesadaran sebagai papan iklan berjalan (Truk dengan nama perusahaan yang tertulis berfungsi sebagai iklan berjalan untuk mempromosikan perusahaan) akan menguat, sehingga akan berujung pada cara mengemudi yang aman dan beretika baik."
    },
    {
        "is_header": True,
        "jp": f"３．７ トラックを{kotoba('運転', 'うんてん', 'mengemudi')}する{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}のみなさんへ",
        "id": "3.7 Untuk Anda Sekalian Pengemudi yang Mengemudikan Truk"
    },
    {
        "is_header": True,
        "jp": f"◆トラックの{kotoba('特性', 'とくせい', 'karakteristik')}に{kotoba('応じた', 'おうじた', 'sesuai')}{kotoba('運転技能', 'うんてんぎのう', 'keterampilan mengemudi')}の{kotoba('習得', 'しゅうとく', 'penguasaan')}",
        "id": "◆ Penguasaan Keterampilan Mengemudi yang Sesuai dengan Karakteristik Truk"
    },
    {
        "is_header": False,
        "jp": f"トラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}の{kotoba('仕事', 'しごと', 'pekerjaan')}の{kotoba('大半', 'たいはん', 'sebagian besar')}は{kotoba('運転', 'うんてん', 'mengemudi')}ですから、トラックを{kotoba('運転', 'うんてん', 'mengemudi')}する{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}のみなさんは、しっかりと{kotoba('運転技能', 'うんてんぎのう', 'keterampilan mengemudi')}を{kotoba('学ぶ', 'まなぶ', 'belajar')}{kotoba('必要', 'ひつよう', 'perlu')}があります。",
        "id": "Karena sebagian besar pekerjaan pengemudi truk adalah mengemudi, Anda sekalian yang mengemudikan truk perlu belajar dan menguasai keterampilan mengemudi dengan baik."
    },
    {
        "is_header": False,
        "jp": f"とくにトラックは、{kotoba('他', 'ほか', 'lain')}の{kotoba('車', 'くるま', 'kendaraan')}とは{kotoba('違う', 'ちがう', 'berbeda')}{kotoba('特性', 'とくせい', 'karakteristik')}がありますから、それらをよく{kotoba('理解', 'りかい', 'pahami')}して、トラックの{kotoba('特性', 'とくせい', 'karakteristik')}に{kotoba('応じた', 'おうじた', 'sesuai')}{kotoba('運転技能', 'うんてんぎのう', 'keterampilan mengemudi')}を{kotoba('身につける', 'みにつける', 'menguasai/mempelajari')}{kotoba('必要', 'ひつよう', 'perlu')}があります。",
        "id": "Khususnya, truk memiliki karakteristik yang berbeda dari kendaraan lain. Karena itu, Anda perlu memahaminya dengan baik dan menguasai keterampilan mengemudi yang sesuai dengan karakteristik truk tersebut."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('慣れた', 'なれた', 'terbiasa')}{kotoba('頃', 'ころ', 'saat')}に{kotoba('落とし穴', 'おとしあな', 'jebakan')}がある",
        "id": "・Ada Jebakan Saat Mulai Terbiasa"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('運転', 'うんてん', 'mengemudi')}に{kotoba('慣れない', 'なれない', 'belum terbiasa')}{kotoba('とき', '', 'saat')}は{kotoba('緊張感', 'きんちょうかん', 'rasa tegang')}を{kotoba('持って', 'もって', 'memiliki')}{kotoba('運転', 'うんてん', 'mengemudi')}していても、{kotoba('慣れてくる', 'なれてくる', 'mulai terbiasa')}と{kotoba('緊張感', 'きんちょうかん', 'rasa tegang')}が{kotoba('薄れ', 'うすれ', 'memudar')}、{kotoba('油断', 'ゆだん', 'kecerobohan')}が{kotoba('生まれやすくなります', 'うまれやすくなります', 'mudah muncul')}。{kotoba('そのため', '', 'oleh karena itu')}{kotoba('安全', 'あんぜん', 'aman')}のための{kotoba('基本動作', 'きほんどうさ', 'gerakan dasar')}をしなかったり、やるべきことをやらなくなったりします。それが{kotoba('事故', 'じこ', 'kecelakaan')}につながります。",
        "id": "Saat belum terbiasa mengemudi, Anda mungkin mengemudi dengan penuh rasa tegang. Namun, saat mulai terbiasa, rasa tegang itu akan memudar, dan kecerobohan pun mudah muncul. Oleh karena itu, Anda mungkin tidak melakukan gerakan dasar untuk keselamatan, atau tidak melakukan apa yang seharusnya dilakukan. Hal itulah yang berujung pada kecelakaan."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('運転', 'うんてん', 'mengemudi')}を{kotoba('始めた', 'はじめた', 'memulai')}{kotoba('頃', 'ころ', 'saat')}{kotoba('の', '', 'partikel')} {kotoba('緊張感', 'きんちょうかん', 'rasa tegang')}や{kotoba('慎重さ', 'しんちょうさ', 'kehati-hatian')}を{kotoba('忘れない', 'わすれない', 'jangan lupa')}ようにしましょう。",
        "id": "Janganlah melupakan rasa tegang dan kehati-hatian seperti saat Anda baru mulai mengemudi."
    },

    # --- BAB 4 ---
    {
        "is_header": True,
        "jp": f"４ {kotoba('安全運転', 'あんぜんうんてん', 'berkendara aman')}の{kotoba('基本', 'きほん', 'dasar')}",
        "id": "4 Dasar Berkendara Aman"
    },
    {
        "is_header": True,
        "jp": f"４．１ {kotoba('日常', 'にちじょう', 'sehari-hari')}・{kotoba('休日', 'きゅうじつ', 'hari libur')}の{kotoba('健康管理', 'けんこうかんり', 'manajemen kesehatan')}",
        "id": "4.1 Manajemen Kesehatan Sehari-Hari dan Hari Libur"
    },
    {
        "is_header": True,
        "jp": f"▶{kotoba('健康管理', 'けんこうかんり', 'manajemen kesehatan')}の{kotoba('大切さ', 'たいせつさ', 'pentingnya')}",
        "id": "▶ Pentingnya Manajemen Kesehatan"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('毎日', 'まいにち', 'setiap hari')}{kotoba('運転', 'うんてん', 'mengemudi')}の{kotoba('仕事', 'しごと', 'pekerjaan')}をするトラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}にとって、{kotoba('心身', 'しんしん', 'pikiran dan tubuh')}をいつも{kotoba('良い', 'よい', 'baik')}{kotoba('状態', 'じょうたい', 'kondisi')}に{kotoba('保つ', 'たもつ', 'menjaga')}ことが{kotoba('大切', 'たいせつ', 'penting')}です。{kotoba('運転', 'うんてん', 'mengemudi')}という{kotoba('作業', 'さぎょう', 'tugas/kerja')}は、{kotoba('次', 'つぎ', 'berikut')}のような{kotoba('特徴', 'とくちょう', 'ciri-ciri')}があるからです。",
        "id": "Bagi pengemudi truk yang setiap hari mengemudi, sangatlah penting untuk selalu menjaga tubuh dan pikiran dalam kondisi yang baik. Sebab, tugas mengemudi memiliki ciri-ciri sebagai berikut:"
    },
    {
        "is_header": False,
        "jp": f"①ひとりで{kotoba('行わなければなりません', 'おこなわなければなりません', 'harus melakukan')}。",
        "id": "① Harus dilakukan sendirian."
    },
    {
        "is_header": False,
        "jp": f"②{kotoba('長い', 'ながい', 'panjang')}{kotoba('時間', 'じかん', 'waktu')}{kotoba('行わなければなりません', 'おこなわなければなりません', 'harus melakukan')}。",
        "id": "② Harus dilakukan dalam waktu yang lama."
    },
    {
        "is_header": False,
        "jp": f"③{kotoba('とっさの', '', 'tiba-tiba/seketika')}（{kotoba('非常', 'ひじょう', 'sangat')}に{kotoba('短い', 'みじかい', 'pendek')}{kotoba('時間', 'じかん', 'waktu')}での）{kotoba('判断', 'はんだん', 'keputusan')}が{kotoba('必要', 'ひつよう', 'perlu')}となるときや、{kotoba('緊急', 'きんきゅう', 'darurat')}のときなどに、{kotoba('冷静', 'れいせい', 'tenang')}で{kotoba('適切', 'てきせつ', 'tepat')}な{kotoba('判断', 'はんだん', 'keputusan')}をすることが{kotoba('必要', 'ひつよう', 'perlu')}となります。",
        "id": "③ Saat diperlukan keputusan mendadak/seketika (dalam waktu yang sangat singkat) atau saat darurat, diperlukan pengambilan keputusan yang tenang dan tepat."
    },
    {
        "is_header": False,
        "jp": f"④{kotoba('運転中', 'うんてんちゅう', 'saat mengemudi')}は{kotoba('運転席', 'うんてんせき', 'kursi pengemudi')}に{kotoba('座り続け', 'すわりつづけ', 'terus duduk')}、{kotoba('動く', 'うごく', 'bergerak')}ことが{kotoba('少なく', 'すくなく', 'sedikit')}、{kotoba('姿勢', 'しせい', 'postur/posisi')}を{kotoba('変える', 'かえる', 'mengubah')}ことができない{kotoba('状態', 'じょうたい', 'kondisi')}が{kotoba('続きます', 'つづきます', 'berlanjut')}。",
        "id": "④ Saat mengemudi, Anda harus terus duduk di kursi pengemudi, jarang bergerak, dan tidak dapat mengubah postur tubuh dalam keadaan yang berlanjut."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('体調', 'たいちょう', 'kondisi tubuh')}の{kotoba('悪い', 'わるい', 'buruk')}{kotoba('状態', 'じょうたい', 'kondisi')}で{kotoba('運転', 'うんてん', 'mengemudi')}の{kotoba('仕事', 'しごと', 'pekerjaan')}につけば、これらの{kotoba('作業', 'さぎょう', 'tugas/kerja')}を{kotoba('適切', 'てきせつ', 'tepat')}におこなうことができず、{kotoba('事故', 'じこ', 'kecelakaan')}に{kotoba('つながります', '', 'berujung pada')}。{kotoba('健康', 'けんこう', 'sehat')}を{kotoba('保つ', 'たもつ', 'menjaga')}ことは{kotoba('安全運転', 'あんぜんうんてん', 'berkendara aman')}に{kotoba('欠かせない', 'かかせない', 'tidak terpisahkan')}{kotoba('条件', 'じょうけん', 'syarat')}です。",
        "id": "Jika Anda melakukan pekerjaan mengemudi dalam kondisi tubuh yang buruk, tugas-tugas ini tidak dapat dilakukan dengan tepat, sehingga berujung pada kecelakaan. Menjaga kesehatan adalah syarat mutlak/tidak terpisahkan untuk berkendara dengan aman."
    },
    {
        "is_header": True,
        "jp": f"◆{kotoba('日常生活', 'にちじょうせいかつ', 'kehidupan sehari-hari')}や{kotoba('休日', 'きゅうじつ', 'hari libur')}の{kotoba('注意点', 'ちゅういてん', 'poin perhatian')}",
        "id": "◆ Poin Perhatian dalam Kehidupan Sehari-hari dan Hari Libur"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('深夜', 'しんや', 'tengah malam')}や{kotoba('早朝', 'そうちょう', 'dini hari')}の{kotoba('出発', 'しゅっぱつ', 'keberangkatan')}、{kotoba('宿泊', 'しゅくはく', 'menginap')}を{kotoba('伴う', 'ともなう', 'disertai')}{kotoba('運行', 'うんこう', 'perjalanan')}などトラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}は{kotoba('生活', 'せいかつ', 'kehidupan')}が{kotoba('不規則', 'ふきそく', 'tidak teratur')}になりがちですので、{kotoba('日常生活', 'にちじょうせいかつ', 'kehidupan sehari-hari')}においては、とくに{kotoba('次', 'つぎ', 'berikut')}のことを{kotoba('心掛けましょう', 'こころがけましょう', 'mari usahakan')}。",
        "id": "Pengemudi truk seringkali memiliki ritme hidup yang tidak teratur, seperti berangkat larut malam atau dini hari, serta perjalanan yang mengharuskan menginap. Oleh karena itu, dalam kehidupan sehari-hari, usahakan hal-hal berikut:"
    },
    {
        "is_header": False,
        "jp": f"①{kotoba('十分', 'じゅうぶん', 'cukup')}な{kotoba('睡眠', 'すいみん', 'tidur')}をとる。",
        "id": "① Tidur yang cukup."
    },
    {
        "is_header": False,
        "jp": f"②バランスの{kotoba('良い', 'よい', 'baik')}{kotoba('食事', 'しょくじ', 'makan')}をとる。",
        "id": "② Makan dengan gizi seimbang."
    },
    {
        "is_header": False,
        "jp": f"③やすらぎの{kotoba('場', 'ば', 'tempat')}を{kotoba('持つ', 'もつ', 'memiliki')}。",
        "id": "③ Memiliki tempat/waktu untuk relaksasi."
    },
    {
        "is_header": False,
        "jp": f"④{kotoba('翌日', 'よくじつ', 'keesokan hari')}に{kotoba('疲れ', 'つかれ', 'lelah')}が{kotoba('残らない', 'のこらない', 'tidak tersisa')}くらいの{kotoba('運動', 'うんどう', 'olahraga')}をする。",
        "id": "④ Melakukan olahraga ringan yang tidak menyisakan kelelahan pada keesokan harinya."
    },
    {
        "is_header": False,
        "jp": f"⑤{kotoba('気分', 'きぶん', 'perasaan')}の{kotoba('転換', 'てんかん', 'perubahan/penyegaran')}ができる{kotoba('趣味', 'しゅみ', 'hobi')}を{kotoba('持つ', 'もつ', 'memiliki')}。",
        "id": "⑤ Memiliki hobi untuk menyegarkan pikiran."
    },
    {
        "is_header": False,
        "jp": f"⑥{kotoba('気持ち', 'きもち', 'perasaan')}にゆとりを{kotoba('持つ', 'もつ', 'memiliki')}。",
        "id": "⑥ Memiliki kelonggaran hati."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('休日', 'きゅうじつ', 'hari libur')}はしっかりと{kotoba('休養', 'きゅうよう', 'istirahat')}をとり、{kotoba('軽い', 'かるい', 'ringan')}{kotoba('運動', 'うんどう', 'olahraga')}や{kotoba('趣味', 'しゅみ', 'hobi')}などで、{kotoba('心', 'こころ', 'hati/pikiran')}もからだもリフレッシュさせましょう。",
        "id": "Pada hari libur, beristirahatlah dengan cukup, dan segarkanlah tubuh serta pikiran dengan olahraga ringan atau hobi."
    },
    {
        "is_header": True,
        "jp": f"４．２ {kotoba('飲酒運転', 'いんしゅうんてん', 'berkendara mabuk')}をなくす",
        "id": "4.2 Menghilangkan Kebiasaan Mengemudi Mabuk"
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('飲酒運転', 'いんしゅうんてん', 'berkendara mabuk')}は{kotoba('犯罪', 'はんざい', 'kejahatan')}",
        "id": "・Mengemudi dalam Keadaan Mabuk adalah Tindak Kejahatan"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('飲酒運転', 'いんしゅうんてん', 'berkendara mabuk')}は{kotoba('重大事故', 'じゅうだいじこ', 'kecelakaan fatal')}につながる{kotoba('悪質', 'あくしつ', 'berbahaya')}{kotoba('で', '', 'dan')}{kotoba('危険な', 'きけんな', 'berbahaya')}{kotoba('犯罪行為', 'はんざいこうい', 'tindak pidana')}です。{kotoba('そのため', '', 'oleh karena itu')}{kotoba('罰則', 'ばっそく', 'hukuman/sanksi')}も{kotoba('重く', 'おもく', 'berat')}、{kotoba('事故', 'じこ', 'kecelakaan')}を{kotoba('起こさない', 'おこさない', 'tidak menyebabkan')}{kotoba('場合', 'ばあい', 'kasus')}でも{kotoba('懲役', 'ちょうえき', 'hukuman penjara')}や{kotoba('罰金', 'ばっきん', 'denda')}、{kotoba('運転免許', 'うんてんめんきょ', 'SIM')}の{kotoba('取消し', 'とりけし', 'pencabutan')}や{kotoba('停止', 'ていし', 'penangguhan')}などの{kotoba('処分', 'しょぶん', 'hukuman')}を{kotoba('受けます', 'うけます', 'menerima')}。",
        "id": "Mengemudi di bawah pengaruh alkohol (mabuk) adalah tindakan kriminal berbahaya dan jahat yang dapat berujung pada kecelakaan fatal. Oleh karena itu, hukumannya pun berat. Meskipun Anda tidak menyebabkan kecelakaan, Anda akan menerima hukuman seperti penjara, denda, serta pencabutan atau penangguhan SIM."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('飲酒運転', 'いんしゅうんてん', 'berkendara mabuk')}で{kotoba('人身事故', 'じんしんじこ', 'kecelakaan lalu lintas')}（{kotoba('人', 'ひと', 'orang')}を{kotoba('死亡', 'しぼう', 'mati')}させたり{kotoba('負傷', 'ふしょう', 'terluka')}させた{kotoba('事故', 'じこ', 'kecelakaan')}）を{kotoba('起こした', 'おこした', 'menyebabkan')}{kotoba('場合', 'ばあい', 'kasus')}には、{kotoba('刑務所', 'けいむしょ', 'penjara')}に{kotoba('入れられる', 'いれられる', 'dimasukkan')}ことも{kotoba('少なくありません', 'すくなくありません', 'tidak sedikit')}。どのような{kotoba('場合', 'ばあい', 'kasus')}でも、{kotoba('飲酒運転', 'いんしゅうんてん', 'berkendara mabuk')}は{kotoba('絶対', 'ぜったい', 'mutlak')}にしてはいけません。",
        "id": "Jika menyebabkan kecelakaan yang melibatkan manusia (kecelakaan yang mengakibatkan korban jiwa atau luka) saat mengemudi dalam keadaan mabuk, tidak jarang pelakunya dimasukkan ke penjara. Dalam keadaan apa pun, Anda sama sekali dilarang mengemudi dalam keadaan mabuk."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('飲酒した', 'いんしゅした', 'setelah minum')}{kotoba('翌日', 'よくじつ', 'keesokan hari')}でもお{kotoba('酒', 'さけ', 'alkohol')}の{kotoba('影響', 'えいきょう', 'pengaruh')}が{kotoba('残っていれば', 'のこっていれば', 'jika masih ada')}{kotoba('罰せられる', 'ばっせられる', 'dihukum')}",
        "id": "・Jika Pengaruh Alkohol Masih Tersisa Keesokan Harinya, Anda Tetap Akan Dihukum"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('飲酒した', 'いんしゅした', 'setelah minum')}{kotoba('翌日', 'よくじつ', 'keesokan hari')}でもお{kotoba('酒', 'さけ', 'alkohol')}の{kotoba('影響', 'えいきょう', 'pengaruh')}が{kotoba('残っていれば', 'のこっていれば', 'jika masih ada')}（これを「{kotoba('二日酔い', 'ふつかよい', 'hangover/mabuk sisa')}」と{kotoba('いいます', '', 'disebut')}）、「{kotoba('飲酒運転', 'いんしゅうんてん', 'berkendara mabuk')}」となり{kotoba('罰せられます', 'ばっせられます', 'dihukum')}。お{kotoba('酒', 'さけ', 'alkohol')}を{kotoba('飲んだ', 'のんだ', 'telah minum')}{kotoba('後', 'あと', 'setelah')}に{kotoba('睡眠', 'すいみん', 'tidur')}をとったから、{kotoba('数時間', 'すうじかん', 'beberapa jam')}が{kotoba('経過', 'けいか', 'berlalu')}しているから、「{kotoba('飲酒運転', 'いんしゅうんてん', 'berkendara mabuk')}」にはならないとは{kotoba('決していえません', 'けっしていえません', 'sama sekali tidak bisa dikatakan')}。{kotoba('少し', 'すこし', 'sedikit')}でもお{kotoba('酒', 'さけ', 'alkohol')}の{kotoba('影響', 'えいきょう', 'pengaruh')}が{kotoba('残っている', 'のこっている', 'masih ada')}ときは{kotoba('運転', 'うんてん', 'mengemudi')}してはいけません。",
        "id": "Meskipun keesokan harinya setelah Anda minum, jika pengaruh alkohol masih ada (kondisi ini disebut mabuk karena efek alkohol sebelumnya atau *hangover*), hal ini akan dianggap sebagai \"mengemudi dalam keadaan mabuk\" dan Anda akan dihukum. Sama sekali tidak bisa dijadikan alasan bahwa Anda tidak \"mengemudi mabuk\" hanya karena Anda sudah tidur atau sudah beberapa jam berlalu setelah Anda minum. Anda tidak boleh mengemudi selama pengaruh alkohol masih terasa sekecil apa pun."
    },
    {
        "is_header": True,
        "jp": f"４．３ {kotoba('最高速度', 'さいこうそくど', 'kecepatan maksimum')}（{kotoba('制限速度', 'せいげんそくど', 'batas kecepatan')}）を{kotoba('守る', 'まもる', 'mematuhi')}",
        "id": "4.3 Mematuhi Kecepatan Maksimum (Batas Kecepatan)"
    },
    {
        "is_header": True,
        "jp": f"◆{kotoba('高速自動車国道', 'こうそくじどうしゃこくどう', 'jalan tol nasional')}ではトラックの{kotoba('種別', 'しゅべつ', 'jenis')}で{kotoba('最高速度', 'さいこうそくど', 'kecepatan maksimum')}が{kotoba('違う', 'ちがう', 'berbeda')}",
        "id": "◆ Di Jalan Tol Nasional, Kecepatan Maksimum Berbeda Berdasarkan Jenis Truk"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('最高速度', 'さいこうそくど', 'kecepatan maksimum')}には「{kotoba('法定速度', 'ほうていそくど', 'kecepatan menurut UU')}」と「{kotoba('規制速度', 'きせいそくど', 'kecepatan aturan')}」があります。",
        "id": "Kecepatan maksimum dibagi atas \"kecepatan menurut perundang-undangan (kecepatan legal)\" dan \"kecepatan yang diatur/ditentukan rambu\"."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('法定速度', 'ほうていそくど', 'kecepatan menurut UU')}とは、{kotoba('標識', 'ひょうしき', 'rambu')}や{kotoba('標示', 'ひょうじ', 'marka')}によって{kotoba('速度', 'そくど', 'kecepatan')}が{kotoba('指定', 'してい', 'ditentukan')}されていない{kotoba('場合', 'ばあい', 'kasus')}の{kotoba('法令', 'ほうれい', 'peraturan perundang-undangan')}で{kotoba('定められた', 'さだめられた', 'ditetapkan')}{kotoba('最高速度', 'さいこうそくど', 'kecepatan maksimum')}を{kotoba('いいます', '', 'disebut')}。{kotoba('一般道路', 'いっぱんどうろ', 'jalan umum')}{kotoba('の', '', 'partikel')} {kotoba('場合', 'ばあい', 'kasus')}、トラックの{kotoba('最高速度', 'さいこうそくど', 'kecepatan maksimum')}は{kotoba('時速', 'じそく', 'kecepatan per jam')}60キロです。{kotoba('高速自動車国道', 'こうそくじどうしゃこくどう', 'jalan tol nasional')}{kotoba('の', '', 'partikel')} {kotoba('場合', 'ばあい', 'kasus')}は、トラックの{kotoba('種類', 'しゅるい', 'jenis')}によって{kotoba('異なり', 'ことなり', 'berbeda')}、{kotoba('時速', 'じそく', 'kecepatan per jam')}100キロ、{kotoba('時速', 'じそく', 'kecepatan per jam')}90キロ、{kotoba('時速', 'じそく', 'kecepatan per jam')}80キロの3つに{kotoba('区分', 'くぶん', 'dibagi')}されます。{kotoba('中型', 'ちゅうがた', 'ukuran menengah')}トラックの{kotoba('場合', 'ばあい', 'kasus')}は{kotoba('車両総重量', 'しゃりょうそうじゅうりょう', 'berat total kendaraan')}（{kotoba('荷物', 'にもつ', 'barang')}を{kotoba('最大', 'さいだい', 'maksimal')}に{kotoba('載せた', 'のせた', 'dimuat')}ときのその{kotoba('車', 'くるま', 'kendaraan')}の{kotoba('重さ', 'おもさ', 'berat')}）・{kotoba('最大積載量', 'さいだいせきさいりょう', 'kapasitas muatan maksimal')}（その{kotoba('車', 'くるま', 'kendaraan')}に{kotoba('載せられる', 'のせられる', 'bisa dimuat')}{kotoba('荷物', 'にもつ', 'barang')}の{kotoba('最大', 'さいだい', 'maksimal')}の{kotoba('重さ', 'おもさ', 'berat')}）によって{kotoba('最高速度', 'さいこうそくど', 'kecepatan maksimum')}が{kotoba('異なります', 'ことなります', 'berbeda')}から{kotoba('注意', 'ちゅうい', 'perhatian')}しましょう。",
        "id": "Kecepatan menurut perundang-undangan adalah kecepatan maksimum yang ditetapkan oleh hukum ketika tidak ada kecepatan yang ditentukan oleh rambu lalu lintas atau marka jalan. Pada jalan umum, kecepatan maksimum untuk truk adalah 60 km/jam. Sedangkan di jalan tol nasional, kecepatan maksimum berbeda-beda tergantung jenis truk, yang terbagi dalam tiga kategori: 100 km/jam, 90 km/jam, dan 80 km/jam. Untuk truk menengah, kecepatan maksimum berbeda tergantung pada berat kotor kendaraan (berat kendaraan saat mengangkut beban maksimum) dan beban muatan maksimum (berat muatan maksimum yang dapat dimuat di kendaraan), jadi berhati-hatilah."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('規制速度', 'きせいそくど', 'kecepatan aturan')}とは",
        "id": "・Apa itu Kecepatan yang Diatur (Regulasi)?"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('規制速度', 'きせいそくど', 'kecepatan aturan')}とは、{kotoba('標識', 'ひょうしき', 'rambu')}や{kotoba('標示', 'ひょうじ', 'marka')}により{kotoba('指定', 'してい', 'ditentukan')}された{kotoba('最高速度', 'さいこうそくど', 'kecepatan maksimum')}を{kotoba('いいます', '', 'disebut')}。{kotoba('一般道路', 'いっぱんどうろ', 'jalan umum')}{kotoba('の', '', 'partikel')} {kotoba('場合', 'ばあい', 'kasus')}、{kotoba('時速', 'じそく', 'kecepatan per jam')}40キロや{kotoba('時速', 'じそく', 'kecepatan per jam')}30キロに{kotoba('規制', 'きせい', 'diatur')}されているところが{kotoba('多く', 'おおく', 'banyak')}あります。{kotoba('高速自動車国道', 'こうそくじどうしゃこくどう', 'jalan tol nasional')}についても、{kotoba('雨', 'あめ', 'hujan')}や{kotoba('雪', 'ゆき', 'salju')}、{kotoba('強風', 'きょうふう', 'angin kencang')}などのときには{kotoba('速度', 'そくど', 'kecepatan')}が{kotoba('規制', 'きせい', 'diatur')}されますから、{kotoba('速度', 'そくど', 'kecepatan')}の{kotoba('標識', 'ひょうしき', 'rambu')}や{kotoba('標示', 'ひょうじ', 'marka')}によく{kotoba('注意', 'ちゅうい', 'perhatian')}して{kotoba('走行', 'そうこう', 'berjalan/melaju')}しましょう。",
        "id": "Kecepatan yang diatur adalah kecepatan maksimum yang ditentukan oleh rambu lalu lintas atau marka jalan. Di jalan umum, banyak area yang kecepatannya dibatasi hingga 40 km/jam atau 30 km/jam. Bahkan di jalan tol nasional, kecepatan akan dibatasi saat terjadi hujan, salju, angin kencang, dan lainnya, jadi berkendaralah dengan selalu memperhatikan rambu dan marka kecepatan."
    },
    {
        "is_header": True,
        "jp": f"◆{kotoba('自動車専用道路', 'じどうしゃせんようどうろ', 'jalan khusus mobil')}の{kotoba('最高速度', 'さいこうそくど', 'kecepatan maksimum')}は{kotoba('一般道路', 'いっぱんどうろ', 'jalan umum')}と{kotoba('同じ', 'おなじ', 'sama')}",
        "id": "◆ Kecepatan Maksimum di Jalan Khusus Kendaraan Sama dengan Jalan Umum"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('高速自動車国道', 'こうそくじどうしゃこくどう', 'jalan tol nasional')}と{kotoba('自動車専用道路', 'じどうしゃせんようどうろ', 'jalan khusus mobil')}を{kotoba('合わせて', 'あわせて', 'digabungkan')}「{kotoba('高速道路', 'こうそくどうろ', 'jalan tol')}」と{kotoba('いいます', '', 'disebut')}が、{kotoba('高速自動車国道', 'こうそくじどうしゃこくどう', 'jalan tol nasional')}と{kotoba('自動車専用道路', 'じどうしゃせんようどうろ', 'jalan khusus mobil')}では{kotoba('最高速度', 'さいこうそくど', 'kecepatan maksimum')}が{kotoba('違います', 'ちがいます', 'berbeda')}。",
        "id": "Jalan tol nasional dan jalan khusus kendaraan secara kolektif sering disebut \"jalan tol\", tetapi kecepatan maksimum keduanya berbeda."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('自動車専用道路', 'じどうしゃせんようどうろ', 'jalan特別')}の{kotoba('最高速度', 'さいこうそくど', 'kecepatan maksimum')}は{kotoba('一般道路', 'いっぱんどうろ', 'jalan umum')}と{kotoba('同じ', 'おなじ', 'sama')}であり、{kotoba('標識', 'ひょうしき', 'rambu')}や{kotoba('標示', 'ひょうじ', 'marka')}により{kotoba('速度', 'そくど', 'kecepatan')}が{kotoba('指定', 'してい', 'ditentukan')}されていない{kotoba('場合', 'ばあい', 'kasus')}の{kotoba('最高速度', 'さいこうそくど', 'kecepatan maksimum')}は{kotoba('時速', 'じそく', 'kecepatan per jam')}60キロです。{kotoba('高速自動車国道', 'こうそくじどうしゃこくどう', 'jalan tol nasional')}と{kotoba('同じ', 'おなじ', 'sama')}{kotoba('感覚', 'かんかく', 'perasaan/insting')}で{kotoba('速度', 'そくど', 'kecepatan')}を{kotoba('出す', 'だす', 'mengeluarkan')}と、{kotoba('速度違反', 'そくどいはん', 'pelanggaran kecepatan')}になる{kotoba('おそれ', '', 'kekhawatiran')}がありますから{kotoba('注意', 'ちゅうい', 'perhatian')}しましょう。",
        "id": "Kecepatan maksimum jalan khusus kendaraan sama dengan kecepatan jalan umum, yakni kecepatan maksimum saat tidak ada rambu atau marka penunjuk kecepatan adalah 60 km/jam. Jika Anda mengemudi dengan perasaan kecepatan yang sama seperti di jalan tol nasional, Anda berisiko melakukan pelanggaran batas kecepatan, jadi harap berhati-hati."
    },
    {
        "is_header": True,
        "jp": f"４．４ {kotoba('交差点', 'こうさてん', 'persimpangan')}の{kotoba('通行', 'つうこう', 'melintas')}",
        "id": "4.4 Melintasi Persimpangan"
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('安全', 'あんぜん', 'keselamatan')}の{kotoba('確認', 'かくにん', 'konfirmasi')}と{kotoba('合図', 'あいず', 'sinyal')}",
        "id": "・Memastikan Keselamatan dan Memberikan Sinyal (Lampu Sein)"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('進路変更', 'しんろへんこう', 'pindah jalur')}、{kotoba('転回', 'てんかい', 'putar balik')}、{kotoba('後退', 'こうたい', 'mundur')}などをしようとするときは、{kotoba('あらかじめ', '', 'sebelumnya')}バックミラーなどで{kotoba('安全', 'あんぜん', 'aman')}を{kotoba('確かめて', 'たしかめて', 'memastikan')}から{kotoba('合図', 'あいず', 'sinyal')}をしなければなりません。",
        "id": "Saat hendak mengubah jalur, memutar balik (U-turn), memundurkan kendaraan, dan sebagainya, Anda harus memeriksa keadaan sekitar melalui kaca spion agar aman sebelum memberikan sinyal (lampu sein)."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('左折', 'させつ', 'belok kiri')}・{kotoba('右折', 'うせつ', 'belok kanan')}をする{kotoba('場合', 'ばあい', 'kasus')}の{kotoba('合図', 'あいず', 'sinyal')}は、{kotoba('左折', 'させつ', 'belok kiri')}・{kotoba('右折', 'うせつ', 'belok kanan')}をする{kotoba('地点', 'ちてん', 'titik')}（{kotoba('交差点', 'こうさてん', 'persimpangan')}）の30メートル{kotoba('手前', 'てまえ', 'sebelum')}の{kotoba('地点', 'ちてん', 'titik')}でしなければなりません。",
        "id": "Sinyal untuk berbelok ke kiri atau kanan harus diberikan pada jarak 30 meter sebelum titik berbelok (persimpangan) yang dituju."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('交差点', 'こうさてん', 'persimpangan')}の{kotoba('右折時', 'うせつじ', 'saat belok kanan')}・{kotoba('左折時', 'させつじ', 'saat belok kiri')}は{kotoba('徐行', 'じょこう', 'melaju pelan')}",
        "id": "・Perlahan-lahan Saat Berbelok ke Kanan dan Kiri di Persimpangan"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('自動車', 'じどうしゃ', 'mobil')}は、{kotoba('道路', 'どうろ', 'jalan')}の{kotoba('中央', 'ちゅうおう', 'tengah')}（{kotoba('中央線', 'ちゅうおうせん', 'garis tengah')}があるときは、その{kotoba('中央線', 'ちゅうおうせん', 'garis tengah')}）から{kotoba('左', 'ひだり', 'kiri')}の{kotoba('部分', 'ぶぶん', 'bagian')}を{kotoba('通行', 'つうこう', 'melintas')}しなければなりません。",
        "id": "Mobil harus melaju di bagian kiri dari tengah jalan (jika ada garis tengah, berarti di sisi kiri garis tersebut)."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('交差点', 'こうさてん', 'persimpangan')}では、{kotoba('他', 'ほか', 'lain')}の{kotoba('車', 'くるま', 'kendaraan')}、{kotoba('横断する', 'おうだんする', 'menyeberang')}{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}や{kotoba('自転車', 'じてんしゃ', 'sepeda')}などによく{kotoba('注意', 'ちゅうい', 'perhatikan')}して、できるかぎり{kotoba('安全な', 'あんぜんな', 'aman')}{kotoba('速度', 'そくど', 'kecepatan')}と{kotoba('方法', 'ほうほう', 'cara')}で{kotoba('走行する', 'そうこうする', 'berjalan/melaju')}{kotoba('必要', 'ひつよう', 'perlu')}があります。とくに{kotoba('事故', 'じこ', 'kecelakaan')}の{kotoba('起こりやすい', 'おこりやすい', 'mudah terjadi')}{kotoba('右折時', 'うせつじ', 'saat belok kanan')}・{kotoba('左折時', 'させつじ', 'saat belok kiri')}は{kotoba('徐行', 'じょこう', 'melaju pelan')}（ただちに{kotoba('停止', 'ていし', 'berhenti')}できる{kotoba('速度', 'そくど', 'kecepatan')}で{kotoba('進行する', 'しんこうする', 'maju/melaju')}こと）が{kotoba('義務づけられて', 'ぎむづけられて', 'diwajibkan')}いますから、{kotoba('横断歩道', 'おうだんほどう', 'zebra cross')}の{kotoba('手前', 'てまえ', 'sebelum')}で{kotoba('余裕', 'よゆう', 'waktu/jarak luang')}をもって{kotoba('停止', 'ていし', 'berhenti')}できるよう{kotoba('十分', 'じゅうぶん', 'cukup')}に{kotoba('速度', 'そくど', 'kecepatan')}を{kotoba('落として', 'おとして', 'mengurangi')}{kotoba('進行', 'しんこう', 'maju/melaju')}しましょう。",
        "id": "Di persimpangan, Anda harus sangat memperhatikan kendaraan lain, serta pejalan kaki dan sepeda yang menyeberang, dan mengemudi dengan kecepatan serta cara yang seaman mungkin. Khususnya saat berbelok kanan dan kiri yang rentan terjadi kecelakaan, Anda diwajibkan untuk melaju pelan (dengan kecepatan yang memungkinkan untuk langsung berhenti). Jadi, kurangilah kecepatan secukupnya dan melajulah perlahan agar Anda memiliki jarak henti yang aman di depan zebra cross."
    },
    {
        "is_header": True,
        "jp": f"◆{kotoba('右折車', 'うせつしゃ', 'kendaraan belok kanan')}より{kotoba('直進車', 'ちょくしんしゃ', 'kendaraan lurus')}や{kotoba('左折車', 'させつしゃ', 'kendaraan belok kiri')}が{kotoba('優先', 'ゆうせん', 'prioritas')}",
        "id": "◆ Kendaraan yang Melaju Lurus dan Berbelok Kiri Diprioritaskan daripada Kendaraan Berbelok Kanan"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('交差点', 'こうさてん', 'persimpangan')}では、{kotoba('右折する', 'うせつする', 'berbelok kanan')}{kotoba('車', 'くるま', 'kendaraan')}よりも{kotoba('直進する', 'ちょくしんする', 'berjalan lurus')}{kotoba('車', 'くるま', 'kendaraan')}や{kotoba('左折する', 'させつする', 'berbelok kiri')}{kotoba('車', 'くるま', 'kendaraan')}のほうが{kotoba('優先', 'ゆうせん', 'prioritas')}されます。たとえ{kotoba('自分', 'じぶん', 'sendiri')}のほうが{kotoba('先', 'さき', 'lebih dulu')}に{kotoba('交差点', 'こうさてん', 'persimpangan')}に{kotoba('入って', 'はいって', 'masuk')}いても、{kotoba('直進車', 'ちょくしんしゃ', 'kendaraan lurus')}や{kotoba('左折車', 'させつしゃ', 'kendaraan belok kiri')}の{kotoba('進行', 'しんこう', 'maju/melaju')}を{kotoba('妨げて', 'さまたげて', 'menghalangi')}はいけません。{kotoba('直進車', 'ちょくしんしゃ', 'kendaraan lurus')}や{kotoba('左折車', 'させつしゃ', 'kendaraan belok kiri')}の{kotoba('通過', 'つうか', 'melewati')}を{kotoba('待って', 'まって', 'menunggu')}、{kotoba('安全', 'あんぜん', 'aman')}が{kotoba('確認', 'かくにん', 'konfirmasi')}できてから{kotoba('右折する', 'うせつする', 'berbelok kanan')}ようにしましょう。",
        "id": "Di persimpangan, prioritas diberikan kepada kendaraan yang melaju lurus atau berbelok kiri dibandingkan kendaraan yang berbelok kanan. Meskipun Anda memasuki persimpangan lebih dahulu, Anda tidak boleh menghalangi laju kendaraan yang berjalan lurus atau berbelok ke kiri. Tunggulah kendaraan tersebut melintas dan pastikan keamanan sebelum Anda berbelok ke kanan."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('信号機', 'しんごうき', 'lampu lalu lintas')}のない{kotoba('交差点', 'こうさてん', 'persimpangan')}の{kotoba('通行', 'つうこう', 'melintas')}",
        "id": "・Melintasi Persimpangan Tanpa Lampu Lalu Lintas"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('信号機', 'しんごうき', 'lampu lalu lintas')}のない{kotoba('交差点', 'こうさてん', 'persimpangan')}では、とくに{kotoba('次', 'つぎ', 'berikut')}の{kotoba('点', 'てん', 'poin')}に{kotoba('注意', 'ちゅうい', 'perhatian')}しましょう。",
        "id": "Di persimpangan yang tidak dilengkapi lampu lalu lintas, perhatikanlah poin-poin berikut ini secara khusus."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('交差する', 'こうさする', 'bersilangan')}{kotoba('道路', 'どうろ', 'jalan')}が{kotoba('優先道路', 'ゆうせんどうろ', 'jalan prioritas')}である{kotoba('場合', 'ばあい', 'kasus')}や{kotoba('明らか', 'あきらか', 'jelas')}に{kotoba('道幅', 'みちはば', 'lebar jalan')}が{kotoba('広い', 'ひろい', 'lebar')}{kotoba('場合', 'ばあい', 'kasus')}は、{kotoba('徐行', 'じょこう', 'melaju pelan')}して{kotoba('交差道路側', 'こうさどうろがわ', 'sisi jalan bersilangan')}の{kotoba('車', 'くるま', 'kendaraan')}の{kotoba('通行', 'つうこう', 'melintas')}を{kotoba('妨げない', 'さまたげない', 'tidak menghalangi')}ようにします。",
        "id": "・Jika jalan yang bersilangan adalah jalan utama (prioritas) atau jika jalannya jelas lebih lebar, turunkan kecepatan dan jangan menghalangi kendaraan yang datang dari jalan persilangan tersebut."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('道幅', 'みちはば', 'lebar jalan')}が{kotoba('同じ', 'おなじ', 'sama')}ような{kotoba('道路', 'どうろ', 'jalan')}の{kotoba('交差点', 'こうさてん', 'persimpangan')}では、{kotoba('左方', 'さほう', 'sisi kiri')}からくる{kotoba('車', 'くるま', 'kendaraan')}のほうが{kotoba('優先', 'ゆうせん', 'prioritas')}されますから、{kotoba('左方', 'さほう', 'sisi kiri')}から{kotoba('車', 'くるま', 'kendaraan')}が{kotoba('接近している', 'せっきんしている', 'mendekat')}ときはその{kotoba('通行', 'つうこう', 'melintas')}を{kotoba('妨げない', 'さまたげない', 'tidak menghalangi')}ようにします。",
        "id": "・Di persimpangan yang lebar jalannya relatif sama, prioritas diberikan pada kendaraan yang datang dari arah kiri. Oleh karena itu, jika ada kendaraan yang mendekat dari sebelah kiri, Anda tidak boleh menghalanginya."
    },
    {
        "is_header": False,
        "jp": f"※{kotoba('道幅', 'みちはば', 'lebar jalan')}が{kotoba('同じ', 'おなじ', 'sama')}ような{kotoba('交差点', 'こうさてん', 'persimpangan')}の{kotoba('場合', 'ばあい', 'kasus')}、{kotoba('自車', 'じしゃ', 'kendaraan sendiri')}のほうが{kotoba('交差する', 'こうさする', 'bersilangan')}{kotoba('道路', 'どうろ', 'jalan')}よりも{kotoba('道幅', 'みちはば', 'lebar jalan')}が{kotoba('広く', 'ひろく', 'lebar')}{kotoba('見える', 'みえる', 'terlihat')}ことがありますから{kotoba('注意', 'ちゅうい', 'perhatian')}しましょう。",
        "id": "※Di persimpangan dengan lebar jalan yang serupa, lebar jalan tempat kendaraan Anda melaju terkadang bisa tampak lebih lebar dari jalan persilangan, jadi berhati-hatilah."
    }
    # Data Bab 4 (4.5 - 4.10) Lengkap
    # --- 4.5 車間距離の保持 ---
    {
        "is_header": True,
        "jp": f"４．５ {kotoba('車間距離', 'しゃかんきょり', 'jarak antar kendaraan')}の{kotoba('保持', 'ほじ', 'menjaga')}",
        "id": "4.5 Menjaga Jarak Antar Kendaraan"
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('前車', 'ぜんしゃ', 'kendaraan depan')}が{kotoba('急停止', 'きゅうていし', 'berhenti mendadak')}しても{kotoba('追突しない', 'ついとつしない', 'tidak menabrak')}{kotoba('車間距離', 'しゃかんきょり', 'jarak antar kendaraan')}をとる",
        "id": "・Menjaga Jarak Kendaraan agar Tidak Menabrak Jika Kendaraan Depan Berhenti Mendadak"
    },
    {
        "is_header": False,
        "jp": f"トラック{kotoba('事故', 'じこ', 'kecelakaan')}の{kotoba('特徴', 'とくちょう', 'ciri-ciri')}は{kotoba('追突', 'ついとつ', 'tabrak belakang')}が{kotoba('多い', 'おおい', 'banyak')}ということです。{kotoba('追突事故', 'ついとつじこ', 'kecelakaan tabrak belakang')}を{kotoba('防止する', 'ぼうしする', 'mencegah')}ためには、{kotoba('車間距離', 'しゃかんきょり', 'jarak antar kendaraan')}（{kotoba('前', 'まえ', 'depan')}を{kotoba('走る', 'はしる', 'berjalan')}{kotoba('車', 'くるま', 'kendaraan')}との{kotoba('距離', 'きょり', 'jarak')}）を{kotoba('十分', 'じゅうぶん', 'cukup')}にとることがポイントです。",
        "id": "Salah satu ciri utama kecelakaan truk adalah tingginya insiden tabrakan dari belakang. Untuk mencegah kecelakaan tabrak belakang, intinya adalah mengambil jarak aman antar kendaraan (jarak dengan kendaraan yang melaju di depan) yang cukup."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('十分な', 'じゅうぶんな', 'cukup')}{kotoba('車間距離', 'しゃかんきょり', 'jarak antar kendaraan')}をとっていれば、{kotoba('前', 'まえ', 'depan')}の{kotoba('車', 'くるま', 'kendaraan')}の{kotoba('急な', 'きゅうな', 'mendadak')}{kotoba('減速', 'げんそく', 'kurang kecepatan')}や{kotoba('停止', 'ていし', 'berhenti')}にも{kotoba('対応', 'たいおう', 'merespons')}できます。",
        "id": "Jika Anda menjaga jarak antar kendaraan yang cukup, Anda dapat merespons penurunan kecepatan atau berhentinya kendaraan depan secara mendadak."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('十分な', 'じゅうぶんな', 'cukup')}{kotoba('車間距離', 'しゃかんきょり', 'jarak antar kendaraan')}の{kotoba('目安', 'めやす', 'patokan')}として、{kotoba('一般道路', 'いっぱんどうろ', 'jalan umum')}では、{kotoba('速度計', 'そくどけい', 'speedometer')}の{kotoba('数字', 'すうじ', 'angka')}から15を{kotoba('引いた', 'ひいた', 'dikurangi')}{kotoba('数字以上', 'すうじいじょう', 'angka ke atas')}、{kotoba('高速道路', 'こうそくどうろ', 'jalan tol')}では{kotoba('速度計', 'そくどけい', 'speedometer')}の{kotoba('数字', 'すうじ', 'angka')}をメートルに{kotoba('置き換えた', 'おきかえた', 'diganti')}{kotoba('数字以上', 'すうじいじょう', 'angka ke atas')}と{kotoba('覚えて', 'おぼえて', 'ingatlah')}おきましょう。",
        "id": "Sebagai patokan jarak antar kendaraan yang cukup, ingatlah: di jalan umum, angkanya sama dengan atau lebih besar dari angka pada spidometer dikurangi 15; sedangkan di jalan tol, angkanya sama dengan atau lebih besar dari angka spidometer yang dikonversi menjadi satuan meter."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('意識', 'いしき', 'secara sadar')}して{kotoba('車間距離', 'しゃかんきょり', 'jarak antar kendaraan')}をとる",
        "id": "・Menjaga Jarak Aman Kendaraan Secara Sadar"
    },
    {
        "is_header": False,
        "jp": f"トラックは{kotoba('運転席', 'うんてんせき', 'kursi pengemudi')}が{kotoba('高い', 'たかい', 'tinggi')}ために{kotoba('路面', 'ろめん', 'permukaan jalan')}がよく{kotoba('見えます', 'みえます', 'terlihat')}。{kotoba('そのため', '', 'oleh karena itu')}トラック{kotoba('運転者', 'うんてんしゃ', '描く')}は{kotoba('車間距離', 'しゃかんきょり', 'jarak antar kendaraan')}が{kotoba('実際', 'じっさい', 'sebenarnya')}よりも{kotoba('長い', 'ながい', 'panjang')}ように{kotoba('感じやすく', 'かんじやすく', 'mudah merasa')}、{kotoba('車間距離', 'しゃかんきょり', 'jarak antar kendaraan')}を{kotoba('短く', 'みじかく', 'pendek')}してしまうことが{kotoba('多い', 'おおい', 'banyak')}ので、{kotoba('意識', 'いしき', 'secara sadar')}して{kotoba('十分な', 'じゅうぶんな', 'cukup')}{kotoba('車間距離', 'しゃかんきょり', 'jarak antar kendaraan')}をとるようにしましょう。",
        "id": "Karena kursi pengemudi truk tinggi, permukaan jalan terlihat jelas. Hal ini sering membuat pengemudi truk merasa jarak antar kendaraan lebih panjang dari yang sebenarnya, sehingga rentan memperpendek jarak. Oleh karena itu, sadarilah hal ini dan pastikan Anda mengambil jarak antar kendaraan yang cukup."
    },

    # --- 4.6 スマートフォンなどの使用運転の禁止 ---
    {
        "is_header": True,
        "jp": f"４．６ スマートフォンなどの{kotoba('使用運転', 'しよううんてん', 'mengemudi sambil menggunakan')}の{kotoba('禁止', 'きんし', 'larangan')}",
        "id": "4.6 Larangan Mengemudi Sambil Menggunakan Smartphone dll."
    },
    {
        "is_header": True,
        "jp": f"◆スマートフォン{kotoba('等', 'など', 'dan lain-lain')}の{kotoba('使用運転', 'しよううんてん', 'mengemudi sambil menggunakan')}の{kotoba('危険性', 'きけんせい', 'bahaya')}",
        "id": "◆ Bahayanya Mengemudi Sambil Menggunakan Smartphone dll."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('走行中', 'そうこうちゅう', 'saat melaju')}にスマートフォンや{kotoba('携帯電話', 'けいたいでんわ', 'handphone')}などを{kotoba('操作したり', 'そうさしたり', 'mengoperasikan')}{kotoba('画面', 'がめん', 'layar')}を{kotoba('注視する', 'ちゅうしする', 'menatap')}と、{kotoba('停止した', 'ていしした', 'berhenti')}{kotoba('前車', 'ぜんしゃ', 'kendaraan depan')}に{kotoba('気づく', 'きづく', 'menyadari')}のが{kotoba('遅れて', 'おくれて', 'terlambat')}{kotoba('追突する', 'ついとつする', 'menabrak')}などの{kotoba('事故', 'じこ', 'kecelakaan')}につながります。",
        "id": "Mengoperasikan ponsel cerdas (smartphone) atau handphone dan menatap layarnya saat mengemudi dapat memperlambat Anda menyadari kendaraan di depan yang telah berhenti, sehingga berujung pada kecelakaan tabrakan dari belakang."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('そのため', '', 'oleh karena itu')}{kotoba('走行中', 'そうこうちゅう', 'saat melaju')}のスマートフォンなどの{kotoba('操作', 'そうさ', 'pengoperasian')}や{kotoba('画面', 'がめん', 'layar')}の{kotoba('注視', 'ちゅうし', 'menatap')}は{kotoba('禁止', 'きんし', 'dilarang')}されていて、{kotoba('違反した', 'いはんした', 'melanggar')}{kotoba('場合', 'ばあい', 'kasus')}には{kotoba('重い', 'おもい', 'berat')}{kotoba('処罰', 'しょばつ', 'hukuman')}がおこなわれます。{kotoba('交通事故', 'こうつうじこ', 'kecelakaan lalu lintas')}を{kotoba('起こした', 'おこした', 'menyebabkan')}{kotoba('場合', 'ばあい', 'kasus')}は、{kotoba('懲役', 'ちょうえき', 'hukuman penjara')}または{kotoba('罰金刑', 'ばっきんけい', 'hukuman denda')}を{kotoba('受けます', 'うけます', 'menerima')}。",
        "id": "Oleh karena itu, mengoperasikan smartphone atau menatap layarnya saat sedang melaju adalah dilarang. Jika melanggar, Anda akan menerima hukuman yang berat. Jika Anda sampai menyebabkan kecelakaan lalu lintas, Anda akan dipenjara atau didenda."
    },
    {
        "is_header": True,
        "jp": f"◆{kotoba('使用', 'しよう', 'penggunaan')}は{kotoba('安全な', 'あんぜんな', 'aman')}{kotoba('場所', 'ばしょ', 'tempat')}での{kotoba('停止時', 'ていしじ', 'saat berhenti')}に{kotoba('行う', 'おこなう', 'melakukan')}",
        "id": "◆ Lakukan Penggunaan di Tempat yang Aman Saat Berhenti"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('走行中', 'そうこうちゅう', 'saat melaju')}に、スマートフォンなどを{kotoba('使用', 'しよう', 'menggunakan')}しなければならないときは、{kotoba('必ず', 'かならず', 'selalu/pasti')}{kotoba('駐車場', 'ちゅうしゃじょう', 'tempat parkir')}などの{kotoba('安全な', 'あんぜんな', 'aman')}{kotoba('場所', 'ばしょ', 'tempat')}に{kotoba('車', 'くるま', 'kendaraan')}を{kotoba('止めて', 'とめて', 'memberhentikan')}から{kotoba('操作', 'そうさ', 'pengoperasian')}します。{kotoba('道路', 'どうろ', 'jalan')}の{kotoba('左端', 'ひだりはし', 'tepi kiri')}に{kotoba('停止して', 'ていしして', 'berhenti')}{kotoba('の', '', 'partikel')} {kotoba('使用', 'しよう', 'penggunaan')}は、{kotoba('後続車', 'こうぞくしゃ', 'kendaraan belakang')}に{kotoba('追突される', 'ついとつされる', 'ditabrak dr belakang')}{kotoba('危険', 'きけん', 'bahaya')}があるだけでなく、{kotoba('車体', 'しゃたい', 'bodi kendaraan')}の{kotoba('大きな', 'おおきな', 'besar')}トラックは{kotoba('他', 'ほか', 'lain')}の{kotoba('交通', 'こうつう', 'lalu lintas')}の{kotoba('妨げ', 'さまたげ', 'hambatan')}になり{kotoba('渋滞', 'じゅうたい', 'macet')}などを{kotoba('招く', 'まねく', 'mengundang')}{kotoba('おそれ', '', 'kekhawatiran')}もありますから{kotoba('避けましょう', 'さけましょう', 'mari hindari')}。",
        "id": "Jika Anda harus menggunakan smartphone dan sebagainya saat mengemudi, Anda harus selalu memberhentikan kendaraan di tempat yang aman seperti tempat parkir sebelum mengoperasikannya. Menggunakan perangkat dengan berhenti di tepi kiri jalan tidak hanya berisiko ditabrak oleh kendaraan dari belakang, tetapi truk besar juga berpotensi menghalangi arus lalu lintas lain dan menyebabkan kemacetan. Jadi, hindarilah tindakan ini."
    },
    {
        "is_header": False,
        "jp": f"なお、{kotoba('走行中', 'そうこうちゅう', 'saat melaju')}に{kotoba('着信音', 'ちゃくしんおん', 'nada dering')}が{kotoba('鳴る', 'なる', 'berbunyi')}だけでも、それに{kotoba('気', 'き', 'perhatian')}をとられて{kotoba('前方', 'ぜんぽう', 'depan')}への{kotoba('注意', 'ちゅうい', 'perhatian')}が{kotoba('欠ける', 'かける', 'kurang/hilang')}ことがあります。{kotoba('走行中', 'そうこうちゅう', 'saat melaju')}は{kotoba('電源', 'でんげん', 'daya')}を{kotoba('切って', 'きって', 'mematikan')}おくか、マナーモードやドライブモードにしておきましょう。",
        "id": "Selain itu, sekadar nada dering yang berbunyi saat mengemudi pun bisa mengalihkan perhatian dan menyebabkan berkurangnya kewaspadaan ke arah depan. Saat mengemudi, matikanlah perangkat atau atur menjadi mode senyap (*manner mode*) atau *drive mode*."
    },

    # --- 4.7 歩行者などの保護 ---
    {
        "is_header": True,
        "jp": f"４．７ {kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}などの{kotoba('保護', 'ほご', 'perlindungan')}",
        "id": "4.7 Perlindungan Pejalan Kaki dll."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('安全な', 'あんぜんな', 'aman')}{kotoba('間隔', 'かんかく', 'jarak/celah')}をとる",
        "id": "・Berikan Jarak (Ruang) yang Aman"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}や{kotoba('自転車', 'じてんしゃ', 'sepeda')}はちょっと{kotoba('接触した', 'せっしょくした', 'menyentuh/menyerempet')}だけでも{kotoba('重大な', 'じゅうだいな', 'fatal')}{kotoba('人身事故', 'じんしんじこ', 'kecelakaan lalu lintas')}につながります。{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}や{kotoba('自転車', 'じてんしゃ', 'sepeda')}の{kotoba('側方', 'そくほう', 'sisi samping')}を{kotoba('通る', 'とおる', 'melintas')}ときは、{kotoba('安全な', 'あんぜんな', 'aman')}{kotoba('間隔', 'かんかく', 'jarak/celah')}をあけるか、それができない{kotoba('場合', 'ばあい', 'kasus')}は{kotoba('徐行', 'じょこう', 'melaju pelan')}しましょう。",
        "id": "Pejalan kaki dan sepeda bisa mengalami kecelakaan fatal bahkan jika hanya terserempet sedikit. Ketika melintasi samping pejalan kaki atau sepeda, berilah jarak yang aman, atau jika tidak memungkinkan, pelankan laju kendaraan Anda (徐行)."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('安全な', 'あんぜんな', 'aman')}{kotoba('間隔', 'かんかく', 'jarak/celah')}については、{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}や{kotoba('自転車', 'じてんしゃ', 'sepeda')}が{kotoba('急に', 'きゅうに', 'tiba-tiba')}{kotoba('ふらついたりした', '', 'oleng')}{kotoba('場合', 'ばあい', 'kasus')}でも{kotoba('安全', 'あんぜん', 'keselamatan')}が{kotoba('保てる', 'たもてる', 'dijaga')}よう、1メートル{kotoba('以上', 'いじょう', 'ke atas')}の{kotoba('間隔', 'かんかく', 'jarak/celah')}が{kotoba('必要', 'ひつよう', 'perlu')}です。",
        "id": "Jarak yang aman di sini berarti Anda membutuhkan setidaknya jarak lebih dari 1 meter agar keselamatan tetap terjaga meskipun sepeda atau pejalan kaki tersebut tiba-tiba oleng."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('横断歩道', 'おうだんほどう', 'zebra cross')}に{kotoba('接近する', 'せっきんする', 'mendekat')}ときの{kotoba('注意点', 'ちゅういてん', 'poin perhatian')}",
        "id": "・Poin-poin Perhatian Saat Mendekati Zebra Cross"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('信号機', 'しんごうき', 'lampu lalu lintas')}のない{kotoba('横断歩道', 'おうだんほどう', 'zebra cross')}に{kotoba('接近する', 'せっきんする', 'mendekat')}{kotoba('場合', 'ばあい', 'kasus')}は、{kotoba('次', 'つぎ', 'berikut')}のものを{kotoba('守りましょう', 'まもりましょう', 'mari patuhi')}。",
        "id": "Saat Anda mendekati zebra cross yang tidak memiliki lampu lalu lintas, patuhilah hal-hal berikut:"
    },
    {
        "is_header": False,
        "jp": f"①{kotoba('横断する', 'おうだんする', 'menyeberang')}{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}や{kotoba('自転車', 'じてんしゃ', 'sepeda')}がいないことが{kotoba('明らかな', 'あきらかな', 'jelas')}ときは、そのまま{kotoba('進む', 'すすむ', 'maju')}ことができます。",
        "id": "① Jika jelas terlihat bahwa tidak ada pejalan kaki atau sepeda yang akan menyeberang, Anda dapat terus melaju."
    },
    {
        "is_header": False,
        "jp": f"②{kotoba('横断する', 'おうだんする', 'menyeberang')}{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}や{kotoba('自転車', 'じてんしゃ', 'sepeda')}がいるかいないか{kotoba('明らか', 'あきらか', 'jelas')}でないときは、{kotoba('横断歩道', 'おうだんほどう', 'zebra cross')}の{kotoba('手前', 'てまえ', 'sebelum')}で{kotoba('停止', 'ていし', 'berhenti')}できる{kotoba('速度', 'そくど', 'kecepatan')}に{kotoba('落として', 'おとして', 'mengurangi')}{kotoba('進行', 'しんこう', 'maju/melaju')}します。",
        "id": "② Jika tidak jelas apakah ada atau tidak ada pejalan kaki atau sepeda yang akan menyeberang, kurangi kecepatan hingga pada kecepatan di mana Anda bisa berhenti tepat sebelum zebra cross."
    },
    {
        "is_header": False,
        "jp": f"③{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}や{kotoba('自転車', 'じてんしゃ', 'sepeda')}が{kotoba('横断して', 'おうだんして', 'menyeberang')}いたり、{kotoba('横断', 'おうだん', 'menyeberang')}しようとしているときは、{kotoba('横断歩道', 'おうだんほどう', 'zebra cross')}の{kotoba('手前', 'てまえ', 'sebelum')}で{kotoba('一時停止', 'いちじていし', 'berhenti sementara')}をして、{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}や{kotoba('自転車', 'じてんしゃ', 'sepeda')}の{kotoba('通行', 'つうこう', 'melintas')}を{kotoba('妨げない', 'さまたげない', 'tidak menghalangi')}ようにします。",
        "id": "③ Saat ada pejalan kaki atau sepeda yang sedang menyeberang atau hendak menyeberang, hentikan kendaraan sejenak (一時停止) tepat sebelum zebra cross agar tidak menghalangi mereka melintas."
    },
    {
        "is_header": False,
        "jp": f"④{kotoba('横断歩道', 'おうだんほどう', 'zebra cross')}の{kotoba('直前', 'ちょくぜん', 'tepat sebelum')}に{kotoba('車', 'くるま', 'kendaraan')}が{kotoba('停止', 'ていし', 'berhenti')}しているときは、{kotoba('停止車', 'ていししゃ', 'mobil berhenti')}の{kotoba('前方', 'ぜんぽう', 'depan')}に{kotoba('出る', 'でる', 'keluar')}{kotoba('前', 'まえ', 'sebelum')}に{kotoba('一時停止', 'いちじていし', 'berhenti sementara')}して、{kotoba('横断歩道', 'おうだんほどう', 'zebra cross')}の{kotoba('安全確認', 'あんぜんかくにん', 'konfirmasi安全性')}をします。",
        "id": "④ Jika ada mobil yang berhenti tepat di depan zebra cross, hentikanlah kendaraan sejenak sebelum Anda mendahului mobil yang berhenti tersebut, dan pastikan kondisi zebra cross aman."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('幼児', 'ようじ', 'balita')}や{kotoba('高齢者', 'こうれいしゃ', 'lansia')}などの{kotoba('保護', 'ほご', 'perlindungan')}",
        "id": "・Melindungi Anak-anak, Lansia, dan Pejalan Kaki Berkebutuhan Khusus"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('幼児', 'ようじ', 'balita')}や{kotoba('高齢者', 'こうれいしゃ', 'lansia')}など{kotoba('次', 'つぎ', 'berikut')}に{kotoba('掲げる', 'かかげる', 'mencantumkan')}{kotoba('人', 'ひと', 'orang')}が{kotoba('通行', 'つうこう', 'melintas')}しているときは、{kotoba('一時停止', 'いちじていし', 'berhenti sementara')}か{kotoba('徐行', 'じょこう', 'melaju pelan')}をして、その{kotoba('通行', 'つうこう', 'melintas')}を{kotoba('妨げない', 'さまたげない', 'tidak menghalangi')}ようにします。",
        "id": "Jika orang-orang yang tercantum di bawah ini sedang melintas, berhentilah sejenak (一時停止) atau kurangi kecepatan (徐行) agar Anda tidak menghalangi mereka melintas:"
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('高齢の', 'こうれいの', 'lanjut usia')}{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}",
        "id": "- Pejalan kaki lanjut usia."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('保護者', 'ほごしゃ', 'wali/pendamping')}が{kotoba('付き添わない', 'つきそわない', 'tidak mendampingi')}{kotoba('児童', 'じどう', 'anak-anak')}や{kotoba('幼児', 'ようじ', 'balita')}",
        "id": "- Anak-anak atau balita yang tidak didampingi oleh walinya."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('身体障害者用', 'しんたいしょうがいしゃよう', 'untuk penyandang cacat fisik')}の{kotoba('車いす', 'くるまいす', 'kursi roda')}に{kotoba('乗った', 'のった', 'naik')}{kotoba('人', 'ひと', 'orang')}",
        "id": "- Orang yang menggunakan kursi roda khusus difabel."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('身体', 'しんたい', 'fisik')}に{kotoba('障害', 'しょうがい', 'cacat')}のある{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}や{kotoba('通行', 'つうこう', 'melintas')}に{kotoba('支障', 'ししょう', 'hambatan')}のある{kotoba('人', 'ひと', 'orang')}",
        "id": "- Pejalan kaki yang memiliki cacat fisik atau kesulitan berjalan."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('白', 'しろ', 'putih')}または{kotoba('黄色', 'きいろ', 'kuning')}の{kotoba('つえ', '', 'tongkat')}を{kotoba('持った', 'もった', 'membawa')}{kotoba('目', 'め', 'mata')}が{kotoba('見えない', 'みえない', 'tidak bisa melihat')}{kotoba('人', 'ひと', 'orang')}",
        "id": "- Tuna netra yang membawa tongkat putih atau kuning."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('盲導犬', 'もうどうけん', 'anjing penuntun')}を{kotoba('連れた', 'つれた', 'membawa')}{kotoba('目', 'め', 'mata')}が{kotoba('見えない', 'みえない', 'tidak bisa melihat')}{kotoba('人', 'ひと', 'orang')}",
        "id": "- Tuna netra yang dipandu anjing penuntun."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('白', 'しろ', 'putih')}または{kotoba('黄色', 'きいろ', 'kuning')}の{kotoba('つえ', '', 'tongkat')}を{kotoba('持った', 'もった', 'membawa')}{kotoba('耳', 'みみ', 'telinga')}が{kotoba('聞こえない', 'きこえない', 'tidak bisa mendengar')}{kotoba('人', 'ひと', 'orang')}や{kotoba('身体', 'しんたい', 'fisik')}に{kotoba('障害', 'しょうがい', 'cacat')}のある{kotoba('人', 'ひと', 'orang')}",
        "id": "- Tuna rungu atau orang cacat fisik yang membawa tongkat putih atau kuning."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('自転車', 'じてんしゃ', 'sepeda')}の{kotoba('保護', 'ほご', 'perlindungan')}",
        "id": "・Melindungi Sepeda"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('自転車', 'じてんしゃ', 'sepeda')}は{kotoba('車', 'くるま', 'kendaraan')}の{kotoba('一種', 'いっしゅ', 'satu jenis')}であり、{kotoba('原則', 'げんそく', 'prinsip')}として{kotoba('車道', 'しゃどう', 'jalan kendaraan')}を{kotoba('通行する', 'つうこうする', 'melintas')}こととされています。{kotoba('自転車', 'じてんしゃ', 'sepeda')}は、{kotoba('不安定', 'ふあんてい', 'tidak stabil')}であり、{kotoba('自動車', 'じどうしゃ', 'mobil')}のように{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}の{kotoba('体', 'からだ', 'tubuh')}が{kotoba('守られて', 'まもられて', 'dilindungi')}いません。{kotoba('車道', 'しゃどう', 'jalan kendaraan')}を{kotoba('通行する', 'つうこうする', 'melintas')}{kotoba('自転車', 'じてんしゃ', 'sepeda')}の{kotoba('安全', 'あんぜん', 'keselamatan')}に{kotoba('十分', 'じゅうぶん', 'cukup')}に{kotoba('配慮', 'はいりょ', 'perhatian')}しましょう。",
        "id": "Sepeda juga merupakan salah satu jenis kendaraan dan pada prinsipnya diwajibkan untuk melaju di badan jalan. Sepeda tidak stabil, dan pengendara sepeda tidak terlindungi bodinya layaknya pengendara mobil. Berikanlah perhatian yang cukup terhadap keselamatan sepeda yang melaju di badan jalan."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('歩道', 'ほどう', 'trotoar')}を{kotoba('横切る', 'よこぎる', 'menyeberangi')}{kotoba('とき', '', 'saat')}",
        "id": "・Saat Menyeberangi Trotoar"
    },
    {
        "is_header": False,
        "jp": f"お{kotoba('客様', 'きゃくさま', 'pelanggan')}の{kotoba('構内', 'こうない', 'area dlm')}や{kotoba('営業所', 'えいぎょうしょ', 'kantor')}などに{kotoba('出入りする', 'でいりする', 'keluar masuk')}ために、{kotoba('歩道', 'ほどう', 'trotoar')}や{kotoba('路側帯', 'ろそくたい', 'bahu jalan')}を{kotoba('横切る', 'よこぎる', 'menyeberangi')}ときは、{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}がいない{kotoba('場合', 'ばあい', 'kasus')}でも{kotoba('手前', 'てまえ', 'sebelum')}で{kotoba('一時停止', 'いちじていし', 'berhenti sementara')}しなければいけません。",
        "id": "Ketika hendak menyeberangi trotoar atau bahu jalan untuk keluar/masuk garasi pelanggan atau kantor, Anda wajib menghentikan kendaraan sejenak sebelum masuk trotoar meskipun tidak ada pejalan kaki."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('路線バス', 'ろせんバス', 'bus umum')}の{kotoba('保護', 'ほご', 'perlindungan')}",
        "id": "・Melindungi Bus Umum"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('道路', 'どうろ', 'jalan')}には{kotoba('多く', 'おおく', 'banyak')}の{kotoba('路線バス', 'ろせんバス', 'bus umum')}が{kotoba('走って', 'はしって', 'melaju')}います。{kotoba('路線バス', 'ろせんバス', 'bus umum')}は、{kotoba('道路上', 'どうろじょう', 'di jalan')}の{kotoba('停留所', 'ていりゅうじょ', 'halte')}で{kotoba('合図', 'あいず', 'sinyal')}を{kotoba('出して', 'だして', 'mengeluarkan')}、{kotoba('停車する', 'ていしゃする', 'berhenti')}ことがよくあります。バスには{kotoba('多く', 'おおく', 'banyak')}のお{kotoba('客さん', 'きゃくさん', 'penumpang')}が{kotoba('乗って', 'のって', 'naik')}いますので、バスの{kotoba('安全', 'あんぜん', 'keselamatan')}にも{kotoba('十分', 'じゅうぶん', 'cukup')}な{kotoba('配慮', 'はいりょ', 'perhatian')}が{kotoba('必要', 'ひつよう', 'perlu')}です。{kotoba('路線バス', 'ろせんバス', 'bus umum')}が{kotoba('停留所', 'ていりゅうじょ', 'halte')}から{kotoba('発進する', 'はっしんする', 'berangkat')}ため{kotoba('合図', 'あいず', 'sinyal')}をしたときは、{kotoba('急', 'きゅう', 'mendadak')}ブレーキなどで{kotoba('避ける', 'さける', 'menghindari')}こととなる{kotoba('場合', 'ばあい', 'kasus')}を{kotoba('除いて', 'のぞいて', 'kecuali')}、バスに{kotoba('進路', 'しんろ', 'jalur')}を{kotoba('譲り', 'ゆずり', 'mengalah/memberikan')}、バスの{kotoba('発進', 'はっしん', 'keberangkatan')}を{kotoba('妨げない', 'さまたげない', 'tidak menghalangi')}ようにします。",
        "id": "Ada banyak bus umum yang melintas di jalan raya. Bus umum sering memberi tanda untuk berhenti di halte jalan. Karena bus mengangkut banyak penumpang, Anda harus sangat memperhatikan keselamatan mereka. Saat bus umum di halte menyalakan sinyal (lampu sein) untuk kembali melaju, berikanlah jalur kepada bus tersebut dan jangan halangi bus berangkat, kecuali jika Anda terpaksa melakukan rem mendadak untuk menghindarinya."
    },

    # --- 4.8 緊急自動車の優先 ---
    {
        "is_header": True,
        "jp": f"４．８ {kotoba('緊急自動車', 'きんきゅうじどうしゃ', 'mobil darurat')}の{kotoba('優先', 'ゆうせん', 'prioritas')}",
        "id": "4.8 Prioritas Kendaraan Darurat"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('救急車', 'きゅうきゅうしゃ', 'ambulans')}などの{kotoba('緊急自動車', 'きんきゅうじどうしゃ', 'mobil darurat')}が{kotoba('接近して', 'せっきんして', 'mendekat')}きたときには、{kotoba('次', 'つぎ', 'berikut')}のような{kotoba('方法', 'ほうほう', 'cara')}で{kotoba('緊急自動車', 'きんきゅうじどうしゃ', 'mobil darurat')}に{kotoba('進路', 'しんろ', 'jalur')}を{kotoba('譲り', 'ゆずり', 'mengalah/memberi')}、その{kotoba('通行', 'つうこう', 'melintas')}を{kotoba('妨げない', 'さ文字', 'tidak menghalangi')}ようにしなければいけません。",
        "id": "Apabila kendaraan darurat seperti ambulans mendekat, Anda harus memberi jalan dan tidak menghalangi lewatnya dengan cara sebagai berikut:"
    },
    {
        "is_header": False,
        "jp": f"①{kotoba('交差点', 'こうさてん', 'persimpangan')}やその{kotoba('付近', 'ふきん', 'sekitar')}では、{kotoba('交差点', 'こうさてん', 'persimpangan')}を{kotoba('避けて', 'さけて', 'menghindari')}{kotoba('道路', 'どうろ', 'jalan')}の{kotoba('左側', 'ひだりがわ', 'sisi kiri')}に{kotoba('寄って', 'よって', 'menepi')}{kotoba('一時停止', 'いちじていし', 'berhenti sementara')}をします。",
        "id": "① Di persimpangan atau sekitarnya, hindari berhenti di persimpangan, menepilah ke sisi kiri jalan, dan berhentilah sejenak (一時停止)."
    },
    {
        "is_header": False,
        "jp": f"②{kotoba('交差点', 'こうさてん', 'persimpangan')}やその{kotoba('付近以外', 'ふきんいがい', 'selain sekitar')}の{kotoba('場所', 'ばしょ', 'tempat')}では、{kotoba('道路', 'どうろ', 'jalan')}の{kotoba('左側', 'ひだりがわ', 'sisi kiri')}に{kotoba('寄って', 'よって', 'menepi')}{kotoba('進路', 'しんろ', 'jalur')}を{kotoba('譲ります', 'ゆずります', 'memberikan')}。この{kotoba('場合', 'ばあい', 'kasus')}には{kotoba('一時停止', 'いちじていし', 'berhenti sementara')}は{kotoba('義務づけられて', 'ぎむづけられて', 'diwajibkan')}いませんが、{kotoba('状況', 'じょうきょう', 'situasi')}に{kotoba('応じて', 'おうじて', 'sesuai')}{kotoba('一時停止', 'いちじていし', 'berhenti sementara')}をして{kotoba('緊急自動車', 'きんきゅうじどうしゃ', 'mobil darurat')}の{kotoba('通行', 'つうこう', 'melintas')}を{kotoba('妨げない', 'さまたげない', 'tidak menghalangi')}ようにしましょう。",
        "id": "② Di tempat selain persimpangan dan sekitarnya, menepilah ke sisi kiri jalan dan berikanlah jalan. Pada kasus ini, Anda tidak diwajibkan untuk berhenti sejenak, namun berhentilah sejenak sesuai dengan situasi agar tidak menghalangi lewatnya kendaraan darurat."
    },
    {
        "is_header": False,
        "jp": f"③{kotoba('一方通行路', 'いっぽうつうこうろ', 'jalan satu arah')}でも{kotoba('左側', 'ひだりがわ', 'sisi kiri')}に{kotoba('寄って', 'よって', 'menepi')}{kotoba('進路', 'しんろ', 'jalur')}を{kotoba('譲る', 'ゆずる', 'memberikan')}のが{kotoba('原則', 'げんそく', 'prinsip')}ですが、{kotoba('左側', 'ひだりがわ', 'sisi kiri')}に{kotoba('寄る', 'よる', 'menepi')}とかえって{kotoba('緊急自動車', 'きんきゅうじどうしゃ', 'mobil darurat')}の{kotoba('通行', 'つうこう', 'melintas')}の{kotoba('妨げ', 'さまたげ', 'hambatan')}となるような{kotoba('場合', 'ばあい', 'kasus')}は、{kotoba('右側', 'みぎがわ', 'sisi kanan')}に{kotoba('寄って', 'よって', 'menepi')}{kotoba('進路', 'しんろ', 'jalur')}を{kotoba('譲ります', 'ゆずります', 'memberikan')}。",
        "id": "③ Meskipun berada di jalan satu arah, pada prinsipnya Anda harus menepi ke kiri dan memberi jalan. Namun, jika dengan menepi ke kiri Anda malah menghalangi jalan mobil darurat, menepilah ke sisi kanan dan beri jalan."
    },
    {
        "is_header": False,
        "jp": f"※{kotoba('緊急自動車', 'きんきゅうじどうしゃ', 'mobil darurat')}は、{kotoba('道路', 'どうろ', 'jalan')}の{kotoba('右側部分', 'みぎがわぶぶん', 'bagian sisi kanan')}にはみ{kotoba('出して', 'だして', 'keluar')}{kotoba('通行する', 'つうこうする', 'melintas')}ことができます。そのような{kotoba('場合', 'ばあい', 'kasus')}は{kotoba('対向車線側', 'たいこうしゃせんがわ', 'sisi jalur berlawanan')}を{kotoba('走行する', 'そうこうする', 'berjalan')}{kotoba('車', 'くるま', 'kendaraan')}も{kotoba('道路', 'どうろ', 'jalan')}の{kotoba('左側', 'ひだりがわ', 'sisi kiri')}に{kotoba('寄って', 'よって', 'menepi')}{kotoba('進路', 'しんろ', 'jalur')}を{kotoba('譲る', 'ゆずる', 'memberikan')}{kotoba('義務', 'ぎむ', 'kewajiban')}があります。",
        "id": "※ Mobil darurat diperbolehkan melintasi lajur bagian kanan jalan. Dalam kasus demikian, kendaraan yang melintas di jalur arah yang berlawanan juga wajib menepi ke kiri jalan dan memberikan jalan."
    },

    # --- 4.9 踏切の通行 ---
    {
        "is_header": True,
        "jp": f"４．９ {kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}の{kotoba('通行', 'つうこう', 'melintas')}",
        "id": "4.9 Melintasi Perlintasan Kereta Api"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('車体', 'しゃたい', 'bodi kendaraan')}の{kotoba('大きい', 'おおきい', 'besar')}トラックが{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}で{kotoba('列車', 'れっしゃ', 'kereta api')}と{kotoba('衝突すれば', 'しょうとつすれば', 'jika bertabrakan')}、{kotoba('多く', 'おおく', 'banyak')}の{kotoba('死傷者', 'ししょうしゃ', 'korban tewas dan luka')}を{kotoba('出す', 'だす', 'mengeluarkan')}{kotoba('重大事故', 'じゅうだいじこ', 'kecelakaan fatal')}につながりますから、より{kotoba('一層', 'いっそう', 'lebih')}の{kotoba('慎重な', 'しんちょうな', 'hati-hati')}{kotoba('運転', 'うんてん', 'mengemudi')}が{kotoba('必要', 'ひつよう', 'perlu')}です。",
        "id": "Apabila truk besar sampai menabrak kereta api di perlintasan, hal ini akan berujung pada kecelakaan fatal yang memakan banyak korban tewas dan luka. Oleh karena itu, diperlukan cara mengemudi yang lebih berhati-hati."
    },
    {
        "is_header": True,
        "jp": f"◆{kotoba('一時停止', 'いちじていし', 'berhenti sementara')}と{kotoba('安全確認', 'あんぜんかくにん', 'konfirmasi keselamatan')}",
        "id": "◆ Berhenti Sejenak dan Konfirmasi Keselamatan"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}に{kotoba('接近した', 'せっきんした', 'mendekat')}ときは{kotoba('減速', 'げんそく', 'kurang kecepatan')}し、{kotoba('停止線', 'ていしせん', 'garis henti')}があるときは{kotoba('停止線', 'ていしせん', 'garis henti')}の{kotoba('直前', 'ちょくぜん', 'tepat sebelum')}、{kotoba('停止線', 'ていしせん', 'garis henti')}がないときは{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}の{kotoba('直前', 'ちょくぜん', 'tepat sebelum')}で{kotoba('一時停止', 'いちじていし', 'berhenti sementara')}します。{kotoba('窓', 'まど', 'jendela')}を{kotoba('開ける', 'あける', 'membuka')}などして{kotoba('自分', 'じぶん', 'sendiri')}の{kotoba('目', 'め', 'mata')}と{kotoba('耳', 'みみ', 'telinga')}で{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}の{kotoba('左右', 'さゆう', 'kiri dan kanan')}の{kotoba('安全確認', 'あんぜんかくにん', 'konfirmasi keselamatan')}をします。",
        "id": "Saat mendekati perlintasan kereta, kurangi kecepatan, dan hentikan kendaraan sejenak tepat di depan garis berhenti (jika ada), atau tepat di depan perlintasan (jika tidak ada garis henti). Buka kaca jendela agar Anda dapat menggunakan mata dan telinga untuk memastikan perlintasan di sebelah kiri dan kanan aman."
    },
    {
        "is_header": False,
        "jp": f"※{kotoba('前車', 'ぜんしゃ', 'kendaraan depan')}に{kotoba('続いて', 'つづいて', 'mengikuti')}{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}を{kotoba('通過する', 'つうかする', 'lewat')}{kotoba('場合', 'ばあい', 'kasus')}でも、{kotoba('一時停止', 'いちじていし', 'berhenti sementara')}して{kotoba('安全確認', 'あんぜんかくにん', 'konfirmasi keselamatan')}をする{kotoba('必要', 'ひつよう', 'perlu')}があります。",
        "id": "※ Meskipun Anda melewati perlintasan dengan membuntuti mobil di depan Anda, Anda tetap wajib berhenti sejenak untuk memeriksa keamanan."
    },
    {
        "is_header": False,
        "jp": f"※{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}に{kotoba('信号機', 'しんごうき', 'lampu lalu lintas')}が{kotoba('設置されて', 'せっちされて', 'terpasang')}いて、{kotoba('青信号', 'あおしんごう', 'lampu hijau')}のときは{kotoba('一時停止', 'いちじていし', 'berhenti sementara')}せずに{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}を{kotoba('通過する', 'つうかする', 'lewat')}ことができますが、この{kotoba('場合', 'ばあい', 'kasus')}でも{kotoba('左右', 'さゆう', 'kiri dan kanan')}の{kotoba('安全確認', 'あんぜんかくにん', 'konfirmasi keselamatan')}はしなければいけません。",
        "id": "※ Jika perlintasan dilengkapi lampu lalu lintas dan sedang berwarna hijau, Anda bisa melintas tanpa harus berhenti sejenak. Meski demikian, Anda tetap wajib mengecek sisi kanan dan kiri terlebih dahulu."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}に{kotoba('進入してはいけない', 'しんにゅうしてはいけない', 'tidak boleh masuk')}{kotoba('場合', 'ばあい', 'kasus')}",
        "id": "・Kapan Anda DILARANG Memasuki Perlintasan Kereta Api"
    },
    {
        "is_header": False,
        "jp": f"①{kotoba('警報機', 'けいほうき', 'alarm')}が{kotoba('鳴り始めた', 'なりはじめた', 'mulai bunyi')}ときや、{kotoba('遮断機', 'しゃだんき', 'palang perlintasan')}が{kotoba('降り始めたり', 'おりはじめたり', 'mulai turun')}、{kotoba('降りている', 'おりている', 'sedang turun')}ときは、{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}に{kotoba('進入してはいけません', 'しんにゅうしてはいけません', 'tidak boleh masuk')}。",
        "id": "① Anda dilarang memasuki perlintasan saat alarm tanda kereta mulai berbunyi, atau saat palang perlintasan mulai turun atau sedang turun."
    },
    {
        "is_header": False,
        "jp": f"②{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}の{kotoba('先', 'さき', 'setelah/depan')}の{kotoba('道路', 'どうろ', 'jalan')}が{kotoba('渋滞', 'じゅうたい', 'macet')}などにより{kotoba('混雑している', 'こんざつしている', 'padat')}ときに{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}に{kotoba('進入する', 'しんにゅうする', 'masuk')}と、{kotoba('踏切内', 'ふみきりない', 'dalam perlintasan')}で{kotoba('動き', 'うごき', 'pergerakan')}がとれなくなる{kotoba('おそれ', '', 'kekhawatiran')}があります。{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}に{kotoba('進入する', 'しんにゅうする', 'masuk')}{kotoba('前', 'まえ', 'sebelum')}には、{kotoba('必ず', 'かならず', 'pasti/selalu')}{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}の{kotoba('先', 'さき', 'setelah/depan')}の{kotoba('道路状況', 'どうろじょうきょう', 'kondisi jalan')}を{kotoba('確認', 'かくにん', 'konfirmasi')}し、トラックの{kotoba('入れる', 'いれる', 'bisa masuk')}{kotoba('十分な', 'じゅうぶんな', 'cukup')}{kotoba('場所', 'ばしょ', 'tempat')}がない{kotoba('場合', 'ばあい', 'kasus')}には、{kotoba('絶対', 'ぜったい', 'mutlak')}に{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}に{kotoba('進入してはいけません', 'しんにゅうしてはいけません', 'tidak boleh masuk')}。",
        "id": "② Jika jalan di depan perlintasan sedang macet parah, memasuki perlintasan akan berisiko membuat kendaraan Anda terjebak dan tidak bisa bergerak di tengah rel kereta. Sebelum memasuki perlintasan kereta, Anda harus memeriksa keadaan jalan di depan. Apabila tidak ada ruang yang cukup agar truk Anda bisa masuk dan lewat, Anda MUTLAK DILARANG memasuki perlintasan."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}の{kotoba('通行方法', 'つうこうほうほう', 'cara lewat')}",
        "id": "・Cara Melintasi Perlintasan Kereta Api"
    },
    {
        "is_header": False,
        "jp": f"①{kotoba('踏切通行中', 'ふみきりつうかちゅう', 'saat lewat perlintasan')}のエンジンの{kotoba('停止', 'ていし', 'berhenti')}（エンスト）を{kotoba('防止する', 'ぼうしする', 'mencegah')}ために、{kotoba('踏切内', 'ふみきりない', 'dalam perlintasan')}では、{kotoba('変速せず', 'へんそくせず', 'tanpa oper gigi')}{kotoba('発進した', 'はっしんした', 'telah melaju')}ときの{kotoba('低速', 'ていそく', 'gigi rendah')}ギアのままで{kotoba('通過', 'つうか', 'melewati')}します。",
        "id": "① Untuk mencegah terjadinya mati mesin di tengah perlintasan, jangan pindah gigi saat berada di dalam perlintasan kereta. Terus melaju dengan gigi rendah yang Anda pakai saat mulai jalan."
    },
    {
        "is_header": False,
        "jp": f"②{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}や{kotoba('自転車', 'じてんしゃ', 'sepeda')}、{kotoba('対向車', 'たいこうしゃ', 'kendaraan dari depan')}に{kotoba('注意', 'ちゅうい', 'perhatian')}しながら、{kotoba('落輪しない', 'らくりんしない', 'roda tidak jatuh')}ようやや{kotoba('中央寄り', 'ちゅうおうより', 'agak ke tengah')}を{kotoba('走行', 'そうこう', 'berjalan/melaju')}します。",
        "id": "② Tetap waspada terhadap pejalan kaki, sepeda, dan kendaraan yang melaju dari arah berlawanan, lalu melajulah agak ke tengah perlintasan agar roda kendaraan tidak terperosok."
    },
    {
        "is_header": True,
        "jp": f"【{kotoba('踏切内', 'ふみきりない', 'dalam perlintasan')}で{kotoba('動き', 'うごき', 'pergerakan')}がとれなくなったときの{kotoba('措置', 'そち', 'tindakan')}】",
        "id": "[Tindakan Apabila Kendaraan Terjebak dan Tidak Bisa Bergerak di Tengah Perlintasan]"
    },
    {
        "is_header": False,
        "jp": f"①{kotoba('警報機', 'けいほうき', 'alarm')}のある{kotoba('踏切', 'ふみきり', 'perlintasan kereta api')}では、{kotoba('警報機', 'けいほうき', 'alarm')}の{kotoba('柱', 'はしら', 'tiang')}などに{kotoba('取り付けて', 'とりつけて', 'terpasang')}ある{kotoba('非常', 'ひじょう', 'darurat')}を{kotoba('知らせる', 'しらせる', 'memberi tahu')}ボタンを{kotoba('使います', 'つかいます', 'menggunakan')}。",
        "id": "① Jika perlintasan dilengkapi alarm, gunakanlah tombol darurat yang terpasang di tiang alarm."
    },
    {
        "is_header": False,
        "jp": f"②{kotoba('非常', 'ひじょう', 'darurat')}を{kotoba('知らせる', 'しらせる', 'memberi tahu')}ボタンがない{kotoba('場合', 'ばあい', 'kasus')}には、{kotoba('車', 'くるま', 'kendaraan')}に{kotoba('備えている', 'そなえている', 'menyediakan')}{kotoba('発炎筒', 'はつえんとう', 'suar/flare')}などを{kotoba('使用して', 'しようして', 'menggunakan')}、できるだけ{kotoba('早く', 'はやく', 'cepat')}{kotoba('列車', 'れっしゃ', 'kereta api')}にわかるように{kotoba('合図', 'あいず', 'sinyal')}をします。",
        "id": "② Jika tidak ada tombol darurat, gunakan alat sinyal seperti flare/suar yang disediakan di dalam kendaraan untuk memberi sinyal pada kereta api secepatnya."
    },
    {
        "is_header": False,
        "jp": f"③{kotoba('発炎筒', 'はつえんとう', 'suar/flare')}がなかったり{kotoba('使い切って', 'つかいきって', 'telah habis')}{kotoba('しまっている', '', 'kondisi')}ときは、{kotoba('煙', 'けむり', 'asap')}の{kotoba('出やすい', 'でやすい', 'mudah keluar')}ものを{kotoba('燃やす', 'もやす', 'membakar')}などして{kotoba('列車', 'れっしゃ', 'kereta api')}に{kotoba('合図', 'あいず', 'sinyal')}をします。",
        "id": "③ Jika flare tidak tersedia atau sudah habis, bakarlah sesuatu yang dapat mengeluarkan banyak asap sebagai sinyal peringatan kepada kereta api."
    },

    # --- 4.10 高速道路の走行 ---
    {
        "is_header": True,
        "jp": f"４．１０ {kotoba('高速道路', 'こうそくどうろ', 'jalan tol')}の{kotoba('走行', 'そうこう', 'berjalan/melaju')}",
        "id": "4.10 Berkendara di Jalan Tol"
    },
    {
        "is_header": True,
        "jp": f"◆{kotoba('車', 'くるま', 'kendaraan')}の{kotoba('点検', 'てんけん', 'inspeksi/pemeriksaan')}",
        "id": "◆ Pemeriksaan (Inspeksi) Kendaraan"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('高速道路', 'こうそくどうろ', 'jalan tol')}を{kotoba('通行する', 'つうこうする', 'melintas')}{kotoba('場合', 'ばあい', 'kasus')}は、{kotoba('燃料', 'ねんりょう', 'bahan bakar')}、{kotoba('冷却水', 'れいきゃくすい', 'air pendingin')}、エンジンオイルの{kotoba('不足', 'ふそく', 'kekurangan')}により、{kotoba('停止する', 'ていしする', 'berhenti')}ことのないよう、とくに{kotoba('次', 'つぎ', 'berikut')}の{kotoba('点検', 'てんけん', 'inspeksi/pemeriksaan')}をする{kotoba('必要', 'ひつよう', 'perlu')}があります。",
        "id": "Saat akan melalui jalan tol, Anda wajib melakukan pemeriksaan pada hal-hal berikut agar kendaraan tidak tiba-tiba berhenti karena kehabisan bahan bakar, air pendingin radiator, maupun oli mesin."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('燃料', 'ねんりょう', 'bahan bakar')}の{kotoba('量', 'りょう', 'jumlah')}が{kotoba('十分', 'じゅうぶん', 'cukup')}であるか。",
        "id": "・Apakah jumlah bahan bakar cukup?"
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('冷却水', 'れいきゃくすい', 'air pendingin')}の{kotoba('量', 'りょう', 'jumlah')}が{kotoba('規定', 'きてい', 'standar/ketentuan')}の{kotoba('範囲内', 'はんいない', 'dalam batas')}にあるか。",
        "id": "・Apakah volume air pendingin ada pada batas yang ditentukan?"
    },
    {
        "is_header": False,
        "jp": f"・ラジエータキャップが{kotoba('確実', 'かくじつ', 'pasti/kuat')}に{kotoba('締まっている', 'しまっている', 'kencang')}か。",
        "id": "・Apakah tutup radiator terpasang kencang?"
    },
    {
        "is_header": False,
        "jp": f"・エンジンオイルの{kotoba('量', 'りょう', 'jumlah')}が{kotoba('適当', 'てきとう', 'sesuai/cukup')}であるか。",
        "id": "・Apakah jumlah oli mesin sudah memadai?"
    },
    {
        "is_header": False,
        "jp": f"・ファンベルトの{kotoba('張り具合', 'はりぐあい', 'tingkat kekencangan')}が{kotoba('適当', 'てきとう', 'sesuai/cukup')}であるか、また、{kotoba('損傷', 'そんしょう', 'kerusakan')}がないか。",
        "id": "・Apakah tingkat ketegangan V-belt/fan belt pas dan tidak ada kerusakan padanya?"
    },
    {
        "is_header": False,
        "jp": f"・タイヤの{kotoba('空気圧', 'くうきあつ', 'tekanan angin')}が{kotoba('適当', 'てきとう', 'sesuai/cukup')}であるか。",
        "id": "・Apakah tekanan angin ban sudah pas?"
    },
    {
        "is_header": False,
        "jp": f"・タイヤの{kotoba('溝', 'みぞ', 'alur/kembangan')}の{kotoba('深さ', 'ふかさ', 'kedalaman')}が{kotoba('十分', 'じゅうぶん', 'cukup')}であるか。",
        "id": "・Apakah alur (kembangan) ban masih cukup dalam?"
    },
    {
        "is_header": True,
        "jp": f"▶{kotoba('積荷', 'つみに', 'muatan barang')}の{kotoba('点検', 'てんけん', 'inspeksi/pemeriksaan')}",
        "id": "▶ Pemeriksaan Barang Muatan"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('高速走行', 'こうそくそうこう', 'berjalan kecepatan tinggi')}で{kotoba('荷物', 'にもつ', 'barang')}を{kotoba('落として', 'おとして', 'menjatuhkan')}しまうとたいへん{kotoba('危険', 'きけん', 'bahaya')}です。{kotoba('高速道路', 'こうそくどうろ', 'jalan tol')}を{kotoba('通行する', 'つうこうする', 'melintas')}ときは、{kotoba('前もって', 'まえもって', 'sebelumnya')}{kotoba('荷物', 'にもつ', 'barang')}が{kotoba('落ちたり', 'おちたり', 'jatuh')}{kotoba('飛んだり', 'とんだり', 'terbang')}しないように{kotoba('点検', 'ていけん', 'inspeksi/pemeriksaan')}し、{kotoba('荷物', 'にもつ', 'barang')}を{kotoba('積み直す', 'つみなおす', 'memuat ulang')}など{kotoba('必要な', 'ひつような', 'perlu')}{kotoba('措置', 'そち', 'tindakan')}をとらなければいけません。",
        "id": "Akan sangat berbahaya jika muatan sampai jatuh ke jalan saat melaju dalam kecepatan tinggi. Sebelum melintasi jalan tol, Anda wajib mengecek apakah muatan berisiko jatuh atau terbang. Jika ada, lakukan tindakan perbaikan seperti memuatnya ulang."
    },
    {
        "is_header": True,
        "jp": f"◆{kotoba('通行区分', 'つうこうくぶん', 'jalur kendaraan')}の{kotoba('遵守', 'じゅんしゅ', 'kepatuhan')}",
        "id": "◆ Mematuhi Aturan Lajur Kendaraan"
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('一番', 'いちばん', 'paling')}{kotoba('右側', 'みぎがわ', 'sisi kanan')}の{kotoba('車通行帯', 'しゃつうこうたい', 'jalur kendaraan')}（{kotoba('追越車線', 'おいこししゃせん', 'jalur menyalip')}）は{kotoba('追越し', 'おいこし', 'menyalip')}のために{kotoba('空けて', 'あけて', 'mengosongkan')}おき、{kotoba('走行車線', 'そうこうしゃせん', 'jalur mengemudi')}のやや{kotoba('左側', 'ひだりがわ', 'sisi kiri')}を{kotoba('走行', 'そうこう', 'berjalan/melaju')}します。",
        "id": "・Kosongkan lajur kendaraan yang paling kanan (lajur untuk mendahului), dan berkendaralah agak ke kiri di dalam lajur yang semestinya."
    },
    {
        "is_header": False,
        "jp": f"・トレーラは、{kotoba('高速自動車国道', 'こうそくじどうしゃこくどう', 'jalan tol nasional')}においては、{kotoba('標識', 'ひょうしき', 'rambu')}などで{kotoba('車線', 'しゃせん', 'jalur')}が{kotoba('指定されて', 'していされて', 'ditentukan')}いる{kotoba('場合', 'ばあい', 'kasus')}などを{kotoba('除いて', 'のぞいて', 'kecuali')}、{kotoba('一番', 'いちばん', 'paling')}{kotoba('左側', 'ひだりがわ', 'sisi kiri')}の{kotoba('車線', 'しゃせん', 'jalur')}を{kotoba('走行', 'そうこう', 'berjalan/melaju')}します。",
        "id": "・Di jalan tol nasional, truk trailer wajib melaju di lajur paling kiri, kecuali jika ada ketentuan jalur tertentu yang ditetapkan oleh rambu lalu lintas."
    },
    {
        "is_header": False,
        "jp": f"・トレーラは、{kotoba('自動車専用道路', 'じどうしゃせんようどうろ', 'jalan khusus mobil')}においては、{kotoba('標識', 'ひょうしき', 'rambu')}などで{kotoba('指定された', 'していされた', 'ditentukan')}{kotoba('区間', 'くかん', 'area/bagian')}については、{kotoba('一番', 'いちばん', 'paling')}{kotoba('左側', 'ひだりがわ', 'sisi kiri')}の{kotoba('車線', 'しゃせん', 'jalur')}を{kotoba('走行', 'そうこう', 'berjalan/melaju')}します。",
        "id": "・Di jalan tol khusus kendaraan, truk trailer juga wajib melaju di lajur paling kiri pada area-area yang ditetapkan oleh rambu lalu lintas."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('路肩', 'ろかた', 'bahu jalan')}や{kotoba('路側帯', 'ろそくたい', 'pinggir jalan')}を{kotoba('走行してはいけません', 'そうこうしてはいけません', 'tidak boleh berjalan')}。",
        "id": "・Dilarang berkendara di pinggir jalan/trotoar atau di bahu jalan."
    }
# Data lanjutan materi (Bab 4.11 - 7.2)
    {
        "is_header": True,
        "jp": f"4.11 {kotoba('坂道', 'さかみち', 'jalan tanjakan/turunan')}・カーブ・トンネルの{kotoba('走行', 'そうこう', 'berjalan/melaju')}",
        "id": "4.11 Berkendara di Jalan Tanjakan/Turunan, Tikungan, dan Terowongan"
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('坂道', 'さかみち', 'jalan tanjakan/turunan')}では{kotoba('上り', 'のぼり', 'menanjak')}の{kotoba('車', 'くるま', 'kendaraan')}が{kotoba('優先', 'ゆうせん', 'prioritas')}",
        "id": "・Di Jalan Menanjak, Kendaraan yang Menanjak Didahulukan"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('坂道', 'さかみち', 'jalan tanjakan/turunan')}では、{kotoba('上り坂', 'のぼりざか', 'tanjakan')}での{kotoba('発進', 'はっしん', 'melaju')}がむずかしいため、{kotoba('狭い', 'せまい', 'sempit')}{kotoba('道', 'みち', 'jalan')}では、{kotoba('下り', 'くだり', 'turunan')}の{kotoba('車', 'くるま', 'kendaraan')}が、{kotoba('上り', 'のぼり', 'menanjak')}の{kotoba('車', 'くるま', 'kendaraan')}に{kotoba('道', 'みち', 'jalan')}を{kotoba('譲りましょう', 'ゆずりましょう', 'mari berikan')}。ただし、{kotoba('近く', 'ちかく', 'dekat')}に{kotoba('待避所', 'たいひしょ', 'tempat menepi')}があるときは、{kotoba('上り', 'のぼり', 'menanjak')}の{kotoba('車', 'くるま', 'kendaraan')}でも、その{kotoba('待避所', 'たいひしょ', 'tempat menepi')}に{kotoba('入って', 'はいって', 'masuk')}{kotoba('待ちましょう', 'まちましょう', 'mari tunggu')}。",
        "id": "Karena sulit untuk melajukan kendaraan yang berhenti di tanjakan, di jalan yang sempit, kendaraan yang sedang menuruni jalan harus mengalah dan memberi jalan pada kendaraan yang sedang menanjak. Namun, jika ada tempat untuk menepi (shelter) di dekatnya, kendaraan yang menanjak pun sebaiknya masuk ke sana dan menunggu kendaraan dari atas turun."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('下り坂', 'くだりざか', 'turunan')}はブレーキが{kotoba('効かなくなる', 'きかなくなる', 'tidak berfungsi')}「フェード{kotoba('現象', 'げんしょう', 'fenomena')}」に{kotoba('注意', 'ちゅうい', 'perhatian')}",
        "id": "・Waspada Fenomena \"Fade\" Saat Menurun di Mana Rem Tidak Berfungsi"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('長い', 'ながい', 'panjang')}{kotoba('下り坂', 'くだりざか', 'turunan')}で、フットブレーキを{kotoba('使い過ぎる', 'つかいすぎる', 'terlalu sering pakai')}と、ブレーキライニングが{kotoba('過熱して', 'かねつして', 'terlalu panas')}{kotoba('摩擦力', 'まさつりょく', 'gaya gesek')}が{kotoba('低下し', 'ていかし', 'menurun')}、ブレーキがきかなくなることがあります。これを「フェード{kotoba('現象', 'げんしょう', 'fenomena')}」と{kotoba('いいます', '', 'disebut')}。{kotoba('下り坂', 'くだりざか', 'turunan')}でこの{kotoba('現象', 'げんしょう', 'fenomena')}が{kotoba('発生する', 'はっせいする', 'terjadi')}と、{kotoba('速度', 'そくど', 'kecepatan')}をコントロールすることができず、たいへん{kotoba('危険な', 'きけんな', 'berbahaya')}{kotoba('状態', 'じょうたい', 'kondisi')}になります。",
        "id": "Jika Anda terlalu sering menggunakan rem kaki di jalan turunan yang panjang, kampas rem akan terlalu panas, gaya gesek menurun, dan rem bisa tidak berfungsi. Hal ini disebut \"Fenomena Fade\" (*Fade Phenomenon*). Jika fenomena ini terjadi di jalan turunan, Anda tidak akan bisa mengontrol kecepatan kendaraan dan berujung pada kondisi yang sangat berbahaya."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('長い', 'ながい', 'panjang')}{kotoba('下り坂', 'くだりざか', 'turunan')}を{kotoba('走行する', 'そうこうする', 'berjalan')}ときは、{kotoba('低速', 'ていそく', 'rendah')}ギアによるエンジンブレーキや{kotoba('排気', 'はいき', 'gas buang')}ブレーキなどを{kotoba('活用し', 'かつようし', 'memanfaatkan')}、フットブレーキの{kotoba('使用', 'しよう', 'penggunaan')}は{kotoba('少なく', 'すくなく', 'sedikit')}しましょう。また、ギア{kotoba('抜け', 'ぬけ', 'lepas')}などが{kotoba('起こった', 'おこった', 'terjadi')}{kotoba('場合', 'ばあい', 'kasus')}は、{kotoba('ただちに', '', 'segera')}フットブレーキを{kotoba('用いて', 'もちいて', 'menggunakan')}トラックを{kotoba('十分', 'じゅうぶん', 'cukup')}に{kotoba('減速', 'げんそく', 'kurang kecepatan')}または{kotoba('停車', 'ていしゃ', 'berhenti')}させましょう。",
        "id": "Saat melaju di turunan panjang, manfaatkanlah rem mesin (*engine brake*) dengan gigi rendah atau rem gas buang (*exhaust brake*), dan kurangi pemakaian rem kaki. Selain itu, jika terjadi gigi persneling terlepas atau semacamnya, segera gunakan rem kaki untuk mengurangi kecepatan truk atau memberhentikannya."
    },
    {
        "is_header": True,
        "jp": f"◆カーブの{kotoba('手前', 'てまえ', 'sebelum')}で{kotoba('十分', 'じゅうぶん', 'cukup')}に{kotoba('減速する', 'げんそくする', 'mengurangi kecepatan')}",
        "id": "◆ Mengurangi Kecepatan Secukupnya Sebelum Tikungan (Kurva)"
    },
    {
        "is_header": False,
        "jp": f"カーブで{kotoba('速度', 'そくど', 'kecepatan')}を{kotoba('出し過ぎる', 'だしすぎる', 'terlalu cepat')}と、スリップしてカーブを{kotoba('曲がり切れずに', 'まがりきれずに', 'tidak habis berbelok')}{kotoba('道路外', 'どうろがい', 'luar jalan')}に{kotoba('飛び出したり', 'とびだしたり', 'melompat keluar')}、{kotoba('横転する', 'おうてんする', 'terguling')}{kotoba('危険', 'きけん', 'bahaya')}があります。とくにハンドルを{kotoba('切りながら', 'きりながら', 'sambil memutar')}ブレーキをかけると{kotoba('横転しやすくなります', 'おうてんしやすくなります', 'mudah terguling')}から、カーブの{kotoba('手前', 'てまえ', 'sebelum')}で{kotoba('十分', 'じゅうぶん', 'cukup')}に{kotoba('減速して', 'げんそくして', 'mengurangi kecepatan')}おきます。",
        "id": "Jika Anda melaju terlalu cepat di tikungan, ban bisa selip sehingga kendaraan tidak bisa berbelok penuh dan terlempar ke luar jalan, atau ada bahaya kendaraan terguling. Khususnya jika Anda mengerem sambil memutar setir, kendaraan akan lebih mudah terguling, jadi turunkanlah kecepatan secukupnya sebelum tikungan."
    },
    {
        "is_header": False,
        "jp": f"また、ハンドルを{kotoba('切り返す', 'きりかえす', 'memutar balik')}S{kotoba('字', 'じ', 'huruf')}カーブは{kotoba('横転しやすくなります', 'おうてんしやすくなります', 'mudah terguling')}から、ハンドル{kotoba('操作', 'そうさ', 'operasi')}などを{kotoba('慎重に', 'しんちょうに', 'hati-hati')}{kotoba('行う', 'おこなう', 'melakukan')}{kotoba('必要', 'ひつよう', 'perlu')}があります。",
        "id": "Selain itu, tikungan berbentuk huruf S yang mengharuskan memutar balik setir sangat rentan membuat kendaraan terguling, sehingga Anda harus mengoperasikan setir dengan sangat hati-hati."
    },
    {
        "is_header": True,
        "jp": f"◆トンネルでの{kotoba('事故', 'じこ', 'kecelakaan')}は{kotoba('重大事故', 'じゅうだいじこ', 'kecelakaan fatal')}につながる",
        "id": "◆ Kecelakaan di Dalam Terowongan Akan Berakibat Fatal"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('高速道路', 'こうそくどうろ', 'jalan tol')}のトンネル{kotoba('内', 'ない', 'dalam')}で{kotoba('事故', 'じこ', 'kecelakaan')}が{kotoba('発生すれば', 'はっせいすれば', 'jika terjadi')}、{kotoba('多く', 'おおく', 'banyak')}の{kotoba('車', 'くるま', 'kendaraan')}が{kotoba('巻き込まれる', 'まきこまれる', 'terlibat')}{kotoba('事故', 'じこ', 'kecelakaan')}につながりますから、{kotoba('次', 'つぎ', 'berikut')}のことを{kotoba('守り', 'まもり', 'mematuhi')}、{kotoba('慎重な', 'しんちょうな', 'hati-hati')}{kotoba('運転', 'うんてん', 'mengemudi')}を{kotoba('行いましょう', 'おこないましょう', 'mari lakukan')}。",
        "id": "Jika terjadi kecelakaan di dalam terowongan jalan tol, banyak kendaraan lain akan terlibat. Oleh karena itu, patuhilah hal-hal berikut dan berkendaralah dengan hati-hati."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('高速', 'こうそく', 'kecepatan tinggi')}でトンネルに{kotoba('入る', 'はいる', 'masuk')}と{kotoba('視力', 'しりょく', 'penglihatan')}が{kotoba('急激に', 'きゅうげきに', 'drastis')}{kotoba('低下します', 'ていかします', 'menurun')}。また、トンネルの{kotoba('手前', 'てまえ', 'sebelum')}で{kotoba('前車', 'ぜんしゃ', 'kendaraan depan')}が{kotoba('減速する', 'げんそくする', 'mengurangi kecepatan')}ことがありますから、{kotoba('あらかじめ', '', 'sebelumnya')}{kotoba('手前', 'てまえ', 'sebelum')}で{kotoba('速度', 'そくど', 'kecepatan')}を{kotoba('落として', 'おとして', 'menurunkan')}おくこと。",
        "id": "・Masuk ke terowongan dengan kecepatan tinggi akan membuat daya penglihatan menurun drastis. Selain itu, kendaraan di depan mungkin melambat sebelum terowongan, jadi turunkan kecepatan kendaraan Anda sebelumnya."
    },
    {
        "is_header": False,
        "jp": f"・トンネル{kotoba('内', 'ない', 'dalam')}で{kotoba('渋滞', 'じゅうたい', 'macet')}が{kotoba('発生して', 'はっせいして', 'terjadi')}いることがあります。トンネルに{kotoba('入る', 'はいる', 'masuk')}{kotoba('前', 'まえ', 'sebelum')}に{kotoba('情報板', 'じょうほうばん', 'papan informasi')}などで{kotoba('交通状況', 'こうつうじょうきょう', 'kondisi lalin')}の{kotoba('把握', 'はあく', 'memahami')}に{kotoba('努める', 'つとめる', 'berusaha')}こと。",
        "id": "・Kemacetan terkadang terjadi di dalam terowongan. Sebelum masuk, berusahalah mengetahui kondisi lalu lintas melalui papan informasi, dll."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('信号機', 'しんごうき', 'lampu lalu lintas')}のあるトンネルでは、{kotoba('必ず', 'かならず', 'selalu/pasti')}{kotoba('信号', 'しんごう', 'lampu lalin')}に{kotoba('従います', 'したがいます', 'patuh')}。",
        "id": "・Di terowongan yang ada lampu lalu lintasnya, Anda wajib mematuhi lampu tersebut."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('照明設備', 'しょうめいせつび', 'fasilitas penerangan')}のあるトンネルでもヘッドライトを{kotoba('点灯します', 'てんとうします', 'menyalakan')}。",
        "id": "・Meski terowongan memiliki penerangan, nyalakan selalu lampu utama (headlight)."
    },
    {
        "is_header": False,
        "jp": f"・トンネルの{kotoba('入口', 'いりぐち', 'pintu masuk')}と{kotoba('出口', 'でぐち', 'pintu keluar')}では{kotoba('天候', 'てんこう', 'cuaca')}が{kotoba('変わっている', 'かわっている', 'berubah')}ことがあります。{kotoba('出口', 'でぐち', 'pintu keluar')}に{kotoba('接近した', 'せっきんした', 'mendekat')}ときは{kotoba('天候', 'てんこう', 'cuaca')}や{kotoba('道路状況', 'どうろじょうきょう', 'kondisi jalan')}によく{kotoba('注意', 'ちゅうい', 'perhatian')}しましょう。",
        "id": "・Cuaca di pintu masuk dan pintu keluar terowongan bisa saja berbeda. Saat mendekati pintu keluar, perhatikan cuaca dan kondisi jalan dengan saksama."
    },
    {
        "is_header": True,
        "jp": f"4.12 {kotoba('信号', 'しんごう', 'lampu lalu lintas')}の{kotoba('遵守', 'じゅんしゅ', 'kepatuhan')}",
        "id": "4.12 Mematuhi Lampu Lalu Lintas"
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('黄信号', 'きしんごう', 'lampu kuning')}は{kotoba('原則', 'げんそく', 'prinsipnya')}{kotoba('停止', 'ていし', 'berhenti')}",
        "id": "・Pada Prinsipnya, Lampu Kuning Berarti Berhenti"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('黄信号', 'きしんごう', 'lampu kuning')}の{kotoba('意味', 'いみ', 'arti')}は、{kotoba('停止位置', 'ていしいち', 'posisi henti')}に{kotoba('近づいている', 'ちかづいている', 'mendekati')}ために{kotoba('急停止', 'きゅうていし', 'berhenti mendadak')}になって{kotoba('後続車', 'こうぞくしゃ', 'kendaraan belakang')}に{kotoba('追突される', 'ついとつされる', 'ditabrak dr belakang')}{kotoba('おそれ', '', 'kekhawatiran')}がある{kotoba('場合', 'ばあい', 'kasus')}などを{kotoba('除いて', 'のぞいて', 'kecuali')}、{kotoba('交差点', 'こうさてん', 'persimpangan')}の{kotoba('手前', 'てまえ', 'sebelum')}で{kotoba('停止する', 'ていしする', 'berhenti')}ということです。",
        "id": "Lampu kuning berarti Anda harus berhenti sebelum persimpangan, kecuali jika Anda sudah terlalu dekat dengan garis henti sehingga mengerem mendadak berisiko membuat kendaraan Anda ditabrak dari belakang."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('信号', 'しんごう', 'lampu lalin')}が{kotoba('黄色', 'きいろ', 'kuning')}に{kotoba('変わったら', 'かわったら', 'berubah')}、{kotoba('早めに', 'はやめに', 'lebih awal')}{kotoba('減速して', 'げんそくして', 'mengurangi kecepatan')}{kotoba('交差点', 'こうさてん', 'persimpangan')}の{kotoba('手前', 'てまえ', 'sebelum')}で{kotoba('停止', 'ていし', 'berhenti')}しましょう。",
        "id": "Jika lampu lalu lintas berubah kuning, turunkanlah kecepatan lebih awal dan berhentilah sebelum persimpangan."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('赤', 'あか', 'merah')}の{kotoba('点滅信号', 'てんめつしんごう', 'lampu berkedip')}は{kotoba('一時停止', 'いちじていし', 'berhenti sementara')}",
        "id": "・Lampu Merah Berkedip Berarti Wajib Berhenti Sejenak"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('赤', 'あか', 'merah')}の{kotoba('点滅信号', 'てんめつしんごう', 'lampu berkedip')}の{kotoba('場合', 'ばあい', 'kasus')}、{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}は{kotoba('他', 'ほか', 'lain')}の{kotoba('交通', 'こうつう', 'lalu lintas')}に{kotoba('注意して', 'ちゅういして', 'memperhatikan')}{kotoba('進行する', 'しんこうする', 'maju')}ことができますが、{kotoba('車', 'くるま', 'kendaraan')}は{kotoba('停止位置', 'ていしいち', 'posisi henti')}で{kotoba('一時停止', 'いちじていし', 'berhenti sementara')}し、{kotoba('安全', 'あんぜん', 'aman')}を{kotoba('確認した', 'かくにんした', 'memastikan')}{kotoba('後', 'あと', 'setelah')}でなければ{kotoba('進行', 'しんこう', 'maju')}できません。",
        "id": "Pada lampu merah yang berkedip, pejalan kaki boleh terus berjalan dengan memperhatikan lalu lintas lain, tetapi kendaraan bermotor wajib berhenti sejenak di posisi henti, dan baru boleh melaju setelah memastikan keadaan aman."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('黄', 'き', 'kuning')}の{kotoba('点滅信号', 'てんめつしんごう', 'lampu berkedip')}は、{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}も{kotoba('車', 'くるま', 'kendaraan')}も{kotoba('他', 'ほか', 'lain')}の{kotoba('交通', 'こうつう', 'lalu lintas')}に{kotoba('注意して', 'ちゅういして', 'memperhatikan')}{kotoba('進行する', 'しんこうする', 'maju')}ことができます。",
        "id": "Pada lampu kuning yang berkedip, baik pejalan kaki maupun kendaraan dapat terus melaju sambil memperhatikan lalu lintas lain."
    },
    {
        "is_header": True,
        "jp": f"▶{kotoba('右折矢印信号', 'うせつやじるししんごう', 'lampu panah kanan')}",
        "id": "▶ Lampu Tanda Panah Belok Kanan"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('対面する', 'たいめんする', 'berhadapan')}{kotoba('信号', 'しんごう', 'lampu lalin')}が{kotoba('赤', 'あか', 'merah')}でも、その{kotoba('下', 'した', 'bawah')}に{kotoba('青色', 'あおいろ', 'biru')}の{kotoba('灯火', 'とうか', 'lampu')}の{kotoba('右折矢印信号', 'うせつやじるししんごう', 'lampu panah kanan')}が{kotoba('表示された', 'ひょうじされた', 'ditampilkan')}ときは、{kotoba('右折', 'うせつ', 'belok kanan')}や{kotoba('転回', 'てんかい', 'putar balik')}をすることができます。{kotoba('右折矢印信号', 'うせつやじるししんごう', 'lampu panah kanan')}が{kotoba('表示されて', 'ひょうじされて', 'ditampilkan')}{kotoba('右折していく', 'うせつしていく', 'belok kanan')}ときは、{kotoba('交差点', 'こうさてん', 'persimpangan')}に{kotoba('進入してくる', 'しんにゅうしてくる', 'masuk')}{kotoba('対向車', 'たいこうしゃ', 'kendaraan dari depan')}がいないかどうかを{kotoba('確認', 'かくにん', 'konfirmasi')}しましょう。<br>※{kotoba('転回禁止', 'てんかいきんし', 'dilarang putar balik')}の{kotoba('標識', 'ひょうしき', 'rambu')}や{kotoba('標示', 'ひょうじ', 'marka')}のある{kotoba('交差点', 'こうさてん', 'persimpangan')}では、{kotoba('転回', 'てんかい', 'putar balik')}をすることはできません。",
        "id": "Meskipun lampu lalu lintas utama di depan Anda berwarna merah, jika di bawahnya menyala lampu panah warna hijau/biru yang menunjuk ke kanan, Anda diperbolehkan berbelok ke kanan atau putar balik (U-turn). Saat berbelok kanan dengan panduan lampu panah ini, pastikan tidak ada kendaraan dari arah berlawanan yang memasuki persimpangan.<br>※ Di persimpangan yang terdapat rambu atau marka \"dilarang putar balik\", Anda tidak diperbolehkan untuk putar balik meskipun lampu menyala."
    },
    {
        "is_header": True,
        "jp": f"4.13 {kotoba('道路標識', 'どうろひょうしき', 'rambu jalan')}・{kotoba('道路標示', 'どうろひょうじ', 'marka jalan')}の{kotoba('遵守', 'じゅんしゅ', 'kepatuhan')}",
        "id": "4.13 Mematuhi Rambu Jalan dan Marka Jalan"
    },
    {
        "is_header": True,
        "jp": f"◆{kotoba('道路標識', 'どうろひょうしき', 'rambu jalan')}と{kotoba('道路標示', 'どうろひょうじ', 'marka jalan')}",
        "id": "◆ Rambu Jalan dan Marka Jalan"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('道路標識', 'どうろひょうしき', 'rambu jalan')}とは、{kotoba('交通規制', 'こうつうきせい', 'aturan lalu lintas')}などを{kotoba('示す', 'しめす', 'menunjukkan')}{kotoba('標示板', 'ひょうじばん', 'papan tanda')}のことです。{kotoba('道路標示', 'どうろひょうじ', 'marka jalan')}とは、ペイントや{kotoba('道路鋲', 'どうろびょう', 'paku jalan')}などで{kotoba('路面', 'ろめん', 'permukaan jalan')}に{kotoba('描かれた', 'えがかれた', 'digambar')}{kotoba('線', 'せん', 'garis')}や{kotoba('記号', 'きごう', 'simbol')}、{kotoba('文字', 'もじ', 'huruf')}などをいい、{kotoba('規制標示', 'きせいひょうじ', 'marka aturan')}と{kotoba('指示標示', 'しじひょうじ', 'marka petunjuk')}があります。",
        "id": "Rambu jalan adalah papan penanda yang menunjukkan pengaturan/aturan lalu lintas dan semacamnya. Marka jalan adalah garis, simbol, atau huruf yang digambar di atas permukaan jalan menggunakan cat atau paku jalan, dan mencakup marka pengaturan (regulasi) serta marka petunjuk (instruksi)."
    },
    {
        "is_header": True,
        "jp": f"◆{kotoba('道路標識', 'どうろひょうしき', 'rambu jalan')}や{kotoba('道路標示', 'どうろひょうじ', 'marka jalan')}は{kotoba('運転', 'うんてん', 'mengemudi')}にとって{kotoba('重要な', 'じゅうような', 'penting')}{kotoba('情報源', 'じょうほうげん', 'sumber informasi')}",
        "id": "◆ Rambu Jalan dan Marka Jalan adalah Sumber Informasi Penting untuk Mengemudi"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('一般道路', 'いっぱんどうろ', 'jalan umum')}における{kotoba('自動車', 'じどうしゃ', 'mobil')}の{kotoba('法定最高速度', 'ほうていさいこうそくど', 'batas kecepatan hukum')}は{kotoba('時速', 'じそく', 'kecepatan per jam')}60キロですが、{kotoba('速度規制標識', 'そくどきせいひょうしき', 'rambu batas kecepatan')}や{kotoba('標示', 'ひょうじ', 'marka')}によって、{kotoba('時速', 'じそく', 'kecepatan per jam')}40キロや30キロに{kotoba('制限されている', 'せいげんされている', 'dibatasi')}{kotoba('道路', 'どうろ', 'jalan')}はたくさんあります。これは、{kotoba('時速', 'じそく', 'kecepatan per jam')}40キロや30キロで{kotoba('走行しなければ', 'そうこうしなければ', 'jika tidak berjalan')}{kotoba('危険', 'きけん', 'bahaya')}であるということを{kotoba('伝えている', 'つたえている', 'menyampaikan')}のです。",
        "id": "Batas kecepatan maksimum resmi untuk kendaraan bermotor di jalan umum adalah 60 km/jam, tetapi banyak jalan yang dibatasi kecepatannya menjadi 40 km/jam atau 30 km/jam melalui rambu dan marka pembatas kecepatan. Hal ini menyampaikan pesan bahwa akan berbahaya jika Anda tidak melaju pada 40 km/jam atau 30 km/jam di area tersebut."
    },
    {
        "is_header": False,
        "jp": f"また、{kotoba('道路標示', 'どうろひょうじ', 'marka jalan')}によって、この{kotoba('先', 'さき', 'depan')}に{kotoba('横断歩道', 'おうだんほどう', 'zebra cross')}や{kotoba('自転車横断帯', 'じてんしゃおうだんたい', 'jalur penyeberangan sepeda')}{kotoba('等', 'など', 'dan lain-lain')}があることが{kotoba('前もって', 'まえもって', 'sebelumnya')}{kotoba('把握でき', 'はあくでき', 'bisa dipahami')}、{kotoba('速度', 'そくど', 'kecepatan')}を{kotoba('落とす', 'おとす', 'menurunkan')}などの{kotoba('安全な', 'あんぜんな', 'aman')}{kotoba('運転', 'うんてん', 'mengemudi')}ができます。このように{kotoba('道路標識', 'どうろひょうしき', 'rambu jalan')}や{kotoba('道路標示', 'どうろひょうじ', 'marka jalan')}は、{kotoba('危険', 'きけん', 'bahaya')}を{kotoba('知らせてくれる', 'しらせてくれる', 'memberitahu')}{kotoba('重要な', 'じゅうような', 'penting')}{kotoba('情報源', 'じょうほうげん', 'sumber informasi')}です。",
        "id": "Selain itu, melalui marka jalan, Anda dapat mengetahui dari awal bahwa di depan terdapat zebra cross atau jalur penyeberangan sepeda, sehingga Anda bisa berkendara dengan aman seperti dengan menurunkan kecepatan. Dengan demikian, rambu jalan dan marka jalan merupakan sumber informasi penting yang memberitahu Anda tentang adanya bahaya."
    },
    {
        "is_header": True,
        "jp": f"4.14 {kotoba('駐車', 'ちゅうしゃ', 'parkir')}・{kotoba('停車', 'ていしゃ', 'berhenti')}",
        "id": "4.14 Parkir dan Berhenti"
    },
    {
        "is_header": True,
        "jp": f"☑「{kotoba('駐車', 'ちゅうしゃ', 'parkir')}」と「{kotoba('停車', 'ていしゃ', 'berhenti')}」のちがい",
        "id": "☑ Perbedaan antara \"Parkir (Chuusha)\" dan \"Berhenti (Teisha)\""
    },
    {
        "is_header": False,
        "jp": f"{kotoba('駐車', 'ちゅうしゃ', 'parkir')}とは、{kotoba('車', 'くるま', 'kendaraan')}がしばらくの{kotoba('間', 'あいだ', 'selama')}{kotoba('停止する', 'ていしする', 'berhenti')}ことや、{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}が{kotoba('車', 'くるま', 'kendaraan')}から{kotoba('離れて', 'はなれて', 'meninggalkan')}いてすぐに{kotoba('運転できない', 'うんてんできない', 'tidak bisa mengemudi')}{kotoba('状態', 'じょうたい', 'kondisi')}で{kotoba('停止する', 'ていしする', 'berhenti')}ことを{kotoba('いいます', '', 'disebut')}。{kotoba('停車', 'ていしゃ', 'berhenti')}とは、{kotoba('短い', 'みじかい', 'singkat')}{kotoba('時間', 'じかん', 'waktu')}の{kotoba('停止', 'ていし', 'berhenti')}を{kotoba('いいます', '', 'disebut')}。{kotoba('人', 'ひと', 'orang')}の{kotoba('乗り降り', 'のりおり', 'naik turun')}や、5{kotoba('分以内', 'ふんいない', 'dalam 5 menit')}の{kotoba('荷物', 'にもつ', 'barang')}の{kotoba('積卸し', 'つみおろし', 'bongkar muat')}のための{kotoba('停止', 'ていし', 'berhenti')}は、{kotoba('駐車', 'ちゅうしゃ', 'parkir')}ではなく{kotoba('停車', 'ていしゃ', 'berhenti')}になります。",
        "id": "Parkir berarti kendaraan berhenti untuk sementara waktu, atau pengemudi meninggalkan kendaraan sehingga berada dalam kondisi tidak dapat segera dikemudikan kembali. Berhenti (Teisha) adalah berhenti dalam waktu yang singkat. Berhenti untuk menaikkan/menurunkan orang atau bongkar muat barang dalam waktu kurang dari 5 menit dianggap sebagai berhenti sementara (Teisha), bukan parkir."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('駐停車', 'ちゅうていしゃ', 'parkir dan berhenti')}の{kotoba('禁止場所', 'きんしばしょ', 'tempat terlarang')}",
        "id": "・Tempat Terlarang untuk Parkir dan Berhenti"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('駐停車', 'ちゅうていしゃ', 'parkir dan berhenti')}するときには、まず{kotoba('駐車', 'ちゅうしゃ', 'parkir')}や{kotoba('停車', 'ていしゃ', 'berhenti')}の{kotoba('禁止場所', 'きんしばしょ', 'tempat terlarang')}でないかどうかを{kotoba('確認', 'かくにん', 'konfirmasi')}しなければいけません。{kotoba('駐車', 'ちゅうしゃ', 'parkir')}が{kotoba('禁止されていない', 'きんしされていない', 'tidak dilarang')}{kotoba('道路', 'どうろ', 'jalan')}でも、{kotoba('駐車する', 'ちゅうしゃする', 'parkir')}{kotoba('車', 'くるま', 'kendaraan')}の{kotoba('右側', 'みぎがわ', 'sisi kanan')}に3.5メートル{kotoba('以上', 'いじょう', 'ke atas')}の{kotoba('余地', 'よち', 'ruang sisa')}がない{kotoba('場所', 'ばしょ', 'tempat')}での{kotoba('駐車', 'ちゅうしゃ', 'parkir')}はできません。",
        "id": "Saat hendak parkir atau berhenti, pertama-tama pastikan tempat tersebut bukan area yang dilarang. Bahkan di jalan yang tidak dilarang parkir sekalipun, Anda tidak diperbolehkan parkir di area yang menyisakan ruang kurang dari 3,5 meter di sebelah kanan kendaraan yang diparkir."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('高速道路', 'こうそくどうろ', 'jalan tol')}での{kotoba('駐停車', 'ちゅうていしゃ', 'parkir dan berhenti')}",
        "id": "・Parkir dan Berhenti di Jalan Tol"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('高速道路', 'こうそくどうろ', 'jalan tol')}では、{kotoba('危険防止', 'きけんぼうし', 'mencegah bahaya')}のためや{kotoba('故障', 'こしょう', 'rusak/mogok')}など{kotoba('場合', 'ばあい', 'kasus')}を{kotoba('除いて', 'のぞいて', 'kecuali')}、{kotoba('駐停車', 'ちゅうていしゃ', 'parkir dan berhenti')}が{kotoba('禁止されて', 'きんしされて', 'dilarang')}います。",
        "id": "Di jalan tol, parkir dan berhenti dilarang, kecuali dalam kondisi mencegah bahaya, kendaraan mogok/rusak, dan semacamnya."
    },
    {
        "is_header": True,
        "jp": f"◆{kotoba('駐車時', 'ちゅうしゃじ', 'saat parkir')}には「{kotoba('輪止め', 'わどめ', 'ganjal roda')}」をする",
        "id": "◆ Gunakan \"Ganjal Roda\" Saat Parkir"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('路面', 'ろめん', 'permukaan jalan')}が{kotoba('平らな', 'たいらな', 'rata')}ように{kotoba('見えて', 'みえて', 'terlihat')}も、{kotoba('実際', 'じっさい', 'sebenarnya')}には{kotoba('傾いている', 'かたむいている', 'miring')}{kotoba('駐車場所', 'ちゅうしゃばしょ', 'tempat parkir')}が{kotoba('少なくありません', 'すくなくありません', 'tidak sedikit')}。{kotoba('駐車時', 'ちゅうしゃじ', 'saat parkir')}は、{kotoba('駐車', 'ちゅうしゃ', 'parkir')}ブレーキを{kotoba('確実', 'かくじつ', 'pasti/kuat')}にかけるとともに、{kotoba('必ず', 'かならず', 'selalu/pasti')}「{kotoba('輪止め', 'わどめ', 'ganjal roda')}」をする{kotoba('習慣', 'しゅうかん', 'kebiasaan')}をつけて、トラックが{kotoba('勝手に', 'かってに', 'sendirinya')}{kotoba('動き出す', 'うごきだす', 'mulai bergerak')}のを{kotoba('防ぎましょう', 'ふせぎましょう', 'mari cegah')}。",
        "id": "Meski permukaan jalan terlihat rata, seringkali area parkir sebenarnya dalam kondisi miring. Saat parkir, pastikan rem parkir diaktifkan dengan kuat, dan biasakan untuk selalu memasang \"ganjal roda\" guna mencegah truk bergerak sendiri."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('駐車', 'ちゅうしゃ', 'parkir')}・{kotoba('停車', 'ていしゃ', 'berhenti')}のルール",
        "id": "・Aturan Parkir dan Berhenti Sejenak"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('歩道', 'ほどう', 'trotoar')}や{kotoba('路側帯', 'ろそくたい', 'pinggir jalan')}の{kotoba('有無', 'うむ', 'ada tidaknya')}、{kotoba('路側帯', 'ろそくたい', 'pinggir jalan')}の{kotoba('種類', 'しゅるい', 'jenis')}などにより、{kotoba('駐停車', 'ちゅうていしゃ', 'parkir dan berhenti')}のルールが{kotoba('定められて', 'さだめられて', 'ditetapkan')}います。",
        "id": "Aturan memarkir dan memberhentikan kendaraan ditetapkan berdasarkan ada tidaknya trotoar atau bahu jalan, serta jenis bahu jalan tersebut."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('人', 'ひと', 'orang')}の{kotoba('乗り降り', 'のりおり', 'naik turun')}や{kotoba('荷物', 'にもつ', 'barang')}の{kotoba('積卸し', 'つみおろし', 'bongkar muat')}のために{kotoba('停車する', 'ていしゃする', 'berhenti')}ときは、できるだけ{kotoba('道路', 'どうろ', 'jalan')}の{kotoba('左側', 'ひだりがわ', 'sisi kiri')}に{kotoba('沿い', 'そい', 'mengikuti')}、{kotoba('他', 'ほか', 'lain')}の{kotoba('交通', 'こうつう', 'lalu lintas')}の{kotoba('妨げ', 'さまたげ', 'hambatan')}にならないようにします。",
        "id": "・Saat berhenti untuk menaikkan/menurunkan orang atau bongkar muat barang, menepilah sedekat mungkin dengan sisi kiri jalan agar tidak mengganggu lalu lintas lain."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('歩道', 'ほどう', 'trotoar')}や{kotoba('路側帯', 'ろそくたい', 'pinggir jalan')}のない{kotoba('道路', 'どうろ', 'jalan')}に{kotoba('駐車する', 'ちゅうしゃする', 'parkir')}ときは、{kotoba('道路', 'どうろ', 'jalan')}の{kotoba('左側', 'ひだりがわ', 'sisi kiri')}に{kotoba('沿います', 'そいます', 'mengikuti')}。",
        "id": "・Saat memarkir kendaraan di jalan yang tidak memiliki trotoar atau bahu jalan, menepilah mengikuti sisi kiri jalan."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('歩道', 'ほどう', 'trotoar')}のある{kotoba('道路', 'どうろ', 'jalan')}では{kotoba('車道', 'しゃどう', 'jalan kendaraan')}の{kotoba('左側', 'ひだりがわ', 'sisi kiri')}に{kotoba('沿います', 'そいます', 'mengikuti')}。",
        "id": "・Di jalan yang dilengkapi trotoar, menepilah di sepanjang sisi kiri dari badan jalan (jalan khusus kendaraan bermotor)."
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('路側帯', 'ろそくたい', 'pinggir jalan')}のある{kotoba('道路', 'どうろ', 'jalan')}では、{kotoba('路側帯', 'ろそくたい', 'pinggir jalan')}の{kotoba('幅', 'はば', 'lebar')}が0.75メートル{kotoba('以下', 'いか', 'ke bawah')}の{kotoba('場合', 'ばあい', 'kasus')}は{kotoba('路側帯', 'ろそくたい', 'pinggir jalan')}に{kotoba('入る', 'はいる', 'masuk')}ことはできませんから、{kotoba('車道', 'しゃどう', 'jalan kendaraan')}の{kotoba('左端', 'ひだりはし', 'ujung kiri')}に{kotoba('沿います', 'そいます', 'mengikuti')}。{kotoba('路側帯', 'ろそくたい', 'pinggir jalan')}の{kotoba('幅', 'はば', 'lebar')}が0.75メートルを{kotoba('超える', 'こえる', 'melebihi')}{kotoba('場合', 'ばあい', 'kasus')}には{kotoba('路側帯', 'ろそくたい', 'pinggir jalan')}のなかに入って{kotoba('駐車', 'ちゅうしゃ', 'parkir')}できますが、{kotoba('左側', 'ひだりがわ', 'sisi kiri')}に0.75メートル{kotoba('以上', 'いじょう', 'ke atas')}の{kotoba('余地', 'よち', 'ruang sisa')}をあける{kotoba('必要', 'ひつよう', 'perlu')}があります。",
        "id": "・Di jalan yang terdapat garis pinggir jalan (bahu jalan), jika lebarnya 0,75 meter atau kurang, kendaraan tidak boleh masuk melampaui garis tersebut; jadi berhentilah menempel di sisi kiri badan jalan. Jika lebar pinggir jalan melebihi 0,75 meter, Anda boleh parkir di dalamnya, asalkan menyisakan ruang bebas minimal 0,75 meter di sebelah kiri kendaraan."
    },
    {
        "is_header": True,
        "jp": f"・{kotoba('駐停車できない', 'ちゅうていしゃできない', 'tidak bisa parkir dan berhenti')}{kotoba('路側帯', 'ろそくたい', 'pinggir jalan')}",
        "id": "・Pinggir Jalan (Bahu Jalan) di Mana Kendaraan Dilarang Parkir/Berhenti"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('路側帯', 'ろそくたい', 'pinggir jalan')}の{kotoba('幅', 'はば', 'lebar')}が0.75メートルを{kotoba('超える', 'こえる', 'melebihi')}{kotoba('場合', 'ばあい', 'kasus')}でも、{kotoba('白', 'しろ', 'putih')}の2{kotoba('本', 'ほん', 'buah')}の{kotoba('実線', 'じっせん', 'garis utuh')}の{kotoba('標示', 'ひょうじ', 'marka')}（{kotoba('歩行者用路側帯', 'ほこうしゃようろそくたい', 'pinggir jalan u/ pejalan kaki')}）や{kotoba('白', 'しろ', 'putih')}の{kotoba('実線', 'じっせん', 'garis utuh')}と{kotoba('破線', 'はせん', 'garis putus-putus')}の{kotoba('標示', 'ひょうじ', 'marka')}（{kotoba('駐停車禁止路側帯', 'ちゅうていしゃきんしろそくたい', 'pinggir jalan dilarang parkir')}）のある{kotoba('場所', 'ばしょ', 'tempat')}では、{kotoba('路側帯', 'ろそくたい', 'pinggir jalan')}に{kotoba('入る', 'はいる', 'masuk')}ことはできません。",
        "id": "Bahkan jika lebar pinggir jalan melebihi 0,75 meter, jika marka jalan berupa dua garis putih penuh/utuh (menandakan zona khusus pejalan kaki), atau satu garis penuh dan satu garis putus-putus (menandakan zona larangan parkir & berhenti), Anda tidak boleh memasukinya."
    },
    {
        "is_header": True,
        "jp": f"4.15 {kotoba('夜間', 'やかん', 'malam hari')}の{kotoba('運転', 'うんてん', 'mengemudi')}",
        "id": "4.15 Mengemudi di Malam Hari"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('夜間', 'やかん', 'malam hari')}の{kotoba('運転中', 'うんてんちゅう', 'saat mengemudi')}は、{kotoba('車', 'くるま', 'kendaraan')}の{kotoba('外', 'そと', 'luar')}が{kotoba('見えにくくなる', 'みえにくくなる', 'menjadi sulit terlihat')}{kotoba('おそれ', '', 'kekhawatiran')}があるため、{kotoba('室内灯', 'しつないとう', 'lampu kabin')}（{kotoba('車', 'くるま', 'kendaraan')}の{kotoba('中', 'なか', 'dalam')}を{kotoba('明るく', 'あかるく', 'terang')}するためのライト）をつけないようにしましょう。",
        "id": "Saat mengemudi di malam hari, jangan menyalakan lampu kabin (lampu penerangan dalam mobil), karena dikhawatirkan hal tersebut dapat membuat jarak pandang ke luar mobil menjadi sulit terlihat."
    },
    {
        "is_header": True,
        "jp": f"5 {kotoba('運転', 'うんてん', 'mengemudi')}マナーの{kotoba('基本', 'きほん', 'dasar')}",
        "id": "5 Dasar-Dasar Etika Mengemudi"
    },
    {
        "is_header": True,
        "jp": f"5.1 {kotoba('他', 'ほか', 'lain')}の{kotoba('車', 'くるま', 'kendaraan')}のお{kotoba('手本', 'てほん', 'contoh/teladan')}となるような{kotoba('安全', 'あんぜん', 'aman')}でマナーの{kotoba('良い', 'よい', 'baik')}{kotoba('運転', 'うんてん', 'mengemudi')}を{kotoba('心掛ける', 'こころがける', 'mengusahakan')}",
        "id": "5.1 Mengusahakan Berkendara yang Aman dan Beretika Baik sebagai Teladan bagi Kendaraan Lain"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('事業用', 'じぎょうよう', 'untuk bisnis')}トラックを{kotoba('運転している', 'うんてんしている', 'mengemudikan')}{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}のみなさんは、{kotoba('他', 'ほか', 'lain')}の{kotoba('車', 'くるま', 'kendaraan')}のお{kotoba('手本', 'てほん', 'contoh/teladan')}となるような{kotoba('安全', 'あんぜん', 'aman')}でマナーの{kotoba('良い', 'よい', 'baik')}{kotoba('運転', 'うんてん', 'mengemudi')}を{kotoba('心掛けなければ', 'こころがけなければ', 'harus mengusahakan')}いけません。{kotoba('一般', 'いっぱん', 'umum')}の{kotoba('車', 'くるま', 'kendaraan')}からみれば、{kotoba('車体', 'しゃたい', 'bodi kendaraan')}の{kotoba('大きい', 'おおきい', 'besar')}トラックが{kotoba('近く', 'ちかく', 'dekat')}を{kotoba('走っている', 'はしっている', 'berjalan/melaju')}だけで{kotoba('怖く', 'こわく', 'takut')}{kotoba('感じます', 'かんじます', 'merasa')}から、「{kotoba('幅寄せ', 'はばよせ', 'memepet')}」や「あおり{kotoba('運転', 'うんてん', 'mengemudi')}」などは{kotoba('絶対', 'ぜったい', 'mutlak')}してはいけないことです。",
        "id": "Anda sekalian yang mengemudikan truk bisnis (komersial) haruslah mengusahakan cara berkendara yang aman dan beretika baik agar bisa menjadi teladan bagi kendaraan lain. Dari sudut pandang kendaraan pribadi pada umumnya, truk berukuran besar yang sekadar melaju di dekat mereka saja sudah terasa menakutkan, sehingga perbuatan seperti \"memepet dengan sengaja\" atau \"mengemudi secara agresif (tailgating)\" adalah hal yang mutlak dilarang."
    },
    {
        "is_header": True,
        "jp": f"5.2 トラックは{kotoba('走る', 'はしる', 'berjalan')}「{kotoba('広告塔', 'こうこくとう', 'papan iklan')}」",
        "id": "5.2 Truk adalah \"Papan Iklan Berjalan\""
    },
    {
        "is_header": False,
        "jp": f"トラックには、{kotoba('会社', 'かいしゃ', 'perusahaan')}やお{kotoba('客様', 'きゃくさま', 'pelanggan')}の{kotoba('名前', 'なまえ', 'nama')}、トレードマークや{kotoba('商品名', 'しょうひんめい', 'nama produk')}が{kotoba('大きく', 'おおきく', 'besar')}{kotoba('書かれて', 'かかれて', 'tertulis')}います。{kotoba('そのため', '', 'oleh karena itu')}、トラックは{kotoba('次', 'つぎ', 'berikut')}の3つのイメージを{kotoba('背負って', 'せおって', 'memikul')}{kotoba('走って', 'はしって', 'berjalan/melaju')}います。",
        "id": "Di truk, nama perusahaan, pelanggan, merek dagang, atau nama produk tertulis dengan huruf yang besar. Oleh karena itu, truk melaju dengan memikul ketiga citra berikut:"
    },
    {
        "is_header": False,
        "jp": f"・{kotoba('会社', 'かいしゃ', 'perusahaan')}のイメージ",
        "id": "・Citra perusahaan"
    },
    {
        "is_header": False,
        "jp": f"・お{kotoba('客様', 'きゃくさま', 'pelanggan')}のイメージ",
        "id": "・Citra pelanggan"
    },
    {
        "is_header": False,
        "jp": f"・トラック{kotoba('運送業界', 'うんそうぎょうかい', 'industri angkutan')}のイメージ",
        "id": "・Citra industri angkutan truk"
    },
    {
        "is_header": False,
        "jp": f"まさに、トラックは「{kotoba('走る', 'はしる', 'berjalan')}{kotoba('広告塔', 'こうこくとう', 'papan iklan')}」です。{kotoba('他車', 'たしゃ', 'kendaraan lain')}や{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}への{kotoba('気づかい', 'きづかい', 'perhatian/kepedulian')}、{kotoba('不安感', 'ふあんかん', 'rasa cemas')}を{kotoba('与えない', 'あたえない', 'tidak memberikan')}という{kotoba('義務', 'ぎむ', 'kewajiban')}と{kotoba('責任', 'せきにん', 'tanggung jawab')}を{kotoba('負っている', 'おっている', 'memikul')}ということでもあります。",
        "id": "Truk benar-benar merupakan \"papan iklan berjalan\". Hal ini juga berarti bahwa Anda memikul kewajiban dan tanggung jawab untuk senantiasa menunjukkan kepedulian terhadap kendaraan lain maupun pejalan kaki, serta tidak membuat mereka merasa cemas."
    },
    {
        "is_header": True,
        "jp": f"5.3 {kotoba('運転', 'うんてん', 'mengemudi')}マナーの{kotoba('基本', 'きほん', 'dasar')}は「{kotoba('思いやり', 'おもいやり', 'simpati/kepedulian')}」と「{kotoba('譲りあい', 'ゆずりあい', 'saling mengalah')}」",
        "id": "5.3 Dasar Etika Mengemudi adalah \"Simpati/Rasa Peduli\" dan \"Saling Mengalah\""
    },
    {
        "is_header": False,
        "jp": f"{kotoba('道路', 'どうろ', 'jalan')}は{kotoba('多く', 'おおく', 'banyak')}の{kotoba('人', 'ひと', 'orang')}が{kotoba('通行する', 'つうこうする', 'melintas')}{kotoba('公共', 'こうきょう', 'publik')}の{kotoba('場所', 'ばしょ', 'tempat')}です。{kotoba('公共', 'こうきょう', 'publik')}の{kotoba('場所', 'ばしょ', 'tempat')}を{kotoba('安全', 'あんぜん', 'aman')}で{kotoba('円滑に', 'えんかつに', 'lancar')}{kotoba('利用する', 'りようする', 'memanfaatkan')}ための{kotoba('最小限', 'さいしょうげん', 'minimum')}の{kotoba('決まり', 'きまり', 'aturan')}が「{kotoba('交通', 'こうつう', 'lalu lintas')}ルール」ですが、{kotoba('交通', 'こうつう', 'lalu lintas')}ルールだけでは{kotoba('解決できない', 'かいけつできない', 'tidak bisa diselesaikan')}ケースもあります。これを{kotoba('解決する', 'かいけつする', 'menyelesaikan')}のが{kotoba('運転', 'うんてん', 'mengemudi')}マナーであり、「{kotoba('思いやり', 'おもいやり', 'simpati/kepedulian')}」や「{kotoba('譲りあい', 'ゆずりあい', 'saling mengalah')}」です。いつも「{kotoba('相手', 'あいて', 'lawan/orang lain')}に{kotoba('譲る', 'ゆずる', 'mengalah')}」という{kotoba('姿勢', 'しせい', 'sikap')}で{kotoba('運転', 'うんてん', 'mengemudi')}しましょう。",
        "id": "Jalan raya adalah fasilitas publik yang dilalui oleh banyak orang. Aturan minimum untuk menggunakan tempat publik secara aman dan lancar disebut \"Aturan Lalu Lintas\", tetapi ada pula kasus-kasus yang tidak bisa diselesaikan hanya dengan aturan. Sesuatu yang dapat menyelesaikan hal ini adalah etika mengemudi, yaitu \"simpati/rasa peduli\" dan \"saling mengalah\". Berkendaralah selalu dengan sikap \"mengalah kepada orang lain\"."
    },
    {
        "is_header": True,
        "jp": f"5.4 {kotoba('相手', 'あいて', 'lawan/orang lain')}を{kotoba('思いやる', 'おもいやる', 'memperhatikan/peduli')}{kotoba('運転', 'うんてん', 'mengemudi')}を",
        "id": "5.4 Mengemudi dengan Memperhatikan/Peduli pada Orang Lain"
    },
    {
        "is_header": False,
        "jp": f"トラックは{kotoba('他車', 'たしゃ', 'kendaraan lain')}よりも{kotoba('大きく', 'おおきく', 'besar')}、{kotoba('高い', 'たかい', 'tinggi')}{kotoba('運転席', 'うんてんせき', 'kursi pengemudi')}から{kotoba('他', 'ほか', 'lain')}の{kotoba('車', 'くるま', 'kendaraan')}や{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}を{kotoba('見下ろす', 'みおろす', 'melihat ke bawah')}かたちになるので、トラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}は{kotoba('他', 'ほか', 'lain')}の{kotoba('人', 'ひと', 'orang')}よりも{kotoba('自分', 'じぶん', 'sendiri')}のほうが{kotoba('強い', 'つよい', 'kuat')}という{kotoba('意識', 'いしき', 'kesadaran')}を{kotoba('持ちやすくなります', 'もちやすくなります', 'mudah memiliki')}。「{kotoba('強い', 'つよい', 'kuat')}{kotoba('者', 'もの', 'orang')}は{kotoba('弱い', 'よわい', 'lemah')}{kotoba('者', 'もの', 'orang')}を{kotoba('助ける', 'たすける', 'membantu')}」、この{kotoba('原則', 'げんそく', 'prinsip')}に{kotoba('立ち', 'たち', 'berdiri')}、{kotoba('相手', 'あいて', 'lawan/orang lain')}の{kotoba('立場', 'たちば', 'posisi')}を{kotoba('思いやる', 'おもいやる', 'memperhatikan/peduli')}{kotoba('運転', 'うんてん', 'mengemudi')}が{kotoba('求められます', 'もとめられます', 'dituntut')}。",
        "id": "Truk lebih besar dari mobil lain, dan posisinya yang menatap kendaraan lain serta pejalan kaki dari kursi pengemudi yang tinggi, membuat pengemudi truk rentan merasa bahwa dirinya \"lebih kuat\" dibandingkan orang lain. Pengemudi dituntut untuk memiliki sikap kepedulian yang mempertimbangkan sudut pandang orang lain dengan berpegang pada prinsip \"yang kuat membantu yang lemah\"."
    },
    {
        "is_header": True,
        "jp": f"5.5 {kotoba('狭い', 'せまい', 'sempit')}{kotoba('道路', 'どうろ', 'jalan')}ですれ{kotoba('違う', 'ちがう', 'berpapasan')}ときは{kotoba('相手', 'あいて', 'lawan/kendaraan lain')}に{kotoba('進路', 'しんろ', 'jalur')}を{kotoba('譲る', 'ゆずる', 'memberikan')}",
        "id": "5.5 Memberikan Jalan kepada Kendaraan Lain Saat Berpapasan di Jalan Sempit"
    },
    {
        "is_header": False,
        "jp": f"トラックは{kotoba('車幅', 'しゃはば', 'lebar mobil')}が{kotoba('広い', 'ひろい', 'lebar')}ので、{kotoba('狭い', 'せまい', 'sempit')}{kotoba('道路', 'どうろ', 'jalan')}で{kotoba('対向車', 'たいこうしゃ', 'kendaraan dari depan')}が{kotoba('接近している', 'せっきんしている', 'mendekat')}ときに、そのまま{kotoba('強引に', 'ごういんに', 'dengan paksa')}{kotoba('進行する', 'しんこうする', 'maju')}と{kotoba('対向車', 'たいこうしゃ', 'kendaraan dari depan')}と{kotoba('接触する', 'せっしょくする', 'bersentuhan')}{kotoba('おそれ', '', 'kekhawatiran')}があります。このようなときは{kotoba('相手', 'あいて', 'lawan/kendaraan lain')}が{kotoba('止まるだろう', 'とまるだろう', 'akan berhenti')}とは{kotoba('考えず', 'かんがえず', 'tanpa berpikir')}、{kotoba('自分', 'じぶん', 'sendiri')}のほうが{kotoba('停止して', 'ていしして', 'berhenti')}{kotoba('相手', 'あいて', 'lawan/kendaraan lain')}に{kotoba('進路', 'しんろ', 'jalur')}を{kotoba('譲る', 'ゆずる', 'memberikan')}ようにしましょう。{kotoba('左', 'ひだり', 'kiri')}に{kotoba('寄って', 'よって', 'menepi')}{kotoba('停止する', 'ていしする', 'berhenti')}ときには、{kotoba('歩行者', 'ほこうしゃ', 'pejalan kaki')}や{kotoba('自転車', 'じてんしゃ', 'sepeda')}、{kotoba('道路脇', 'どうろわき', 'sisi jalan')}の{kotoba('看板', 'かんばん', 'papan reklame')}や{kotoba('工作物', 'こうさくぶつ', 'struktur bangunan')}などに{kotoba('接触しない', 'せっしょくしない', 'tidak bersentuhan')}よう{kotoba('十分', 'じゅうぶん', 'cukup')}{kotoba('注意', 'ちゅうい', 'perhatian')}しましょう。",
        "id": "Karena lebar bodi truk lebih lebar, saat berpapasan dengan kendaraan dari arah berlawanan di jalan yang sempit, jika truk memaksakan diri untuk terus melaju, dikhawatirkan akan terjadi benturan dengan kendaraan arah berlawanan tersebut. Di saat seperti ini, janganlah berpikir \"pasti lawan (kendaraan depan) yang akan berhenti\", melainkan inisiatiflah untuk berhenti sendiri dan memberikan jalan. Saat menepi ke sebelah kiri untuk berhenti, berhati-hatilah agar tidak menyenggol pejalan kaki, sepeda, papan reklame di pinggir jalan, maupun struktur bangunan lainnya."
    },
    {
        "is_header": True,
        "jp": f"5.6 {kotoba('車', 'くるま', 'kendaraan')}の{kotoba('外', 'そと', 'luar')}へ{kotoba('物', 'もの', 'barang')}を{kotoba('投げ捨てない', 'なげすてない', 'tidak membuang')}",
        "id": "5.6 Tidak Membuang Sampah/Barang ke Luar Kendaraan"
    },
    {
        "is_header": False,
        "jp": f"トラックの{kotoba('窓', 'まど', 'jendela')}から{kotoba('紙くず', 'かみくず', 'kertas bekas')}やペットボトル、{kotoba('空缶', 'あきかん', 'kaleng kosong')}などを{kotoba('投げ捨てる', 'なげすてる', 'membuang sembarangan')}トラック{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}がいます。こうした「ポイ{kotoba('捨て', 'すて', 'buang sembarangan')}」はたいへんマナーの{kotoba('悪い', 'わるい', 'buruk')}{kotoba('行為', 'こうい', 'tindakan')}であり、{kotoba('法令', 'ほうれい', 'perundang-undangan')}でも{kotoba('禁止されて', 'きんしされて', 'dilarang')}います。{kotoba('走行時', 'そうこうじ', 'saat melaju')}や{kotoba('駐停車時', 'ちゅうていしゃじ', 'saat parkir/berhenti')}の「ポイ{kotoba('捨て', 'すて', 'buang sembarangan')}」は{kotoba('絶対', 'ぜったい', 'mutlak')}にしていけません。",
        "id": "Ada pengemudi truk yang membuang gumpalan kertas bekas, botol plastik, atau kaleng kosong dari jendela truk. \"Membuang sampah sembarangan\" seperti ini adalah perilaku dengan etika yang sangat buruk, dan juga dilarang oleh hukum/undang-undang. Baik saat sedang melaju maupun sedang parkir, Anda sangat dilarang untuk membuang sampah sembarangan."
    },
    {
        "is_header": True,
        "jp": f"6 エコドライブの{kotoba('実践', 'じっせん', 'praktik')}",
        "id": "6 Praktik Eco-Drive"
    },
    {
        "is_header": True,
        "jp": f"・エコドライブの4つの{kotoba('効果', 'こうか', 'efek')}",
        "id": "・4 Efek Eco-Drive"
    },
    {
        "is_header": False,
        "jp": f"エコドライブとは、{kotoba('燃料消費量', 'ねんりょうしょうひりょう', 'konsumsi bahan bakar')}やCO2（{kotoba('二酸化炭素', 'にさんかたんそ', 'karbon dioksida')}）の{kotoba('排出量', 'はいしゅつりょう', 'jumlah emisi')}を{kotoba('減らし', 'へらし', 'mengurangi')}、{kotoba('地球温暖化', 'ちきゅうおんだんか', 'pemanasan global')}の{kotoba('防止', 'ぼうし', 'pencegahan')}につながる{kotoba('運転技術', 'うんてんぎじゅつ', 'keterampilan mengemudi')}や{kotoba('心がけ', 'こころがけ', 'sikap mental')}を{kotoba('いいます', '', 'disebut')}。",
        "id": "Eco-Drive (kendara ramah lingkungan) mengacu pada teknik mengemudi dan sikap mental yang dapat mengurangi jumlah konsumsi bahan bakar dan emisi CO2 (karbon dioksida), serta dapat membantu mencegah pemanasan global."
    },
    {
        "is_header": False,
        "jp": f"① CO2や{kotoba('排出', 'はいしゅつ', 'emisi')}ガスの{kotoba('抑制', 'よくせい', 'penekanan')}によって、{kotoba('環境保全', 'かんきょうほぜん', 'pelestarian lingkungan')}に{kotoba('寄与する', 'きよする', 'berkontribusi')}。",
        "id": "① Berkontribusi pada pelestarian lingkungan dengan menekan emisi gas buang dan CO2."
    },
    {
        "is_header": False,
        "jp": f"② ゆとりのある{kotoba('運転', 'うんてん', 'mengemudi')}で{kotoba('交通事故', 'こうつうじこ', 'kecelakaan lalu lintas')}が{kotoba('減少する', 'げんしょうする', 'berkurang')}。",
        "id": "② Mengurangi jumlah kecelakaan lalu lintas berkat cara mengemudi yang lebih relaks (tidak tergesa-gesa)."
    },
    {
        "is_header": False,
        "jp": f"③ {kotoba('燃料費', 'ねんりょうひ', 'biaya bahan bakar')}やタイヤなどの{kotoba('経費', 'けいひ', 'biaya pengeluaran')}を{kotoba('少なく', 'すくなく', 'sedikit')}できる。",
        "id": "③ Mampu mengurangi biaya operasional seperti biaya bahan bakar dan ban."
    },
    {
        "is_header": False,
        "jp": f"④ エンジンやブレーキなどの{kotoba('損耗', 'そんもう', 'keausan/kerusakan')}が{kotoba('抑えられ', 'おさえられ', 'ditekan')}、{kotoba('修繕費', 'しゅうぜんひ', 'biaya perbaikan')}を{kotoba('少なく', 'すくなく', 'sedikit')}できる。",
        "id": "④ Keausan pada mesin, rem, dan lainnya dapat ditekan sehingga mampu mengurangi biaya perbaikan kendaraan."
    },
    {
        "is_header": False,
        "jp": f"つまり、「{kotoba('環境', 'かんきょう', 'lingkungan')}」「{kotoba('安全', 'あんぜん', 'keselamatan')}」「{kotoba('経営', 'けいえい', 'manajemen')}」のいずれにも{kotoba('大きな', 'おおきな', 'besar')}{kotoba('効果', 'こうか', 'efek')}があるということです。",
        "id": "Artinya, hal ini memberikan dampak positif yang besar terhadap \"Lingkungan\", \"Keselamatan\", maupun \"Manajemen/Finansial Bisnis\"."
    },
    {
        "is_header": True,
        "jp": f"◆エコドライブの8つのポイント",
        "id": "◆ 8 Poin Eco-Drive"
    },
    {
        "is_header": False,
        "jp": f"① {kotoba('おだやかな', '', 'tenang/halus')}{kotoba('発進', 'はっしん', 'melaju')}と{kotoba('加速', 'かそく', 'akselerasi')}",
        "id": "① Mengawali jalan dan akselerasi secara perlahan (halus)."
    },
    {
        "is_header": False,
        "jp": f"② {kotoba('早めの', 'はやめの', 'lebih awal')}シフトアップ",
        "id": "② Melakukan perpindahan gigi (*shift-up*) lebih awal."
    },
    {
        "is_header": False,
        "jp": f"③ {kotoba('定速走行', 'ていそくそうこう', 'berkendara kecepatan konstan')}の{kotoba('励行', 'れいこう', 'pelaksanaan rutin')}",
        "id": "③ Rutin mempertahankan kecepatan kendaraan konstan/stabil."
    },
    {
        "is_header": False,
        "jp": f"④ エンジンブレーキの{kotoba('活用', 'かつよう', 'pemanfaatan')}",
        "id": "④ Memanfaatkan *engine brake* (rem mesin)."
    },
    {
        "is_header": False,
        "jp": f"⑤ {kotoba('経済速度', 'けいざいそくど', 'kecepatan ekonomis')}の{kotoba('遵守', 'じゅんしゅ', 'kepatuhan')}",
        "id": "⑤ Mematuhi batas kecepatan ekonomis."
    },
    {
        "is_header": False,
        "jp": f"⑥ {kotoba('予知運転', 'よちうんてん', 'mengemudi prediktif')}による{kotoba('停止', 'ていし', 'berhenti')}・{kotoba('発進', 'はっしん', 'melaju')}",
        "id": "⑥ Berhenti dan melaju dengan teknik mengemudi prediktif (antisipatif)."
    },
    {
        "is_header": False,
        "jp": f"⑦ {kotoba('不必要な', 'ふひつような', 'tidak diperlukan')}{kotoba('空ぶかし', 'からぶかし', 'menginjak gas kosong')}の{kotoba('抑制', 'よくせい', 'penekanan/pengurangan')}",
        "id": "⑦ Tidak menginjak pedal gas (revving) saat mesin kosong tanpa alasan yang perlu."
    },
    {
        "is_header": False,
        "jp": f"⑧ {kotoba('必要最小限', 'ひつようさいしょうげん', 'minimal yang diperlukan')}のアイドリング",
        "id": "⑧ Melakukan *idling* (menyalakan mesin saat diam) hanya seminimal mungkin sesuai kebutuhan."
    },
    {
        "is_header": True,
        "jp": f"7 {kotoba('適切な', 'てきせつな', 'tepat/sesuai')}{kotoba('運行経路', 'うんこうけいろ', 'rute perjalanan')}",
        "id": "7 Rute Perjalanan yang Tepat"
    },
    {
        "is_header": True,
        "jp": f"7.1 {kotoba('安全性', 'あんぜんせい', 'keselamatan')}に{kotoba('配慮した', 'はいりょした', 'mempertimbangkan')}{kotoba('選択', 'せんたく', 'pilihan')}",
        "id": "7.1 Pilihan Rute dengan Mempertimbangkan Keselamatan"
    },
    {
        "is_header": False,
        "jp": f"トラックの{kotoba('運行', 'うんこう', 'perjalanan')}ルートを{kotoba('決める', 'きめる', 'menentukan')}のは{kotoba('運行管理者', 'うんこうかんりしゃ', 'manajer operasi')}の{kotoba('仕事', 'しごと', 'pekerjaan')}です。{kotoba('運行', 'うんこう', 'perjalanan')}ルートは、{kotoba('到着時間', 'とうちゃくじかん', 'waktu tiba')}、{kotoba('経済運転', 'けいざいうんてん', 'berkendara ekonomis')}、{kotoba('気象条件', 'きしょうじょうけん', 'kondisi cuaca')}、{kotoba('地理的条件', 'ちりてきじょうけん', 'kondisi geografis')}などを{kotoba('考慮して', 'こうりょして', 'mempertimbangkan')}{kotoba('決められています', 'きめられています', 'telah ditentukan')}ので、{kotoba('運転者', 'うんてんしゃ', 'pengemudi')}は{kotoba('決められた', 'きめられた', 'telah ditentukan')}{kotoba('運行経路', 'うんこうけいろ', 'rute perjalanan')}に{kotoba('従って', 'したがって', 'mematuhi')}{kotoba('走行しなければ', 'そうこうしなければ', 'harus melaju')}いけません。{kotoba('自分', 'じぶん', 'sendiri')}の{kotoba('判断', 'はんだん', 'keputusan')}で{kotoba('運行経路', 'うんこうけいろ', 'rute perjalanan')}を{kotoba('変更してはいけません', 'へんこうしてはいけません', 'dilarang mengubah')}。",
        "id": "Yang berwenang menentukan rute operasional truk adalah Manajer Operasi (*Operation Manager*). Rute ini ditetapkan dengan mempertimbangkan perkiraan waktu tiba, cara mengemudi yang hemat bahan bakar (ekonomis), kondisi cuaca, serta kondisi geografis, sehingga pengemudi diwajibkan berkendara melintasi rute yang telah ditetapkan. Anda tidak boleh mengubah rute perjalanan hanya berdasarkan penilaian pribadi Anda sendiri."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('交通事故', 'こうつうじこ', 'kecelakaan lalu lintas')}の{kotoba('危険性', 'きけんせい', 'risiko bahaya')}が{kotoba('高い', 'たかい', 'tinggi')}{kotoba('場所', 'ばしょ', 'tempat')}を{kotoba('知っておく', 'しっておく', 'mengetahui')}ことも{kotoba('重要', 'じゅうよう', 'penting')}です。{kotoba('各都道府県警', 'かくとどうふけんけい', 'kepolisian tiap prefektur')}の「{kotoba('交通事故発生', 'こうつうじこはっせい', 'terjadinya kecelakaan lalu lintas')}マップ」や「{kotoba('事故危険箇所検索', 'じこきけんかしょけんさく', 'pencarian lokasi rawan kecelakaan')}マップ」などを{kotoba('活用しましょう', 'かつようしましょう', 'mari manfaatkan')}。",
        "id": "Mengetahui area atau titik-titik yang berisiko tinggi terjadinya kecelakaan lalu lintas juga merupakan hal yang vital. Mari manfaatkan \"Peta Lokasi Terjadinya Kecelakaan Lalu Lintas\" atau \"Peta Pencarian Area Bahaya Rawan Kecelakaan\" yang disediakan oleh pihak kepolisian di setiap prefektur."
    },
    {
        "is_header": True,
        "jp": f"7.2 {kotoba('経路情報', 'けいろじょうほう', 'informasi rute')}の{kotoba('事前把握', 'じぜんはあく', 'memahami sebelumnya')}",
        "id": "7.2 Memahami Informasi Rute Terlebih Dahulu"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('運行経路', 'うんこうけいろ', 'rute perjalanan')}の{kotoba('道路事情', 'どうろじじょう', 'kondisi jalan')}や{kotoba('交通状況', 'こうつうじょうきょう', 'kondisi lalu lintas')}、{kotoba('気象状況', 'きしょうじょうきょう', 'kondisi cuaca')}はいつも{kotoba('変化します', 'へんかします', 'berubah')}から、{kotoba('事前', 'じぜん', 'sebelumnya')}にできるだけ{kotoba('情報', 'じょうほう', 'informasi')}を{kotoba('集めておく', 'あつめておく', 'mengumpulkan')}ことが{kotoba('大切', 'たいせつ', 'penting')}です。",
        "id": "Kondisi jalan di rute operasional Anda, maupun kondisi kepadatan lalu lintas serta cuaca akan senantiasa berubah-ubah, jadi sangatlah penting untuk mengumpulkan informasi sebanyak-banyaknya sejak awal."
    },
    {
        "is_header": False,
        "jp": f"また、{kotoba('運行経路', 'うんこうけいろ', 'rute perjalanan')}におけるヒヤリ・ハットの{kotoba('多い', 'おおい', 'banyak')}{kotoba('場所', 'ばしょ', 'tempat')}や{kotoba('事故', 'じこ', 'kecelakaan')}の{kotoba('多く', 'おおく', 'banyak')}{kotoba('起こっている', 'おこっている', 'terjadi')}{kotoba('場所', 'ばしょ', 'tempat')}をしっかり{kotoba('知っておきましょう', 'しっておきましょう', 'mari ketahui')}。",
        "id": "Selain itu, ketahuilah dengan saksama lokasi-lokasi di mana banyak terjadi insiden nyaris celaka (Hiyari Hatto) atau area-area di mana kecelakaan paling sering terjadi di sepanjang rute Anda."
    },
    {
        "is_header": True,
        "jp": f"▶{kotoba('大雨', 'おおあめ', 'hujan deras')}や{kotoba('大雪', 'おおゆき', 'salju lebat')}などの{kotoba('異常気象時', 'いじょうきしょうじ', 'saat cuaca ekstrem')}は{kotoba('運行経路', 'うんこうけいろ', 'rute perjalanan')}に{kotoba('注意する', 'ちゅういする', 'memperhatikan')}",
        "id": "▶ Perhatikan Rute Perjalanan Saat Cuaca Ekstrem Seperti Hujan Lebat atau Badai Salju"
    },
    {
        "is_header": False,
        "jp": f"{kotoba('大雨', 'おおあめ', 'hujan deras')}、{kotoba('大雪', 'おおゆき', 'salju lebat')}、{kotoba('暴風雨', 'ぼうふうう', 'badai hujan')}、{kotoba('暴風雪', 'ぼうふうせつ', 'badai salju')}、{kotoba('濃霧', 'のうむ', 'kabut tebal')}などの{kotoba('異常気象時', 'いじょうきしょうじ', 'saat cuaca ekstrem')}は{kotoba('危険な', 'きけんな', 'berbahaya')}{kotoba('状況', 'じょうきょう', 'situasi')}が{kotoba('起こりやすい', 'おこりやすい', 'mudah terjadi')}ので、{kotoba('運行経路', 'うんこうけいろ', 'rute perjalanan')}をチェックするなど、{kotoba('安全', 'あんぜん', 'keselamatan')}を{kotoba('確保する', 'かくほする', 'memastikan')}ために{kotoba('必要な', 'ひつような', 'yang diperlukan')}{kotoba('対策', 'たいさく', 'tindakan/persiapan')}をしましょう。{kotoba('大雨', 'おおあめ', 'hujan deras')}の{kotoba('場合', 'ばあい', 'kasus')}は、{kotoba('冠水しやすい', 'かんすいしやすい', 'mudah banjir/terendam')}{kotoba('道路', 'どうろ', 'jalan')}や、{kotoba('洪水', 'こうずい', 'banjir')}の{kotoba('おそれ', '', 'kekhawatiran')}のある{kotoba('川沿い', 'かわぞい', 'sepanjang sungai')}の{kotoba('道路', 'どうろ', 'jalan')}を{kotoba('避けます', 'さけます', 'menghindari')}。{kotoba('台風', 'たいふう', 'angin topan')}による{kotoba('強風', 'きょうふう', 'angin kencang')}が{kotoba('予想される', 'よそうされる', 'diperkirakan')}{kotoba('場合', 'ばあい', 'kasus')}は、{kotoba('突風', 'とっぷう', 'angin kencang tiba-tiba')}の{kotoba('吹きやすい', 'ふきやすい', 'mudah berhembus')}{kotoba('橋', 'はし', 'jembatan')}の{kotoba('通行', 'つうこう', 'melintas')}を{kotoba('避けます', 'さけます', 'menghindari')}。{kotoba('大雪', 'おおゆき', 'salju lebat')}の{kotoba('場合', 'ばあい', 'kasus')}は、チェーン{kotoba('規制', 'きせい', 'aturan')}の{kotoba('有無', 'うむ', 'ada tidaknya')}など、{kotoba('気象状況', 'きしょうじょうきょう', 'kondisi cuaca')}に{kotoba('応じて', 'おうじて', 'sesuai')}{kotoba('運行経路', 'うんこうけいろ', 'rute perjalanan')}を{kotoba('検討する', 'けんとうする', 'mempertimbangkan')}ことが{kotoba('大切', 'たいせつ', 'penting')}です。",
        "id": "Pada kondisi cuaca yang ekstrem (abnormal) seperti saat hujan lebat, hujan salju lebat, badai topan berhujan, badai salju, maupun saat kabut tebal, situasi berbahaya akan sangat rentan terjadi. Maka itu, ambil tindakan yang diperlukan untuk menjamin keselamatan Anda, seperti memeriksa rute perjalanan. Pada saat hujan lebat, hindari jalan-jalan yang rentan terendam banjir atau jalan yang berbatasan dengan sungai yang rawan meluap. Jika diprediksi akan muncul angin kuat akibat topan, hindarilah menyeberangi jembatan yang mudah terkena hembusan angin puting beliung tiba-tiba. Sementara jika terjadi hujan salju lebat, sangat penting bagi Anda untuk mempertimbangkan dan menyesuaikan rute perjalanan dengan kondisi cuaca tersebut, misalnya memeriksa ada atau tidaknya regulasi kewajiban pemakaian rantai salju."
    }
]

# Cara menggabungkan dengan data sebelumnya:
# data_lengkap = data_bab1 + data_lanjutan
