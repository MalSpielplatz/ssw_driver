import streamlit as st
from data_bab1 import data_bab1

st.set_page_config(
    page_title="Modul SSW Truk", page_icon="🚛", layout="wide"
)

st.markdown(
    """
    <style>
    /* Styling standar Ruby bawaan HTML */
    ruby { font-size: 1.3rem; line-height: 2.2; }
    rt { font-size: 0.7rem; color: #e63946; font-weight: bold; } /* Furigana Merah */
    
    /* Styling Kartu Putih */
    .materi-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05); /* Bayangan tipis */
        border: 1px solid #eef0f2;
        margin-bottom: 15px;
        height: 100%; /* Agar tinggi kartu kiri dan kanan sama */
    }
    
    .text-jp { color: #1d3557; }
    .text-id { font-size: 1.1rem; line-height: 1.8; color: #2b2d42; display: flex; align-items: center;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("📚 Navigasi Materi")
# Dropdown simpel seperti di gambar
subbab_options = [
    "Bab 1.1: Peran Truk (トラックの役割)",
    "Bab 1.2: Jika Transportasi Berhenti",
    # ... dst
]

selected_subbab = st.sidebar.selectbox("Pilih Bab / Sub-bab:", subbab_options)

# Ambil key (misal "1.1")
key = selected_subbab.split(":")[0].replace("Bab ", "")
materi_list = data_bab1.get(key, [])

for item in materi_list:
    if item.get("is_header"):
        # Header menggunakan format judul besar seperti di gambar
        st.markdown(f"<h2>{item['jp']} / {item['id']}</h2>", unsafe_allow_html=True)
        st.write("---")
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
