import streamlit as st
from data_bab1 import data_bab1

st.set_page_config(
    page_title="Modul SSW Truk", page_icon="🚛", layout="wide"
)

st.markdown(
    """
    <style>
    /* Styling Kartu Putih */
    .materi-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        border: 1px solid #eef0f2;
        margin-bottom: 15px;
    }
    /* line-height 2.8 agar tumpukan 3 lapis (Furigana-Kanji-Arti) tidak bertabrakan */
    .text-jp { color: #1d3557; line-height: 2.8; font-size: 1.15rem; }
    .text-id { font-size: 1.05rem; line-height: 1.8; color: #2b2d42; display: flex; align-items: center; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("📚 Navigasi Modul")
# Sidebar HANYA berisi daftar Bab, BUKAN sub-bab
bab_options = [
    "Bab 1: Pengetahuan Dasar Pengemudi Truk",
    "Bab 2: Keselamatan & Pengaruh Kecelakaan",
    "Bab 3: Sikap Mental & Penampilan",
    "Bab 4: Dasar-Dasar Mengemudi Aman"
]

selected_bab = st.sidebar.radio("Pilih Bab:", bab_options)

if selected_bab.startswith("Bab 1"):
    st.title("🚛 Bab 1: Pengetahuan Dasar Pengemudi Truk")
    st.caption("第１章 トラック運転者の基本")
    st.divider()

    # Looping seluruh isi Bab 1 dari atas ke bawah secara berurutan
    for item in data_bab1:
        if item.get("is_header"):
            st.markdown(f"<h3 style='color:#1d3557; margin-top: 25px;'>{item['jp']} <br> <span style='font-size:0.75em; color:#666;'>{item['id']}</span></h3>", unsafe_allow_html=True)
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
elif selected_bab.startswith("Bab 2"):
    st.info("Materi Bab 2 sedang dalam penyusunan.")
