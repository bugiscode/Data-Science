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

Dataset:
[https://github.com/bugiscode/Data-Science/blob/main/dataset/data_siswa.csv](https://github.com/bugiscode/Data-Science/blob/main/dataset/data_siswa.csv)

Dataset berisi:

* Data demografi
* Nilai akademik
* Status pembayaran
* Status mahasiswa

---

## Setup Environment

```bash
git clone https://github.com/bugiscode/Data-Science
cd Data-Science

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

---

# Business Dashboard

Dashboard dibuat menggunakan Metabase untuk membantu monitoring performa mahasiswa dan memahami faktor penyebab dropout.

---

## Tujuan Dashboard

* Mengidentifikasi faktor utama penyebab dropout
* Monitoring performa akademik mahasiswa
* Mendukung pengambilan keputusan berbasis data

---

## Visualisasi Dashboard

1. Distribusi Status Mahasiswa
2. Rata-rata Admission Grade berdasarkan Status
3. Hubungan Status Pembayaran dengan Dropout
4. Performa Akademik Semester 1

---

## Insight Dashboard

* Proporsi dropout cukup tinggi (~32%) → menunjukkan masalah signifikan
* Admission grade tidak menunjukkan perbedaan signifikan antar status
* Mahasiswa dengan pembayaran tidak lancar memiliki risiko dropout lebih tinggi
* Performa akademik semester awal sangat berpengaruh terhadap keberhasilan mahasiswa
* Hasil ini menunjukkan bahwa faktor akademik memiliki peran yang lebih dominan dibanding faktor awal saat masuk

---

## Cara Menjalankan Dashboard (Metabase)

Dashboard disertakan dalam file:

```
metabase.db.mv.db
```

---

### Versi Metabase

```
metabase:v0.46.4
```

---

### Langkah Menjalankan

1. Pull image Metabase:

```bash
docker pull metabase/metabase:v0.46.4
```

2. Jalankan container:

```bash
docker run -d -p 3000:3000 --name metabase metabase/metabase:v0.46.4
```

3. Copy database ke container:

```bash
docker cp metabase.db.mv.db metabase:/metabase.db/metabase.db.mv.db
```

4. Restart container:

```bash
docker restart metabase
```

5. Akses di browser:

```
http://localhost:3000
```

---

### Login

```
Email: arif76440@mail.com
Password: arif123
```

---

### Lokasi Dashboard

* Collection: **Mahasiswa**
* Dashboard: **Student Dropout Monitoring Dashboard**

---

# Sistem Machine Learning

Prototype dibuat menggunakan Streamlit.

---

## Fitur

* Input data mahasiswa
* Prediksi dropout
* Interface sederhana

---

## Akses Online

[https://datascience-siswa.streamlit.app/](https://datascience-siswa.streamlit.app/)

---

## Run Lokal

```bash
streamlit run app.py
```

---

# Hasil Modeling

Model: **Random Forest**

---

## Performa

* Accuracy: 90%
* Precision: 91%
* Recall: 82%

---

## Insight Modeling

* Performa akademik lebih berpengaruh dibanding nilai masuk
* Status pembayaran berkontribusi terhadap dropout
* Admission grade tidak dominan

---

# Conclusion

## Insight Data

* Dropout dipengaruhi oleh kombinasi faktor, bukan satu variabel
* Performa akademik semester awal sangat berpengaruh
* Status pembayaran memiliki pengaruh signifikan
* Admission grade tidak dominan

---

## Insight Model

* Model Random Forest mencapai akurasi sekitar 90%
* Fitur penting:

  * Jumlah mata kuliah yang disetujui
  * Nilai semester
  * Status pembayaran
* Model cukup baik, namun masih terdapat kesalahan prediksi dropout

---

# Rekomendasi Action Items

1. Implementasi sistem early warning berbasis ML
2. Monitoring performa sejak semester awal
3. Program mentoring mahasiswa berisiko
4. Bantuan finansial bagi mahasiswa
5. Pemanfaatan dashboard untuk monitoring rutin

---

# Keterbatasan

* Belum dilakukan hyperparameter tuning
* Tidak menggunakan data eksternal
* Masih terdapat false negative

---

# Penutup

Pendekatan data science membantu institusi dalam memahami dan mengurangi dropout melalui analisis data dan prediksi berbasis machine learning.