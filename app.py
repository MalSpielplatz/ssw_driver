import asyncio
import re
import edge_tts
import streamlit as st
from data_bab1 import data_bab1, data_lanjutan

# Gabungkan list data materi Bab 1
data_bab1_lengkap = data_bab1 + data_lanjutan

st.set_page_config(
    page_title="Modul SSW Truk",
    page_icon="🚛",
    layout="wide"
)

VOICES = {
    "Nanami (perempuan)": "ja-JP-NanamiNeural",
    "Keita (laki-laki)": "ja-JP-KeitaNeural",
}

# ---------------------------------------------------------------------------
# Helper untuk Text-to-Speech (TTS)
# ---------------------------------------------------------------------------
_KOTOBA = re.compile(
    r"<div[^>]*>\s*<span[^>]*>.*?</span>\s*<span[^>]*>(.*?)</span>\s*<span[^>]*>.*?</span>\s*</div>",
    re.S,
)
_TAG = re.compile(r"<[^>]+>")
_NOMOR = re.compile(r"^[0-9０-９．.\s]+")  # buang nomor bab di awal judul

def plain_text(html: str) -> str:
    text = _KOTOBA.sub(r"\1", html)
    text = _TAG.sub("", text).replace("&nbsp;", "")
    return _NOMOR.sub("", text).strip()

@st.cache_data(show_spinner=False)
def synth(text: str, voice: str, rate: str) -> bytes:
    async def run() -> bytes:
        audio = b""
        async for chunk in edge_tts.Communicate(text, voice, rate=rate).stream():
            if chunk["type"] == "audio":
                audio += chunk["data"]
        return audio
    return asyncio.run(run())

# ---------------------------------------------------------------------------
# Styling CSS & Sidebar
# ---------------------------------------------------------------------------
st.markdown("""
<style>
/* Styling Kartu Putih Minimalis */
.materi-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.04);
    border: 1px solid #e2e8f0;
    margin-bottom: 15px;
}
.text-jp {
    color: #1e293b;
    line-height: 2.8;
    font-size: 1.15rem;
}
.text-id {
    font-size: 1.05rem;
    line-height: 1.8;
    color: #2b2d42;
    display: flex;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📚 Navigasi Modul")

# Pengaturan Suara TTS di Sidebar
st.sidebar.markdown("---")
st.sidebar.header("🔊 Pengaturan Suara")
voice_name = st.sidebar.selectbox("Pilih Suara", list(VOICES.keys()))
speed = st.sidebar.slider("Kecepatan (%)", -50, 30, -10, step=10)
show_id = st.sidebar.checkbox("Tampilkan terjemahan Indonesia", value=True)

VOICE = VOICES[voice_name]
RATE = f"{speed:+d}%"

# Navigasi menggunakan Dropdown per Bab
bab_options = [
    "Bab 1: Pengetahuan Dasar Pengemudi Truk",
    "Bab 2: Keselamatan & Pengaruh Kecelakaan",
    "Bab 3: Sikap Mental & Penampilan",
    "Bab 4: Dasar-Dasar Mengemudi Aman"
]
selected_bab = st.sidebar.selectbox("Pilih Bab:", bab_options)

# ---------------------------------------------------------------------------
# Render Konten Berdasarkan Pilihan Bab
# ---------------------------------------------------------------------------
if selected_bab.startswith("Bab 1"):
    st.title("🚛 Bab 1: Pengetahuan Dasar Pengemudi Truk")
    st.caption("第１章 トラック運転者の基本")
    st.divider()

    # Looping seluruh isi Bab 1 secara berurutan
    for i, item in enumerate(data_bab1_lengkap):
        if item.get("is_header"):
            st.markdown(
                f"<h3 style='color:#1e293b; margin-top: 25px;'>{item['jp']} <br> <span style='font-size:0.75em; color:#64748b;'>{item['id']}</span></h3>",
                unsafe_allow_html=True
            )
            st.write("")
        else:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"<div class='materi-card text-jp'>{item['jp']}</div>", unsafe_allow_html=True)
                # Tombol Putar Audio TTS di bawah teks Jepang
                if st.button("🔊 Putar Audio", key=f"play_{i}"):
                    try:
                        with st.spinner("Membuat audio..."):
                            audio = synth(plain_text(item["jp"]), VOICE, RATE)
                        st.audio(audio, format="audio/mp3", autoplay=True)
                    except Exception as e:
                        st.error(f"Gagal membuat audio: {e}")

            with col2:
                if show_id:
                    st.markdown(f"<div class='materi-card text-id'>{item['id']}</div>", unsafe_allow_html=True)

elif selected_bab.startswith("Bab 2"):
    st.info("Materi Bab 2 sedang dalam penyusunan.")
elif selected_bab.startswith("Bab 3"):
    st.info("Materi Bab 3 sedang dalam penyusunan.")
elif selected_bab.startswith("Bab 4"):
    st.info("Materi Bab 4 sedang dalam penyusunan.")
