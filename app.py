import streamlit as st
from data_bab1 import data_bab1

st.set_page_config(
    page_title="Modul SSW Truk - Pembelajaran Interaktif",
    page_icon="🚛",
    layout="wide",
)

st.markdown(
    """
    <style>
    ruby { font-size: 1.25rem; line-height: 2.2; }
    rt { font-size: 0.7rem; color: #e63946; font-weight: bold; }
    .materi-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #1d3557;
        margin-bottom: 12px;
    }
    .text-jp { font-size: 1.15rem; line-height: 2.2; color: #1d3557; }
    .text-id { font-size: 1.05rem; line-height: 1.8; color: #2b2d42; }
    </style>
""",
    unsafe_allow_html=True,
)

st.sidebar.title("📚 Navigasi Materi Bab 1")
subbab = st.sidebar.selectbox(
    "Pilih Sub-bab:",
    [
        "1.1 Peran Truk (トラックの役割)",
        "1.2 Sikap Mental Pengemudi Truk (トラック運転者の心構え)",
    ],
)

st.title("🚛 Modul SSW Truk (特定技能・トラック)")
st.caption(
    "Aplikasi Belajar Modul SSW Driver Truk dengan Furigana & Terjemahan Side-by-Side"
)
st.divider()

key = subbab.split()[0]  # mengambil "1.1" atau "1.2"
materi_list = data_bab1.get(key, [])

for item in materi_list:
    if item["is_header"]:
        st.markdown(f"### {item['jp']} / {item['id']}", unsafe_allow_html=True)
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
