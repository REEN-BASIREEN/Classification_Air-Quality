import streamlit as st
from joblib import load
import numpy as np

# โหลดโมเดลที่อัปโหลดมา
model = load('best_model.pkl')  # ชื่อไฟล์โมเดล

# ฟังก์ชันสำหรับการทำนาย HealthImpactScore และ HealthImpactClass
def make_prediction(AQI, PM10, PM2_5, NO2, SO2, O3, Temperature, Humidity, Windspeed, RespiratoryCases,
                    CardiovascularCases, HospitalAdmissions,):
    conditions = [AQI, PM10, PM2_5, NO2, SO2, O3, Temperature, Humidity, Windspeed, RespiratoryCases,
                  CardiovascularCases, HospitalAdmissions,]

    prediction = model.predict([conditions])
    health_impact_class = int(prediction[0])

    return health_impact_class




# Streamlit UI
st.title('Health Impact Prediction Based on Air Quality and Weather Conditions')  # ชื่อแอปพลิเคชัน

# ส่วนสำหรับกรอกข้อมูลด้านคุณภาพอากาศ
st.header('Air Quality Metrics')
aqi = st.number_input('aqi')
pm10 = st.number_input('PM10 (μg/m3)')
pm2_5 = st.number_input('PM2.5 (μg/m3)')
no2 = st.number_input('NO2 (μg/m3)')
so2 = st.number_input('SO2 (μg/m3)')
o3 = st.number_input('O3 (μg/m3)')

# ส่วนสำหรับกรอกข้อมูลสภาพอากาศ
st.header('Weather Conditions')
temperature = st.number_input('Temperature (°C)')
humidity = st.number_input('Humidity (%)')
windspeed = st.number_input('Windspeed (km/h)')

# ส่วนสำหรับกรอกข้อมูลผลกระทบต่อสุขภาพ
st.header('Health Impact Metrics')
respiratory_cases = st.number_input('Respiratory Cases')
cardiovascular_cases = st.number_input('Cardiovascular Cases')
hospital_admissions = st.number_input('Hospital Admissions')




# ปุ่มทำนาย
if st.button('Predict'):
    health_impact_class = make_prediction(aqi, pm10, pm2_5, no2, so2, o3, temperature, humidity,
                                                               windspeed, respiratory_cases, cardiovascular_cases,
                                                               hospital_admissions,)

    # แสดงผลลัพธ์การทำนาย

    st.write(f'Health Impact Class: {health_impact_class}')
