import streamlit as st

st.set_page_config(
    page_title="Modul SSW Truk - Pembelajaran Interaktif",
    page_icon="🚛",
    layout="wide",
)

st.markdown(
    """
    <style>
    ruby {
        font-size: 1.25rem;
        line-height: 2.2;
    }
    rt {
        font-size: 0.7rem;
        color: #e63946;
        font-weight: bold;
    }
    .materi-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #1d3557;
        margin-bottom: 12px;
    }
    .text-jp {
        font-size: 1.15rem;
        line-height: 2.2;
        color: #1d3557;
    }
    .text-id {
        font-size: 1.05rem;
        line-height: 1.8;
        color: #2b2d42;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.sidebar.title("📚 Navigasi Materi")
pilihan_bab = st.sidebar.selectbox(
    "Pilih Bab / Sub-bab:", ["Bab 1.1: Peran Truk (トラックの役割)", "Bab 1.2: Next Subbab"]
)

st.title("🚛 Modul SSW Truk (特定技能・トラック)")
st.caption("Aplikasi Belajar Modul SSW Driver Truk dengan Furigana & Terjemahan Side-by-Side")
st.divider()

data_bab1_1 = [
    {
        "jp": "1.1 トラックの<ruby>役<rt>やく</rt>割<rt>わり</rt></ruby>",
        "id": "1.1 Peran Truk",
        "is_header": True,
    },
    {
        "jp": "<ruby>皆<rt>みな</rt></ruby>さんは<ruby>今<rt>いま</rt></ruby>、<ruby>日<rt>に</rt>本<rt>ほん</rt></ruby>でトラック<ruby>運<rt>うん</rt>転<rt>てん</rt>者<rt>しゃ</rt></ruby>になるための<ruby>勉<rt>べん</rt>強<rt>きょう</rt></ruby>を<ruby>始<rt>はじ</rt></ruby>めたところだと思います。",
        "id": "Saat ini, Anda sekalian mungkin baru saja mulai belajar untuk menjadi pengemudi truk di Jepang.",
        "is_header": False,
    },
    {
        "jp": "では、<ruby>日<rt>に</rt>本<rt>ほん</rt></ruby>では、トラックはどれだけ<ruby>活<rt>かつ</rt>躍<rt>やく</rt></ruby>しているのでしょうか。",
        "id": "Lalu, seberapa besarkah peran truk di Jepang?",
        "is_header": False,
    },
    {
        "jp": "トラックは、<ruby>身<rt>み</rt>近<rt>ぢか</rt></ruby>な<ruby>食<rt>しょく</rt>料<rt>りょう</rt>品<rt>ひん</rt></ruby>や<ruby>衣<rt>い</rt>料<rt>りょう</rt></ruby>・<ruby>雑<rt>ざっ</rt>貨<rt>か</rt></ruby>をはじめ、<ruby>工<rt>こう</rt>業<rt>ぎょう</rt>製<rt>せい</rt>品<rt>ひん</rt></ruby>や<ruby>部<rt>ぶ</rt>品<rt>ひん</rt></ruby>、<ruby>建<rt>けん</rt>設<rt>せつ</rt>資<rt>し</rt>材<rt>ざい</rt></ruby>のほか、<ruby>石<rt>せき</rt>油<rt>ゆ</rt></ruby>やガスなどの<ruby>液<rt>えき</rt>体<rt>たい</rt></ruby>や<ruby>気<rt>き</rt>体<rt>たい</rt></ruby>も<ruby>運<rt>はこ</rt></ruby>びます。",
        "id": "Truk mengangkut barang-barang kebutuhan sehari-hari seperti bahan makanan, pakaian, dan barang kebutuhan harian, hingga produk industri, suku cadang, dan bahan bangunan, serta cairan dan gas seperti minyak bumi dan gas.",
        "is_header": False,
    },
]

if "Bab 1.1" in pilihan_bab:
    for item in data_bab1_1:
        if item["is_header"]:
            st.markdown(
                f"### {item['jp']} / {item['id']}", unsafe_allow_html=True
            )
            st.write("")
        else:
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(
                    f"<div class='materi-card text-jp'>{item['jp']}</div>",
                    unsafe_allow_html=True,
                )
            with col2:
                st.markdown(
                    f"<div class='materi-card text-id'>{item['id']}</div>",
                    unsafe_allow_html=True,
                )
else:
    st.info("Materi untuk sub-bab ini sedang disiapkan.")
