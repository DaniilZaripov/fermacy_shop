import streamlit as st

from database import create_tables
from get_data import get_all_drugs, get_drug_info

create_tables()  # Вызов функции создания таблиц при запуске приложения

st.title("Интернет-приложение «Аптека»")

available_drugs = get_all_drugs()
selected_drug = st.selectbox("Выберите лекарство:", available_drugs)

if selected_drug:
    drug_info = get_drug_info(selected_drug)
    if not drug_info:
        st.warning("Информация о лекарстве не найдена")
    else:
        for drug_id, name, price, expiration_date, provider_name, pharmacy_id, count, pharmacy_name, pharmacy_address in drug_info:
            st.write(f"**Лекарство:** {name}")
            st.write(f"**Цена:** {price} руб.")
            st.write(f"**Срок годности:** {expiration_date}")
            st.write(f"**Поставщик:** {provider_name}")
            st.write(f"**Филиал аптеки:** {pharmacy_name}")
            st.write(f"**Адрес аптеки:** {pharmacy_address}")
            st.write(f"**Количество:** {count}")
            st.write("---")
