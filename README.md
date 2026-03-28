# PROYEK AKHIR: MENYELESAIKAN PERMASALAHAN INSTITUSI PENDIDIKAN

---

# Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan yang menghadapi permasalahan tingginya angka mahasiswa dropout. Hal ini berdampak pada kualitas lulusan, reputasi institusi, serta efisiensi operasional.

Untuk mengatasi permasalahan tersebut, diperlukan solusi berbasis data guna:

* Mengidentifikasi mahasiswa berisiko dropout
* Memahami faktor utama penyebab dropout
* Mendukung pengambilan keputusan berbasis data

---

## Permasalahan Bisnis

Permasalahan utama yang dihadapi:

* Tingginya jumlah mahasiswa dropout
* Tidak adanya sistem prediksi risiko dropout
* Sulit mengidentifikasi faktor utama penyebab dropout
* Monitoring performa mahasiswa belum optimal

---

## Tujuan Proyek

* Menganalisis faktor-faktor yang memengaruhi dropout
* Membangun model machine learning untuk prediksi dropout
* Membuat dashboard monitoring performa mahasiswa
* Mengembangkan prototype sistem prediksi berbasis Streamlit

---

## Cakupan Proyek

* Data Understanding
* Data Cleaning & Preparation
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Modeling Machine Learning
* Evaluasi Model
* Dashboard (Metabase)
* Deployment (Streamlit)

---

# Persiapan

## Sumber Data

Dataset yang digunakan:

[https://github.com/bugiscode/Data-Science/blob/main/dataset/data_siswa.csv](https://github.com/bugiscode/Data-Science/blob/main/dataset/data_siswa.csv)

Dataset berisi informasi mahasiswa seperti:

* Data demografi
* Nilai akademik
* Status pembayaran
* Status mahasiswa (Graduate, Dropout, Enrolled)

---

## Setup Environment

### Python Version

```
Python 3.10+
```

---

### Langkah Setup

```bash
# Clone repository
git clone https://github.com/bugiscode/Data-Science
cd Data-Science

# Membuat virtual environment
python -m venv venv

# Aktivasi environment
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

# Install dependency
pip install -r requirements.txt
```

---

# Business Dashboard

Dashboard dibuat menggunakan Metabase untuk membantu monitoring performa mahasiswa dan memahami faktor penyebab dropout.

## Tujuan Dashboard
- Mengidentifikasi faktor utama penyebab dropout
- Monitoring performa akademik mahasiswa
- Mendukung pengambilan keputusan berbasis data

---

## Visualisasi Dashboard

Dashboard terdiri dari beberapa visualisasi utama:

1. Distribusi Status Mahasiswa  
2. Rata-rata Admission Grade berdasarkan Status  
3. Hubungan Status Pembayaran dengan Dropout  
4. Performa Akademik Semester 1  

---

## Insight Dashboard

- Proporsi dropout cukup tinggi (~32%) → menunjukkan masalah signifikan  
- Admission grade tidak menunjukkan perbedaan signifikan antar status  
- Mahasiswa dengan pembayaran tidak lancar memiliki risiko dropout lebih tinggi  
- Performa akademik semester awal sangat berpengaruh terhadap keberhasilan mahasiswa  

Insight ini konsisten dengan hasil analisis pada notebook dan model machine learning.

---

## Cara Menjalankan Dashboard (Metabase)

Dashboard dibuat menggunakan Metabase dan disertakan dalam file database berikut:

File:metabase.db.mv.db


### Langkah menjalankan:

1. Install Metabase (jika belum)
2. Jalankan Metabase: java -jar metabase.jar
3. Akses di browser: http://localhost:3000
4. Login menggunakan:
- Email: arif76440@gmail.com
- Password: arif123  
5. Dashboard dapat diakses pada:
- Collection: **Mahasiswa**  
- Dashboard: **Student Dropout Monitoring Dashboard**
---

# Sistem Machine Learning

Prototype dikembangkan menggunakan **Streamlit** untuk memprediksi risiko dropout.

---

## Fitur Aplikasi

* Input data mahasiswa
* Prediksi risiko dropout secara real-time
* Interface sederhana dan mudah digunakan

---

## Akses Online

[https://datascience-siswa.streamlit.app/](https://datascience-siswa.streamlit.app/)

---

## 💻 Menjalankan Secara Lokal

```bash
streamlit run app.py
```

---

# Hasil Modeling

Model yang digunakan: **Random Forest**

### Alasan Pemilihan

* Mampu menangkap pola kompleks
* Tidak sensitif terhadap scaling
* Performa stabil

---

## Performa Model

* Accuracy: **90%**
* Precision: **91%**
* Recall: **82%**

---

## Interpretasi Model

* Model mampu mengklasifikasikan mayoritas mahasiswa dengan baik
* Recall dropout sedikit lebih rendah → masih ada dropout yang tidak terdeteksi
* Dalam konteks bisnis, ini menjadi area yang dapat ditingkatkan

---

## Feature Importance

Fitur paling berpengaruh:

* Jumlah mata kuliah semester 2 yang disetujui
* Nilai semester 2
* Jumlah mata kuliah semester 1
* Status pembayaran

---

## Insight Modeling

* Performa akademik selama perkuliahan lebih berpengaruh dibanding nilai masuk
* Admission grade tidak terbukti sebagai faktor dominan
* Faktor finansial juga berkontribusi terhadap dropout

---

# Conclusion

Berdasarkan hasil analisis dan modeling:

* Tidak terdapat satu faktor tunggal penyebab dropout
* Faktor utama berasal dari kombinasi:

  * Performa akademik
  * Jumlah mata kuliah yang diselesaikan
  * Status pembayaran
* Admission grade tidak memiliki pengaruh dominan
* Model machine learning mampu memberikan prediksi dengan performa yang baik (~90%)

---

# Rekomendasi Action Items

Berdasarkan hasil proyek, berikut langkah yang dapat dilakukan:

1. Mengembangkan sistem **early warning berbasis machine learning**
2. Melakukan monitoring performa akademik sejak semester pertama
3. Memberikan program mentoring bagi mahasiswa berisiko
4. Menyediakan bantuan finansial atau skema pembayaran fleksibel
5. Menggunakan dashboard sebagai alat monitoring rutin

---

# Keterbatasan

* Model belum dilakukan hyperparameter tuning
* Belum menggunakan data eksternal tambahan
* Masih terdapat kemungkinan false negative pada dropout

---

# Penutup

Proyek ini menunjukkan bahwa pendekatan data science dapat membantu institusi pendidikan dalam:

* Mengidentifikasi risiko dropout
* Memahami faktor penyebab
* Mendukung pengambilan keputusan

Dengan implementasi yang tepat, solusi ini dapat meningkatkan kualitas pendidikan dan menurunkan angka dropout secara signifikan.
