
# 📘 PROYEK AKHIR: MENYELESAIKAN PERMASALAHAN INSTITUSI PENDIDIKAN

---

# Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan yang menghadapi permasalahan tingginya angka mahasiswa dropout. Hal ini berdampak pada kualitas lulusan, reputasi institusi, serta efisiensi operasional.

Untuk mengatasi permasalahan tersebut, diperlukan solusi berbasis data guna mengidentifikasi mahasiswa yang berpotensi dropout sejak dini.

---

## Permasalahan Bisnis

Beberapa permasalahan utama yang dihadapi:

* Tingginya jumlah mahasiswa dropout
* Tidak adanya sistem prediksi risiko dropout
* Sulit mengidentifikasi faktor utama penyebab dropout
* Keterbatasan monitoring performa mahasiswa

---

## Cakupan Proyek

Proyek ini mencakup:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Feature selection
* Modeling machine learning
* Evaluasi model
* Pembuatan dashboard (Metabase)
* Deployment aplikasi (Streamlit)

---

## Persiapan

### Sumber Data

Dataset yang digunakan:
[Student Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

---

### Setup Environment

#### 1. Clone Repository

```bash
git clone https://github.com/bugiscode/Data-Science
cd Data-Science
```

#### 2. Membuat Virtual Environment

```bash
python -m venv venv
```

#### 3. Aktivasi Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

#### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 5. Menjalankan Aplikasi

```bash
streamlit run app.py
```

### Python Version

* Python 3.10+

---

# Business Dashboard

Dashboard dibuat menggunakan Metabase untuk membantu monitoring performa mahasiswa.

Fitur dashboard:

* Distribusi status mahasiswa (Graduate vs Dropout)
* Rata-rata nilai berdasarkan status
* Hubungan status pembayaran dengan dropout
* Performa akademik semester awal

Insight utama:

* Mahasiswa dengan nilai rendah cenderung dropout
* Status pembayaran sangat berpengaruh terhadap dropout
* Faktor akademik lebih dominan dibanding faktor demografi

Akses dashboard:

* Email: arif76440WGMAIL.COM
* Password: arif123

---

# Menjalankan Sistem Machine Learning

Prototype machine learning dikembangkan menggunakan Streamlit.

Fitur:

* Input data mahasiswa
* Prediksi risiko dropout secara real-time

Link aplikasi:
👉 [https://datascience-siswa.streamlit.app/](https://datascience-siswa.streamlit.app/)

Cara menjalankan lokal:

```bash
streamlit run app.py
```

---

# Conclusion

Berdasarkan analisis data dan modeling:

* Performa akademik semester awal merupakan faktor utama dropout
* Jumlah mata kuliah yang lulus sangat memengaruhi keberhasilan mahasiswa
* Status pembayaran memiliki pengaruh signifikan terhadap dropout
* Admission grade tidak terbukti sebagai faktor dominan

Model machine learning yang dibangun memiliki performa:

* Accuracy: 90%
* Precision: 91%
* Recall: 82%

Hasil ini menunjukkan model cukup baik dalam mengidentifikasi mahasiswa berisiko dropout.
