import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- Import Library สำหรับแกะ Pipeline ของโมเดล ---
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# ===== 1. ตั้งค่าหน้าเว็บ =====
st.set_page_config(page_title="Starbucks Spend Predictor", page_icon="☕", layout="centered")

# ===== 2. โหลดโมเดล =====
@st.cache_resource
def load_model():
    try:
        return joblib.load("starbucks_model.pkl")
    except Exception as e:
        return str(e)

with st.spinner("กำลังปลุกบาริสต้า (โหลดโมเดล)..."):
    model = load_model()

if isinstance(model, str):
    st.error(f"เกิดข้อผิดพลาดในการโหลดโมเดล: {model}")
    st.stop()

# ===== 3. ส่วนหัวของเว็บ =====
st.title("☕ Starbucks Spend Predictor")
st.markdown("""
แอปพลิเคชันนี้ใช้ **Machine Learning** เพื่อทำนาย **ยอดใช้จ่ายรวม (Total Spend)** ของลูกค้า Starbucks 
ช่วยให้ร้านสามารถวางแผนจัดการสต็อกวัตถุดิบและคาดการณ์รายได้ได้อย่างแม่นยำยิ่งขึ้น
""")
st.divider()

# ===== 4. ฟอร์มรับข้อมูลลูกค้า =====
st.subheader("📝 กรอกข้อมูลพฤติกรรมการสั่งซื้อ")

col1, col2 = st.columns(2)

with col1:
    order_channel = st.selectbox("ช่องทางการสั่งซื้อ", ['Drive-Thru', 'Mobile App', 'In-Store', 'Kiosk'])
    store_location_type = st.selectbox("ทำเลที่ตั้งสาขา", ['Urban', 'Suburban', 'Rural'])
    region = st.selectbox("ภูมิภาค", ['Northeast', 'Southwest', 'Midwest', 'Southeast', 'West'])
    customer_age_group = st.selectbox("ช่วงอายุลูกค้า", ['18-24', '25-34', '35-44', '45-54', '55+'])
    customer_gender = st.selectbox("เพศ", ['Male', 'Female', 'Other'])

with col2:
    drink_category = st.selectbox("ประเภทเครื่องดื่ม", ['Coffee', 'Tea', 'Frappuccino', 'Refresher', 'Bakery', 'Other'])
    cart_size = st.number_input("จำนวนรายการในตะกร้า", min_value=1, max_value=20, value=1)
    num_customizations = st.number_input("จำนวนการปรับแต่ง (เช่น เพิ่มวิป, เปลี่ยนนม)", min_value=0, max_value=10, value=0)
    is_rewards_member = st.checkbox("เป็นสมาชิก Starbucks Rewards")
    has_food_item = st.checkbox("สั่งอาหารทานเล่นด้วย")
    order_ahead = st.checkbox("สั่งล่วงหน้า (Order Ahead)")

# ===== 5. ปุ่มทำนายผล =====
if st.button("✨ ทำนายยอดใช้จ่าย", type="primary", use_container_width=True):
    
    # สร้าง DataFrame ตามโครงสร้างที่โมเดลต้องการเป๊ะๆ
    input_data = pd.DataFrame([{
        'order_channel': order_channel,
        'store_location_type': store_location_type,
        'region': region,
        'customer_age_group': customer_age_group,
        'customer_gender': customer_gender,
        'is_rewards_member': is_rewards_member,
        'cart_size': cart_size,
        'num_customizations': num_customizations,
        'drink_category': drink_category,
        'has_food_item': has_food_item,
        'order_ahead': order_ahead
    }])

    # ทำนายผล
    prediction = model.predict(input_data)
    
    # แสดงผลลัพธ์
    st.success("ทำนายผลสำเร็จ!")
    st.markdown(f"""
    <div style="text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px;">
        <h3 style="color: #333;">ยอดใช้จ่ายที่คาดการณ์</h3>
        <h1 style="color: #00704A; font-size: 3em;">${prediction[0]:.2f}</h1>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()