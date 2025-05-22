# Dashboard Perkembangan Kasus COVID-19 di Pulau Sulawesi


## Deskripsi Proyek

Dashboard interaktif ini dikembangkan untuk memvisualisasikan dan menganalisis perkembangan kasus harian, tingkat kesembuhan, dan rasio kematian COVID-19 di provinsi-provinsi Pulau Sulawesi. Proyek ini bertujuan untuk membantu pengguna memahami tren pandemi secara lokal melalui visualisasi data yang mudah dipahami, seperti grafik garis, batang, tabel data, serta perbandingan persentase dan akumulasi total antar provinsi.

Data yang digunakan berasal dari berkas Excel resmi yang berasal dari Badan Pusat Statistik (BPS) Indonesia


## Daftar Isi

* [Deskripsi Proyek](#deskripsi-proyek)
* [Fitur Utama](#fitur-utama)
* [Teknologi yang Digunakan](#teknologi-yang-digunakan)
* [Cara Menjalankan](#cara-menjalankan)
* [Anggota Tim](#anggota-tim)


## Fitur Utama

* **Pemilihan Provinsi & Tahun Interaktif**: Pengguna dapat dengan mudah memilih provinsi dan tahun untuk memfilter data yang ditampilkan.
* **Visualisasi Tren Harian**: Menampilkan grafik (garis atau batang) untuk kasus Konfirmasi, Sembuh, dan Meninggal setiap bulan.
* **Tabel Data Detail**: Menyajikan data mentah dalam format tabel untuk setiap provinsi dan tahun yang dipilih.
* **Ringkasan Akumulasi & Persentase**: Menampilkan total kasus Konfirmasi, Meninggal, dan Sembuh, beserta persentasenya dari total seluruh kasus pada tahun yang dipilih.
* **Perbandingan Antar Provinsi**: Memungkinkan pengguna membandingkan total akumulasi kasus COVID-19 antara dua provinsi berbeda dalam tahun yang sama.


## Teknologi yang Digunakan

* **Python**: Bahasa pemrograman utama yang digunakan.
* **Streamlit**: Framework untuk membangun dashboard interaktif berbasis web dengan cepat.
* **Pandas**: Digunakan untuk manipulasi dan analisis data, termasuk pembersihan dan filtering.
* **Plotly Express**: Library untuk membuat visualisasi data yang menarik dan interaktif.
* **NumPy**: Digunakan untuk perhitungan numerik dan statistik.


## Cara Menjalankan

Ikuti langkah-langkah berikut untuk menjalankan dashboard ini di sistem Anda:

1.  **Pastikan Python Terinstal**: Jika belum, unduh dan instal Python dari [python.org](https://www.python.org/).

2.  **Instal Dependensi**: Buka terminal atau command prompt Anda dan jalankan perintah berikut untuk menginstal semua library yang dibutuhkan:
    ```bash
    pip install streamlit pandas plotly numpy openpyxl
    ```
    *Catatan: `openpyxl` diperlukan untuk membaca berkas `.xlsx`.*

3.  **Siapkan Struktur Direktori Data**:
    Buat folder baru bernama `data` di direktori yang sama dengan berkas `app.py` Anda.

4.  **Unduh Data Resmi**:
    Unduh data COVID-19 yang relevan dari situs web resmi **BPS (Badan Pusat Statistik)**. Setelah mengunduh, Anda perlu mengonversi atau mengatur data tersebut ke dalam format berkas Excel (`.xlsx`). Pastikan setiap berkas Excel memiliki nama file sesuai dengan provinsi yang digunakan dalam kode (contoh: `GORONTALO.xlsx`, `SULAWESI BARAT.xlsx`, dst.) dan letakkan di folder `data/`.

    Pastikan setiap berkas Excel tersebut memiliki *sheet* untuk setiap tahun (2020, 2021, 2022, 2023) dengan struktur kolom: `Bulan`, `Konfirmasi`, `Meninggal`, `Sembuh`. Data bulan seharusnya dimulai dari baris ke-3 di setiap *sheet*.

5.  **Jalankan Aplikasi**:
    Setelah dependensi terinstal dan data disiapkan, jalankan aplikasi Streamlit dengan perintah:
    ```bash
    streamlit run app.py
    ```
    Aplikasi akan otomatis terbuka di browser web default Anda.


## Anggota Tim

Proyek ini dikembangkan oleh kelompok:

1. NUR ALIM - 240907501030
2. FAWAZ - 240907502041
3. PUTRI AMELIA - 240907501022
4. FATHIYYAH MUHAYRIKA SARIKA - 240907500019
5. NUR HUSNA - 240907500016
6. NAJWA JAUZA NUWAYYAR - 240907502014 
7. FARHAN FAHLEVY - 240907502021