# Student Dropout Prediction - Data Science Project

---

## 1. Business Understanding

### Latar Belakang

Jaya Jaya Institut merupakan institusi pendidikan yang menghadapi permasalahan tingginya angka mahasiswa yang tidak menyelesaikan studi (dropout). Tingginya angka dropout dapat berdampak pada reputasi institusi serta efektivitas proses pendidikan.

Untuk mengatasi permasalahan tersebut, diperlukan solusi berbasis data untuk mendeteksi mahasiswa yang berpotensi dropout sejak dini.

---

### Permasalahan

* Tingginya angka dropout mahasiswa
* Tidak adanya sistem deteksi dini mahasiswa berisiko
* Sulitnya mengidentifikasi faktor utama penyebab dropout

---

### Tujuan

* Membangun model machine learning untuk prediksi dropout
* Mengidentifikasi faktor utama yang mempengaruhi dropout
* Membantu institusi dalam pengambilan keputusan berbasis data

---

### Manfaat

* Early warning system
* Intervensi lebih cepat terhadap mahasiswa berisiko
* Penurunan tingkat dropout

---

## 2. Data Understanding

Dataset yang digunakan berisi informasi mahasiswa meliputi:

* Data akademik (nilai, performa semester)
* Data demografis
* Status pembayaran
* Status mahasiswa (Dropout, Graduate, Enrolled)

---

## 3. Exploratory Data Analysis (EDA)

Beberapa insight penting yang diperoleh:

* Mahasiswa dengan performa akademik rendah memiliki risiko dropout lebih tinggi
* Nilai masuk (admission grade) berkorelasi dengan keberhasilan studi
* Mahasiswa dengan status pembayaran tidak lancar memiliki kecenderungan lebih tinggi untuk dropout

---

## 4. Data Preparation

Langkah-langkah yang dilakukan:

* Encoding fitur kategorikal
* Mapping target (Dropout = 1, selain itu = 0)
* Pembagian data train dan test
* Feature scaling menggunakan StandardScaler

---

## 5. Modeling

Model yang digunakan:

* Logistic Regression sebagai baseline
* Random Forest sebagai model utama

Hasil:
Model Random Forest memberikan performa terbaik dalam mendeteksi mahasiswa dropout.

---

## 6. Evaluation

Metode evaluasi yang digunakan:

* Accuracy
* Precision
* Recall (fokus utama)
* Confusion Matrix

Insight:
Model memiliki nilai recall yang tinggi sehingga efektif digunakan sebagai sistem deteksi dini mahasiswa yang berpotensi dropout.

---

## 7. Feature Importance

Faktor utama yang mempengaruhi dropout:

* Performa akademik semester pertama
* Nilai masuk (Admission Grade)
* Status pembayaran (Tuition Fees Up To Date)

---

## 8. Machine Learning Prototype (Streamlit)

Aplikasi Streamlit digunakan sebagai prototype untuk memprediksi risiko dropout mahasiswa.

Fitur utama:

* Input data mahasiswa
* Prediksi Dropout atau Tidak
* Probabilitas risiko
* Interpretasi hasil
* Rekomendasi tindakan

Link aplikasi:
(ISI LINK STREAMLIT COMMUNITY CLOUD DI SINI)

---

## 9. Dashboard Monitoring

Dashboard dibuat menggunakan Metabase untuk memonitor performa mahasiswa dan memahami faktor penyebab dropout.

Visualisasi utama:

1. Distribusi Status Mahasiswa
2. Rata-rata Nilai Masuk berdasarkan Status Mahasiswa
3. Performa Akademik Semester 1 berdasarkan Status
4. Status Pembayaran Mahasiswa

Insight dashboard:

* Sekitar 32% mahasiswa mengalami dropout
* Performa akademik rendah berhubungan dengan risiko dropout tinggi
* Mahasiswa dengan pembayaran tidak lancar lebih berisiko dropout

Akses Dashboard:

Email: root@mail.com  
Password: root123  

Link Dashboard:
(Sertakan jika menggunakan Tableau / Looker)

Dashboard dapat digunakan untuk memonitor performa mahasiswa dan mengidentifikasi faktor yang mempengaruhi dropout.

---

## 10. Deployment

Prototype telah di-deploy menggunakan Streamlit Community Cloud sehingga dapat diakses secara online dan digunakan oleh pengguna.

---

## 11. Conclusion

Model machine learning berhasil mengidentifikasi mahasiswa yang berpotensi dropout.

Model terbaik adalah Random Forest dengan performa yang baik dalam mendeteksi mahasiswa berisiko.

Faktor utama yang mempengaruhi dropout adalah:

* Performa akademik
* Nilai masuk
* Status pembayaran

Model ini dapat digunakan sebagai sistem early warning untuk membantu institusi dalam melakukan intervensi dini.

---

## 12. Action Items

* Melakukan monitoring performa akademik mahasiswa secara berkala
* Memberikan perhatian khusus kepada mahasiswa dengan performa rendah
* Mengembangkan program mentoring bagi mahasiswa berisiko
* Mengimplementasikan sistem early warning berbasis machine learning

---

## 13. Cara Menjalankan Project

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Jalankan aplikasi:

```
streamlit run app.py
```

---

## 14. Struktur Folder

```
submission/
├── notebook.ipynb
├── app.py
├── model.pkl
├── scaler.pkl
├── features.pkl
├── requirements.txt
├── README.md
├── metabase.db.mv.db
├── dashboard.png
```

---

## 15. Catatan

* Model menggunakan Random Forest
* Data telah melalui proses preprocessing dan scaling
* Dashboard dan aplikasi saling melengkapi sebagai solusi end-to-end

---

## 16. Author

Nama: (Isi Nama Kamu)
Project: Data Science Submission Dicoding
