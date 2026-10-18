import streamlit as st
from data_bab1 import data_bab1

st.set_page_config(
    page_title="Modul SSW Truk - Bab 1", page_icon="🚛", layout="wide"
)

st.markdown(
    """
    <style>
    .materi-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #1d3557;
        margin-bottom: 12px;
    }
    /* line-height 2.8 sangat penting agar susunan 3 tingkat tidak bertabrakan */
    .text-jp { font-size: 1.15rem; line-height: 2.8; color: #1d3557; }
    .text-id { font-size: 1.05rem; line-height: 1.8; color: #2b2d42; padding-top: 10px;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("📚 Navigasi Bab 1")
subbab_options = [
    "1.1 Peran Truk (トラックの役割)",
    "1.2 Sikap Mental Pengemudi Truk (トラック運転者の心構え)",
    "1.3 Kualifikasi Pengemudi Truk (トラック運転者に必要な資格)",
    "1.4 Kewajiban Pemeriksaan & Pemeliharaan (点検・整備の義務)",
    "1.5 Pencegahan Overload (過積載の防止)",
    "1.6 Pencegahan Mengemudi Lelah & Kesehatan (過労運転の防止と健康管理)",
]

selected_subbab = st.sidebar.selectbox("Pilih Sub-bab:", subbab_options)

st.title("🚛 Modul SSW Truk (特定技能・トラック)")
st.caption("Bab 1: Pengetahuan Dasar Pengemudi Truk (トラック運転者の基本的知識)")
st.divider()

key = selected_subbab.split()[0]  # Mengambil "1.1", "1.2", dll.
materi_list = data_bab1.get(key, [])

for item in materi_list:
    if item.get("is_header"):
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
