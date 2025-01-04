import streamlit as st
from datetime import datetime

# Judul aplikasi
st.title("Selamat Ulang Tahun untuk Dedek Sayang")

# Gambar latar belakang
st.image("IMG_9528.JPG", use_column_width=True)

# Input nama pacar
nama_pacar = st.text_input("Masukkan nama Dedek:")

# Tanggal ulang tahun yang sudah ditentukan
tanggal_ulang_tahun = datetime(2004, 1, 5)

# Nama yang benar (dalam huruf kecil)
nama_benar = "ika sasongko kusumawati pribadi"

# Tombol untuk mengirim ucapan
if st.button("Ini Tombol Apa Hayo"):
    # Validasi input
    if not nama_pacar:
        st.error("Silakan masukkan nama Dedek terlebih dahulu!")
    elif nama_pacar.lower() != nama_benar:
        st.error("KAMU SIAPA SAYA TAK KENAL")
    else:
        # Menghitung usia
        usia = datetime.today().year - tanggal_ulang_tahun.year
        if (datetime.today().month, datetime.today().day) < (tanggal_ulang_tahun.month, tanggal_ulang_tahun.day):
            usia -= 1

        # Mengubah nama_pacar menjadi title case
        nama_pacar_title = nama_pacar.title()

        # Ucapan selamat ulang tahun
        ucapan = f"""
        🎉 Selamat Ulang Tahun, {nama_pacar_title}! 🎉
        
        Hari ini adalah hari istimewa untukmu. 
        Semoga semua impianmu menjadi kenyataan dan hidupmu dipenuhi dengan cinta dan kebahagiaan. 
        Setiap detik bersamamu adalah anugerah, dan aku bersyukur memilikimu. 
        Selamat merayakan usia ke-{usia}!

        💖 Dengan cinta, 
        MAMAS 💖 
        """
        
        st.success(ucapan)

        # Menambahkan gambar pada ucapan
        st.image("IMG_0941.JPG", use_column_width=True)