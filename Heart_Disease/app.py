import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# ----------------------------
# CUSTOM CSS
# ----------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.big-font {
    font-size:30px !important;
    font-weight:bold;
    color:#d63384;
}

.result-box {
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:22px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# LOAD MODEL
# ----------------------------
model = joblib.load("Logistic_Reg_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

# ----------------------------
# HEADER
# ----------------------------
st.markdown(
    "<p class='big-font'>❤️ Heart Disease Risk Prediction System</p>",
    unsafe_allow_html=True
)

st.write(
    "AI-powered healthcare application that predicts the risk of heart disease using Machine Learning."
)

# ----------------------------
# SIDEBAR
# ----------------------------
with st.sidebar:
    st.header("👨‍💻 Project Information")

    st.write("""
    **Developer:** Ammar

    **Model:** Logistic Regression

    **Tech Stack:**
    - Python
    - Numpy
    - Matplotlib
    - seaborn
    - Scikit-Learn
    - Pandas
    - Streamlit
    """)

    st.markdown("Dataset:")
    st.markdown("[Heart Disease Dataset](heart.csv)")

    
    
    st.markdown("---")

    st.subheader("🔗 Connect")

    st.markdown(
        "[GitHub](https://github.com/)"
    )
             


# ----------------------------
# INPUT SECTION
# ----------------------------
st.subheader("📋 Patient Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 18, 100, 40)
    sex = st.selectbox("Sex", ["M", "F"])
    chest_pain = st.selectbox("Chest Pain Type",["ATA", "NAP", "TA", "ASY"])

with col2:
    resting_bp = st.number_input("Resting Blood Pressure",80,200,120)

    cholesterol = st.number_input("Cholesterol",100,600,200)

    fasting_bs = st.selectbox("Fasting Blood Sugar >120",[0, 1])

with col3:
    resting_ecg = st.selectbox("Resting ECG",["Normal", "ST", "LVH"])

    max_hr = st.slider("Maximum Heart Rate",60,220,150)

    exercise_angina = st.selectbox("Exercise Angina",["Y", "N"])

    oldpeak = st.slider("Oldpeak (ST Depression)",0.0,6.0,1.0)

    st_slope = st.selectbox("ST Slope",["Up", "Flat", "Down"])

# ----------------------------
# PREDICT BUTTON
# ----------------------------
if st.button("🔍 Predict Risk", use_container_width=True):

    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]

    probability = model.predict_proba(
        scaled_input
    )[0][1]

    st.divider()

    st.subheader("📊 Prediction Results")

    col1, col2 = st.columns(2)

    with col1:

        if prediction == 1:
            st.error(
                "⚠️ High Risk of Heart Disease"
            )
        else:
            st.success(
                "✅ Low Risk of Heart Disease"
            )

    with col2:
        st.metric(
            "Risk Probability",
            f"{probability*100:.2f}%"
        )

    st.progress(float(probability))

    chart_df = pd.DataFrame({
        "Category": ["Low Risk", "High Risk"],
        "Probability": [
            1-probability,
            probability
        ]
    })

    st.bar_chart(
        chart_df.set_index("Category")
    )

# ----------------------------
# FOOTER
# ----------------------------
st.divider()

st.markdown("""
### 🚀 About this Project

This application uses a trained Logistic Regression model to predict
heart disease risk based on patient health indicators.

**Developer:** Ammar

**Skills Demonstrated**
- Machine Learning
- Feature Engineering
- Model Deployment
- Streamlit Development
- Healthcare Analytics
""")