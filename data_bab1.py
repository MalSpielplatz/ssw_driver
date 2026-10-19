# Fungsi 3 susun: Furigana merah di atas, Kanji di tengah, Arti di bawah
def kotoba(kanji, furigana, arti):
    furigana_html = f"{furigana}" if furigana else "&nbsp;"
    return f"<div style='display: inline-flex; flex-direction: column; align-items: center; vertical-align: bottom; margin: 0 2px;'><span style='font-size: 0.6em; line-height: 1.1; color: #e63946; font-weight: bold;'>{furigana_html}</span><span style='font-size: 1.2em; line-height: 1.2; font-weight: 500; color: #0f172a;'>{kanji}</span><span style='font-size: 0.6em; line-height: 1.1; color: #1d3557;'>{arti}</span></div>"

# Data berurutan ke bawah untuk scroll panjang
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
        "jp": f"トラックは、{kotoba('身近', 'みぢか', 'dekat')}な{kotoba('食料品', 'しょくりょうひん', 'bahan makanan')}や{kotoba('衣料', 'いりょう', 'pakaian')}・{kotoba('雑貨', 'ざっか', 'barang')}をはじめ、{kotoba('工業製品', 'こうぎょうせいひん', 'produk industri')}や{kotoba('部品', 'ぶひん', 'suku cadang')}、{kotoba('建設資材', 'けんせつしざい', 'bahan bangunan')}のほか、{kotoba('石油', 'せきゆ', 'minyak')}やガスなどの{kotoba('液体', 'えきたい', 'cairan')}や{kotoba('気体', 'きたい', 'gas')}も{kotoba('運', 'はこ', 'mengangkut')}びます。",
        "id": "Truk mengangkut kebutuhan sehari-hari seperti bahan makanan, pakaian, dan barang kelontong, produk industri dan suku cadang, bahan bangunan, serta benda cair dan gas seperti minyak dan gas."
    },
    {
        "is_header": False,
        "jp": f"また、{kotoba('巨大', 'きょだい', 'raksasa')}な{kotoba('橋', 'はし', 'jembatan')}やプラント{kotoba('設備', 'せつび', 'fasilitas')}など、{kotoba('特殊', 'とくしゅ', 'khusus')}な{kotoba('物', 'もの', 'barang')}も{kotoba('運', 'はこ', 'mengangkut')}びます。{kotoba('宅配便', 'たくはいびん', 'jasa pengiriman')}やコンビニの{kotoba('荷物', 'にもつ', 'barang/paket')}を{kotoba('運', 'はこ', 'mengangkut')}んでいるのもトラックです。",
        "id": "Selain itu, truk juga mengangkut benda-banya khusus seperti jembatan raksasa dan fasilitas pabrik. Truk juga yang mengangkut paket pengiriman dan barang-barang minimarket."
    },
    {
        "is_header": False,
        "jp": f"{kotoba('鉄道', 'てつどう', 'kereta api')}、{kotoba('船', 'ふね', 'kapal')}、{kotoba('飛行機', 'ひこうき', 'pesawat terbang')}による{kotoba('輸送', 'ゆそう', 'transportasi/pengangkutan')}も{kotoba('行', 'おこな', 'dilakukan')}われていますが、{kotoba('駅', 'えき', 'stasiun')}、{kotoba('港', 'みなと', 'pelabuhan')}、{kotoba('空港', 'くうこう', 'bandara')}の{kotoba('先', 'さき', 'tujuan')}の{kotoba('輸送', 'ゆそう', 'pengangkutan')}はトラックが{kotoba('運', 'はこ', 'mengangkut')}んでいます。",
        "id": "Meskipun transportasi dengan kereta api, kapal, dan pesawat terbang juga dilakukan, angkutan lanjutan dari stasiun, pelabuhan, dan bandara dilakukan oleh truk."
    },
    {
        "is_header": True,
        "jp": "１．２ もしもトラック輸送が止まったら",
        "id": "1.2 Jika Transportasi Truk Berhenti"
    },
    {
        "is_header": False,
        "jp": f"トラック{kotoba('輸送', 'ゆそう', 'transportasi')}は、{kotoba('人々', 'ひとびと', 'orang-orang')}が{kotoba('仕事', 'しごと', 'pekerjaan')}をしたり、{kotoba('生活', 'せいかつ', 'kehidupan')}をしたりするためにとても{kotoba('大切', 'たいせつ', 'penting')}です。もしも{kotoba('日本中', 'にほんじゅう', 'seluruh Jepang')}のトラック{kotoba('輸送', 'ゆそう', 'transportasi')}が{kotoba('止', 'と', 'berhenti')}まったら、{kotoba('商品', 'しょうひん', 'produk')}や{kotoba('部品', 'ぶひん', 'suku cadang')}、{kotoba('薬', 'くすり', 'obat')}などが{kotoba('運', 'はこ', 'mengangkut')}べなくなり、{kotoba('日本中', 'にほんじゅう', 'seluruh Jepang')}のお{kotoba('店', 'みせ', 'toko')}や{kotoba('工場', 'こうじょう', 'pabrik')}、{kotoba('病院', 'びょういん', 'rumah sakit')}などで{kotoba('仕事', 'しごと', 'bekerja')}ができなくなってしまいます。",
        "id": "Transportasi truk sangat penting bagi orang-orang untuk bekerja dan menjalani kehidupan. Jika transportasi truk di seluruh Jepang terhenti, barang dagangan, suku cadang, obat-obatan, dll. tidak akan bisa diangkut, dan toko-toko, pabrik-pabrik, rumah sakit, dll. di seluruh Jepang tidak akan bisa beroperasi."
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
