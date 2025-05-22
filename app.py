import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(layout="wide")

# ================== JUDUL DAN ANGGOTA ==================
st.title("Dashboard Perkembangan Kasus Covid-19 di Pulau Sulawesi")
st.markdown("""
**Kelompok:**
1. NUR ALIM - 240907501030
2. FAWAZ - 240907502041
3. PUTRI AMELIA - 240907501022
4. Fathiyyah Muhayrika Sarika - 240907500019
5. Nur Husna - 240907500016
6. Najwa Jauza Nuwayyar - 240907502014 
7. Farhan Fahlevy - 240907502021

Website ini menyajikan data perkembangan COVID-19 untuk provinsi-provinsi di Pulau Sulawesi. 
Anda dapat memilih provinsi dan tahun untuk melihat tren kasus Konfirmasi terkena virus, Sembuh, dan Meninggal, 
baik dalam bentuk grafik, data tabel, persentase, maupun perbandingannya dengan Provinsi lain. Visualisasi ini membantu memahami bagaimana pandemi berkembang secara lokal.
""")

# ================== LOAD DATA ==================
@st.cache_data
def load_data_excel():
    folder = "data"
    provinsi_files = {
        'GORONTALO': 'GORONTALO.xlsx',
        'SULAWESI BARAT': 'SULAWESI BARAT.xlsx',
        'SULAWESI SELATAN': 'SULAWESI SELATAN.xlsx',
        'SULAWESI TENGAH': 'SULAWESI TENGAH.xlsx',
        'SULAWESI TENGGARA': 'SULAWESI TENGGARA.xlsx',
        'SULAWESI UTARA': 'SULAWESI UTARA.xlsx',
    }

    data = {}
    for prov, file_name in provinsi_files.items():
        file_path = os.path.join(folder, file_name)
        sheets = pd.read_excel(file_path, sheet_name=None, skiprows=2)
        # Pastikan sheet_name adalah tahun: 2020, 2021, 2022, 2023
        for year, df in sheets.items():
            df.columns = ['Bulan', 'Konfirmasi', 'Meninggal', 'Sembuh']
            df['Tahun'] = int(year)
            if prov not in data:
                data[prov] = {}
            data[prov][int(year)] = df
    return data

data_all = load_data_excel()

# Pilih Provinsi & Tahun
provinsi_list = list(data_all.keys())
provinsi_pilihan = st.selectbox("Pilih Provinsi:", provinsi_list)

tahun_list = sorted(data_all[provinsi_pilihan].keys())
tahun_pilihan = st.selectbox("Pilih Tahun:", tahun_list)

# Load data terpilih
df_tampil = data_all[provinsi_pilihan][tahun_pilihan]

# Tabel Data
st.subheader(f"Tabel Data Covid-19 di {provinsi_pilihan} - {tahun_pilihan}")
st.dataframe(df_tampil, use_container_width=True)

# Pilih jenis grafik
tipe_grafik = st.radio("Pilih Tipe Grafik:", ['Garis', 'Batang'], horizontal=True)

# Grafik
st.subheader("Grafik Perkembangan Tiap Bulan")
if tipe_grafik == 'Garis':
    fig = px.line(df_tampil, x='Bulan', y=['Konfirmasi', 'Meninggal', 'Sembuh'],
                  markers=True, title=f"Grafik Covid-19 di {provinsi_pilihan} - {tahun_pilihan}")
else:
    fig = px.bar(df_tampil, x='Bulan', y=['Konfirmasi', 'Meninggal', 'Sembuh'],
                 barmode='group', title=f"Grafik Covid-19 di {provinsi_pilihan} - {tahun_pilihan}")
st.plotly_chart(fig, use_container_width=True)

# Akumulasi Total & Persentase
total_konfirmasi = df_tampil['Konfirmasi'].sum()
total_meninggal = df_tampil['Meninggal'].sum()
total_sembuh = df_tampil['Sembuh'].sum()
total_semua = total_konfirmasi + total_meninggal + total_sembuh

st.subheader("Akumulasi Total")
st.write(f"**Konfirmasi:** {total_konfirmasi} | **Meninggal:** {total_meninggal} | **Sembuh:** {total_sembuh}")

st.write("**Persentase:**")
st.progress(total_konfirmasi / total_semua)
st.write(f"Konfirmasi: {round((total_konfirmasi/total_semua)*100, 2)}%")
st.progress(total_meninggal / total_semua)
st.write(f"Meninggal: {round((total_meninggal/total_semua)*100, 2)}%")
st.progress(total_sembuh / total_semua)
st.write(f"Sembuh: {round((total_sembuh/total_semua)*100, 2)}%")

# Perbandingan Provinsi
st.subheader("Perbandingan dengan Provinsi Lain")
provinsi_banding = st.selectbox("Bandingkan dengan:", [p for p in provinsi_list if p != provinsi_pilihan])
df_banding = data_all[provinsi_banding][tahun_pilihan]

total_konfirmasi_2 = df_banding['Konfirmasi'].sum()
total_meninggal_2 = df_banding['Meninggal'].sum()
total_sembuh_2 = df_banding['Sembuh'].sum()

st.write(f"### Perbandingan Akumulasi Total Tahun {tahun_pilihan}")
df_comp = pd.DataFrame({
    'Kategori': ['Konfirmasi', 'Meninggal', 'Sembuh'],
    provinsi_pilihan: [total_konfirmasi, total_meninggal, total_sembuh],
    provinsi_banding: [total_konfirmasi_2, total_meninggal_2, total_sembuh_2]
})

fig_comp = px.bar(df_comp, x='Kategori', y=[provinsi_pilihan, provinsi_banding],
                  barmode='group', title=f"Perbandingan {provinsi_pilihan} & {provinsi_banding} - {tahun_pilihan}")
st.plotly_chart(fig_comp, use_container_width=True)

# ================== FOOTER ==================
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #3b31c4;
    color: white;
    text-align: center;
    padding: 10px;
    font-size: 14px;
    z-index: 100;
}
</style>

<div class="footer">
    © 2025 | Kelompok 3 Visualisasi Data - <b>Kelas B Bisnis Digital 2024</b><br>
    Universitas Negeri Makassar<br>
    Sumber: <b>Badan Pusat Statistik (BPS)</b> & <b>Andra Farm</b>
</div>
""", unsafe_allow_html=True)