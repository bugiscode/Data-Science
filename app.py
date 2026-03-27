import streamlit as st
import pandas as pd
import joblib

# ===============================
# LOAD MODEL
# ===============================
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

st.set_page_config(page_title="Student Dropout Prediction", layout="wide")

# ===============================
# HEADER
# ===============================
st.title("🎓 Student Dropout Prediction System")

st.markdown("""
Aplikasi ini digunakan untuk memprediksi kemungkinan mahasiswa mengalami **dropout** 
berdasarkan data akademik, demografi, dan faktor ekonomi.

Gunakan sebagai **early warning system** untuk membantu pengambilan keputusan.
""")

st.info("Model: Random Forest | Fokus: Deteksi Risiko Dropout")
st.caption("* Semua field wajib diisi")

st.markdown("---")

# ===============================
# LABEL FRIENDLY
# ===============================
label_map = {
    "Marital_status": "Status Pernikahan",
    "Application_mode": "Mode Pendaftaran",
    "Application_order": "Urutan Pilihan",
    "Course": "Program Studi",
    "Daytime_evening_attendance": "Waktu Kuliah",
    "Previous_qualification": "Pendidikan Sebelumnya",
    "Previous_qualification_grade": "Nilai Pendidikan Sebelumnya",
    "Nationality": "Kewarganegaraan",
    "Mothers_qualification": "Pendidikan Ibu",
    "Fathers_qualification": "Pendidikan Ayah",
    "Mothers_occupation": "Pekerjaan Ibu",
    "Fathers_occupation": "Pekerjaan Ayah",
    "Admission_grade": "Nilai Masuk",
    "Displaced": "Status Pindahan",
    "Educational_special_needs": "Kebutuhan Khusus",
    "Debtor": "Memiliki Tunggakan",
    "Tuition_fees_up_to_date": "Status Pembayaran",
    "Gender": "Jenis Kelamin",
    "Scholarship_holder": "Penerima Beasiswa",
    "Age_at_enrollment": "Usia Saat Masuk",
    "International": "Mahasiswa Internasional",
    "Unemployment_rate": "Tingkat Pengangguran",
    "Inflation_rate": "Tingkat Inflasi",
    "GDP": "GDP"
}

# ===============================
# CONTOH INPUT (HINT)
# ===============================
example_values = {
    "Age_at_enrollment": 20,
    "Admission_grade": 120,
    "Previous_qualification_grade": 130,
    "Curricular_units_1st_sem_grade": 12,
    "Curricular_units_2nd_sem_grade": 13,
    "Unemployment_rate": 10,
    "Inflation_rate": 2,
    "GDP": 1.5
}

# ===============================
# INPUT HELPER
# ===============================
input_data = {}
errors = []

def input_number(label, key):
    example = example_values.get(key, 1)

    val = st.number_input(
        f"{label} *",
        value=None,
        placeholder=f"Contoh: {example}",
        key=key
    )

    if val is None:
        errors.append(label)

    return val

# ===============================
# INPUT SECTION
# ===============================
st.subheader("📥 Input Data Mahasiswa")

st.info("Gunakan nilai sesuai kondisi mahasiswa. Contoh diberikan sebagai panduan.")

tab1, tab2, tab3 = st.tabs(["📊 Akademik", "👤 Demografi", "📈 Ekonomi & Lainnya"])

# ===============================
# TAB 1 - AKADEMIK
# ===============================
with tab1:
    st.markdown("### Data Akademik")

    academic_features = [f for f in features if "Curricular" in f or "grade" in f]

    for f in academic_features:
        label = label_map.get(f, f.replace("_", " "))
        input_data[f] = input_number(label, f)

# ===============================
# TAB 2 - DEMOGRAFI
# ===============================
with tab2:
    st.markdown("### Data Mahasiswa")

    demo_features = [f for f in features if any(x in f for x in ["Age", "Gender", "Nationality", "Marital"])]

    for f in demo_features:
        label = label_map.get(f, f.replace("_", " "))
        input_data[f] = input_number(label, f)

# ===============================
# TAB 3 - LAINNYA
# ===============================
with tab3:
    st.markdown("### Data Ekonomi & Lainnya")

    used = list(input_data.keys())
    other_features = [f for f in features if f not in used]

    for f in other_features:
        label = label_map.get(f, f.replace("_", " "))
        input_data[f] = input_number(label, f)

st.markdown("---")

st.warning("Pastikan semua field telah diisi sebelum melakukan prediksi.")

# ===============================
# PREDICTION
# ===============================
if st.button("🔍 Prediksi Risiko Dropout"):

    # VALIDASI WAJIB
    if len(errors) > 0:
        st.error(f"❌ Data belum lengkap. {len(errors)} field wajib belum diisi.")
        st.stop()

    try:
        input_df = pd.DataFrame([input_data])

        # urutan kolom sesuai model
        input_df = input_df[features]

        # scaling
        input_scaled = scaler.transform(input_df)

        # prediction
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]

    except Exception:
        st.error("❌ Terjadi error saat memproses data. Pastikan semua input valid.")
        st.stop()

    st.markdown("## 📊 Hasil Prediksi")

    if prediction == 1:
        st.error(f"⚠️ Mahasiswa Berisiko Dropout ({probability:.2%})")
    else:
        st.success(f"✅ Mahasiswa Tidak Berisiko Dropout ({probability:.2%})")

    st.markdown("---")

    # ===============================
    # INTERPRETASI
    # ===============================
    st.subheader("🧠 Interpretasi")

    st.write("""
    - Probabilitas menunjukkan tingkat risiko dropout  
    - Semakin tinggi nilai → semakin tinggi risiko  
    - Model mempertimbangkan faktor akademik, demografi, dan ekonomi  
    """)

    # ===============================
    # REKOMENDASI
    # ===============================
    st.subheader("🎯 Rekomendasi")

    if probability > 0.7:
        st.warning("Perlu intervensi segera (mentoring intensif & monitoring ketat)")
    elif probability > 0.4:
        st.info("Perlu perhatian (evaluasi akademik)")
    else:
        st.success("Kondisi aman, tetap lakukan monitoring")

# ===============================
# FOOTER
# ===============================
st.caption("© 2026 | Student Dropout Prediction | Data Science Project")