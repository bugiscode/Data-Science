# Proyek Akhir: Prediksi Dropout Mahasiswa

---

## Business Understanding

Jaya Jaya Institut menghadapi permasalahan tingginya angka mahasiswa yang tidak menyelesaikan studi (dropout). Hal ini berdampak pada kualitas pendidikan serta reputasi institusi.

### Permasalahan Bisnis

* Tingginya angka dropout mahasiswa
* Tidak adanya sistem deteksi dini (early warning system)
* Sulit mengidentifikasi faktor utama penyebab dropout

### Cakupan Proyek

Proyek ini mencakup:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Pembuatan model machine learning
* Evaluasi model
* Deployment dalam bentuk aplikasi Streamlit
* Pembuatan dashboard monitoring

### Persiapan

Sumber data: Dataset performa mahasiswa

Catatan penting:
Dataset hanya menggunakan mahasiswa dengan status **Dropout** dan **Graduate**.
Data dengan status **Enrolled dihapus** agar model melakukan klasifikasi biner secara valid sesuai tujuan proyek.

Setup environment:

```
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
```

---

## Business Dashboard

Dashboard dibuat menggunakan Metabase untuk membantu monitoring performa mahasiswa.

Visualisasi utama:

1. Distribusi Status Mahasiswa
2. Rata-rata Nilai Masuk berdasarkan Status
3. Performa Akademik Semester 1
4. Status Pembayaran Mahasiswa

Insight utama:

* Sekitar 32.1% mahasiswa mengalami dropout
* Mahasiswa dengan nilai masuk rendah memiliki risiko lebih tinggi
* Performa akademik semester awal menjadi indikator kuat
* Mahasiswa dengan pembayaran tidak lancar lebih berisiko dropout

Akses Dashboard:

* Email: [root@mail.com](mailto:root@mail.com)
* Password: root123

File dashboard:

* metabase.db.mv.db
* dashboard.png

---

## Menjalankan Sistem Machine Learning

Model machine learning dibangun menggunakan algoritma Random Forest untuk klasifikasi dropout.

Cara menjalankan aplikasi:

```
streamlit run app.py
```

Fitur aplikasi:

* Input data mahasiswa
* Prediksi risiko dropout
* Probabilitas risiko
* Rekomendasi tindakan

File yang digunakan:

* model.pkl
* scaler.pkl
* features.pkl

---

## Conclusion

Model machine learning berhasil memprediksi risiko dropout dengan akurasi sekitar 86%.

Faktor utama yang mempengaruhi dropout:

* Performa akademik mahasiswa
* Nilai masuk (admission grade)
* Status pembayaran

Mahasiswa dengan performa akademik rendah dan kendala finansial memiliki risiko dropout lebih tinggi.

Model ini dapat digunakan sebagai sistem early warning untuk membantu institusi dalam melakukan intervensi lebih dini.

---

## Rekomendasi Action Items

* Mengimplementasikan sistem early warning berbasis machine learning
* Melakukan monitoring performa akademik sejak semester pertama
* Memberikan program mentoring kepada mahasiswa berisiko
* Melakukan evaluasi terhadap status pembayaran mahasiswa secara berkala

---
