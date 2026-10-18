import streamlit as st

# Fungsi untuk membuat struktur 3 susun menggunakan CSS Flexbox
def kotoba(kanji, furigana, arti):
    return f"""
    <div style="display: inline-flex; flex-direction: column; align-items: center; vertical-align: bottom; margin: 0 2px;">
        <span style="font-size: 0.6em; line-height: 1.1; color: #555;">{furigana}</span>
        <span style="font-size: 1.2em; line-height: 1.2;">{kanji}</span>
        <span style="font-size: 0.6em; line-height: 1.1; color: #0066cc;">{arti}</span>
    </div>
    """

# Membuat 2 kolom untuk meniru \switchcolumn
col1, col2 = st.columns(2)

with col1:
    # Memasukkan teks Jepang dengan fungsi kotoba
    # Ditambahkan line-height agar susunan tidak bertabrakan dengan baris atas/bawahnya
    teks_jepang = f"""
    <div style="line-height: 2.8; font-size: 18px;">
    みなさんは{kotoba('今', 'いま', 'sekarang')}、
    {kotoba('日本', 'にほん', 'Jepang')}でトラック
    {kotoba('運転者', 'うんてんしゃ', 'pengemudi')}になるための
    {kotoba('勉強', 'べんきょう', 'belajar')}を
    {kotoba('始', 'はじ', 'mulai')}めたところだと
    {kotoba('思', 'おも', 'berpikir')}います。
    </div>
    """
    st.markdown(teks_jepang, unsafe_allow_html=True)

with col2:
    # Kolom kanan untuk terjemahan Indonesia
    st.markdown("""
    <div style="font-size: 18px; padding-top: 10px;">
    Anda sekalian saat ini mungkin baru saja mulai belajar untuk menjadi pengemudi truk di Jepang.
    </div>
    """, unsafe_allow_html=True)
