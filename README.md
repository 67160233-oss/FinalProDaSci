# ☕ Starbucks Customer Spend Predictor

## 📌 ภาพรวมของโปรเจค (Project Overview)
แอปพลิเคชันนี้สร้างขึ้นเพื่อทำนาย **ยอดใช้จ่ายรวม (Total Spend)** ของลูกค้า Starbucks โดยวิเคราะห์จากพฤติกรรมการสั่งซื้อ เช่น ช่องทางการสั่ง, ประเภทเครื่องดื่ม, การเป็นสมาชิก Rewards และการปรับแต่งเครื่องดื่ม โปรเจคนี้ช่วยแก้ปัญหาการคาดการณ์รายได้และการเตรียมสต็อกวัตถุดิบของสาขาต่างๆ

## 📊 ข้อมูลที่ใช้ (Dataset)
* **Dataset:** Starbucks Customer Ordering Patterns
* **Features:** ช่องทางการสั่ง, ทำเลร้าน, ช่วงอายุ, การปรับแต่งเครื่องดื่ม, สมาชิก Rewards ฯลฯ
* **Target Variable:** `total_spend` (ยอดใช้จ่ายรวมในบิลนั้น)

## 🤖 โมเดล Machine Learning (Model Evaluation)
เพื่อหาโมเดลที่มีประสิทธิภาพที่สุด ได้ทำการเปรียบเทียบโมเดล 3 รูปแบบ (เพื่อหา R2 Score ที่ดีที่สุด):
1. **Linear Regression**
2. **Random Forest Regressor**
3. **Gradient Boosting Regressor** 🏆 *(หรือเปลี่ยนชื่อโมเดลตามตัวที่ชนะใน Colab ของคุณ)*

โมเดลที่ใช้งานในระบบนี้ถูกรวมเข้ากับ `Pipeline` เพื่อจัดการ Missing Values และทำ One-Hot Encoding อย่างเป็นระบบ

## 🌐 การใช้งาน (Deployment)
โปรเจคนี้ถูก Deploy ผ่าน Streamlit Community Cloud 
สามารถทดลองใช้งานได้ที่: `[ใส่ URL Streamlit ของคุณตรงนี้]`
