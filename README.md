
# 🎮 Analisis Sentimen Ulasan PUBG Mobile

Repositori ini berisi proyek **analisis sentimen** terhadap **ulasan pengguna PUBG Mobile** yang dikumpulkan melalui web scraping. Proyek ini bertujuan untuk mengklasifikasikan opini pengguna ke dalam tiga kategori sentimen: **positif**, **negatif**, dan **netral**, menggunakan pendekatan machine learning.

---

## 🧭 Alur Proyek

1. **Load Dataset**

   * Mengimpor data ulasan pengguna PUBG Mobile yang telah dikumpulkan melalui proses scraping.
   * Dataset disimpan dalam format CSV dan dimuat menggunakan library `pandas`.

2. **Reprocessing Data**

   * Menyesuaikan format data agar konsisten dan siap untuk diproses lebih lanjut.
   * Mengatasi nilai yang hilang dan memastikan tipe data sesuai.

3. **Cleaning Teks**

   * Melakukan pembersihan teks ulasan dengan:

     * Menghapus karakter khusus, angka, dan tanda baca.
     * Mengubah teks menjadi huruf kecil (lowercasing).
     * Menghapus stopwords menggunakan library `Sastrawi`.
     * Melakukan stemming untuk mendapatkan akar kata.

4. **Pelabelan**

   * Menentukan label sentimen berdasarkan skor atau kata kunci tertentu dalam ulasan.
   * Kategori sentimen meliputi:

     * **Positif**
     * **Negatif**
     * **Netral**

5. **Splitting Data**

   * Membagi dataset menjadi dua bagian:

     * **Data Latih (Training Set)**: Digunakan untuk melatih model.
     * **Data Uji (Testing Set)**: Digunakan untuk menguji performa model.
   * Pembagian dilakukan dengan rasio 80:20 menggunakan `train_test_split` dari `scikit-learn`.

6. **Pemodelan**

   * Membangun model klasifikasi sentimen menggunakan algoritma seperti:

     * **Naive Bayes**
     * **Support Vector Machine (SVM)**
     * **Logistic Regression**
   * Menggunakan TF-IDF untuk ekstraksi fitur dari teks.

7. **Testing (Data Uji)**

   * Menguji model yang telah dilatih menggunakan data uji.
   * Mengevaluasi performa model berdasarkan metrik seperti akurasi, presisi, recall, dan F1-score.

---

## 🗂️ Struktur Direktori

```
Projec_Analisis_Sentimen/
├── data/
│   └── ulasan.csv       # Dataset hasil scraping ulasan PUBG Mobile
├── scrapping.py               # Script untuk scraping data ulasan
├── notebook.ipynb             # Notebook utama berisi proses analisis
├── requirements.txt           # Daftar dependensi Python
└── README.md                  # Dokumentasi proyek
```

---

## 🛠️ Teknologi dan Library

* **Bahasa Pemrograman:** Python
* **Library:**

  * `pandas`, `numpy` – manipulasi data
  * `scikit-learn` – pemodelan machine learning
  * `nltk`, `Sastrawi` – pemrosesan bahasa alami Bahasa Indonesia
  * `matplotlib`, `seaborn` – visualisasi data
  * `tweepy` atau `google-play-scraper` – pengambilan data ulasan (scraping)

---

## 🚀 Cara Menjalankan Proyek

1. **Klon repositori**

   ```bash
   git clone https://github.com/Rezayasaputra29/Projec_Analisis_Sentimen.git
   cd Projec_Analisis_Sentimen
   ```

2. **(Opsional) Buat virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate           # Windows
   ```

3. **Install dependensi**

   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan notebook**

   ```bash
   jupyter notebook notebook.ipynb
   ```

---

## 📬 Kontak

**Reza Yasa Putra**
GitHub: [@Rezayasaputra29](https://github.com/Rezayasaputra29)


