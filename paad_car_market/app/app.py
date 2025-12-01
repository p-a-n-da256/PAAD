import streamlit as st
import pandas as pd
import os

# ======== Глобальная функция загрузки данных ===========
@st.cache_data
def load_data():
    # Текущая папка app/
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # Путь ../data/processed/cars_processed.csv
    csv_path = os.path.join(BASE_DIR, "..", "data", "processed", "cars_processed.csv")
    csv_path = os.path.normpath(csv_path)

    return pd.read_csv(csv_path)


# ======== ГЛАВНАЯ СТРАНИЦА ===========
st.set_page_config(
    page_title="Анализ рынка автомобилей",
    page_icon="🚗"
)

st.title("Анализ рынка автомобилей 🚗")
st.write("Выберите раздел слева, чтобы начать работу.")

# загружаем данные
df = load_data()

st.subheader("Пример данных")
st.dataframe(df.head(10))
