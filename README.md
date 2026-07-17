# Capital Bikeshare Analysis
Bike Sharing merupakan generasi baru dari penyewaan sepeda tradisional, di mana seluruh proses mulai dari keanggotaan, peminjaman, hingga pengembalian sepeda telah dilakukan secara otomatis. Melalui sistem ini, pengguna dapat meminjam sepeda di satu stasiun dan mengembalikannya di stasiun lain dengan menggunakan aplikasi ponsel pintar, GPS, dan pemindaian barcode. Berbeda dengan layanan transportasi lain seperti bus atau kereta bawah tanah, durasi perjalanan serta lokasi keberangkatan dan kedatangan dicatat secara rinci dalam sistem ini. Salah satu implementasi bike sharing yang cukup dikenal adalah Capital Bikeshare, yaitu layanan penyewaan sepeda publik yang beroperasi di wilayah Washington, D.C. dan sekitarnya. Sistem ini menyediakan jaringan stasiun dengan ribuan sepeda yang dapat diakses oleh pengguna untuk perjalanan jarak pendek. Dengan dukungan teknologi seperti aplikasi mobile dan sistem pelacakan, Capital Bikeshare dirancang untuk memberikan kemudahan, fleksibilitas, serta mendukung mobilitas perkotaan yang lebih berkelanjutan.

## Project Overview
Project ini menganalisis data dari aplikasi Capital Bikeshare untuk mengevaluasi kinerja layanan serta mengidentifikasi pola penggunaan sepeda. Melalui analisis ini, diharapkan dapat diperoleh berbagai insight mengenai perilaku pengguna, tren penyewaan, faktor-faktor yang memengaruhi jumlah penyewaan, serta informasi yang dapat digunakan sebagai dasar dalam pengambilan keputusan untuk meningkatkan kualitas layanan dan operasional. 

## Business Problem
Seiring dengan meningkatnya penggunaan layanan Capital Bikeshare, perusahaan perlu memastikan ketersediaan sepeda, menjaga kualitas armada, serta mengoptimalkan operasional di setiap stasiun. Namun, permintaan penyewaan dapat berubah-ubah karena faktor seperti cuaca, musim, hari, dan waktu. Tanpa pemahaman yang baik terhadap pola penggunaan tersebut, perusahaan berisiko mengalami ketidakseimbangan distribusi sepeda, penurunan kualitas layanan, dan operasional yang kurang efisien. Oleh karena itu, analisis data diperlukan untuk memahami pola penggunaan, mengidentifikasi faktor yang memengaruhi permintaan, serta menghasilkan insight yang mendukung pengambilan keputusan dan peningkatan kualitas layanan. 

## Dataset Description
Dataset utama yang digunakan berkaitan dengan catatan historis selama dua tahun, yaitu tahun 2011 dan 2012, dari sistem Capital Bikeshare di Washington D.C., Amerika Serikat, yang tersedia untuk umum di http://capitalbikeshare.com/system-data. Data tersebut kemudian diagregasi dalam basis per jam dan harian, lalu dilengkapi dengan informasi cuaca dan musiman yang sesuai. Informasi cuaca diperoleh dari http://www.freemeteo.com.

## Data Cleaning
blabla

## Dashboard
Untuk melihat hasil visualisasi data dalam bentuk dashboard, ada dua cara sebagai berikut:
#### Akses dashboard online di Streamlit Cloud
[Klik di sini untuk melihat dashboard](https://bikesharingdashboard-kmrvb3enktryxype49mf6p.streamlit.app/).

#### Run di Lokal
1. Clone repository
2. Install library yang dibutuhkan
3. Jalankan dashboard, ketik pada terminal sebagai berikut
   "streamlit run bike_sharing_db.py"

### Dependencies
- Python 3.x
- streamlit
- pandas
- numpy
- matplotlib
- seaborn
- Babel

### Catatan
- Pastikan semua file CSV ada di folder 'data/'
- Dashboard di Streamlit Cloud otomatis redeploy jika ada perubahan di Github.

## Dashboard Overview
imsage
## Key Insights & Business Recommendation

## Conclusion
Analisis dilakukan dengan menggunakan Python melalui Colab. Dari proses analisis, diperoleh kesimpulan sebagai berikut:
- Menjelang akhir pekan yaitu pada hari Kamis, Jumat dan Sabtu pada jam 17.00-18.00 terjadi kenaikan jumlah pengguna bike-sharing dibandingkan hari-hari dan jam-jam yang lainnya.
- Terjadi kenaikan jumlah pengguna bike-sharing yang cukup signifikan dari tahun 2011 ke tahun 2012 yaitu sekitar 1 juta pengguna
- Mayoritas pengguna bike-sharing melakukan penyewaan sepeda pada musim gugur, ketika cuaca sedang cerah, sedikit awan ataupun berawan sebagian.
- Mayoritas pengguna bike-sharing melakukan penyewaan ketika hari kerja dan bukan hari libur
