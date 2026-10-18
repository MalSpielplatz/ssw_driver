import streamlit as st
from data_bab1 import data_bab1

st.set_page_config(
    page_title="Modul SSW Truk", page_icon="🚛", layout="wide"
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
    .text-jp { font-size: 1.15rem; line-height: 2.8; color: #1d3557; }
    .text-id { font-size: 1.05rem; line-height: 1.8; color: #2b2d42; padding-top: 10px;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("📚 Navigasi Modul")
# Sidebar HANYA berisi daftar Bab utama
bab_options = [
    "Bab 1: Dasar Pengemudi Truk",
    "Bab 2: Kepatuhan Aturan Lalu Lintas",
    "Bab 3: Pengetahuan Dasar Truk",
    "Bab 4: Keterampilan Mengemudi Dasar"
]

selected_bab = st.sidebar.radio("Pilih Bab:", bab_options)

if selected_bab.startswith("Bab 1"):
    st.title("🚛 Bab 1: Pengetahuan Dasar Pengemudi Truk")
    st.caption("第１章 トラック運転者の基本")
    st.divider()

    # Looping seluruh isi Bab 1 agar bisa di-scroll panjang ke bawah
    for item in data_bab1:
        if item.get("is_header"):
            # Format header: Jepang di atas, Indonesia lebih kecil di bawahnya
            st.markdown(f"<h3 style='color:#1d3557;'>{item['jp']} <br> <span style='font-size:0.75em; color:#666;'>{item['id']}</span></h3>", unsafe_allow_html=True)
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
# Lanjutkan untuk Bab 3 dan 4...
