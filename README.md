# 🎮 Proyek Analisis Sentimen Ulasan PUBG Mobile

Repositori ini berisi proyek **analisis sentimen** terhadap **ulasan pengguna PUBG Mobile** yang dikumpulkan melalui web scraping. Proyek ini bertujuan untuk mengklasifikasikan opini pengguna ke dalam tiga kategori sentimen: **positif**, **negatif**, dan **netral**, menggunakan pendekatan machine learning.

---

## 📌 Fitur Proyek

* Scraping data ulasan dari PUBG Mobile (misalnya dari Google Play Store atau media sosial)
* Pembersihan dan pra-pemrosesan data teks berbahasa Indonesia
* Ekstraksi fitur menggunakan metode **TF-IDF**
* Pelatihan model machine learning untuk klasifikasi sentimen
* Evaluasi model menggunakan metrik seperti akurasi dan F1-score

---

## 🗂️ Struktur Direktori

```
Projec_Analisis_Sentimen/
├── scrapping.py               # Script scraping ulasan PUBG Mobile
├── notebook.ipynb             # Notebook utama (EDA, preprocessing, training, evaluasi)
├── requirements.txt           # Daftar dependensi
├── data/
│   └── ulasan.csv       # Data hasil scraping ulasan PUBG
└── README.md                  # Dokumentasi proyek
```

---

## 🔧 Tools & Library

* **Python 3.x**
* `pandas`, `numpy` – manipulasi data
* `scikit-learn` – machine learning pipeline
* `nltk`, `Sastrawi` – preprocessing teks bahasa Indonesia
* `matplotlib`, `seaborn` – visualisasi data
* `google-play-scraper` atau API serupa (untuk scraping, jika digunakan)

---

## 🚀 Cara Menjalankan Proyek

1. **Clone repositori**

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

## 🔄 Alur Proyek

1. **Scraping ulasan PUBG Mobile** dari Google Play Store (atau platform lain)
2. **Pra-pemrosesan teks:**

   * Case folding (ubah huruf kecil semua)
   * Hapus tanda baca, angka, dan stopword
   * Tokenisasi & stemming
3. **Ekstraksi fitur:** menggunakan TF-IDF
4. **Pelatihan model:** menggunakan beberapa algoritma seperti Logistic Regression, Naive Bayes, dll
5. **Evaluasi model** dengan metrik akurasi dan F1-score

---

## 📬 Kontak

**Reza Yasa Putra**
GitHub: [@Rezayasaputra29](https://github.com/Rezayasaputra29)

---


